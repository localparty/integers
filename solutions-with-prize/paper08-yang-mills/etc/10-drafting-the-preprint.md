# Drafting the Preprint: Instructions for Opus

You are organizing a completed mathematical proof into a submission-ready
preprint. This is an editorial and structural task, not a mathematical
one. Do not add new mathematics, change any arguments, or fill in gaps
you perceive. Your job is assembly, consolidation, and clarity.

Read this entire document before doing anything.


---


## Context: What Has Been Proved

The proof establishes the Yang-Mills mass gap for SU(N) lattice gauge
theory. The full proof chain, in order, is:

1. **Lattice mass gap** (Theorems 1-5): The Weitzenböck spectral gap on
   CP^{N-1} controls a Kaluza-Klein cluster expansion via
   Kotecký-Preiss, giving Δ₀ > 0 at all practical couplings β < 10¹⁴.
   SU(2) is handled exactly via 2D Yang-Mills on S².

2. **Balaban UV stability** (Literature): Balaban's block-spin RG
   (CMP 95-119, 1982-1988) controls the effective action at each step.

3. **RG preservation** (Proved): The recursion C_{k+1} = C_k/4 +
   C_new + O(g_k² C_k) has a stable fixed point. The 1/4 contraction
   reduces the continuum limit to a single block-spin step.

4. **Dimension-6 classification** (Proved):
   - Non-derivative operators Tr(F³), d^{abc}F³: coefficient exactly
     zero by C-symmetry (non-perturbative, unconditional).
   - Derivative operator Tr(DF)²: form factor O(Δ²) by translation
     invariance + spectral intermediate-state mechanism (exact).

5. **Balaban analyticity (B1)-(B2)** (Proved by extraction): The
   small-field effective action is analytic with k-independent radius,
   extending to SL(N,C). Follows from Balaban's polymer expansion
   convergence.

6. **Stability of excitation number** (New argument): Every C-even
   dimension-6 gauge-invariant operator has exc ≥ 2. Combined with
   (B1)-(B2), this gives the non-perturbative single-step bound
   |⟨1|δE_k(0)|1⟩_c| ≤ C_new g_k⁴ Δ²_{k+1}.

7. **Continuum mass gap** (Proved): Δ_∞ > 0.

Three [VERIFY] items remain — reading exercises from Balaban's
published construction, not mathematical gaps.


---


## Repository Structure: What Exists and Where

### Directory to rename
`/Users/gsix/yang-mills/paper/` → rename to
`/Users/gsix/yang-mills/research/`

This directory contains 50+ exploratory files accumulated during the
proof development. Most are superseded. It should be preserved as
research history but not confused with the final paper.

### Directory to create
`/Users/gsix/yang-mills/preprint/`

This is the submission-ready paper. Every file in it should be
directly used in the preprint. Nothing exploratory, nothing superseded.

### Source directories for content
- `/Users/gsix/yang-mills/research/` (formerly paper/) — old drafts,
  some sections still current
- `/Users/gsix/yang-mills/etc/proof/` — the definitive proof documents
  produced in the final session
- `/Users/gsix/yang-mills/etc/` — supporting documents
- `/Users/gsix/yang-mills/referee/` — referee reports (useful for
  "addressing objections" section)
- `/Users/gsix/yang-mills/luscher-test/` — numerical results


---


## The Preprint Structure

The paper should have this structure. For each section, the source
material is identified precisely.

### Title and Abstract
**Title:** "The Yang-Mills Mass Gap: A Proof via Kaluza-Klein Topology
and Balaban's Renormalization Group"

**Abstract source:** `research/00-abstract.md`
IMPORTANT: The abstract currently says the continuum limit is "Open."
This is now OUTDATED. The continuum limit has been proved (conditionally
on three [VERIFY] items that are Balaban reading exercises). Update the
abstract summary table accordingly, changing "Continuum limit | Open"
to "Continuum limit | Proved (conditional on three verifications from
Balaban's construction; see Section 5.6 and Appendix H)".
Do not change any other mathematics in the abstract.

---

### Section 1: Introduction
**Source:** `research/02-introduction.md`
Use as-is. The introduction remains current.

---

### Section 2: The Geometric Framework
**Source:** `research/03-the-11d-arena.md`
Describes how CP^{N-1} geometry enters the proof. Use as-is.

---

### Section 3: Quantitative Predictions
**Source:** `research/08-quantitative-results.md`
Use as-is.

---

### Section 4: The Lattice Proof (Part I — Lattice Mass Gap)
This is a consolidation of the core lattice proof.

**Primary sources (in order):**
- `etc/proof/01-setup.md` — mathematical setup
- `etc/proof/02-spectral-gap.md` — Theorem 1: Weitzenböck gap
- `etc/proof/03-cluster-expansion.md` — Theorems 2-3: bond activities,
  Kotecký-Preiss convergence
- `etc/proof/04-lattice-mass-gap.md` — Theorem 4: Δ₀ > 0
- `etc/proof/05-decoupling.md` — Theorem 5: IR equivalence

**SU(2) exact proof:**
- `research/20-appendix-H-su2-warmup.md` — complete, self-contained

Do NOT use files 21-53 from research/ for this section. The
etc/proof/ versions are definitive and supersede them.

---

### Section 5: The Lattice Proof (Part II — Continuum Limit)
This is the new proof of the continuum limit, assembled from the
final session documents. This section did not exist in the old paper.

**Assemble in this order:**

**5.1 Balaban's RG Framework**
Source: `etc/proof/06-balaban-descent.md`
(What we use from Balaban; what he does and does not prove.)

**5.2 Power Counting and the Remaining Problem**
Source: `etc/proof/07-power-counting.md`
(Parity vanishing proved; operator identity disproved; precise
statement of what needs to be bounded.)

**5.3 Dimension-6 Operator Classification**
Consolidate from:
- `etc/proof/single-step-case-b.md` — C-symmetry eliminates Tr(F³)
  exactly (Theorem: Case B). Use Sections 1-5 and 8 only.
- `etc/proof/single-step-computation.md` — Tr(DF)² form factor bound,
  perturbative. Use Sections 4 and 9 only (the core mechanism and
  honest assessment). Omit Sections 1-3 (setup, already covered) and
  Sections 5-8 (higher-loop and non-perturbative corrections, absorbed
  into balaban-B1-B2-proof.md).
Keep all [PROVED] / [ARGUED] / [CONDITIONAL] markers exactly.

**5.4 The RG Recursion**
Source: `etc/proof/rg-preservation.md`
Use Sections 1-6 (the main argument and honest assessment). Omit
Sections 7-9 (alternative approaches, superseded).

**5.5 The Two-Derivative Spectral Lemma**
Source: `etc/proof/two-derivative-spectral-lemma.md`
Include Sections 1-4 (setup, definition, lemma proof, verification)
and Section 8 (honest status table). Omit Sections 5-7 (the
application to δE_k — this is now in 5.6, and Section 7 is
superseded by the corrected mechanism in multi-time-slice-analysis.md).

**5.6 Balaban Analyticity and Stability of Excitation Number**
Source: `etc/proof/balaban-B1-B2-proof.md`
Include all four Parts:
- Part I: Proof of (B1)
- Part II: Proof of (B2)
- Part III: Stability of excitation number (the new lemma)
- Part IV: Final status table (Table IV.1 is the complete proof chain)
This subsection closes the proof. Table IV.1 is the definitive
statement of what has been proved and what remains as [VERIFY].

**5.7 The Continuum Mass Gap**
Source: `etc/proof/09-continuum-limit.md`
The final statement: Δ_∞ > 0.

---

### Section 6: Addressing Referee Objections
**Source:** `referee/` directory — all 8 files

The referee reports identified seven specific technical objections
(A through G). Several were resolved in the final session. Create
a consolidated section that, for each objection, states:
- The objection (one paragraph from the referee file)
- Resolution status: RESOLVED / PARTIALLY RESOLVED / [VERIFY]
- Where the resolution appears in the paper

Resolution map (for Opus to use):
- A (vacuum subtraction): RESOLVED — operator identity disproved in
  Section 5.2; correct mechanism in Section 5.5
- B (parity of E_k): RESOLVED — Section 5.2, Theorem 6(a)
- C (locality/support radius): RESOLVED — Section 5.6, Part I, Step (c)
- D (momentum convolution): RESOLVED — Section 5.5, multi-time-slice
  analysis corrected the flawed mechanism; spectral intermediate-state
  argument is correct
- E (first-order perturbation theory): RESOLVED — Section 5.4
- F (inductive stability): RESOLVED — Section 5.4 (1/4 contraction
  prevents blow-up) and Section 5.6 Part III (stability lemma)
- G (Balaban applicability): [VERIFY] — Section 5.6 Parts I-II provide
  the extraction; three reading exercises remain

---

### Section 7: Why Previous Approaches Failed
**Source:** `research/09-why-previous-approaches-failed.md`
Use as-is. Provides context for the mathematical community.

---

### Section 8: Conclusion
**Source:** `research/11-conclusion.md`
IMPORTANT: The conclusion currently discusses the continuum limit
as open. Insert the following paragraph before the final closing
paragraph of the conclusion:

"Since the initial drafting of this conclusion, the continuum limit
argument has been completed. The key new ingredients are: (i) the
exact elimination of non-derivative dimension-6 operators by charge
conjugation symmetry; (ii) the two-derivative spectral lemma, which
gives a non-perturbative $\hat{\Delta}^2$ suppression via the
intermediate-state spectral mechanism; (iii) extraction of Balaban's
analyticity properties (B1)-(B2) from his published polymer expansion
convergence theorems; and (iv) the stability of excitation number
lemma, which promotes the dimension-6 classification to a
non-perturbative statement. Three verification items remain, each
corresponding to an implicit property of Balaban's construction that
is verifiable from his published papers (CMP 109, 1987). The proof
chain is given in full in Table IV.1 of Section 5.6 and Appendix H."

Do not change any other text in the conclusion.

---

### Appendices

**Appendix A: Laplacian Spectrum on CP^{N-1}**
Source: `research/12-appendix-A-laplacian-spectrum.md`
Copy as-is.

**Appendix B: Instantons on CP^{N-1}**
Source: `research/13-appendix-B-instantons-on-cp2.md`
Copy as-is.

**Appendix C: Transfer Matrix**
Source: `research/14-appendix-C-transfer-matrix.md`
Copy as-is.

**Appendix D: Reflection Positivity**
Source: `research/15-appendix-D-reflection-positivity.md`
Add this note at the very top, before the first line of the file:
"NOTE: Rigorous reflection positivity for the Wilson action is
established via the Osterwalder-Seiler theorem (1978); see Section
4.1. This appendix provides physical context and motivation."

**Appendix E: Gauge Field Laplacian (Weitzenböck)**
Source: `research/18-appendix-G-gauge-laplacian.md`
Copy as-is.

**Appendix F: Area Law Implies Mass Gap**
Source: `research/17-appendix-F-area-law-mass-gap.md`
Copy as-is.

**Appendix G: The Multi-Time-Slice Analysis**
Source: `etc/proof/multi-time-slice-analysis.md`
This is a new appendix documenting the error found in an earlier
version of the closing argument and its correction. Include in full.
Add this header note:
"This appendix documents a stress-test of the temporal derivative
mechanism in the continuum limit argument. An error in an earlier
version of the closing argument was identified here and corrected;
the spectral intermediate-state mechanism (Section 5.5) is the
result. The appendix is included to show the argument has been
critically examined."

**Appendix H: Balaban Analyticity Extraction**
Source: `etc/proof/balaban-analyticity-extraction.md`
Include in full. This appendix maps exactly which Balaban results
are used and identifies the three [VERIFY] items for referees.

**Appendix I: Lüscher Test and Numerical Predictions**
Sources (assemble in order):
1. `luscher-test/lattice-data-summary.md` — the lattice data used
2. `luscher-test/38-luscher-results.md` — the main results
3. `luscher-test/RESULTS.md` — summary and conclusions
Add this header:
"This appendix reports the numerical test of the confining string
worldsheet prediction. The test uses existing published lattice data;
no new simulations were performed."

**References**
Source: `research/19-references.md`
Copy as-is. Add the following entries if not already present:
- Balaban, T.: "Renormalization group approach to lattice gauge field
  theories I-IX," CMP 95-119, 1982-1988.
- Dimock, J.: arXiv:1108.1335 (2011).
- Kotecký, R., Preiss, D.: CMP 83 (1982), 493-515.


---


## Files NOT to Include in the Preprint

The following exist in the repository but should NOT appear in the
preprint directory. They are research history, superseded drafts,
or exploratory dead ends.

From `research/` (formerly paper/):
- 01-strategy.md (planning document)
- 04-existence.md (superseded by etc/proof/01-setup.md)
- 06-osterwalder-schrader.md (superseded)
- 07-the-kk-bridge.md (superseded)
- 10-open-problems.md (superseded by proof status table)
- 21-53.md (all intermediate proof drafts, superseded by etc/proof/)
- All subdirectories: path-A/, path-B/, path-C/, 2d-attack-*/,
  attack-1/, attack-2/, attack-3/ (exploratory, not in paper)
- PLAN.md, TABLE-OF-CONTENTS.md (planning documents)

From `etc/proof/` — do NOT include in preprint sections:
- path-1-balaban-three-point.md (superseded approach)
- path-1a-integration-by-parts.md (superseded approach)
- path-1b-operator-decomposition.md (superseded approach)
- path-2-spectral-perturbation.md (superseded approach)
- path-2a-regularity-estimate.md (superseded approach)
- the-zero-mode-lemma.md (key findings absorbed into
  conjecture-1-closing.md and multi-time-slice-analysis.md)
- 10-open-problem.md (superseded by balaban-B1-B2-proof.md Part IV)
- conjecture-1-closing.md (superseded by balaban-B1-B2-proof.md,
  which contains the corrected, final argument)


---


## Task Instructions for Opus

**Step 1: Rename the directory.**
Move `/Users/gsix/yang-mills/paper/` to
`/Users/gsix/yang-mills/research/`.
Verify the move completed before proceeding.

**Step 2: Create the preprint directory structure.**
Create:
- `/Users/gsix/yang-mills/preprint/`
- `/Users/gsix/yang-mills/preprint/sections/`

**Step 3: Create preprint/README.md.**
Content: A short file (half page) explaining what this directory is
(submission-ready preprint), what research/ is (research history),
the reading order for the paper, and the three [VERIFY] items and
where to check them. The three [VERIFY] items are:
1. Analyticity of individual polymer activities (CMP 109, Sections 2-4)
2. k-independence of analyticity radius (CMP 109, Section 3)
3. Exactness of dimension-6 projection (CMP 109, Section 2)

**Step 4: Create preprint/PROOF-CHAIN.md.**
Copy Table IV.1 verbatim from `etc/proof/balaban-B1-B2-proof.md`.
Add above it: "The following table gives the complete proof chain.
Items marked [VERIFY] are reading exercises from Balaban's published
construction (CMP 109, 1987), not mathematical gaps."

**Step 5: Create preprint/TABLE-OF-CONTENTS.md.**
List every file in preprint/sections/ in reading order with one-line
descriptions and their source files.

**Step 6: Copy and edit all non-assembled sections.**
For Sections 1, 2, 3, 7, and all appendices: copy the source file
to preprint/sections/ with the filename convention below, applying
only the specific edits noted above. No other changes.

**Step 7: Assemble Section 4 (Lattice Mass Gap, Part I).**
Create `preprint/sections/04-lattice-proof-part1.md` by concatenating
in order: etc/proof/01-setup.md, 02-spectral-gap.md,
03-cluster-expansion.md, 04-lattice-mass-gap.md, 05-decoupling.md.
Add a section header before each file's content:
"## [Title of section from that file's first heading]"
Do not merge or edit the mathematical content.

Also copy `research/20-appendix-H-su2-warmup.md` as the SU(2)
subsection, appended at the end of Section 4 under the header
"## The SU(2) Exact Proof".

**Step 8: Assemble Section 5 (Continuum Limit).**
Create `preprint/sections/05-continuum-limit.md`.
This is the most complex assembly task. Structure:

Header: "# Section 5: The Continuum Limit"

Then for each subsection 5.1-5.7, add:
"## 5.X [Subsection Title]"
followed by the relevant content from the source file (as specified
above under "Section 5"), followed by a one-sentence transition
to the next subsection.

Transition templates (fill in the blanks):
- After 5.1: "With Balaban's framework established, we turn to the
  precise identification of the remaining bound."
- After 5.2: "The dimension-6 operator analysis now resolves this
  identification."
- After 5.3: "We now show how these operator bounds propagate
  through the RG."
- After 5.4: "The RG recursion is controlled; it remains to prove
  the single-step bound C_new."
- After 5.5: "We apply this lemma using analyticity properties of
  Balaban's construction."
- After 5.6: "The bound is established. We collect the conclusion."

**Step 9: Update the abstract and conclusion.**
Apply the specific text changes described above.

**Step 10: Assemble Section 6 (Referee Objections).**
Create `preprint/sections/06-referee-objections.md` following the
resolution map above.

**Step 11: Assemble Appendix I (Lüscher Test).**
Concatenate the three source files with appropriate subsection headers.

**Step 12: Final check.**
List all files in preprint/sections/ and verify every section and
appendix in the target structure is present. Report any missing files.


---


## Filename Convention for preprint/sections/

Use this naming:
- `00-abstract.md`
- `01-introduction.md`
- `02-geometric-framework.md`
- `03-quantitative-predictions.md`
- `04-lattice-proof-part1.md`
- `05-continuum-limit.md`
- `06-referee-objections.md`
- `07-previous-approaches.md`
- `08-conclusion.md`
- `A-laplacian-spectrum.md`
- `B-instantons.md`
- `C-transfer-matrix.md`
- `D-reflection-positivity.md`
- `E-weitzenboeck.md`
- `F-area-law-mass-gap.md`
- `G-multi-time-slice-analysis.md`
- `H-balaban-analyticity.md`
- `I-luscher-test.md`
- `references.md`


---


## Critical Constraints

1. **Do not change any mathematics.** If uncertain whether something
   is a mathematical change, do not make it. Flag it instead.

2. **Preserve all [VERIFY] markers exactly.** These are honest flags
   for the referee. Removing or softening them is dishonest and
   undermines the paper's credibility.

3. **Preserve all status markers** ([PROVED], [ARGUED], [CONDITIONAL])
   in proof documents. The honest accounting of proof status is a
   strength.

4. **Only five categories of new text are permitted:**
   a. The abstract table update (specified exactly above)
   b. The conclusion paragraph insertion (specified exactly above)
   c. The Appendix D note (specified exactly above)
   d. The Appendix G and I header notes (specified above)
   e. Section 5 transitions (specified above)
   f. README.md and PROOF-CHAIN.md (created from scratch as specified)
   Everything else is copying from source files.

5. **If a source file has an internal conflict** (e.g., says something
   is open that has since been proved), flag it with a comment
   `<!-- CONFLICT: [description] -->` rather than resolving it.

6. **The research/ directory must remain intact and unchanged.**
   Only rename it from paper/ to research/. Do not modify any files
   within it.


---


## What Success Looks Like

When complete, the repository structure is:

```
yang-mills/
├── etc/
│   ├── proof/           (unchanged — the definitive proof documents)
│   └── 10-drafting-the-preprint.md   (this file)
├── luscher-test/        (unchanged)
├── preprint/
│   ├── README.md
│   ├── TABLE-OF-CONTENTS.md
│   ├── PROOF-CHAIN.md
│   └── sections/
│       ├── 00-abstract.md
│       ├── 01-introduction.md
│       ├── 02-geometric-framework.md
│       ├── 03-quantitative-predictions.md
│       ├── 04-lattice-proof-part1.md
│       ├── 05-continuum-limit.md
│       ├── 06-referee-objections.md
│       ├── 07-previous-approaches.md
│       ├── 08-conclusion.md
│       ├── A-laplacian-spectrum.md
│       ├── B-instantons.md
│       ├── C-transfer-matrix.md
│       ├── D-reflection-positivity.md
│       ├── E-weitzenboeck.md
│       ├── F-area-law-mass-gap.md
│       ├── G-multi-time-slice-analysis.md
│       ├── H-balaban-analyticity.md
│       ├── I-luscher-test.md
│       └── references.md
├── referee/             (unchanged)
└── research/            (renamed from paper/, unchanged inside)
```

The preprint directory should be self-contained: a reader with access
only to preprint/ and the Balaban CMP series should be able to
verify the entire proof.
