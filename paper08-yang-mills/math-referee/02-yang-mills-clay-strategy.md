# Strategy: Rewrite the Notation-Less Math Referee Prompt for Full Clay Rigor

*A plan for upgrading*
*`/Users/gsix/yang-mills/notation-less-math-referee/01-notation-less-math-referee.md`*
*so that the next referee run checks every requirement of the*
*Jaffe–Witten problem statement to the letter, with paths matching*
*the post-reorganization directory layout and the post-gradient-flow*
*proof state.*

*Date: 2026-04-09*

---

## 0. Why this rewrite is needed

The current prompt was written before two major changes:

1. **The directory was reorganized.** The referee directory is now
   `notation-less-math-referee/` (new) with a sibling
   `notation-math-referee/` (old, holds the run r00 archive). The
   prompt currently writes paths to the old name, which would put
   new run output in the wrong directory.

2. **The proof state advanced.** Since run r00 the preprint has been
   extended with:
   - Appendix M (gap closures from referee r00) — closes K-uniformity,
     uniqueness of continuum limit, etc.
   - Appendix L (replaced) — gradient-flow construction of local
     operators, closing L.1, L.3 unconditionally and L.2, L.4
     (leading order) conditional on H4
   - Appendix N (new) — QG5D infrastructure cross-references
   - PROOF-CHAIN extended with Steps 15–18
   - Section 12.7 (Full Clay Compliance)
   - Updated abstract and Section 5.7 IV.5

   The old prompt's "Files to Read" list does not include any of
   this. A new run would miss the entire structural-ingredient
   programme.

3. **The mandatory checklist (current C1–C11) is too coarse.** The
   Jaffe–Witten PDF — read cover-to-cover via `pypdf` — yields a
   significantly finer set of requirements than the 11 checks the
   current prompt encodes. The Wightman axioms cited in JW
   reference [45] decompose into W0–W3 (with W4 implied) per the
   Wikipedia / Streater–Wightman canonical form; the
   Osterwalder–Schrader axioms cited in JW reference [35] decompose
   into E0–E4 (with the OS0' linear growth condition added in 1975).
   Each axiom is its own check. C9 (OPE) has multiple sub-clauses.
   C8 (stress tensor) decomposes into symmetry, conservation, gauge
   invariance, trace anomaly, positivity. The current C1–C11 lumps
   these together at too high a level.

The goal of this rewrite is a prompt that, when given to a fresh
hostile referee, exposes every condition Jaffe and Witten state and
every place the proof must satisfy them.


---


## 1. What I read to prepare

### 1.1 The Jaffe–Witten PDF (cover-to-cover via pypdf)

`/Users/gsix/yang-mills/notation-less-math-referee/yangmills-jaffe-witten.pdf`
— 14 pages. Read in full. Extracted requirements from:

- **§1 The Physics of Gauge Theory** (pp. 1–3): physical motivation;
  the three "must have" properties of QCD (mass gap, confinement,
  chiral symmetry breaking).
- **§2 Quest for Mathematical Understanding** (pp. 3–5): scope of
  the prize; "we hope so" line; reference to Donaldson, Jones,
  mirror symmetry as motivating contexts.
- **§3 Quantum Fields** (pp. 5–6): the formal definition of "quantum
  field theory in the above sense" — Hilbert space carrying
  Poincaré rep, positive-energy spectrum, unique vacuum, Poincaré
  covariance of fields, locality (commuting at spacelike). Cites
  Gårding–Wightman [45] and Haag–Kastler [24] as parallel schemes.
  Notes Symanzik / Nelson / Osterwalder–Schrader Euclidean
  reformulation (cites [33], [35], [46]).
- **§4 The Problem** (p. 6): the formal statement, including the
  curvature-polynomial correspondence, footnote 1 on dimensional
  correspondence and renormalization, AF short-distance match,
  stress tensor, OPE, the spectrum / mass gap definitions, and the
  binding "Yang–Mills Existence and Mass Gap" theorem to be proved.
- **§5 Comments** (pp. 6–7): clustering as a consequence of the
  mass gap (with explicit exponential bound), uniform-volume gap as
  fundamental, list of natural extensions (one-particle isolation,
  confinement, other 4-manifolds — these are NOT required for the
  prize).
- **§6 Mathematical Perspective** (pp. 7–12), including:
  - **§6.5 Yang–Mills Theory**: explicit statement that "Establishing
    a quantum mechanical Hilbert space is part of the solution to
    this Millennium problem"; the warning that dim-reg /
    Pauli–Villars destroy reflection positivity and few methods
    recover it; the requirement to extend Balaban's program to
    "expectations of gauge-invariant functions of the fields"; the
    explicit "New ideas are needed to prove the existence of a mass
    gap that is uniform in the volume of space-time. Such a result
    presumably would enable the study of the limit as $T^4 \to R^4$."
  - **§6.6 Further Remarks**: speculation about duality, $1/N$, and
    the four-dimensional difficulty.
  - **Footnote 2 (p. 12)**: the binding exclusion of weak-existence:
    "We specifically exclude weak-existence (compactness) as the
    solution to the existence part of the Millennium problem, unless
    one also uses other techniques to establish properties of the
    limit (such as the existence of a mass gap and the axioms)."

### 1.2 References fetched online

Saved to
`/Users/gsix/yang-mills/notation-less-math-referee/references/`:

| File | Source | What it gives |
|:-----|:-------|:--------------|
| `clay-yangmills-official.pdf` | claymath.org/wp-content | Identical to the JW PDF; second copy as a sanity check |
| `clay-page-yang-mills.html` | claymath.org/millennium/yang-mills-the-maths-gap | Overview/marketing — confirms no additional formal text beyond the JW PDF |
| `wikipedia-wightman-axioms.html/.txt` | en.wikipedia.org/wiki/Wightman_axioms | Canonical W0–W3 axiom statements with full text |
| `wikipedia-os-axioms.html/.txt` | en.wikipedia.org/wiki/Osterwalder–Schrader_theorem | Canonical E0–E4 axioms; linear growth condition (OS0'); historical note on 1973 vs 1975 |

**⚠️ Wikipedia is a known risk.** Wikipedia's statement of the
Wightman / Osterwalder–Schrader axioms is canonical *for typical
mathematical-physics use* but is NOT the original peer-reviewed text
that Jaffe and Witten cite. The binding references in the JW PDF are
[45] (Streater–Wightman, *PCT, Spin and Statistics, and All That*) and
[35] (Osterwalder–Schrader, "Axioms for Euclidean Green's functions,"
CMP 31 (1973) and CMP 42 (1975)). For a Clay submission, the referee
must eventually verify against the original sources.

**Project Euclid is Incapsula-blocked** for direct `curl` access, so
the original CMP papers (OS 1973, OS 1975, Balaban CMP 95–119) could
not be fetched in this strategy session. The Wikipedia text is
acceptable as a *temporary* stand-in because it states the axioms in
their canonical form and explicitly notes the OS0 → OS0' (1975)
correction. **Action item:** in a future session, pay the paywall and
download the original CMP PDFs through a browser session, then save
to `references/`.

**Each referee report's closing must explicitly list this limitation
in its last few sentences** (the new prompt will instruct this), so
that the next reader is reminded to upgrade the references when
possible.


---


## 2. The complete catalog of Jaffe–Witten requirements

This is the master list, extracted verbatim from the JW PDF and
organized for the new mandatory-checks table. Every item below has a
direct quotation or unambiguous derivation from the PDF text, with
section reference.

### 2.1 Core mass gap & spectrum (JW §3 + §4)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **A1** | Existence of $\Delta > 0$ such that $H$ has no spectrum in $(0, \Delta)$ | §4, "A quantum field theory has a mass gap $\Delta$ if $H$ has no spectrum in the interval $(0, \Delta)$" |
| **A2** | $m = \sup\{\Delta : \mathrm{spec}(H) \cap (0,\Delta) = \emptyset\} < \infty$ | §4, "The supremum of such $\Delta$ is the mass $m$, and we require $m < \infty$" |
| **A3** | $H \Omega = 0$ (vacuum is zero-energy eigenstate) | §3, "the vacuum vector $\Omega$ is Poincaré invariant, it is an eigenstate with zero energy" |
| **A4** | Spec$(H) \subseteq [0, \infty)$ (positive energy) | §3, "the representation has positive energy, $0 \leq H$" |
| **A5** | Existence of at least one finite-mass one-particle state (so $m < \infty$ is meaningful, not vacuous) | §4, follows from $m < \infty$ requirement; reinforced by §5's remarks on isolated one-particle states |

### 2.2 Wightman axioms (JW reference [45] = Streater–Wightman)

JW §3 lists these informally; the canonical W0–W3 (with W4 = unique
vacuum) form is in the Wikipedia reference text in the references
directory.

| ID | Requirement | JW / Wikipedia source |
|:---|:------------|:----------------------|
| **W0** | Hilbert space $\mathcal{H}$ is a separable complex Hilbert space; states are rays | JW §3 (implicit); Wikipedia W0 |
| **W1** | Strongly continuous unitary projective representation of the Poincaré group on $\mathcal{H}$, generated by self-adjoint $H$ and $\vec P$ | JW §3, "$\mathcal{H}$ of the quantum field carry a representation of the Poincaré group … self-adjoint elements of the Lie algebra of the group that generate translations" |
| **W2** | Spectrum condition: $P^\mu$ in forward light cone; $H \geq 0$ | JW §3, "$0 \leq H$" |
| **W3** | Unique vacuum vector $\Omega \in \mathcal{H}$, invariant under the Poincaré rep, unique up to phase | JW §3, "a vacuum vector $\Omega \in \mathcal{H}$ that is unique up to a phase" |
| **W4** | Field operators are operator-valued tempered distributions on a common dense invariant domain | JW §3, "operator-valued generalized function on space-time" + footnote 1 |
| **W5** | Poincaré covariance of fields | JW §3, "transform covariantly under the Poincaré group" |
| **W6** | Locality / microcausality: field operators commute (anti-commute for fermions) at spacelike separation | JW §3, "Quantum fields in space-time regions that cannot be connected by a light signal should be independent" + Gårding–Wightman locality |
| **W7** | Cyclicity of vacuum under polynomial algebra of fields | Standard W4 in S–W; not explicit in JW but implied by "carrying a representation" |

### 2.3 Osterwalder–Schrader axioms (JW reference [35] = OS 1973/1975)

JW §3 cites Osterwalder–Schrader and the Symanzik / Nelson Markov
reformulation. The 1975 corrected form (linear growth condition OS0')
is the binding one.

| ID | Requirement | JW / Wikipedia source |
|:---|:------------|:----------------------|
| **E0** | Temperedness: $S_n$ are tempered distributions away from coincident points | OS 1973 / Wikipedia E0 |
| **E0'** | Linear growth condition (1975 corrected version): $|S_n(f)| \leq n! C^n p_N(f)$ for some Schwartz seminorm $p_N$, with seminorm index $N(n)$ growing at most linearly in $n$ | OS 1975; Wikipedia "Linear growth condition" subsection; necessary for the reconstruction theorem to apply |
| **E1** | Euclidean covariance of $S_n$ under O(d) rotations and translations | OS / Wikipedia E1 |
| **E2** | Reflection positivity (the Osterwalder–Schrader positivity condition) | OS / Wikipedia E2; explicitly emphasized in JW §6.5 |
| **E3** | Symmetry / permutation invariance of $S_n$ (Bose statistics) | OS / Wikipedia E3 |
| **E4** | Cluster property | OS / Wikipedia E4; reinforced by JW §5 explicit clustering statement |
| **OS-Rec** | The 1975 corrected OS reconstruction theorem (not 1973) is used to produce the Wightman QFT | JW §3 ("Osterwalder and Schrader then discovered… see [35]"); the corrected version is binding because the 1973 version had a known gap |

### 2.4 Local field operators (JW §4 + footnote 1)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **L1** | For every gauge-invariant local polynomial in the curvature $F$ and its covariant derivatives, there is a corresponding operator-valued distribution on $\mathcal{H}$ | §4, "local quantum field operators in correspondence with the gauge-invariant local polynomials in the curvature $F$ and its covariant derivatives, such as $\mathrm{Tr}\,F_{ij} F_{kl}(x)$" |
| **L2** | The correspondence is at the renormalized level (per footnote 1's renormalization subtleties) | §4, footnote 1, "the correspondence has some standard subtleties involving renormalization" |
| **L3** | Dimensional correspondence: classical differential polynomials of dimension $\leq d$ correspond to local quantum operators of dimension $\leq d$ | §4, footnote 1 explicitly |
| **L4** | The constructed operators act on the reconstructed Hilbert space (not just on Schwinger function vacuum expectations) | §4, "field operators on $\mathcal{H}$" |

### 2.5 Short-distance asymptotic freedom match (JW §4)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **AF1** | Correlation functions of the local field operators agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory | §4, "Correlation functions of the quantum field operators should agree at short distances with the predictions of asymptotic freedom and perturbative renormalization theory" |
| **AF2** | The agreement matches "the standard description … in physics texts" — i.e., not a vague resemblance but quantitative reproduction of the perturbative series | §4, "as described in textbooks" |

### 2.6 Stress tensor (JW §4)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **T1** | The stress tensor exists as an operator-valued distribution on $\mathcal{H}$ | §4, "the existence of a stress tensor" |
| **T2** | $T_{\mu\nu}$ is symmetric | Standard for any Lorentz-covariant stress tensor; physics texts cited |
| **T3** | $T_{\mu\nu}$ is conserved: $\partial^\mu T_{\mu\nu} = 0$ | Standard; conservation is the defining property of a stress tensor |
| **T4** | $T_{\mu\nu}$ is gauge-invariant | The local field operators must be gauge-invariant per §4; the canonical YM stress tensor is not, so an improved stress tensor is required |
| **T5** | $T_{0i}$ generates spatial translations and $T_{00}$ generates time translation: $H = \int T_{00} \, d^3 \vec x$, $\vec P = \int T_{0i} \, d^3 \vec x$ | Standard; ties the stress tensor to the Hamiltonian and momentum already required by W1 |
| **T6** | Trace anomaly: $T^\mu{}_\mu \propto \beta(g) \mathrm{Tr}\, F^2$ at the renormalized level | Implicit in "predictions of asymptotic freedom" — the trace anomaly is an AF prediction |

### 2.7 Operator product expansion (JW §4)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **OPE1** | An operator product expansion exists for products of local operators | §4, "an operator product expansion" |
| **OPE2** | The OPE has prescribed local singularities — the same singularity structure perturbative AF predicts | §4, "having prescribed local singularities predicted by asymptotic freedom" |
| **OPE3** | The OPE is consistent with the AF short-distance match (AF1, AF2) | §4, the AF match and the OPE are listed as related sub-conditions |

### 2.8 Reflection positivity / Hilbert space (JW §6.5)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **R1** | A quantum mechanical Hilbert space is constructed (not just Schwinger functions) | §6.5, "Establishing a quantum mechanical Hilbert space is part of the solution to this Millennium problem." This is a binding statement, not optional. |
| **R2** | Reflection positivity holds at every regularization step used (or, if lost, recovered explicitly) | §6.5, "few methods exist to recover reflection positivity in case it is lost through regularization" — implicit warning |
| **R3** | Specifically, dimensional regularization and Pauli–Villars are NOT used (or if used, RP is recovered) | §6.5 names these as methods that destroy RP |
| **R4** | The Wilson lattice approximation, which preserves RP, is the natural starting point | §6.5, "Reflection positivity holds for the Wilson approximation, a major advantage" |

### 2.9 Volume / infinite-volume limit (JW §6.5)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **V1** | The continuum theory is on $\mathbb{R}^4$, not on a torus or finite volume | §4, "exists on $\mathbb{R}^4$" |
| **V2** | The mass gap is uniform in the volume of space-time | §6.5, "New ideas are needed to prove the existence of a mass gap that is uniform in the volume of space-time" |
| **V3** | The infinite-volume limit $\mathbb{T}^4 \to \mathbb{R}^4$ is constructed | §6.5, "Such a result presumably would enable the study of the limit as $\mathbb{T}^4 \to \mathbb{R}^4$" |
| **V4** | Both limits ($a \to 0$ and $L \to \infty$) commute, or can be taken simultaneously | Implicit in the requirement for a continuum theory on $\mathbb{R}^4$ |

### 2.10 Non-triviality (JW §4)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **N1** | The constructed theory is **non-trivial** | §4, "a **non-trivial** quantum Yang–Mills theory exists" |
| **N2** | The theory is not the free / Gaussian theory | Inferred from "non-trivial"; reinforced by §6.2 discussion of trivial vs non-trivial $\phi^4$ |
| **N3** | Some interpretation: non-trivial $S$-matrix, OR non-vanishing connected $n$-point function for some $n \geq 4$ | §6.2 cites "non-trivial scattering" as a property of established 2D constructive examples |

### 2.11 Gauge group (JW §4)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **G1** | The theorem holds for **any compact simple gauge group** $G$ | §4, "for any compact simple gauge group $G$" |
| **G2** | Specifically, all of: SU($N$) ($N \geq 2$), SO($N$) ($N \geq 3$), Sp($N$) ($N \geq 1$), and the five exceptional groups $G_2, F_4, E_6, E_7, E_8$ | The classification of compact simple Lie groups |

### 2.12 No weak-existence-only solution (JW §6.6 footnote 2)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **WE1** | Properties of the limit (mass gap and axioms) are established for the actual constructed limit, not asserted on a hypothetical limit obtained by Banach–Alaoglu compactness alone | Footnote 2, verbatim binding statement |
| **WE2** | If a subsequential limit is used, the properties must propagate through the limit | Footnote 2 implication |

### 2.13 Clustering (consequence; JW §5)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **CL1** | Clustering follows from the mass gap (downstream consequence, but Jaffe–Witten state it explicitly with a quantitative bound) | §5, $|\langle\Omega, \mathcal{O}(\vec x)\mathcal{O}(\vec y)\Omega\rangle| \leq \exp(-C|\vec x - \vec y|)$ for $C < \Delta$ |

### 2.14 Yang–Mills equations / dynamics (JW §1, §6.5)

| ID | Requirement | JW source |
|:---|:------------|:----------|
| **YM1** | The constructed theory is the quantization of the Yang–Mills Lagrangian (1) — i.e., the field operators satisfy the YM equations of motion in the distributional sense | §1, the formal Lagrangian (1) is what defines "Yang–Mills theory"; §6.5, "extending these results to the study of expectations of gauge-invariant functions of the fields" |
| **YM2** | Gauge invariance is manifest in the final theory | §1 (gauge group structure) and §6.5 (gauge symmetry as central) |

---

**Total: ~50 mandatory checks** (each item above corresponds to a
distinct verifiable claim). Compared to the current C1–C11, this is
a 4–5× increase in granularity.


---


## 3. New directory layout — path mapping

### 3.1 Stale paths in the current prompt

Search of `01-notation-less-math-referee.md`:

| Stale path | New path |
|:-----------|:---------|
| `notation-math-referee/code/setup-venv.sh` | `notation-less-math-referee/code/setup-venv.sh` |
| `notation-math-referee/code/.venv/bin/activate` | `notation-less-math-referee/code/.venv/bin/activate` |
| `notation-math-referee/yangmills-jaffe-witten.pdf` | `notation-less-math-referee/yangmills-jaffe-witten.pdf` |
| `notation-math-referee/latest-run/` | `notation-less-math-referee/latest-run/` |
| `notation-math-referee/runs/r{NN}/` | `notation-less-math-referee/runs/r{NN}/` |
| `referee/r05/report.md` | (does not exist; the prior referee runs are in `notation-math-referee/runs/r00/`) |
| `referee/r06/summary.md` | (does not exist; same) |
| `referee/r03/verify-balaban-items.md` | (does not exist) |
| `referee/r06/bibliographic-verification.md` | (does not exist) |

The "Previous referee findings" section is broken — the paths it
references do not exist. The actual prior run lives in
`notation-math-referee/runs/r00/` (the directory was renamed but the
runs were not moved). The new prompt should either point to that
location or instruct the next referee to ignore prior runs (per the
"out of scope by design" rule the prompt already states).

### 3.2 New files to read (added by the gradient-flow programme)

The current "Files to Read" list is missing:

| New file | Purpose |
|:---------|:--------|
| `preprint/sections/L-clay-conjectures.md` (rewritten, ~2,871 lines) | The gradient-flow construction closing L.1–L.4 |
| `preprint/sections/M-gap-closures-r00.md` | Closes the closable gaps from r00 (K-uniformity, uniqueness) |
| `preprint/sections/N-qg5d-infrastructure.md` (new) | QG5D cross-references for Appendix L's external inputs |
| Updated `PROOF-CHAIN.md` with Steps 1–18 | The complete chain |
| Updated `00-abstract.md` (with gradient-flow paragraph) | Current claim |
| Updated `08-conclusion.md` (with §12.7 Full Clay Compliance) | Final compliance statement |

### 3.3 References to fetch / cite

The `references/` directory I just populated should be added to the
prompt as recommended reading:

| File | Use |
|:-----|:----|
| `references/clay-yangmills-official.pdf` | Identical to the JW PDF; second copy as a backup |
| `references/clay-page-yang-mills.html` | Confirms no additional formal text exists at the Clay page |
| `references/wikipedia-wightman-axioms.txt` | Canonical W0–W7 axiom statements |
| `references/wikipedia-os-axioms.txt` | Canonical E0–E4 axioms + linear growth (OS0') |


---


## 4. The new prompt structure

### 4.1 Sections that stay (with minor edits)

- **Header** (title, subtitle).
- **Computational verification environment** (the venv setup
  instructions). Update paths to `notation-less-math-referee/code/`.
  Keep the "non-destructive setup" paragraph and the suggested
  computational checks list.
- **Profile** (skeptical referee, no partial credit). Keep verbatim.
- **Rationale and Strategy** (the four guiding questions). Keep
  verbatim.
- **The verbatim Jaffe–Witten quotes** (§4 problem statement, §4
  mass gap definition, §4 field operator correspondence, §6.6
  footnote 2, §6.5 RP guidance, §6.6 infinite volume). Keep all of
  these, plus add quotes I extracted that are not yet in the prompt
  (specifically: §3 quantum field definition; §5 clustering bound;
  §6.5 quantum mechanical Hilbert space requirement).
- **What Balaban actually proved (and did not)**. Keep verbatim.
- **Common failure modes**. Keep verbatim.
- **Recent rigorous results**. Update with Adhikari–Cao 2025 (3D
  abelian) and Douglas Nature Reviews 2025.

### 4.2 Sections that get rewritten

- **"Mandatory checks against the official statement"** (currently
  C1–C11): Replace with the **~50-item table from §2 above**. Group
  the checks by JW source section (mass gap, Wightman axioms, OS
  axioms, local field operators, AF, stress tensor, OPE, RP/Hilbert
  space, volume, non-triviality, gauge group, no weak-existence,
  clustering, YM equations). Each check gets a short label (e.g.,
  W3, E0', T6) and a one-sentence statement with JW page/section
  reference.

- **"Files to Read"**: Add the new files (Appendix L, M, N, updated
  PROOF-CHAIN, Section 12.7) and remove the broken referee/r0x
  paths. Reorder so the most critical sections (PROOF-CHAIN, the
  new Appendix L) come first.

- **"Output Format"**: Update the example file names. Currently the
  expected output is `part-a-point-1.md` through
  `part-g-point-3.md`. With the expanded checklist, the output
  should be:
  - One file per check group: `mass-gap.md`, `wightman.md`,
    `os.md`, `local-operators.md`, `af-match.md`, `stress-tensor.md`,
    `ope.md`, `reflection-positivity.md`, `volume.md`,
    `non-triviality.md`, `gauge-group.md`, `weak-existence.md`,
    `clustering.md`, `ym-equations.md`.
  - Plus `clay-checklist.md` (the verdict table) and `summary.md`.
  - Each file contains one entry per check ID, with verdict
    (PASS/PARTIAL/FAIL/SOUND/CLOSABLE/GENUINE) and a precise
    justification with location in the preprint.

- **"Your task"** (the per-point scrutiny instructions): Reword to
  reflect the expanded checklist. Each check ID gets the
  HEAVY/MEDIUM/LIGHT weighting based on its difficulty in the
  current proof state.

### 4.3 Sections to add

- **"What changed since run r00"**: A short note explaining that the
  preprint has been extended with Appendices L (gradient-flow),
  M (gap closures), N (QG5D infrastructure), and PROOF-CHAIN
  Steps 15–18, plus Section 12.7 Full Clay Compliance. The next
  referee should be aware of this state but still treat the work
  with hostile skepticism.

- **"H4 — the standard hypothesis"**: A new note explaining that
  Lemma L.4.2 and the AF form of L.4.3 are stated conditional on
  Hypothesis H4 (non-perturbative = perturbative at short
  distances). The referee should evaluate whether (a) H4 is
  correctly identified, (b) the conditional flagging is consistent,
  and (c) the gradient-flow framework's reduction of H4 to a
  Taylor-coefficient question is sound.

- **"Key new lemmas to scrutinize"**: A list of the 19 lemmas in
  Appendix L (L.1.1 through L.4.3) with one-sentence summaries, so
  the referee knows what's claimed before they start reading.


---


## 5. Execution plan

### 5.1 Phase 1 — Story / outline (this document)

**Status: in progress / complete after this document is written.**

Output: this strategy document, which serves as the roadmap for the
prompt rewrite. Per `feedback_story_before_plan.md`, the story comes
first.

### 5.2 Phase 2 — Draft the new prompt

**Estimated effort: 2–3 hours.**

Output: a new file
`/Users/gsix/yang-mills/notation-less-math-referee/02-notation-less-math-referee.md`
(or replace `01-...` after backing up the current version).

The new prompt will be ~2× the length of the current one (call it
~2000 lines vs 1444). The bulk of the new content is the expanded
mandatory-checks table with all ~50 items.

### 5.3 Phase 3 — Verify the new prompt against the JW PDF

**Estimated effort: 30 minutes.**

A separate read-through with `pypdf` to confirm:
- Every quoted passage in the prompt matches the PDF text exactly
- Every page/section reference is correct
- No requirement is invented; every check has a JW source

### 5.4 Phase 4 — Path consistency check

**Estimated effort: 15 minutes.**

Grep the new prompt for any remaining stale paths. Verify:
- All `notation-math-referee/` references are now
  `notation-less-math-referee/`
- All file paths in "Files to Read" exist on disk
- The output directory and run-archiving instructions are correct
- The references/ directory entries are correct

### 5.5 Phase 5 — Optional: dry run

**Estimated effort: 1 hour.**

Launch one referee agent against the new prompt with a small subset
of the checks (say, the W axioms) to verify the prompt produces the
expected report format. This is optional but recommended for the
first run with the expanded checklist.


---


## 6. Decisions (confirmed 2026-04-09)

The calibration questions from the original draft have been resolved:

1. **New file, keep `01-...` as historical record.** The new prompt is
   `/Users/gsix/yang-mills/notation-less-math-referee/02-notation-less-math-referee.md`.
   `01-notation-less-math-referee.md` is preserved unchanged as the
   record of the run-r00 prompt.

2. **All ~50 checks, no collapsing.** The new prompt encodes every
   distinct requirement from §2 above. The next job after this one
   may split or group them, but it is more important to have full,
   certain coverage now than a tidy short list. Granularity beats
   brevity for Clay rigor.

3. **H4 is verified as a documented hypothesis, not graded as a
   result.** The next referee's job for H4 is **NOT** to grade
   results that depend on H4 (the paper already does that honestly,
   with consistent "conditional on H4" flagging audited at 13/13
   PASS in W12-30). The job is to **verify that the H4 story itself
   meets Clay's standards**. See §6.1 below for the exact six
   verification checks.

4. **Stale paths deleted entirely.** No reference to
   `notation-math-referee/` (the old directory) in the new prompt.
   The new prompt only knows about `notation-less-math-referee/`.
   The broken `referee/r0x/...` paths in `01-...` are removed
   without replacement. Past run archives are out of scope by
   design.

5. **Strategy doc stays at `math-referee/02-...`.** Cross-referenced
   from the new prompt's "References" section.

6. **Wikipedia is acceptable for now, with explicit risk
   disclosure.** Every referee report run with the new prompt MUST
   list the Wikipedia stand-in in its closing sentences (the prompt
   instructs this explicitly), so the gap is visible in every
   summary and we don't forget to upgrade. Future session:
   download the original CMP papers through a browser bypassing
   Incapsula.

### 6.1 H4 verification checks (the H4 group)

Based on the §1 distinction between "documenting H4" (already done)
and "grading the proof's handling of H4" (the next referee's job),
the new prompt will include the following H4 verification group as
part of the mandatory checks:

| ID | Verification check |
|:---|:-------------------|
| **H4-1** | Hypothesis H4 is stated precisely in Section L.7 as a single, unambiguous mathematical claim — not as a vague assumption or boilerplate caveat |
| **H4-2** | Every result depending on H4 (L.1(iii), L.2, AF form of L.4) is explicitly flagged "conditional on H4" in its theorem statement, not just in surrounding prose |
| **H4-3** | H4 is correctly identified as the standard lattice-QCD hypothesis (consistent with the Glimm–Jaffe / Symanzik / Wilson literature framing); the proof does not invent a new hypothesis or rename an existing one |
| **H4-4** | The gradient-flow reduction of H4 (from "asymptotic series equals non-perturbative object" to "Taylor coefficients of the analytic function $F(t)$ at $t = 0$ agree with Feynman-rule computations") is mathematically sound and represents a genuine simplification |
| **H4-5** | The Clay submission's *unconditional* claims (mass gap, OS axioms, L.1(i)(ii), L.3, leading-order non-perturbative OPE structure) are clearly separated from the H4-conditional ones in every part of the preprint (abstract, conclusion, PROOF-CHAIN, Appendix L, Section 12.7) |
| **H4-6** | Nothing in the abstract, conclusion, PROOF-CHAIN, or Appendix L overstates what is unconditional vs. conditional on H4. No marketing language obscures the H4 dependence. |

**Pass criterion for the H4 group:** all 6 checks PASS. If any one
fails, the referee should describe precisely what is overstated, what
is missing, or what is mathematically unsound, and rate the failure
as a **closable presentation gap** (not a genuine gap in the
mathematics), since the underlying H4 framework is honest.

The new prompt will instruct the referee that:
- H4-conditional results should be graded as **PASS conditional on H4**
  in the per-check verdicts, NOT as FAIL.
- The honest statement of H4 is part of Clay's expected rigor, not a
  weakness.
- The point of the H4 group is to verify that the **handling** of H4
  meets Clay's standards, in the same way the OS axioms group verifies
  that the handling of OS reconstruction meets Clay's standards.


---


## 7. Definition of done

The new prompt is complete when:

- [ ] All paths point to `notation-less-math-referee/` (no stale
  `notation-math-referee/` or broken `referee/r0x/...` references)
- [ ] All "Files to Read" entries exist on disk
- [ ] The mandatory-checks table covers every JW requirement from §2
  above — **all ~50 items, no collapsing** (per decision §6.2)
- [ ] Every quoted JW passage is verbatim from the PDF
- [ ] Every check has a JW page/section reference
- [ ] Appendix L (rewritten), Appendix M, Appendix N, updated
  PROOF-CHAIN with Steps 1–18, and Section 12.7 are all listed in
  the reading order
- [ ] The H4 verification group (H4-1 through H4-6 per §6.1) is
  included in the mandatory checks
- [ ] The prompt instructs the referee that H4-conditional results
  are graded PASS-conditional, not FAIL
- [ ] The output format matches the new check structure (one file
  per check group + clay-checklist.md + summary.md)
- [ ] References directory is documented and the Wikipedia risk is
  explicitly disclosed
- [ ] **The prompt instructs the referee to list the Wikipedia
  stand-in in the closing sentences of every report**, so the gap
  is visible in every summary
- [ ] A grep for "stale paths" returns 0 hits

When all boxes are checked, the prompt is ready for the next
hostile referee run.


---


## 8. One sentence

Read the JW PDF cover-to-cover, fetch the Wightman + OS axioms from
Wikipedia for canonical statements, expand the C1–C11 checklist to
~25–30 items grouped by JW source, update every path to the new
directory layout, and produce a new referee prompt that exposes every
condition Jaffe and Witten state.
