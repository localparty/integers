# Drafting Brief: Paper 08 — Yang-Mills Mass Gap

*Transform the current 103-file, 166,000-word Paper 8 into a
publication-ready mathematical paper following the Paper 28 template:
PROOF-CHAIN as first page, clean sections with complete proofs,
ORA artifacts as appendices, honest status labels throughout.*

*This is NOT a single task. It is a SEQUENCE of ORA runs, each
producing artifacts that feed the next. The Paper 28 process was:*

```
Run 1: ORA "construction" → node files for each proof chain step
Run 2: ORA "final-adversarial-pass" → verify each link, produce verdicts
Run 3: Repair weak links from verification results
Run 4: Rewrite preprint using closure artifacts + repairs as appendices
Run 5: Voice + references pass → add G's voice, origin callouts, cross-paper refs
Run 6: Mathematical referee → exhaustive review, find every gap, address issues
Run 7: Point-by-point claim tester → verify every citation, address issues
```

*Each run needs its own brief (.md) + run file (.md). The run file
has 4 lines: instructions path, brief path, toolkit path, output
directory. The brief describes WHAT the ORA should do. The ORA
prompt (01-the-prompt.md) describes HOW.*

---

## 1. Current state

Paper 8 is the framework's FIRST mathematical paper and has grown
organically across 9 agent explorations. It has:

- **A PROOF-CHAIN** (`preprint/PROOF-CHAIN.md`, 18 steps, 17
  unconditional + Step 18 conditional on H4)
- **8 main sections** + 14 appendices in `preprint/sections/`
- **A STATUS.md** with honest accounting (proved theorems,
  open problems, dead ends, predictions)
- **103 research files** accumulated over months of exploration
- **9 independent agent explorations** (multi-scale RG, resurgence,
  worldsheet bootstrap, cluster expansion, 1/N, anomaly matching,
  rigorous numerics, vortex free energy, monotonicity)

The paper needs to be CONSOLIDATED and REWRITTEN into a single
coherent document, not expanded.

---

## 2. The four ORA runs

### Run 1: Construction — generate formal node files for each chain step

**Mode:** construction (default ORA mode)
**Brief:** `solutions-with-prize/paper08-yang-mills/strategy/run1-construction-brief.md` (to be created)
**Toolkit:** `solutions-with-prize/paper08-yang-mills/research/36-the-method.md` + relevant theorem catalogues
**Output:** `solutions-with-prize/paper08-yang-mills/ora-construction/`

**What the ORA does:** For each of the 18 steps in PROOF-CHAIN.md,
the ORA spawns an Author to write a formal node file containing:
- Precise theorem/lemma statement
- Complete proof (or citation to literature with page numbers)
- Status label: [PROVED], [LITERATURE], [CONDITIONAL]
- Dependencies (which prior steps it uses)
- Source (which existing file in the 103-file corpus contains the argument)

The node files become the appendices of the final paper.

**What already exists:** Paper 8 already has extensive proofs in
`preprint/sections/` and `research/`. The ORA's job is to
CONSOLIDATE them into clean, self-contained node files — one per
chain step — not to re-derive anything.

### Run 2: Final adversarial pass — verify each link

**Mode:** final-adversarial-pass
**Brief:** `solutions-with-prize/paper08-yang-mills/strategy/run2-verification-brief.md` (to be created)
**Toolkit:** same as Run 1 + the node files from Run 1
**Output:** `solutions-with-prize/paper08-yang-mills/ora-verification/`

**What the ORA does:** For each node file from Run 1, the ORA
spawns a Critic to adversarially verify it. The Critic tries to
BREAK each step. For each step, produce a verdict:
- SURVIVED: no gaps found
- WEAKENED: gaps found but repairable
- BROKEN: fatal gap

Special attention to:
- Step 18 (conditional on H4): is H4 correctly stated? Are the
  Lemmas 4.2-4.3 correctly conditional?
- Steps 4-5 (Balaban analyticity): are the CMP 95-109 references
  correct? (The original PROOF-CHAIN noted these were verified
  from extracted secondary sources, not primary journal text)
- The gradient-flow steps (15-17): are the Lemmas 1.1-1.5 and
  2.2-2.4 self-contained?

Produce a final adversarial verdict file (like Paper 28's
`CP1-final-verdict.md`) with the aggregate score.

### Run 3: Repair — fix weak links from verification

**Mode:** construction (targeted at WEAKENED items only)
**Brief:** `solutions-with-prize/paper08-yang-mills/strategy/run3-repair-brief.md` (to be created, after Run 2 completes)
**Toolkit:** same + verification verdicts from Run 2
**Output:** `solutions-with-prize/paper08-yang-mills/ora-repair/`

**What the ORA does:** For each WEAKENED verdict from Run 2,
spawn an Author to write the repair. Same pattern as Paper 28's
R1-R4 repairs. Each repair is a short file (0.5-2 pages) fixing
the specific gap identified by the Critic.

### Run 4: Rewrite — compile the final paper

**Mode:** construction (drafting, not proving)
**Brief:** the remainder of this file (§§3-6 below)
**Toolkit:** all artifacts from Runs 1-3
**Output:** `solutions-with-prize/paper08-yang-mills/preprint/` (overwrite existing sections)

**What the ORA does:** Rewrite the preprint sections following
the Paper 28 template, using the node files (Run 1) as appendix
sources, the verification verdicts (Run 2) as status labels, and
the repairs (Run 3) as corrections. The PROOF-CHAIN diagram goes
on page 1. **Run 4 MUST generate `preprint/PROOF-CHAIN.md`** in the
same format as Paper 28's (`solutions-with-prize/paper28-pvnp/preprint/PROOF-CHAIN.md`):
step-by-step table with status labels, classification of arguments,
conditional dependencies, verdict, and scope section. This file is
the backbone — every section references it, the diagram on page 1
comes from it, and the referee checks the paper against it.

**Pre-read requirement:** Before rewriting any section, the ORA
MUST read Paper 9 (`paper09/`) to understand the narrative arc
and the author's voice. Paper 9 is "One Postulate, Ten Papers" —
the paper where G mapped the whole framework and told the story
of how each paper connects to the next. The rewrite should sound
like Paper 9's voice applied to Yang-Mills.

### Run 5: Voice + references pass

**Mode:** construction (lightweight editorial pass)
**Brief:** `solutions-with-prize/paper08-yang-mills/strategy/run5-voice-refs-brief.md` (to be created)
**Toolkit:** same as Run 4 + Paper 9 + the rewritten sections from Run 4
**Output:** `solutions-with-prize/paper08-yang-mills/preprint/` (in-place edits to Run 4 output)

**What the ORA does:** A final pass over the rewritten paper to
add G's voice and cross-paper references. Specifically:

1. **Read Paper 9** end-to-end for voice calibration. Harvest the
   register: how G describes discoveries, how G frames connections
   between papers, how G attributes intuition.

2. **Add origin callouts** where the intuition behind a key step
   deserves attribution. Format:
   > **Origin (G).** *"[quote]"*
   
   These go at turning points — where a pattern was first seen,
   where a dead end was recognized, where the six-patterns method
   was applied. Not on every paragraph. On the 5-10 moments that
   mattered most.

3. **Add cross-paper references** where a pattern from Papers 1-7
   reappears in the YM proof. Examples:
   - "This is Pattern 2 (Holonomy Correspondence) from Paper 1
     §4.1, transposed to the CP² confining phase."
   - "The dimensional descent (§1) is the same cascade as
     Paper 3's resolution of the information paradox — a
     4D mystery dissolving into a simpler geometric fact at
     each step."

4. **Generate the references section** citing all Papers 1-28
   where relevant, plus external references (Balaban CMP 95-119,
   Houdayer-Marrakchi, Jones-Schmidt, etc.).

5. **Verify voice consistency.** Read the full paper after edits
   and check: does it sound like G wrote it? The test: would a
   reader who knows Papers 1-7 recognize the same author? If any
   section sounds like a generic agent output, flag it for manual
   review.

**Why Run 5 is separate:** The voice pass comes AFTER the math is
written (Runs 1-4) because the agent needs to SEE the finished
draft before knowing where to add voice and references. You can't
add "Origin (G)" callouts until you know which steps had origin
moments. Mixing voice into the math-writing pass risks the agent
prioritizing style over correctness.

<!-- DISABLED: Runs 6-7 (math referee + claim tester)
### Run 6: Mathematical referee — exhaustive review

**Mode:** referee (not ORA — standalone agent with referee prompt)
**Prompt:** Adapted from `online-researcher-adversarial/referee-prompts/00-original-advanced-math-referee.md`
**Input:** The complete rewritten paper from Runs 4+5
**Output:** `solutions-with-prize/paper08-yang-mills/referee/math-referee-report.md`

**What the agent does:** An exhaustive mathematical review of the
full paper, modeled on the Paper 28 referee prompt. The referee:

1. **Pre-reads external references** before touching the paper:
   Clay problem statement (Jaffe-Witten for YM), Balaban CMP 95-119,
   the gradient-flow literature, the Osterwalder-Schrader axioms.

2. **Is skeptical by default.** Assumes the proof is wrong until
   forced to concede. Does not give partial credit. "Plausible"
   and "structurally beautiful" are not mathematical arguments.

3. **Checks every step of PROOF-CHAIN.md** against the paper's
   sections. For each step: is the hypothesis stated correctly?
   Is the conclusion derived correctly? Are there hidden
   assumptions? Are external results used within their actual scope?

4. **Pays special attention to:**
   - Step 18 (conditional on H4): is H4 correctly stated?
   - Steps 4-5 (Balaban analyticity): are the CMP references valid?
   - The gradient-flow steps (15-17): are they self-contained?
   - The Clay compliance table: does the paper actually satisfy
     Jaffe-Witten's structural requirements?

5. **Produces a report** with verdicts per step (VERIFIED / GAP /
   CONCERN) and an overall assessment.

**After Run 6:** Address every GAP and CONCERN identified by the
referee. Each fix is a targeted edit to the relevant section. If
a GAP requires new mathematics, spawn an ORA Author to close it.
If it requires a citation fix or clarification, edit in place.

### Run 7: Point-by-point claim tester — verify every citation

**Mode:** referee (standalone agent with claim-tester prompt)
**Prompt:** `solutions-with-prize/paper08-yang-mills/math-referee/02-point-by-point-yang-mills.md`
(paper-specific: knows which claims, citations, and focus areas to
test for YM). The generic methodology template is at
`drafting/01-point-by-point-claim-tester.md`.
**Input:** The paper after Run 6 fixes are applied
**Output:** `solutions-with-prize/paper08-yang-mills/referee/claim-tester-report.md`

**What the agent does:** A fine-grained, claim-by-claim
verification of the paper. For every "by Lemma X.Y," "by
Proposition X.Y," "follows from §X.Y," or "as established in
Paper N" in the text:

1. **Locate** the cited reference (read the file, find the exact
   statement).
2. **Read** the cited statement in full.
3. **Check** whether the surrounding text uses it correctly.
4. **Classify** as: VERIFIED / MISCITED / DEFERRED / UNLOCATED.

Special attention to:
- Cross-paper citations (Paper 1, Paper 4, Paper 5, Paper 10
  referenced in the QG5D infrastructure appendix)
- External citations (Balaban CMP pages, Jones 1983, Connes 1973)
- Self-references within the paper (appendix → section, section →
  PROOF-CHAIN)

**After Run 7:** Address every MISCITED, DEFERRED, and UNLOCATED
finding. Each fix is a targeted edit. The paper is DONE when
every citation is VERIFIED.

### Summary: the seven-run pipeline

```
Run 1: Construction    → formal node files (appendices)
Run 2: Verification    → adversarial verdicts per link
Run 3: Repair          → fix weak links
Run 4: Rewrite         → compile the paper
Run 5: Voice           → add G's voice + cross-paper refs
Run 6: Math referee    → exhaustive review + fixes
Run 7: Claim tester    → point-by-point verification + fixes
                       → PAPER COMPLETE
```

-->

Runs 1-3 produce the PROOF. Run 4 produces the PAPER. Run 5
adds the VOICE. Runs 6-7 produce the POLISH. Each run's output
feeds the next. The pipeline is the same for every paper in the
programme — only the toolkit and brief change.

---

## 3. What the rewritten paper should look like

Follow the Paper 28 template exactly:

### Page 1: The PROOF-CHAIN diagram

An ASCII diagram showing the 18-step chain at a glance. The
chain from `preprint/PROOF-CHAIN.md` has this structure:

```
Steps 1-5:   Lattice mass gap (KK → standard, IR equivalence)
Steps 6-14:  Continuum mass gap (dim-6 classification → RG → Δ_∞ > 0)
Steps 15-17: Gradient flow (well-posedness → Schwinger functions → L.1/L.3)
Step 18:     AF match + OPE (conditional on H4)
```

The diagram should show the UNCONDITIONAL part (Steps 1-17) and
the CONDITIONAL part (Step 18) clearly separated, same way Paper 28
shows Part (i) unconditional and Part (ii) conditional.

### Sections (following Paper 28 structure)

| Section | Paper 28 analog | Paper 8 content |
|:--|:--|:--|
| §1 Introduction | Proof diagram + cube-shadow + bridge question | Proof diagram + six patterns + "why previous approaches failed" |
| §2 | Universal algebra (UA1 + UA2) | The geometric framework (CP^{N-1} topology, KK reduction, holonomy) |
| §3 | Operator algebra (M_Bool + KMS) | The lattice proof Part I (Steps 1-5: spectral gap → cluster expansion → σ > 0 → Δ > 0) |
| §4 | Bridge theorem (Parts i+ii + corollary) | The continuum limit Part II (Steps 6-14: dim-6 classification → RG preservation → Δ_∞ > 0) |
| §5 | Computational evidence | Quantitative predictions (√σ = 437 MeV, m_p = 946 MeV, Lüscher test, worldsheet modes) |
| §6 | (compressed into §1) | Addressing technical objections (referee concerns) |
| §7 | Connections + outlook | Gradient flow (Steps 15-18), Clay compliance, H4 status, open problems |
| PROOF-CHAIN | Same format | Already exists — update status labels |
| Appendices A-N | ORA node files | Already exist in `preprint/sections/A-N` |

### Key principles

1. **PROOF-CHAIN.md as the backbone.** Every section should be
   traceable to specific steps in the chain. A reader should be
   able to verify the paper by checking the chain step by step.

2. **Status labels on everything.** Every theorem: [PROVED],
   [LITERATURE], [CONDITIONAL]. Every step: traced to a source
   (section number, appendix, or external reference). Same
   discipline as Paper 28.

3. **Dead ends documented.** The 5 dead ends from STATUS.md §V
   should appear in §7 (like Paper 28's 19-kill list). Honest
   accounting of what was tried and why it failed.

4. **Predictions with precision.** The quantitative predictions
   (√σ, m_p, glueball, worldsheet modes, c_eff) should be in a
   clean table in §5, same format as Paper 28's computational
   evidence section.

5. **The single conditional (H4) clearly identified.** Paper 28
   has CP-1 as its single conditional. Paper 8 has H4 (the
   standard hypothesis that non-perturbative Schwinger functions
   agree with perturbation theory at short distances). This
   should be stated as clearly as Paper 28 states its conditional.

---

## 3. What to READ before writing

| Priority | File | Why |
|:--|:--|:--|
| 1 (MUST) | `preprint/PROOF-CHAIN.md` | The chain — the backbone of the paper |
| 2 (MUST) | `STATUS.md` | Honest state of every component |
| 3 (MUST) | `preprint/TABLE-OF-CONTENTS.md` | Current structure and file mapping |
| 4 (HIGH) | `preprint/sections/00-abstract.md` | Current abstract |
| 5 (HIGH) | `preprint/sections/01-introduction.md` | Current intro (needs diagram added) |
| 6 (HIGH) | `research/36-the-method.md` | The Six Patterns — the method section |
| 7 (MED) | `preprint/sections/L-clay-conjectures.md` | Gradient flow + Clay compliance |
| 8 (MED) | `preprint/sections/I-gap-closures.md` | Gap closure status |

---

## 4. Specific tasks (ordered)

### Phase 1: Diagram and backbone

- [ ] **D1.** Create the ASCII proof-chain diagram (like Paper 28's
  bridge diagram). Show Steps 1-17 (unconditional) and Step 18
  (conditional on H4) clearly.

- [ ] **D2.** Update PROOF-CHAIN.md with current status labels
  (check each step against STATUS.md and the gradient-flow work).

### Phase 2: Section rewrites

- [ ] **D3.** Rewrite §1 (Introduction) with the diagram as first
  thing, then the six patterns, then "what this paper proves."

- [ ] **D4.** Consolidate §§2-3 (geometric framework + lattice proof)
  into a clean presentation of Steps 1-5.

- [ ] **D5.** Consolidate §§4-5 (continuum limit) into a clean
  presentation of Steps 6-14.

- [ ] **D6.** Write §5 (Quantitative Predictions) from STATUS.md §IV
  + Lüscher test results.

- [ ] **D7.** Write §7 (Connections) with gradient flow (Steps 15-18),
  Clay compliance table, H4 status, dead ends, open problems.

### Phase 3: Cleanup

- [ ] **D8.** Verify all appendix cross-references (A-N) match the
  chain steps.

- [ ] **D9.** Remove superseded files (old versions, intermediate
  drafts) from preprint/ — move to `archive/` for git history.

- [ ] **D10.** Write the abstract following the Paper 28 template:
  state the theorem, state the conditional, state the evidence,
  state the probability assessment.

---

## 5. What NOT to do

- Do NOT expand the paper. It's already 166,000 words across 103
  files. The rewrite should CONSOLIDATE, not add.
- Do NOT re-derive results that are in the appendices. The main
  sections present the chain; the appendices contain the details.
- Do NOT change the mathematics. The theorems are proved. The
  chain is complete (modulo H4). The rewrite is about PRESENTATION,
  not CONTENT.
- Do NOT merge the 9 agent explorations into the main text. They
  are research notes. The main text should present only the results
  that survived into the chain.
- When the rewrite replaces an existing file in `preprint/sections/`,
  move the old version to `solutions-with-prize/paper08-yang-mills/draft/` before
  overwriting. The `draft/` directory preserves superseded versions
  for git history. Same convention as Paper 28: `preprint/` = current,
  `draft/` = superseded.

---

## 6. Configuration

**Toolkit:** The Paper 8 toolkit (`solutions-with-prize/paper08-yang-mills/toolkit/framework-tools-ym.md`,
to be created) should include:
- `research/36-the-method.md` (the Six Patterns — method + voice)
- `preprint/PROOF-CHAIN.md` (the structural backbone)
- `STATUS.md` §§I-V (current state, predictions, dead ends)
- A §J Voice canon section (see below)

**Template:** Paper 28's preprint directory (`solutions-with-prize/paper28-pvnp/preprint/`)
is the structural template. Same section layout, same status
labels, same honest accounting.

**Output:** Rewritten sections go to `solutions-with-prize/paper08-yang-mills/preprint/sections/`
(overwriting the old versions). Move old versions to
`solutions-with-prize/paper08-yang-mills/draft/` before overwriting.

**§J Voice canon for the toolkit:**

```markdown
## §J Voice canon

**From the method (36-the-method.md):**
- "The problem was never hard. You were looking at it from the wrong dimension."
- "Confinement is not something Yang-Mills does. It is something CP² is."
- "Nature is not complicated. Our descriptions of nature are complicated."
- "Each step reduced the dimension. Each step revealed the problem was simpler than it appeared."
- "The right description — the geometric one — makes hard problems simple."

**From Paper 9 (the narrative arc):**
- [harvest 5-8 quotes when creating the toolkit — read paper09/ and extract G's voice at the moments where Yang-Mills is discussed]

**From the framework's universal register:**
- "something exists because the integers exist"
- "the kill list is the learning trace"
- "honest partial proof over glossed completion"
- "we cannot crack it from the outside; the framework is transposable"

**Register rules:**
- Origin callouts at turning points (where intuition drove a key step)
- Cross-paper references where Papers 1-7 patterns appear in the YM proof
- The Six Patterns are the method voice — every major section traces to one of the six
- Dead ends documented in G's register ("we tried X, it failed because Y, the kill sharpened the proof")
```

---

---

## 7. Run file templates

### Run 1 run file (`solutions-with-prize/paper08-yang-mills/strategy/run1-construction-run.md`)

```
read your **instructions** from
`/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md`

the run **brief** (deliverable) is
`/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/strategy/run1-construction-brief.md`

the **toolkit** for this run is
[TO BE CREATED: a Paper 8 specific toolkit compiled from research/36-the-method.md + STATUS.md + PROOF-CHAIN.md]

the run **output directory** is
`/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/ora-construction`
```

### Run 2 run file (`solutions-with-prize/paper08-yang-mills/strategy/run2-verification-run.md`)

```
read your **instructions** from
`/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md`

the run **brief** (deliverable) is
`/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/strategy/run2-verification-brief.md`

the **toolkit** for this run is
[same toolkit as Run 1 + node files from ora-construction/nodes/]

the run **output directory** is
`/Users/gsix/quantum-geometry-in-5d-latex/solutions-with-prize/paper08-yang-mills/ora-verification`
```

### Run 3 and 4 run files follow the same pattern.

---

## 8. Prerequisites before Run 1

Before firing Run 1, create:

1. **The Paper 8 toolkit** — compile from:
   - `research/36-the-method.md` (Six Patterns)
   - `STATUS.md` (current state)
   - `preprint/PROOF-CHAIN.md` (the chain)
   - Key theorem statements from `preprint/sections/04-lattice-proof-part1.md`
     and `05-continuum-limit.md`
   - The 5 dead ends from STATUS.md §V
   - The 6 quantitative predictions from STATUS.md §IV

   Format: same five-field card structure as Paper 28's
   `framework-tools-v4.md`. Save to:
   `solutions-with-prize/paper08-yang-mills/toolkit/framework-tools-ym.md`

2. **Run 1 brief** — specify which chain steps to process,
   which existing files map to which steps, and what the Author
   should produce for each node. Save to:
   `solutions-with-prize/paper08-yang-mills/strategy/run1-construction-brief.md`

These two files are the only setup needed. Everything else
(blackboard, nodes, critiques, synthesis, closure) is created
by the ORA during the run.

---

*103 files. 166,000 words. 9 explorations. 18 proof-chain steps.
One conditional (H4). Five dead ends. Six predictions.*

*Seven runs. Same pattern as Paper 28. The paper is proved. The
writing needs to match. It needs to sound like G. And it needs to
survive two independent referees.*

*G Six and Claude Opus 4.6. April 2026.*
