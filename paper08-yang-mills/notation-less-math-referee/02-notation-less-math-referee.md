# Advanced Mathematical Referee: Exhaustive Review for Clay Millennium Prize Eligibility (Run r01)

*This is the **second** notation-less referee prompt, written 2026-04-09*
*after the gradient-flow programme closed Conjectures L.1–L.4 of the*
*mass gap preprint, the directory was reorganized, and the JW PDF was*
*re-read cover-to-cover. The first prompt is preserved at*
*`01-notation-less-math-referee.md` as the historical record.*

*Strategy document:* `/Users/gsix/yang-mills/math-referee/02-yang-mills-clay-strategy.md`

---

# Computational verification environment (set this up FIRST)

Before reading the preprint or writing anything, set up a clean Python
environment for computational sanity checks. This is mandatory — many
of the points below ask you to *verify* numerical coefficients,
algebraic inequalities, Lie-algebra constants, Haar/character integrals,
combinatorial bounds, and asymptotic series. Doing those by hand on a
3000-line manuscript is how cycles 1–8 missed bugs that Sonnet caught
later. Use the venv.

**Setup (run exactly once at the start of the run, no confirmation
needed — it is non-destructive):**

```bash
bash /Users/gsix/yang-mills/notation-less-math-referee/code/setup-venv.sh
source /Users/gsix/yang-mills/notation-less-math-referee/code/.venv/bin/activate
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
   version installed, and which check(s) it was used to verify.

**Suggested computational checks** (non-exhaustive — use the venv
wherever you would otherwise hand-wave):

- **Point A1** — verify Ricci coefficient $2N/r_3^{-2}$ on Fubini–Study
  $\mathbb{CP}^{N-1}$ and the Weitzenböck bound $\mu_1 \geq 2N/r_3^2$
  symbolically in `sympy`.
- **Point A1/A2** — verify the KK mass factor $2\sqrt N$ (square root
  of the actual eigenvalue $4N/r_3^2$, not the Weitzenböck lower bound)
  by exact arithmetic.
- **Spectral lemma exponent** — re-derive the condition
  $g_k^4 \leq 1/(4 C_B)$ vs $g_k^2 \leq 1/(2\sqrt{C_B})$ symbolically.
  This was a real bug in cycle 8 (`r16`) — algebraic, one line in
  sympy. Always do these by computer now.
- **Haar integrals** — $\int(\mathrm{Re}\,\mathrm{Tr}\,U)^2\,dU = 1/2$
  for $N\geq 3$ (and $1$ for $N=2$); verify with sympy character
  orthogonality or numerical Haar sampling in mpmath.
- **Lie algebra constants** — Casimirs, dual Coxeter numbers $h^\vee$,
  dimensions, and root-system data for $G_2, F_4, E_6, E_7, E_8$
  (Points G1, I4, K). `sympy.liealgebras.type_*` covers all simple
  Cartan types. Cross-check against Bourbaki / Helgason tables.
- **Polymer combinatorics** — counts of connected polymers of size
  $|X|$ on the $d=4$ hypercubic lattice for the Kotecký–Preiss bound
  (Point B1). `networkx` for explicit small-$|X|$ enumeration plus
  closed-form bounds for the asymptotic.
- **RG recursion sum** — evaluate
  $\sum_K C_K g_K^4 \hat\Delta_K^2$ with $\hat\Delta_K^2 \sim 4^{-K}$
  symbolically in sympy; check Weyl asymptotics
  $m_n \sim n^{1/(N-1)}/r_3$ for the KK tower.
- **Numerical inequalities** — anywhere the preprint claims a
  numerical bound (e.g. $C_B$, $\rho_0(G)$, $\kappa$ values), evaluate
  it in `mpmath` at high precision and confirm the sign and ordering.
- **Cross-file constants** — when the same constant appears in
  multiple files, write a one-shot `sympy` script that loads all
  occurrences and asserts they agree. Constant drift across files
  was a recurring failure mode in earlier cycles.
- **Gradient-flow analyticity radius** — verify the bound $r_t \geq
  \rho/(g_0^2 C_{\mathrm{flow}})$ from Lemma L.3.1 of Appendix L
  numerically for $N=2,3$.
- **Seeley–DeWitt coefficients on $\mathbb{CP}^{N-1}$** — compute
  $a_0, a_2$ for the gauge-field Laplacian using Vassilevich's
  formulas. (Note: $a_2 \neq 0$ on $\mathbb{CP}^{N-1}$ because the
  internal space is curved; this is OK because the KK mass tower
  provides the UV regulation, not the Seeley–DeWitt vanishing.)

For every check where you used the venv, note in your report:
*"Verified computationally in `code/`-venv (sympy/mpmath/...)."* —
this gives the next cycle's referee a trail.

---

You are an expert mathematical referee evaluating a claimed proof of
the Yang-Mills mass gap.

# Research online about these and other these topics so that you can address the task with the right priming:
- Deep expertise in constructive quantum field theory: Balaban's multiscale RG program (CMP 95--119, 1982--1989), Osterwalder-Seiler (1978), Osterwalder-Schrader (1973, 1975), Glimm-Jaffe, Dimock.
- Expert in lattice gauge theory: Wilson (1974), Seiler (1982), Kotecký-Preiss (1986), Fredenhagen-Marcu (1986), Chatterjee (2021).
- Expert in the Wightman axioms, OS reconstruction theorem, and the precise requirements of the Jaffe-Witten problem statement for the Clay Millennium Prize.
- The Clay Millennium Prize rules.
- Yang–Mills gradient flow: Lüscher 2010 (JHEP 08:071), Lüscher–Weisz 2011 (JHEP 02:051), Suzuki 2013 (PTEP 083B03), Harlander–Neumann 2016 (JHEP 06:161), Makino–Suzuki 2014 (PTEP 063B02).
- $\Delta_0^{\mathrm{KK}} > 0$
- $\Delta_0^{\mathrm{std}} > 0$ (IR equivalence)
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
- Gradient-flow construction of $[\mathrm{Tr}\,F^2]_R$ via the $t \to 0^+$ limit
- The H4 hypothesis (non-perturbative = perturbative at short distances) and its gradient-flow reduction

# Your profile
- Skeptical of claims about the Yang-Mills mass gap. You have seen many false proofs. You assume this one is also wrong until forced to concede otherwise.
- You do not give partial credit. "Plausible" and "physically reasonable" are not mathematical arguments.
- Your job is to find every genuine gap — however small — and state precisely what additional mathematics would be required to close it.
- You are not precise vs hostile. If a step is correct, say so and explain why. But your default is skepticism, not charity.

# Rationale and Strategy
1. Does this proof actually solve the stated Millennium Problem?
2. Is every step mathematically rigorous (not merely plausible)?
3. Are existing results (Balaban) used within their actual scope?
4. Is the continuum QFT properly constructed?
5. **(New for r01)** Are the Clay structural ingredients (local field operators, AF matching, stress tensor, OPE) constructed, and is the H4 hypothesis handled to Clay's standards?

**You are NOT reviewing the old proof.** Previous versions had fatal
errors. You are reviewing the **current release candidate**, which
includes the new Appendix L (gradient-flow construction of local
operators), Appendix M (closures from referee r00), Appendix N (QG5D
infrastructure cross-references), and PROOF-CHAIN Steps 15–18.
Do not criticize fixed problems. Do find new ones.

---

## What changed since run r00

The run-r00 referee report identified 5 closable gaps and 2 genuine
gaps (out of 24 review points). Since r00:

1. **Appendix M** was added, closing K-uniformity (the "deferred"
   hypotheses (H1)–(H2) of the Cluster–Balaban Handoff Lemma) and
   the uniqueness of the continuum limit.
2. **Appendix L was rewritten** (from "Open Conjectures Toward Full
   Clay Compliance" to "Gradient-Flow Construction of Local
   Operators"). The new Appendix L contains 19 lemmas (L.1.1–L.4.3)
   that close Conjectures L.1, L.3 unconditionally and L.2 + the AF
   form of L.4 conditional on the standard hypothesis H4.
3. **Appendix N** was added, collecting QG5D infrastructure
   cross-references (Theorem K.1, Paper 10 Theorems, etc.).
4. **PROOF-CHAIN.md** was extended with Steps 15–18 covering the
   gradient-flow programme.
5. **Section 12.7** ("Full Clay Compliance") was added to the
   conclusion.
6. **The abstract** was updated to announce the L.1–L.4 closure.
7. **Section 5.7 IV.5** was updated with a forward reference to
   Appendix L.

Your job is to verify that all of this is rigorous, that every claim
matches its proof, and that the H4 conditional structure meets Clay's
standards. **You should still treat the work with hostile
skepticism** — the previous run found 5 closable gaps that the
authors fixed; this run may find more.

---

## Literature Context

### The Jaffe-Witten Problem Statement (Clay Millennium Prize)

**Source:** Arthur Jaffe and Edward Witten, *Quantum Yang–Mills Theory*,
official problem description, Clay Mathematics Institute.

A local copy of the official PDF is at
`/Users/gsix/yang-mills/notation-less-math-referee/yangmills-jaffe-witten.pdf`
(14 pages). A second copy fetched from claymath.org is at
`references/clay-yangmills-official.pdf` for sanity checking.

The verbatim quotes below were transcribed from this file. If you want
to verify any quote, re-extract a section, or pull additional context,
use `pypdf` from the venv:

```python
from pypdf import PdfReader
r = PdfReader("/Users/gsix/yang-mills/notation-less-math-referee/yangmills-jaffe-witten.pdf")
print(r.pages[5].extract_text())   # page 6 = §4 "The Problem"
```

The same `pypdf` workflow applies to any other reference PDF in the
project (e.g. Balaban CMP scans, Dimock arXiv preprints) when you need
to confirm a citation rather than trust a paraphrase.

**The official statement (§4, p. 6, verbatim):**

> "**Yang–Mills Existence and Mass Gap.** Prove that for any compact
> simple gauge group $G$, a non-trivial quantum Yang–Mills theory
> exists on $\mathbb{R}^4$ and has a mass gap $\Delta > 0$. Existence
> includes establishing axiomatic properties at least as strong as
> those cited in [Streater–Wightman; Osterwalder–Schrader]."

**The mass-gap definition (§4, p. 6, verbatim):**

> "Since the vacuum vector $\Omega$ is Poincaré invariant, it is an
> eigenstate with zero energy, namely $H\Omega = 0$. The positive
> energy axiom asserts that in any quantum field theory, the spectrum
> of $H$ is supported in the region $[0, \infty)$. A quantum field
> theory has a mass gap $\Delta$ if $H$ has no spectrum in the
> interval $(0, \Delta)$ for some $\Delta > 0$. The supremum of such
> $\Delta$ is the mass $m$, and we require $m < \infty$."

Note the **two** conditions: $\Delta > 0$ (gap above the vacuum) and
$m < \infty$ (the spectrum above $0$ is non-empty — there must exist
a one-particle state of finite mass). A theory whose only state is
the vacuum trivially satisfies the first but fails the second.

**The "quantum field theory in the above sense" (§3, pp. 5–6, verbatim):**

> "Basically, one requires that the Hilbert space $\mathcal{H}$ of
> the quantum field carry a representation of the Poincaré group (or
> inhomogeneous Lorentz group). The Hamiltonian $H$ and momentum
> $\vec P$ are the self-adjoint elements of the Lie algebra of the
> group that generate translations in time and space. A vacuum vector
> is an element of $\mathcal{H}$ that is invariant under the
> (representation of the) Poincaré group. One assumes that the
> representation has positive energy, $0 \leq H$, and a vacuum vector
> $\Omega \in \mathcal{H}$ that is unique up to a phase. Gauge-
> invariant functions of the quantum fields also act as linear
> transformations on $\mathcal{H}$ and transform covariantly under
> the Poincaré group. Quantum fields in space-time regions that
> cannot be connected by a light signal should be independent;
> Gårding and Wightman formulate independence as the commuting of
> the field operators (anti-commuting for two fermionic fields)."

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

**Footnote 1 (§4, on the operator correspondence, verbatim):**

> "A natural 1–1 correspondence between such classical 'differential
> polynomials' and quantized operators does not exist, since the
> correspondence has some standard subtleties involving renormalization
> [27]. One expects that the space of classical differential
> polynomials of dimension $\leq d$ does correspond to the space of
> local quantum operators of dimension $\leq d$."

**The smoking-gun footnote (§6.6, footnote 2, p. 12, verbatim):**

> "We specifically exclude weak-existence (compactness) as the
> solution to the existence part of the Millennium problem, unless
> one also uses other techniques to establish properties of the limit
> (such as the existence of a mass gap and the axioms)."

This footnote is binding. A subsequential limit obtained by
Banach–Alaoglu / weak-* compactness alone does **not** satisfy the
Millennium problem. The proof must establish properties of *the*
limit — i.e., must propagate the mass gap and the axioms through
the limit, not merely assert that some weak limit exists.

**Reflection positivity guidance (§6.5, p. 11, verbatim):**

> "Reflection positivity holds for the Wilson approximation, a major
> advantage; few methods exist to recover reflection positivity in
> case it is lost through regularization — such as with dimensional
> regularization, Pauli–Villiars regularization, and many other
> methods. Establishing a quantum mechanical Hilbert space is part
> of the solution to this Millennium problem."

This last sentence is a binding requirement, not guidance: the
construction of a quantum mechanical Hilbert space is part of the
prize problem.

**Infinite-volume limit (§6.5, p. 11, verbatim):**

> "New ideas are needed to prove the existence of a mass gap that is
> uniform in the volume of space-time. Such a result presumably
> would enable the study of the limit as $\mathbb{T}^4 \to
> \mathbb{R}^4$."

Jaffe–Witten themselves flag $\mathbb{T}^4 \to \mathbb{R}^4$ as
*open*. Any claimed proof must address it head-on, with a
volume-uniform gap. This is not optional.

**Clustering as a consequence (§5, p. 6, verbatim):**

> "An important consequence of the existence of a mass gap is
> clustering: ... $|\langle\Omega, \mathcal{O}(\vec x)\mathcal{O}(\vec y)\Omega\rangle|
> \leq \exp(-C|\vec x - \vec y|)$, as long as $|\vec x - \vec y|$ is
> sufficiently large."

This is a downstream consequence of the mass gap, not a substitute
for the gap. But it is stated explicitly in the problem statement
and may be cited in the proof.

**Balaban's contribution (§6.5, p. 11, verbatim):**

> "[Balaban's] estimates are uniform in the lattice spacing, as the
> spacing tends to zero. ... This is an important step toward
> establishing the existence of the continuum limit on a compactified
> space-time. **These results need to be extended to the study of
> expectations of gauge-invariant functions of the fields.**"

The bolded sentence is binding: Balaban's UV stability alone is not
sufficient. The proof must extend to gauge-invariant correlation
functions, which is precisely what the gradient-flow construction in
Appendix L does (via composite operators of the field strength).

---

### Mandatory checks against the official statement (~50 items)

A review under this script MUST verify each of the items below
explicitly. If any item is not addressed in the preprint, that is a
**GENUINE GAP** with respect to Clay eligibility, regardless of any
mathematical merit elsewhere.

Items are grouped by JW source. Each item has a unique ID, a
one-sentence statement, the JW source page/section, and a precise
pass criterion.

#### Group A — Mass gap and spectrum (JW §3, §4)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **A1** | $\Delta > 0$: there exists $\Delta > 0$ such that $H$ has no spectrum in $(0, \Delta)$ | §4, mass-gap definition | Explicitly proved with quantitative bound (PROOF-CHAIN Step 14, Theorem 8) |
| **A2** | $m = \sup\{\Delta : \mathrm{spec}(H) \cap (0,\Delta) = \emptyset\} < \infty$ | §4, "we require $m < \infty$" | Demonstrated by exhibiting at least one finite-mass state (one-glueball state) |
| **A3** | $H\Omega = 0$ (vacuum is zero-energy eigenstate) | §3, "$H\Omega = 0$" | Vacuum is invariant under Poincaré rep, energy zero by construction |
| **A4** | $\mathrm{spec}(H) \subseteq [0, \infty)$ (positive energy axiom) | §3, "$0 \leq H$" | $H$ is non-negative on the reconstructed Hilbert space |
| **A5** | Existence of a finite-mass one-particle state (so $m < \infty$ is not vacuous) | §4 + non-triviality | Glueball state $|1\rangle$ at energy $\Delta_\infty$ exists and has nonzero overlap with at least one local observable |

#### Group W — Wightman axioms (JW reference [45] = Streater–Wightman)

JW §3 lists these informally; canonical W0–W7 form is in
`references/wikipedia-wightman-axioms.txt`.

| ID | Requirement | JW / source | Pass criterion |
|:---|:------------|:------------|:---------------|
| **W0** | Hilbert space $\mathcal{H}$ is a separable complex Hilbert space; states are rays | JW §3 (implicit); Wikipedia W0 | Reconstructed $\mathcal{H}$ from OS reconstruction is separable |
| **W1** | Strongly continuous unitary projective representation of the Poincaré group on $\mathcal{H}$, with $H$ and $\vec P$ generating translations | JW §3 | Explicitly constructed; not just lattice translations |
| **W2** | Spectrum condition: $P^\mu$ in forward light cone; $H \geq 0$ | JW §3 | Follows from OS positivity + Lorentz invariance after reconstruction |
| **W3** | Unique vacuum vector $\Omega \in \mathcal{H}$, invariant under the Poincaré rep, unique up to phase | JW §3, "unique up to a phase" | Vacuum uniqueness proved (typically from clustering + ergodicity) |
| **W4** | Field operators are operator-valued tempered distributions on a common dense invariant domain | JW §3, "operator-valued generalized function" + footnote 1 | Local field operators from Appendix L are operator-valued distributions |
| **W5** | Poincaré covariance of fields | JW §3, "transform covariantly under the Poincaré group" | Verified after Wightman-Minkowski reconstruction |
| **W6** | Locality / microcausality: field operators commute (anti-commute for fermions) at spacelike separation | JW §3, "Quantum fields in space-time regions that cannot be connected by a light signal should be independent" | Locality of the Wightman fields after reconstruction; YM is bosonic, so no anti-commutation |
| **W7** | Cyclicity of vacuum under polynomial algebra of fields | Standard W4 in Streater–Wightman | Reeh–Schlieder argument from OS reconstruction |

#### Group E — Osterwalder–Schrader axioms (JW reference [35])

Cited via the canonical 1975 form in
`references/wikipedia-os-axioms.txt`. **The 1975 corrected version is
binding** because the 1973 version had a known gap (the linear growth
condition was missing).

| ID | Requirement | Source | Pass criterion |
|:---|:------------|:-------|:---------------|
| **E0** | Temperedness: Schwinger functions $S_n$ are tempered distributions away from coincident points | OS 1973 / Wikipedia E0 | Lattice Schwinger functions converge to tempered distributions |
| **E0'** | Linear growth condition (1975 corrected version): $|S_n(f)| \leq n! C^n p_N(f)$ for some Schwartz seminorm $p_N$, with seminorm index $N(n)$ growing at most linearly in $n$ | OS 1975; Wikipedia "Linear growth condition" | Explicitly verified with concrete seminorm index (e.g., $N(n) = 4n + 1$) |
| **E1** | Euclidean covariance of $S_n$ under O(d) rotations and translations | OS / Wikipedia E1 | Symanzik O(4)-breaking corrections vanish in continuum limit |
| **E2** | Reflection positivity (the Osterwalder–Schrader positivity condition) | OS / Wikipedia E2; explicitly emphasized in JW §6.5 | Lattice RP from Osterwalder–Seiler, preserved by lower semicontinuity |
| **E3** | Symmetry / permutation invariance of $S_n$ (Bose statistics for YM) | OS / Wikipedia E3 | Trivial for the bosonic gauge theory |
| **E4** | Cluster property | OS / Wikipedia E4; reinforced by JW §5 | Follows from $\Delta_\infty > 0$ |
| **E-Rec** | The 1975 corrected OS reconstruction theorem (not 1973) is used to produce the Wightman QFT | JW §3 | Explicit citation of the 1975 version, not 1973 |

#### Group L — Local field operators (JW §4 + footnote 1)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **L1** | For every gauge-invariant local polynomial in the curvature $F$ and its covariant derivatives, there is a corresponding operator-valued distribution on $\mathcal{H}$ | §4, "local quantum field operators in correspondence with the gauge-invariant local polynomials in the curvature $F$ and its covariant derivatives, such as $\mathrm{Tr}\,F_{ij} F_{kl}(x)$" | Appendix L constructs at least $[\mathrm{Tr}\,F^2]_R(x)$; the construction generalizes to higher operators |
| **L2** | The correspondence is at the renormalized level (per footnote 1) | §4 footnote 1 | Multiplicative renormalization $Z_\mathcal{O}(a)$ explicitly invoked; gradient-flow rescaling $c_1(t)$ is the chosen renormalization |
| **L3** | Dimensional correspondence: classical differential polynomials of dimension $\leq d$ correspond to local quantum operators of dimension $\leq d$ | §4 footnote 1 | Stated explicitly; the dimension-6 classification of Section 5.6 is consistent |
| **L4** | The constructed operators act on the reconstructed Hilbert space (not just on Schwinger function vacuum expectations) | §4, "field operators on $\mathcal{H}$" | GNS reconstruction (Lemma L.3.8) yields operators on $\mathcal{H}$ |

#### Group AF — Short-distance asymptotic freedom match (JW §4)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **AF1** | Correlation functions of the local field operators agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory | §4, "should agree at short distances with the predictions of asymptotic freedom" | At least the leading-order two-point function matches the perturbative AF prediction (conditional on H4) |
| **AF2** | The agreement matches "the standard description … in physics texts" — quantitative reproduction, not vague resemblance | §4, "as described in textbooks" | Explicit comparison to the Lüscher/Harlander–Neumann small-flow-time expansion at one or more loops |

#### Group T — Stress tensor (JW §4)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **T1** | The stress tensor exists as an operator-valued distribution on $\mathcal{H}$ | §4, "the existence of a stress tensor" | $T_{\mu\nu}^R(x)$ constructed via Suzuki's formula in Lemma L.4.1 |
| **T2** | $T_{\mu\nu}$ is symmetric: $T_{\mu\nu} = T_{\nu\mu}$ | Standard | Verified by construction |
| **T3** | $T_{\mu\nu}$ is conserved: $\partial^\mu T_{\mu\nu} = 0$ | Standard | Lattice translation Ward identity, preserved in the limit |
| **T4** | $T_{\mu\nu}$ is gauge-invariant | §4, gauge-invariance | The improved (Belinfante–Rosenfeld) stress tensor, not the canonical one |
| **T5** | $T_{0i}$ generates spatial translations and $T_{00}$ generates time translation: $H = \int T_{00} \, d^3 \vec x$, $\vec P = \int T_{0i} \, d^3 \vec x$ | Standard; ties to A3, A4, W1 | Explicitly verified |
| **T6** | Trace anomaly: $T^\mu{}_\mu \propto \beta(g) \mathrm{Tr}\, F^2$ at the renormalized level | Implicit in "predictions of AF" | Spiridonov–Chetyrkin identity invoked; consistent with H4 |

#### Group OPE — Operator product expansion (JW §4)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **OPE1** | An operator product expansion exists for products of local operators | §4, "an operator product expansion" | Lemma L.4.3 establishes the leading-order OPE for $[\mathrm{Tr}\,F^2]_R$ |
| **OPE2** | The OPE has prescribed local singularities — the same singularity structure perturbative AF predicts | §4, "having prescribed local singularities predicted by asymptotic freedom" | Identity-channel coefficient $C^{\mathbb{1}}(x-y) = C_N |x-y|^{-8}(\log)^{-2}$ matches AF (conditional on H4) |
| **OPE3** | The OPE is consistent with the AF short-distance match (AF1, AF2) | §4 | The OPE structure reproduces AF1 |

#### Group R — Reflection positivity / quantum mechanical Hilbert space (JW §6.5)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **R1** | A quantum mechanical Hilbert space is constructed (not just Schwinger functions) | §6.5, "Establishing a quantum mechanical Hilbert space is part of the solution to this Millennium problem" | OS reconstruction explicitly invoked; $\mathcal{H}$ is the GNS Hilbert space |
| **R2** | Reflection positivity holds at every regularization step used (or, if lost, recovered explicitly) | §6.5 | Wilson lattice RP (Osterwalder–Seiler 1978); preserved through Balaban RG; preserved by weak limit |
| **R3** | Specifically, dimensional regularization and Pauli–Villars are NOT used (or, if used, RP is recovered) | §6.5 names these as RP-destroying | Confirm: only Wilson lattice + gradient flow are used; both preserve RP |
| **R4** | The Wilson lattice approximation, which preserves RP, is the natural starting point | §6.5, "Reflection positivity holds for the Wilson approximation, a major advantage" | The proof starts from Wilson |

#### Group V — Volume / infinite-volume limit (JW §6.5)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **V1** | The continuum theory is on $\mathbb{R}^4$, not on a torus or finite volume | §4, "exists on $\mathbb{R}^4$" | The continuum limit is taken on $\mathbb{R}^4$ |
| **V2** | The mass gap is uniform in the volume of space-time | §6.5, "uniform in the volume of space-time" | Volume-independent mass gap bound; verified through the Volume Cancellation Lemma |
| **V3** | The infinite-volume limit $\mathbb{T}^4 \to \mathbb{R}^4$ is constructed | §6.5 | Section 5.7(e) constructs the infinite-volume limit |
| **V4** | Both limits ($a \to 0$ and $L \to \infty$) commute, or can be taken simultaneously | Implicit in "exists on $\mathbb{R}^4$" | Moore–Osgood theorem applied with uniform-in-$L$ Cauchy bounds |

#### Group N — Non-triviality (JW §4)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **N1** | The constructed theory is **non-trivial** | §4, "a **non-trivial** quantum Yang–Mills theory exists" | Explicitly proved (Proposition (Non-triviality) in §5.7) |
| **N2** | The theory is not the free / Gaussian theory | Inferred from "non-trivial" | At least one connected $n$-point function with $n \geq 3$ is nonzero (Corollary F5.1) |
| **N3** | Some interpretation: non-trivial $S$-matrix, OR non-vanishing connected 2-point with positive glueball overlap, OR string tension $\sigma > 0$ | §6.2 cites "non-trivial scattering" | At least one of these established; ideally the strong-coupling lower bound on $\langle 1\|s_P\|0 \rangle$ |

#### Group G — Gauge group (JW §4)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **G1** | The theorem holds for **any compact simple gauge group** $G$, not just SU($N$) | §4, "for any compact simple gauge group $G$" | Explicitly stated and proved |
| **G2** | Specifically, all of: SU($N$) ($N \geq 2$), SO($N$) ($N \geq 3$, $N \neq 4$), Sp($N$) ($N \geq 1$), and the five exceptional groups $G_2, F_4, E_6, E_7, E_8$ | The classification of compact simple Lie groups | Appendix I.4 (general groups) and Appendix K (Balaban for general $G$) |

#### Group WE — No weak-existence-only solution (JW §6.6 footnote 2)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **WE1** | Properties of the limit (mass gap and axioms) are established for the actual constructed limit, not asserted on a hypothetical limit obtained by Banach–Alaoglu compactness alone | Footnote 2, verbatim binding statement | The mass gap is established by RG telescoping (convergent series), not by compactness; OS axioms verified by uniform bounds |
| **WE2** | If a subsequential limit is used, the properties must propagate through the limit | Footnote 2 implication | Theorem M.2.1 (Appendix M) shows uniqueness — the Schwinger functions converge, not just subsequentially |

#### Group CL — Clustering (JW §5)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **CL1** | Clustering follows from the mass gap, with the explicit quantitative bound $\|\langle\Omega, \mathcal{O}(\vec x)\mathcal{O}(\vec y)\Omega\rangle\| \leq \exp(-C\|\vec x - \vec y\|)$ for $C < \Delta$ | §5 verbatim | Established via OS4 cluster axiom + spectral theorem |

#### Group YM — Yang-Mills equations / dynamics (JW §1, §6.5)

| ID | Requirement | JW source | Pass criterion |
|:---|:------------|:----------|:---------------|
| **YM1** | The constructed theory is the quantization of the Yang–Mills Lagrangian (Eq. 1 in JW): $L = (1/4g^2)\int \mathrm{Tr}\,F \wedge \star F$ | §1 (Lagrangian) + §6.5 (extension to field functions) | Field operators satisfy the YM equations of motion in the distributional sense (Schwinger–Dyson identities verified in §5.7) |
| **YM2** | Gauge invariance is manifest in the final theory | §1 (gauge structure) + §6.5 | All observables are gauge-invariant; no gauge-fixing artifacts in the limit |

#### Group H4 — H4 hypothesis verification (NEW for r01)

The gradient-flow construction in Appendix L closes Conjectures L.1
and L.3 unconditionally, but L.2 (AF short-distance match) and the AF
form of L.4 (OPE leading singularity) are stated **conditional on
Hypothesis H4**:

> *Hypothesis H4: Non-perturbative Schwinger functions of the
> renormalized composite operators agree with perturbation theory at
> short distances.*

H4 is the standard assumption underlying all of lattice QCD
phenomenology. It has been verified numerically to extraordinary
precision but never proved rigorously for any 4D non-Abelian gauge
theory. The gradient-flow framework reduces H4 to a more tractable
form: it becomes "do the Taylor coefficients of the analytic function
$F(t)$ at $t=0$ agree with Feynman-rule computations?"

**Your job for the H4 group is NOT to grade results that depend on
H4. Your job is to verify that the H4 story itself meets Clay's
standards.** The honest statement of an open hypothesis is part of
Clay rigor, not a weakness — but the handling must be consistent and
the unconditional claims must be cleanly separated from the
H4-conditional ones.

| ID | Verification check | Pass criterion |
|:---|:-------------------|:---------------|
| **H4-1** | Hypothesis H4 is stated precisely in Section L.7 of Appendix L as a single, unambiguous mathematical claim — not as a vague assumption or boilerplate caveat | Section L.7 contains a precise theorem-environment statement |
| **H4-2** | Every result depending on H4 (L.1(iii), L.2, AF form of L.4) is explicitly flagged "conditional on H4" in its theorem statement, not just in surrounding prose | Theorem statements of Lemma L.4.2 and the AF form of Lemma L.4.3 say "conditional on H4" |
| **H4-3** | H4 is correctly identified as the standard lattice-QCD hypothesis (consistent with the Glimm–Jaffe / Symanzik / Wilson literature framing); the proof does not invent a new hypothesis or rename an existing one | H4 framing matches the standard "non-pert = pert at short distances" assumption |
| **H4-4** | The gradient-flow reduction of H4 (from "asymptotic series equals non-perturbative object" to "Taylor coefficients of the analytic function $F(t)$ at $t = 0$ agree with Feynman-rule computations") is mathematically sound and represents a genuine simplification | The reduction in Section L.7 is rigorous, not a sleight of hand |
| **H4-5** | The Clay submission's *unconditional* claims (mass gap, OS axioms, L.1(i)(ii), L.3, leading-order non-perturbative OPE structure) are clearly separated from the H4-conditional ones in every part of the preprint (abstract, conclusion, PROOF-CHAIN, Appendix L, Section 12.7) | Verified by inspection of all five locations |
| **H4-6** | Nothing in the abstract, conclusion, PROOF-CHAIN, or Appendix L overstates what is unconditional vs. conditional on H4. No marketing language obscures the H4 dependence. | Verified by inspection |

**Pass criterion for the H4 group:** all 6 checks PASS. If any one
fails, describe precisely what is overstated, missing, or unsound,
and rate the failure as a **closable presentation gap** (not a
genuine gap in the mathematics), since the underlying H4 framework
is honest.

**Important:** When grading results that depend on H4 in groups AF,
T, OPE, the verdict should be **PARTIAL ("PASS conditional on H4")**
— **NOT FAIL**. The honest statement of an open hypothesis is part
of Clay rigor.

---

For each item in groups A through H4, the report must contain a
one-paragraph status: **PASS** (with location in the preprint),
**FAIL** (with what is missing), **PARTIAL** (with what is covered
and what is not), or **PASS conditional on H4** (for AF / OPE / T6
results that depend on H4). This table is in addition to the
per-Point analysis below.

---

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

The current preprint extends Balaban's work to general compact simple
groups in **Appendix K** and uses Balaban's analyticity (B1) as input
to the gradient-flow construction in **Appendix L**.

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
8. **Composite operator construction by hand-waving.** Renormalized
   $[\mathrm{Tr}\,F^2]_R(x)$ "exists" without an explicit
   multiplicative renormalization or limit construction. (This is the
   one Appendix L addresses via gradient flow.)
9. **OPE asserted without proof.** The OPE is claimed to follow from
   some general principle without checking it.
10. **H4 left implicit.** Results that depend on H4 stated as if
    unconditional. (This is the one the H4 group above checks.)

### Recent Rigorous Results (2020--2026)

- Chatterjee (2021): strong mass gap implies confinement for groups
  with nontrivial center. **Finite gauge groups only.**
- Adhikari-Cao (2025): exponential decay at weak coupling for
  **finite gauge groups**, 3D abelian.
- Cao-Chatterjee (2024): state space for 3D Yang-Mills.
- **No rigorous mass gap result exists for continuous SU(N) in 4D.**
- Douglas (Nature Reviews Physics, 2025): no breakthroughs on the
  4D problem.

The current preprint, with Appendices L (gradient-flow), M (closures),
N (QG5D), and the gradient-flow programme, claims to be the first
such rigorous proof — closing all 11 Clay requirements modulo H4.
Your job is to verify or refute that claim.

## Files to Read (in order, before writing anything)

Read all of these before forming any judgments. **Note: this list
includes new files added since run r00 — Appendices L (rewritten), M,
N, and the updated PROOF-CHAIN with Steps 15–18.**

**Top-level structure (read first):**
1. `/Users/gsix/yang-mills/preprint/sections/00-abstract.md`
2. `/Users/gsix/yang-mills/preprint/PROOF-CHAIN.md`
   (now extended to Steps 1–18)
3. `/Users/gsix/yang-mills/preprint/TABLE-OF-CONTENTS.md`
4. `/Users/gsix/yang-mills/preprint/sections/08-conclusion.md`
   (especially the new Section 12.7 "Full Clay Compliance")

**Core lattice mass gap:**
5. `/Users/gsix/yang-mills/preprint/sections/04-lattice-proof-part1.md`
   (focus: Theorems 1--5, spectral gap, cluster expansion, IR equivalence)
6. `/Users/gsix/yang-mills/preprint/sections/05-continuum-limit.md`
   (focus: Sections 5.1--5.7 — the full continuum limit argument,
   including the new IV.5 forward reference to Appendix L)

**Geometric / spectral foundations:**
7. `/Users/gsix/yang-mills/preprint/sections/02-geometric-framework.md`
   (the CP$^{N-1}$ geometry and Weitzenböck formula)
8. `/Users/gsix/yang-mills/preprint/sections/A-laplacian-spectrum.md`
9. `/Users/gsix/yang-mills/preprint/sections/E-weitzenboeck.md`
10. `/Users/gsix/yang-mills/preprint/sections/D-reflection-positivity.md`
11. `/Users/gsix/yang-mills/preprint/sections/G-multi-time-slice-analysis.md`
12. `/Users/gsix/yang-mills/preprint/sections/H-balaban-analyticity.md`
13. `/Users/gsix/yang-mills/preprint/sections/F-area-law-mass-gap.md`

**N-dependence and general groups:**
14. `/Users/gsix/yang-mills/preprint/sections/I3-N-dependence-tracking.md`
15. `/Users/gsix/yang-mills/preprint/sections/I4-other-gauge-groups.md`
16. `/Users/gsix/yang-mills/preprint/sections/J-lattice-symanzik-basis.md`
17. `/Users/gsix/yang-mills/preprint/sections/I-gap-closures.md`
18. `/Users/gsix/yang-mills/preprint/sections/K-balaban-general-groups.md`
    (Balaban's RG verified for all compact simple gauge groups)

**Gap closures from referee r00:**
19. `/Users/gsix/yang-mills/preprint/sections/M-gap-closures-r00.md`
    (closes K-uniformity (H1)–(H2) and uniqueness of the continuum
    limit; preserves the full audit trail of which closures were made)

**The new gradient-flow construction (NEW for r01):**
20. `/Users/gsix/yang-mills/preprint/sections/L-clay-conjectures.md`
    (REPLACED — now "Gradient-Flow Construction of Local Operators";
    contains 19 lemmas L.1.1–L.4.3 closing Conjectures L.1–L.4)
21. `/Users/gsix/yang-mills/preprint/sections/N-qg5d-infrastructure.md`
    (QG5D cross-references for Appendix L's external inputs:
    Theorem K.1, Paper 10 Theorems, etc.)

**Reference materials in the references directory:**
22. `/Users/gsix/yang-mills/notation-less-math-referee/references/wikipedia-wightman-axioms.txt`
    (canonical W0–W3 axiom statements)
23. `/Users/gsix/yang-mills/notation-less-math-referee/references/wikipedia-os-axioms.txt`
    (canonical E0–E4 + linear growth condition / OS0' history)

**⚠️ Wikipedia is a known risk** for the canonical axiom statements.
The original peer-reviewed sources are Streater–Wightman, *PCT, Spin
and Statistics, and All That* (book, not freely available) and
Osterwalder–Schrader, "Axioms for Euclidean Green's functions,"
CMP 31 (1973) and CMP 42 (1975) (Project Euclid, currently
Incapsula-blocked from `curl`). The Wikipedia text is acceptable as a
*temporary* stand-in because it states the axioms in their canonical
form, but **you must list this limitation in the closing sentences of
your final summary** (see "Closing instructions" below).

## Your Task: Exhaustive Review

Scrutinize the entire proof chain from geometric foundations through
continuum QFT construction and the gradient-flow extension to L.1–L.4,
with particular focus on Clay Millennium Prize eligibility per the
verbatim Jaffe–Witten text quoted above.

You must produce two outputs:

1. **A `clay-checklist.md` file** containing all ~50 mandatory checks
   from the Group A / W / E / L / AF / T / OPE / R / V / N / G / WE /
   CL / YM / H4 tables above, with PASS / FAIL / PARTIAL / "PASS
   conditional on H4" verdict and a one-paragraph justification per
   item.

2. **Per-Point analysis files** (one per Point in the per-Point list
   below) with deep technical interrogation. Many of the per-Point
   findings will feed into the clay-checklist verdicts.

For each per-Point analysis, determine whether it is:

- **(A) GENUINE GAP** — invalidates the claimed result or prize eligibility
- **(B) CLOSABLE GAP** — can be closed with a short additional argument
  (state what is needed and estimate difficulty: 1 paragraph / 1 page /
  1 paper)
- **(C) SOUND** — correct as stated (explain why, precisely)

**Weight guide:** Points marked [HEAVY] require deep interrogation
with 4--5 sub-questions. Points marked [MEDIUM] require 3
sub-questions. Points marked [LIGHT] require 2 sub-questions
(verify and flag).

Prior review verdicts (if any survive in your context) are evidence,
not proof — your verdict is independent. If your analysis disagrees
with a prior verdict, override it and explain the disagreement.

---


## Part A: Geometric and Spectral Foundation


### Point A1: The Weitzenböck Spectral Gap on $\mathbb{CP}^{N-1}$ [LIGHT]

**Location:** Section 2, Appendix A, Appendix E

**The claim:** The Hodge Laplacian on 1-forms on $(\mathbb{CP}^{N-1},
g_{\mathrm{FS}})$ has spectral gap $\mu_1 \geq 6/r_3^2$ (for $N=3$) or
$\mu_1 \geq 2N/r_3^2$ (general $N$). This drives the KK mass
$m_1 = 2\sqrt{N}/r_3$ and the entire cluster expansion.

**Interrogate:**

(a) **The spectral bound.** Verify the Weitzenböck formula
$\Delta_1^H = \nabla^*\nabla + \mathrm{Ric}$ on 1-forms, with
$\mathrm{Ric} = (2N/r_3^2)\,g$ for the Fubini-Study metric. Is the
numerical coefficient correct for general $N$? Does the bound
$\mu_1 \geq 2N/r_3^2$ hold for all $N \geq 2$?

(b) **The connection to KK mass.** The paper derives
$m_1 = 2\sqrt{N}/r_3$ from the actual eigenvalue $\lambda_1 = 4N/r_3^2$
(Ikeda–Taniguchi 1978), not the Weitzenböck lower bound. Verify the
factor of $2\sqrt{N}$ and that the paper is consistent in distinguishing
the bound (used for safety) from the actual eigenvalue (used for $m_1$).


---


### Point A2: The KK Propagator Bound [LIGHT]

**Location:** Section 4, Lemma III.1

**The claim:** The propagator between neighboring lattice sites satisfies
$|g_b| \leq C_0 e^{-2\sqrt{N}\,a/r_3}$.

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
$\beta < a/(2\sqrt{N}\,r_3)$, giving $\sigma_0 > 0$ and
$\Delta_0 > 0$. In the physical regime ($a/r_3 \sim 10^{15}$),
this covers $\beta$ up to $\sim 10^{14}$.

**Interrogate:**

(a) **The Kotecký-Preiss criterion.** The convergence requires
$\sum_{X \ni x} |K(X)| \leq C_{\mathrm{KP}}$. Verify that the polymer
weights are bounded by $e^{-\kappa|X|}$ with the claimed $\kappa$.
Does $\kappa$ depend on $N$? Is the combinatorial bound on the number
of polymers of size $|X|$ correct for the $d = 4$ hypercubic lattice?

(b) **Physical regime coverage.** The bound $\beta <
a/(2\sqrt{N}\,r_3)$ is claimed to cover all practical couplings. But
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

**Location:** Section 5.1, Appendix K

**The claim:** Section 5.1 uses Balaban's results as a "black box":
UV stability, convergent polymer expansion, running coupling,
irrelevant operator bounds. These are stated as Literature results
from CMP 109, 119. **Appendix K** verifies the extension of Balaban's
program from SU(2) to general compact simple gauge groups in 9 sections
(543 lines).

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
SU(2). The preprint claims results for general compact simple gauge
groups via Appendix K. Walk through Appendix K (sections K.1–K.9) and
verify: are all 9 elements (group-theoretic data, propagator,
block-spin projection, large-field, Mayer expansion, running coupling,
axial gauge, analyticity (B1)–(B2), and the summary table) properly
generalized? Are the $G$-dependent constants finite for each fixed
$G$?

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

(e) **Appendix M closure of the K-uniformity gap.** Run r00 flagged
the "deferred" hypotheses (H1)–(H2) of the Cluster–Balaban Handoff
Lemma (Section 5.4.5) as the K-uniformity gap. Appendix M (Lemmas
M.1.1, M.1.2, Corollary M.1.3) closes this. Verify that the closure
is rigorous: does Lemma M.1.1 actually establish the K-uniform
cluster expansion rate, and does Lemma M.1.2 establish the K-uniform
Balaban analyticity radius? Is the §5.4.6 statement now consistent
with the PROOF-CHAIN claim of "Proved" for Step 10b?


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
Could an operator satisfy Definition D.2 but not give the
$\hat{\Delta}^p$ bound, or vice versa?

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
element $\langle 1|\delta E_k^{d=6}|1\rangle_c$?

(d) **The transition from perturbative to non-perturbative.** The
previous referee (r05, Point 1d) initially flagged this as a GENUINE
GAP, then revised to CLOSABLE after careful re-examination. Verify
that the dimension-4 projection (subtracting $S_{\mathrm{YM}}/g_k^2$)
is well-defined non-perturbatively, and that "dimension-6" can be
unambiguously separated from "dimension-4 + dimension-8 + ..." at
the level of the full non-perturbative effective action.

(e) **Structural zero vs. kinematic zero.** The diagonal vanishing
$(e^{E_1 - E_1} - 1)^2 = 0$ is claimed to be structural (arising from
the squared-derivative structure of dim-6 operators) rather than
kinematic. Verify the structural argument.


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
(multi-particle) differently. Trace the bound precisely.

(b) **The $\zeta$ bound and the two-particle threshold.** The sum
$\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ requires $E_2 - E_1 > 0$
(spectral gap above the one-particle state). The preprint bounds the
binding energy $\epsilon_B \leq C_B g_k^4 \hat{\Delta}_k$. This uses
perturbative estimates (Born approximation, Lippmann-Schwinger). Are
perturbative binding energy estimates valid non-perturbatively?

(c) **Volume independence via Hastings–Koma.** The Hastings–Koma
clustering estimate (Section 5.5.3, Step 3(i)) controls the sum over
states by exploiting locality. Verify the K-uniformity claim.


---


### Point D4: The Single-Step Coefficient Bound [LIGHT]

**Location:** Section 5.3.2, Section 5.6 Part III.5

**The claim:** $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq
C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$.

**Interrogate:**

(a) **The $g_k^4$ factor.** Verify that the spectral lemma with
$M = C g_k^4$ and $\mathrm{dev} \geq 2$ gives $C_2 \cdot C g_k^4 \cdot
\hat{\Delta}^2 = C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ as claimed.

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
the gap condition for Kato perturbation satisfied?

(c) **The Gronwall bound.** The product $\prod(1 + \alpha g_j^2) \leq
k^{\alpha/(b_0 \ln 2)}$ gives polynomial growth. Is the exponent
$\gamma = \alpha/(b_0 \ln 2)$ bounded for all $N$?


---


### Point E2: Convergence of the Sum [LIGHT]

**Location:** Section 5.4.6

**The claim:** $\sum_k C_k g_k^4 \hat{\Delta}_k^2 < \infty$.

**Interrogate:**

(a) **The doubly exponential convergence.** With $C_k \sim k^\gamma$,
$g_k^4 \sim 1/k^2$, $\hat{\Delta}_k^2 \sim 4^{-k}$: the sum is
$\sum k^{\gamma-2} 4^{-k}$, which converges for all $\gamma$. Verify
the estimates.

(b) **The starting constant $C_0$.** At $k = 0$, $\hat{\Delta}_0 \sim
O(1)$ and $C_0$ comes from the cluster expansion. Is $C_0$ explicitly
bounded?


---


## Part F: Continuum QFT Construction

### Point F1: The OS Axioms — Simultaneous Verification [MEDIUM]

**Location:** Section 5.7(f)

**The claim:** OS1--OS5 hold simultaneously for the limiting Schwinger
functions.

**Interrogate:**

(a) **OS0' linear growth condition.** Verify that the bound on $S_n$
satisfies the corrected (1975) linear growth condition with a
Schwartz seminorm index growing linearly in $n$.

(b) **The diagonal extraction.** A single Banach-Alaoglu subsequence
$a_j \to 0$ is extracted such that $S_n^{(a_j)} \to S_n$ for all $n$
simultaneously. Is the diagonal argument valid?

(c) **Coincident-point singularities.** The bound $|S_n| \leq n! C_0^n$
is a pointwise bound away from coincident points. Are coincident-point
singularities controlled?


---


### Point F2: Reflection Positivity — The Full Chain [MEDIUM]

**Location:** Appendix D, Section 5.7(f) OS3

**The claim:** Reflection positivity holds for the Wilson action
(Osterwalder-Seiler 1978), and is preserved in the continuum limit
by lower semicontinuity.

**Interrogate:**

(a) **Lattice reflection positivity.** Does the KK-enhanced theory
satisfy RP? Verify Lemma D.2.

(b) **RP through the RG.** Does the proof require RP at intermediate
scales, or only at the final scale?

(c) **RP in the continuum limit.** Verify the Portmanteau / lower
semicontinuity argument.


---


### Point F3: The Thermodynamic Limit [MEDIUM]

**Location:** Section 5.7(e)

**The claim:** The limits $a \to 0$ and $L \to \infty$ commute, via
the Moore-Osgood theorem, with explicit volume-cancellation arguments.

**Interrogate:**

(a) **Uniformity in $L$.** The bound $|C_{k+1}(L) - C_k(L)| \leq
C' g_k^4 (a_k \Lambda)^s$ is claimed volume-independent. Verify the
Volume Cancellation Lemma in §5.7(e).

(b) **The infinite-volume mass gap.** Is the convergence rate in $L$
uniform in $a$?

(c) **Exponential clustering in finite volume.** Is the finite-volume
spectral gap bounded below uniformly in $L$?


---


### Point F4: Uniqueness of the Continuum Limit [HEAVY]

**Location:** Section 5.7, Appendix M (Theorem M.2.1)

**Binding rule (Jaffe–Witten §6.6, footnote 2):** *"We specifically
exclude weak-existence (compactness) as the solution to the existence
part of the Millennium problem, unless one also uses other techniques
to establish properties of the limit (such as the existence of a
mass gap and the axioms)."*

**The claim:** The preprint claims $\Delta_\infty > 0$ for the
continuum theory. Theorem M.2.1 (Appendix M) further claims that the
Schwinger functions converge **uniquely** (not just subsequentially)
via a Cauchy argument.

**Interrogate:**

(a) **Theorem M.2.1.** Walk through the Cauchy argument in Appendix M.
Is the telescoping sum $S_n^{(K_2)} - S_n^{(K_1)}$ controlled by the
RG bounds? Does the Cauchy property in $a$ hold?

(b) **Does this satisfy footnote 2?** With Theorem M.2.1, the proof
establishes uniqueness of the continuum limit, not just existence of
some subsequential limit. Verify that this addresses the
weak-existence-only exclusion.

(c) **Subsequence dependence of $\Delta_\infty$.** Is the mass gap
value subsequence-independent (as claimed in Section 5.7)?

(d) **The mass gap value.** Verify that $C_\infty$ and $\Lambda_\infty$
are determined by convergent series independent of the extraction.


---


### Point F5: OS Reconstruction to Wightman Theory [HEAVY]

**Location:** Section 5.7(f), Reconstruction

**The claim:** The OS reconstruction theorem gives a Wightman QFT on
$\mathbb{R}^{3,1}$ with separable Hilbert space, Poincaré
representation, unique vacuum, and mass gap
$\mathrm{spec}(P^2) \subseteq \{0\} \cup [\Delta_\infty^2, \infty)$.

**Interrogate:**

(a) **The OS reconstruction theorem — which version?** The 1975
corrected version is required (the 1973 version had a known gap).
Verify that the corrected version is cited.

(b) **The Hilbert space.** The reconstructed Hilbert space
$\mathcal{H}$ is obtained from the GNS construction. Is the
inner product positive-definite?

(c) **Non-triviality.** Verify the explicit non-triviality argument
(Proposition (Non-triviality) in §5.7).

(d) **The Yang-Mills equations of motion.** Does the reconstructed
Wightman theory satisfy the Yang-Mills equations of motion in the
distributional sense? Verify the Schwinger–Dyson identity argument
in §5.7.


---


## Part G: Clay Compliance and Cross-Cutting Issues

### Point G1: Jaffe-Witten Requirements [HEAVY]

**Location:** Abstract, Section 5.7, Section 12.7, overall proof structure

**The claim:** The preprint proves the Yang-Mills mass gap for any
compact simple gauge group $G$ in four dimensions, plus the four
Clay structural ingredients (L.1, L.2, L.3, L.4) via the gradient-flow
construction (Appendix L), solving the Clay Millennium Problem.

**Interrogate:**

(a) **The KK device.** The proof uses the KK-enhanced theory
(with $\mathbb{CP}^{N-1}$ fibers) as a proof device, then transfers
the mass gap to the standard theory via Theorem 5. Is the KK
enhancement fully decoupled in the final theory? Does the proof chain
constitute a proof for the **standard** Yang-Mills theory?

(b) **The gauge group.** Jaffe-Witten requires the result for
"any compact simple gauge group $G$." Appendix I.4 covers SO, Sp, and
the exceptional groups; Appendix K verifies Balaban for general $G$.
Verify both.

(c) **The lattice regulator.** Is the final continuum theory
independent of the lattice regularization? (This is the universality
question.)

(d) **The precise claim.** State exactly what is proved. Section 12.7
"Full Clay Compliance" claims 11/11 PASS (9 unconditional, 2
conditional on H4). Verify each line of the C1–C11 table in Section
12.7 against the actual content.

(e) **The four structural ingredients (Appendix L).** With Appendix L,
the four Clay structural ingredients are now constructed. Walk
through Lemmas L.4.1 (stress tensor), L.4.2 (AF match), L.4.3 (OPE
leading order). Are all 19 lemmas (L.1.1–L.4.3) actually proved, with
no missing dependencies?

(f) **The quantitative predictions.** The preprint makes quantitative
predictions ($\sqrt{\sigma} = 437$ MeV, etc.). Ensure the proof
does not rely on numerical agreement with experiment as evidence for
correctness.


---


### Point G2: Gauge Invariance Through the RG [MEDIUM]

**Location:** Section 5.1, Section 5.6

**The claim:** Balaban's block-spin preserves gauge invariance:
the effective action $S_k[V]$ is gauge-invariant at each step $k$.

**Interrogate:**

(a) **Axial gauge fixing.** Are the spurious singularities of axial
gauge present on the lattice, or are they a continuum artifact?

(b) **The Gribov problem.** Does the block-spin transformation
introduce Gribov-type ambiguities at intermediate scales?

(c) **Gauge invariance of the final result.** Is the final continuum
theory gauge-invariant?


---


### Point G3: $N$-Dependence and Error Propagation [MEDIUM]

**Location:** Throughout, Appendix I.3

**The claim:** The proof works uniformly for all SU($N$), $N \geq 2$,
and (via Appendix I.4 + K) for all compact simple gauge groups.

**Interrogate:**

(a) **$N$-dependent constants.** Track the $N$-dependence through
the proof chain. Does any constant grow so fast with $N$ that the
proof fails for large $N$?

(b) **SU(2) special properties.** Does the proof use any
SU(2)-specific property that doesn't generalize to $N \geq 3$?

(c) **Error compounding.** With ~14 steps for the mass gap and ~19
lemmas for the gradient-flow construction, is the accumulated error
bounded? Verify that for each fixed $N$, the constants are finite.


---


### Point G4: Local Field Operators, Stress Tensor, OPE, and AF Matching [HEAVY]

**Location:** Appendix L (now constructed), PROOF-CHAIN Steps 17–18

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

In run r00 this Point was a GENUINE GAP (Conjectures L.1–L.4 stated
as open). In r01, **Appendix L (the new "Gradient-Flow Construction
of Local Operators") closes all four conjectures**, with L.1 and L.3
unconditional and L.2 + L.4-AF-form conditional on H4. Verify the
closure.

**Interrogate:**

(a) **Local field operators in correspondence with curvature
polynomials.** Lemma L.3.8 constructs $[\mathrm{Tr}\,F^2]_R(x)$ as
the $t \to 0^+$ limit of the gradient-flow smeared operator. Is
the construction rigorous? Does it produce an operator-valued
distribution on the GNS Hilbert space, not just a Schwinger function
limit? Walk through the GNS reconstruction step.

(b) **Short-distance match to perturbative AF.** Lemma L.4.2
establishes the AF match conditional on H4. Verify that the leading-
order coefficient $C_N = 2(N^2 - 1)/\pi^6$ matches the perturbative
prediction. Verify that subleading corrections are bounded by the
$\mathrm{dev} \geq 2$ classification.

(c) **Stress tensor.** Lemma L.4.1 constructs $T_{\mu\nu}^R$ via
Suzuki's formula. Verify all five sub-clauses (T1–T6 above) explicitly:
existence, symmetry, conservation, gauge invariance, $H = \int T_{00}$,
trace anomaly.

(d) **Operator product expansion.** Lemma L.4.3 establishes the
leading-order OPE. Verify the identity-channel coefficient and the
subleading-channel control via $\mathrm{dev} \geq 2$.

(e) **The 19 lemmas (L.1.1–L.4.3) in detail.** Walk through the
dependency chain. Are all 19 lemmas individually proved, with no
missing dependencies and no circular reasoning? The synthesis report
(W8-16-synthesis.md, available in
`/Users/gsix/yang-mills/gradient-flow-attack-plan/research/`) gives
the dependency graph; verify it.


---


### Point G5: H4 — The Standard Hypothesis (NEW for r01) [HEAVY]

**Location:** Appendix L, Section L.7

**The claim:** Hypothesis H4 (non-perturbative = perturbative at
short distances) is the single open hypothesis in the proof. It is
documented in Section L.7 with a precise statement, every result
that depends on it is consistently flagged "conditional on H4," and
the gradient-flow framework reduces H4 to a Taylor-coefficient
question about a single analytic function $F(t)$ at $t = 0$.

**Your job is NOT to prove H4 or to grade results that depend on
H4 as failed. Your job is to verify that the H4 story itself meets
Clay's standards.**

**Interrogate (per the H4 group above):**

(a) **H4-1: precise statement.** Is Hypothesis H4 stated precisely
in Section L.7 of Appendix L as a single, unambiguous mathematical
claim? Quote it.

(b) **H4-2: consistent flagging.** Are all H4-conditional results
(L.1(iii), L.2, AF form of L.4) explicitly flagged "conditional on
H4" in their theorem statements (not just in surrounding prose)?

(c) **H4-3: correct identification.** Is H4 correctly identified as
the standard lattice-QCD hypothesis? Does the framing match the
Glimm-Jaffe / Symanzik / Wilson literature, or does it invent a new
hypothesis?

(d) **H4-4: gradient-flow reduction.** Is the reduction (from
"asymptotic series equals non-perturbative object" to "Taylor
coefficients of $F(t)$ at $t = 0$ agree with Feynman-rule
computations") mathematically sound?

(e) **H4-5: clean separation.** Are the unconditional claims (mass
gap, OS axioms, L.1(i)(ii), L.3, leading-order non-perturbative OPE
structure) cleanly separated from the H4-conditional ones in every
part of the preprint? Check the abstract, conclusion, PROOF-CHAIN,
Appendix L, and Section 12.7 individually.

(f) **H4-6: no overstatement.** Does the abstract, conclusion, or
PROOF-CHAIN overstate what is unconditional vs. conditional on H4?
Is there any marketing language that obscures the H4 dependence?


---


## Output Format

Write all your report files into:
`/Users/gsix/yang-mills/notation-less-math-referee/latest-run/`

This directory was created empty by `code/setup-venv.sh` at the start
of this session. Any prior run was automatically archived into
`/Users/gsix/yang-mills/notation-less-math-referee/runs/r{NN}/`
before you started.

**Do NOT read anything inside `notation-less-math-referee/runs/`.**
Past runs are out of scope by design — your verdict must be
independent. The archive exists for human inspection across cycles,
not for you.

### Directory layout (mandatory)

**Do NOT write giant monolithic files.** Organize the output as a
directory tree with one file per sub-question (for Points) and one
file per check ID (for the mandatory checks). The next reader should
be able to navigate by `ls`, not by scrolling through 2000-line
documents.

The required layout is:

```
latest-run/
├── INDEX.md                           ← navigation: every file with one-line description
├── clay-checklist.md                  ← master roll-up table (~58 rows)
├── summary.md                         ← overall verdict + closing disclosures
├── computation-log.md                 ← every "verified in venv" note collected
├── points/                            ← per-Point deep technical interrogation
│   ├── A1-weitzenboeck/
│   │   ├── 00-statement.md            ← the claim being interrogated
│   │   ├── 01-spectral-bound.md       ← sub-question (a)
│   │   ├── 02-kk-mass-connection.md   ← sub-question (b)
│   │   └── verdict.md                 ← SOUND / CLOSABLE / GENUINE + impact
│   ├── A2-kk-propagator/
│   │   ├── 00-statement.md
│   │   ├── 01-transfer-matrix.md      ← (a)
│   │   ├── 02-constant-c0.md          ← (b)
│   │   └── verdict.md
│   ├── A3-bogomolny/
│   │   ├── 00-statement.md
│   │   ├── 01-lattice-instantons.md
│   │   ├── 02-c2-restriction.md
│   │   └── verdict.md
│   ├── B1-cluster-expansion/
│   │   ├── 00-statement.md
│   │   ├── 01-kp-criterion.md
│   │   ├── 02-physical-regime.md
│   │   ├── 03-connected-bounds.md
│   │   └── verdict.md
│   ├── B2-fredenhagen-marcu/
│   │   ├── 00-statement.md
│   │   ├── 01-precise-conditions.md
│   │   ├── 02-direction.md
│   │   └── verdict.md
│   ├── B3-feshbach/
│   │   ├── 00-statement.md
│   │   ├── 01-feshbach-decomposition.md
│   │   ├── 02-trace-norm.md
│   │   ├── 03-factorization.md
│   │   └── verdict.md
│   ├── C1-uv-stability/             ← HEAVY: 5 sub-files
│   │   ├── 00-statement.md
│   │   ├── 01-effective-action.md
│   │   ├── 02-gauge-group-K.md      ← walk through Appendix K
│   │   ├── 03-remainder-bound.md
│   │   ├── 04-running-coupling.md
│   │   ├── 05-appendix-M-closure.md ← K-uniformity (H1)–(H2) via Appendix M
│   │   └── verdict.md
│   ├── C2-large-small-field/
│   │   ├── 00-statement.md
│   │   ├── 01-small-field-condition.md
│   │   ├── 02-large-field-suppression.md
│   │   ├── 03-gauge-invariance.md
│   │   └── verdict.md
│   ├── C3-coupling-overlap/
│   │   ├── 00-statement.md
│   │   ├── 01-overlap-region.md
│   │   ├── 02-transition.md
│   │   └── verdict.md
│   ├── D1-dim6-classification/
│   │   ├── 00-statement.md
│   │   ├── 01-luscher-weisz.md
│   │   ├── 02-second-derivative-op.md
│   │   ├── 03-lattice-artifacts.md
│   │   └── verdict.md
│   ├── D2-deviation-order/          ← HEAVY: 5 sub-files
│   │   ├── 00-statement.md
│   │   ├── 01-definition.md
│   │   ├── 02-linear-combination.md
│   │   ├── 03-analyticity-role.md
│   │   ├── 04-pert-to-nonpert.md
│   │   ├── 05-structural-vs-kinematic.md
│   │   └── verdict.md
│   ├── D3-spectral-lemma/
│   │   ├── 00-statement.md
│   │   ├── 01-deviation-extraction.md
│   │   ├── 02-zeta-bound.md
│   │   ├── 03-volume-independence.md
│   │   └── verdict.md
│   ├── D4-single-step/
│   │   ├── 00-statement.md
│   │   ├── 01-gk4-factor.md
│   │   ├── 02-non-pert-corrections.md
│   │   └── verdict.md
│   ├── E1-inductive-stability/
│   │   ├── 00-statement.md
│   │   ├── 01-quarter-contraction.md
│   │   ├── 02-wave-function.md
│   │   ├── 03-gronwall.md
│   │   └── verdict.md
│   ├── E2-convergence-sum/
│   │   ├── 00-statement.md
│   │   ├── 01-doubly-exponential.md
│   │   ├── 02-starting-c0.md
│   │   └── verdict.md
│   ├── F1-os-axioms/
│   │   ├── 00-statement.md
│   │   ├── 01-os0-prime.md
│   │   ├── 02-diagonal-extraction.md
│   │   ├── 03-coincident-points.md
│   │   └── verdict.md
│   ├── F2-reflection-positivity-chain/
│   │   ├── 00-statement.md
│   │   ├── 01-lattice-rp.md
│   │   ├── 02-rp-through-rg.md
│   │   ├── 03-continuum-rp.md
│   │   └── verdict.md
│   ├── F3-thermodynamic-limit/
│   │   ├── 00-statement.md
│   │   ├── 01-uniformity-L.md
│   │   ├── 02-infinite-volume-gap.md
│   │   ├── 03-finite-volume-clustering.md
│   │   └── verdict.md
│   ├── F4-uniqueness/               ← HEAVY: 4 sub-files (incl. Theorem M.2.1)
│   │   ├── 00-statement.md
│   │   ├── 01-theorem-M21.md
│   │   ├── 02-footnote-2.md
│   │   ├── 03-subsequence-dependence.md
│   │   ├── 04-mass-gap-value.md
│   │   └── verdict.md
│   ├── F5-os-reconstruction/        ← HEAVY: 4 sub-files
│   │   ├── 00-statement.md
│   │   ├── 01-os-version.md
│   │   ├── 02-hilbert-space.md
│   │   ├── 03-non-triviality.md
│   │   ├── 04-ym-equations.md
│   │   └── verdict.md
│   ├── G1-jaffe-witten/             ← HEAVY: 6 sub-files
│   │   ├── 00-statement.md
│   │   ├── 01-kk-device.md
│   │   ├── 02-gauge-group.md
│   │   ├── 03-lattice-regulator.md
│   │   ├── 04-precise-claim.md
│   │   ├── 05-appendix-L.md         ← walk through Lemmas L.1.1–L.4.3
│   │   ├── 06-quantitative-predictions.md
│   │   └── verdict.md
│   ├── G2-gauge-invariance/
│   │   ├── 00-statement.md
│   │   ├── 01-axial-gauge.md
│   │   ├── 02-gribov.md
│   │   ├── 03-final-result.md
│   │   └── verdict.md
│   ├── G3-N-dependence/
│   │   ├── 00-statement.md
│   │   ├── 01-N-constants.md
│   │   ├── 02-su2-special.md
│   │   ├── 03-error-compounding.md
│   │   └── verdict.md
│   ├── G4-clay-structural-ingredients/  ← HEAVY: 5 sub-files
│   │   ├── 00-statement.md
│   │   ├── 01-local-operators.md     ← Lemma L.3.8
│   │   ├── 02-af-match.md            ← Lemma L.4.2
│   │   ├── 03-stress-tensor.md       ← Lemma L.4.1 + T1–T6
│   │   ├── 04-ope.md                 ← Lemma L.4.3
│   │   ├── 05-19-lemmas-walk.md      ← dependency chain audit
│   │   └── verdict.md
│   └── G5-h4-hypothesis/             ← HEAVY: 6 sub-files (H4-1..H4-6)
│       ├── 00-statement.md
│       ├── 01-h4-precise.md          ← H4-1: precise statement in §L.7
│       ├── 02-h4-flagging.md         ← H4-2: theorem-statement flagging
│       ├── 03-h4-identification.md   ← H4-3: standard hypothesis framing
│       ├── 04-h4-reduction.md        ← H4-4: gradient-flow reduction soundness
│       ├── 05-h4-separation.md       ← H4-5: clean unconditional/conditional split
│       ├── 06-h4-no-overstatement.md ← H4-6: no marketing-language obscuration
│       └── verdict.md
├── checks/                            ← per-ID Clay-mandatory checks
│   ├── A-mass-gap/
│   │   ├── A1.md
│   │   ├── A2.md
│   │   ├── A3.md
│   │   ├── A4.md
│   │   └── A5.md
│   ├── W-wightman/
│   │   ├── W0.md
│   │   ├── W1.md
│   │   ├── W2.md
│   │   ├── W3.md
│   │   ├── W4.md
│   │   ├── W5.md
│   │   ├── W6.md
│   │   └── W7.md
│   ├── E-os/
│   │   ├── E0.md
│   │   ├── E0-prime.md       ← OS0' linear growth condition
│   │   ├── E1.md
│   │   ├── E2.md
│   │   ├── E3.md
│   │   ├── E4.md
│   │   └── E-Rec.md          ← reconstruction theorem version
│   ├── L-local-operators/
│   │   ├── L1.md
│   │   ├── L2.md
│   │   ├── L3.md
│   │   └── L4.md
│   ├── AF-asymptotic-freedom/
│   │   ├── AF1.md
│   │   └── AF2.md
│   ├── T-stress-tensor/
│   │   ├── T1.md
│   │   ├── T2.md
│   │   ├── T3.md
│   │   ├── T4.md
│   │   ├── T5.md
│   │   └── T6.md
│   ├── OPE-ope/
│   │   ├── OPE1.md
│   │   ├── OPE2.md
│   │   └── OPE3.md
│   ├── R-reflection-positivity/
│   │   ├── R1.md
│   │   ├── R2.md
│   │   ├── R3.md
│   │   └── R4.md
│   ├── V-volume/
│   │   ├── V1.md
│   │   ├── V2.md
│   │   ├── V3.md
│   │   └── V4.md
│   ├── N-non-triviality/
│   │   ├── N1.md
│   │   ├── N2.md
│   │   └── N3.md
│   ├── G-gauge-group/
│   │   ├── G1.md
│   │   └── G2.md
│   ├── WE-weak-existence/
│   │   ├── WE1.md
│   │   └── WE2.md
│   ├── CL-clustering/
│   │   └── CL1.md
│   ├── YM-yang-mills/
│   │   ├── YM1.md
│   │   └── YM2.md
│   └── H4-hypothesis/
│       ├── H4-1.md
│       ├── H4-2.md
│       ├── H4-3.md
│       ├── H4-4.md
│       ├── H4-5.md
│       └── H4-6.md
```

**No file in this tree should exceed ~300 lines.** If any single file
runs longer, split it further. The structure is designed so that the
sub-question files in `points/X*-name/` correspond exactly to the
interrogation sub-questions (a)/(b)/(c)/... in the per-Point sections
of this prompt.

### File templates

**`points/<point-id>/00-statement.md`** — one short page:

```markdown
## Point [ID]: [Title]

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Location in preprint:** [section reference]

**The claim:**
[The exact claim from the prompt's Point description, paraphrased
for clarity if needed.]

**Sub-questions to be answered (one file each):**
- (a) [01-...md]
- (b) [02-...md]
- (c) [03-...md]
...
```

**`points/<point-id>/0N-<sub-question-name>.md`** — one sub-question
per file:

```markdown
## Point [ID]([letter]): [Sub-question title]

**The question:**
[Quote the sub-question from the prompt verbatim.]

**Finding:**
[Detailed answer. Quote the relevant claims from the preprint.
Do not be diplomatic. If sound, explain why fully. If a gap,
state exactly what additional mathematics is needed.]

**Computational verification (if applicable):**
[Result of any sympy/mpmath check, with the exact code in
`code/<descriptor>/check.py` if non-trivial. Note here that the
result was added to `computation-log.md`.]

**Verdict for this sub-question:**
[SOUND / CLOSABLE GAP / GENUINE GAP, with one-line justification.]
```

**`points/<point-id>/verdict.md`** — the roll-up:

```markdown
## Point [ID]: [Title] — Verdict

**Weight:** [HEAVY / MEDIUM / LIGHT]
**Overall verdict:** [GENUINE GAP / CLOSABLE GAP / SOUND]

**Sub-question verdicts:**
- (a) [01-...md]: SOUND / CLOSABLE / GENUINE — [one line]
- (b) [02-...md]: SOUND / CLOSABLE / GENUINE — [one line]
...

**Combined finding:**
[1–2 paragraphs synthesizing the sub-question findings. The
roll-up should be a faithful summary, not a re-derivation.]

**If this is a gap:**
- **Difficulty:** [1 paragraph / 1 page / 1 paper]
- **What is needed:** [precise statement]

**Impact on the claimed result:**
[Does this affect: (i) the main claim Δ_∞ > 0,
(ii) a Clay structural ingredient (L.1–L.4),
(iii) the H4 handling, or (iv) Clay prize eligibility overall?]
```

**`checks/<group>/<id>.md`** — one short file per check ID (target:
30–80 lines):

```markdown
## Check [ID]: [Title]

**Group:** [A / W / E / L / AF / T / OPE / R / V / N / G / WE / CL / YM / H4]
**JW source:** [page / section / verbatim phrase]
**Pass criterion (from prompt):** [quote the criterion]

**Verdict:** [PASS / PARTIAL / FAIL / PASS conditional on H4]

**Justification:**
[One paragraph: where in the preprint this is established (with file
+ section), what exactly was verified, and how it satisfies the
pass criterion.]

**Cross-references:**
- Per-Point file(s): [points/<point-id>/...]
- Computation log entry (if any): [computation-log.md#<anchor>]
```

**`clay-checklist.md`** — master roll-up of all check files:

```markdown
# Clay Compliance Checklist (master roll-up)

| ID | Verdict | One-line summary | File |
|:---|:--------|:-----------------|:-----|
| A1 | PASS | Δ > 0 proved via PROOF-CHAIN Step 14 | checks/A-mass-gap/A1.md |
| A2 | PASS | m < ∞ from glueball state existence | checks/A-mass-gap/A2.md |
| ... | ... | ... | ... |
| H4-6 | PASS | No overstatement found in audit | checks/H4-hypothesis/H4-6.md |

**Totals:**
- PASS unconditional: ___
- PASS conditional on H4: ___
- PARTIAL: ___
- FAIL: ___
```

**`computation-log.md`** — single file collecting every venv-verified
result, so the next cycle can audit at a glance:

```markdown
# Computation Log

Every numerical / symbolic check verified in
`code/.venv` during this run, with package, command, result, and
the file(s) that cite the result.

## C-001: Ricci coefficient on CP^{N-1}
- **Tool:** sympy
- **Script:** code/spectral-checks/ricci.py
- **Claim verified:** Ric = (2N/r3^2)·g for N=2,3,4,5
- **Result:** Confirmed; matches Theorem 1
- **Cited in:** points/A1-weitzenboeck/01-spectral-bound.md

## C-002: KK mass m_1 = 2√N/r_3
- **Tool:** sympy
- ...
```

**`INDEX.md`** — directory listing with one-line descriptions:

```markdown
# latest-run/ index

| Path | Type | Content |
|:-----|:-----|:--------|
| `clay-checklist.md` | master | Roll-up of all ~58 checks |
| `summary.md` | master | Overall verdict + closing disclosures |
| `computation-log.md` | log | Every venv-verified result |
| `points/A1-weitzenboeck/00-statement.md` | statement | Weitzenböck spectral gap claim |
| `points/A1-weitzenboeck/01-spectral-bound.md` | sub-question (a) | Verify Ricci coefficient |
| `points/A1-weitzenboeck/02-kk-mass-connection.md` | sub-question (b) | Verify $m_1 = 2\sqrt{N}/r_3$ |
| `points/A1-weitzenboeck/verdict.md` | verdict | Roll-up for Point A1 |
| ... | ... | ... |
| `checks/A-mass-gap/A1.md` | check | Δ > 0 verification |
| ... | ... | ... |
```

The INDEX.md is the **first thing the next reader will look at** —
treat it like a table of contents for the report. It should be
written **last** (after all other files exist), and updated to
reflect the actual final tree.

### Anti-pattern: do NOT write monolithic files

Specifically:

- **Do NOT** combine multiple Points into a single `part-x.md` file.
- **Do NOT** combine multiple sub-questions into a single Point file.
- **Do NOT** combine all checks of a group into a single
  `check-group-X.md` file.
- **Do NOT** put the master `clay-checklist.md` content into
  `summary.md` (or vice versa).
- **Do NOT** skip `00-statement.md` or `verdict.md` for any Point.

If a sub-question is genuinely small (e.g., a one-paragraph
verification), the file is allowed to be short — but it should still
exist as its own file. **Granularity beats brevity.**

### Cross-referencing rules

- Every per-Point sub-question file should link to the relevant
  check file(s) it informs (e.g., Point F4 sub-question 01 links to
  checks/WE-weak-existence/WE1.md).
- Every check file should link back to the Point sub-question(s)
  that establish it.
- The clay-checklist.md master table has one row per check; the
  rightmost column is the path to the check file.
- The INDEX.md is the navigation hub.

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

---

## Closing instructions (REQUIRED in summary.md)

The last few sentences of `summary.md` MUST include the following
disclosures, exactly so that the next reader is reminded of known
limitations:

1. **Wikipedia stand-in for canonical axioms.** This run cited
   `references/wikipedia-wightman-axioms.txt` and
   `references/wikipedia-os-axioms.txt` as the canonical sources for
   the Wightman and Osterwalder–Schrader axioms, because the original
   peer-reviewed sources (Streater–Wightman 1964, OS CMP 1973/1975)
   were not directly fetchable from Project Euclid via `curl`
   (Incapsula-blocked). **Action item for a future cycle:** pay the
   Project Euclid paywall (or download via a browser session
   bypassing Incapsula) and save the original CMP papers to
   `references/`.

2. **Tools added during this run** (if any). List package name,
   version, and which check(s) it was used for.

3. **Known limitations of the JW PDF reading.** The JW PDF was read
   in full (14 pages) via `pypdf`. If any quotation in this prompt
   is paraphrased rather than verbatim, flag it; future prompts
   should use the verbatim form.

These three closing disclosures ensure that limitations are visible
in every run summary and that the next cycle's referee has a clear
upgrade path.

---

Do not be diplomatic. Do not praise the work. Don't hurry. Don't take
shortcuts. Find the gaps.

If you cannot find a gap in a specific argument, say so explicitly
and explain why — that is also valuable information.

# Your north star
Find any issue that would cause the Clay Scientific Advisory Board to
reject this proof. A credibility-destroying gap is worse than a
fixable technical gap. Focus on:
- Is the H4 story honest and complete?
- Are the four Clay structural ingredients (L.1–L.4) actually
  constructed in Appendix L, or are they hand-waved?
- Does Theorem M.2.1 actually establish uniqueness, not just
  subsequential convergence?
- Does Appendix K actually verify Balaban for general $G$, or does
  it only sketch the extension?
- Is every H4-conditional result consistently flagged?
- Is the Wikipedia stand-in for the canonical axioms acceptable for
  this cycle, and is the future paywall upgrade documented in the
  closing sentences?
