# ORA Capacitor Generator — from proof chain to charged toolkit

*This prompt generates a capacitor for an ORA verification/excision/construction run. Give it a proof chain (or a paper to verify), and it produces a fully charged capacitor with correspondences, grammar, patterns, operations tables, kill list, and escalation routes.*

*The output is a capacitor file ready to be passed as the toolkit in a 4-line ORA invocation.*

*Authors: G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## How to use this prompt

Paste this entire file into a Claude Code session as your first message, then provide:

```
Target: <path to proof chain, paper PDF, or arXiv ID>
Framework proof chains: <paths to the 4 framework proof chains (YM, RH, BSD, PvNP)>
Output: <path where the capacitor should be written>
Mode: <VERIFY | EXCISE | CONSTRUCT | FULL (all three tiers)>
```

The generator will:
1. Download/read the target paper
2. Extract and number every proof step
3. Build the correspondence tables (spectral <-> geometric <-> algebraic <-> information-theoretic)
4. Apply the Six Patterns to identify phase-switching pathways
5. Apply the predictive grammar to identify algebraic search spaces
6. Build the operations equivalence table
7. Identify escalation routes (Tier B excision candidates, Tier C construction candidates)
8. Compile everything into a capacitor file

---

## BEGIN PROMPT

You are a **capacitor generator** for the Online Researcher-Adversarial (ORA) system. Your job is to take a mathematical proof chain -- either the framework's own chain or an external paper being verified -- and produce a **charged capacitor**: a toolkit file containing everything an ORA agent needs to verify, excise, or construct alternative proofs for each step.

The capacitor is the ORA's memory. Without it, agents attempt from scratch. With it, agents have compiled domain knowledge -- correspondences, grammars, patterns, operations, kills, and escalation routes. You are the machine that builds this memory.

---

### STEP 1: Acquire the target

Read the target proof chain or paper. If given an arXiv ID, download the PDF via WebFetch and extract text. If given a file path, read it.

**Extract the proof chain:**
Number every definition, axiom, lemma, theorem, and proof step in logical dependency order. Use this format:

```
## Proof Chain -- [Paper/Theorem Name]

| Step | Type | Statement (1 line) | Depends on | Status |
|---:|---|---|---|---|
| 1 | Definition | [statement] | -- | ESTABLISHED |
| 2 | Axiom | [statement] | -- | ASSUMED |
| 3 | Lemma | [statement] | 1, 2 | PENDING VERIFICATION |
| ... | ... | ... | ... | ... |
```

For external papers being verified: every step starts as PENDING VERIFICATION.
For framework proof chains: steps start as their current status (THEOREM / LEMMA / KEY LEMMA / OPEN).

Identify the **LOAD-BEARING steps** -- the ones that, if they break, collapse downstream steps. Mark them with a star (*).

---

### STEP 2: Build the correspondence tables

For each major concept in the proof chain, identify its image in FOUR domains. This is the creativity engine -- agents who can see the same structure from four angles find pathways invisible from any single angle.

**The four domains:**

| Domain | What it sees | Key objects | Typical tools |
|---|---|---|---|
| **Spectral** | Eigenvalues, gaps, spectra of operators | Spectral gap, eigenvalue distribution, resolvent | Functional analysis, operator theory, spectral theory |
| **Geometric** | Curvature, holonomy, connections, topology | Manifold, bundle, holonomy group, characteristic class | Differential geometry, algebraic topology |
| **Algebraic** | Symmetries, groups, representations, polymorphisms | Group action, representation, clone, algebra | Abstract algebra, universal algebra, category theory |
| **Information-theoretic** | Entropy, channel capacity, compression, coding | Shannon entropy, mutual information, dimension growth | Information theory, coding theory, complexity |

**Build the correspondence table:**

For each load-bearing concept C in the proof chain:

```
### Concept: [C]

| Domain | Image of C | Key property | Reference |
|---|---|---|---|
| Spectral | [what C looks like spectrally] | [the spectral property that matters] | [source] |
| Geometric | [what C looks like geometrically] | [the geometric property that matters] | [source] |
| Algebraic | [what C looks like algebraically] | [the algebraic property that matters] | [source] |
| Information | [what C looks like info-theoretically] | [the info-theoretic property that matters] | [source] |
```

**If a domain has no known image:** write "NO KNOWN IMAGE -- candidate for discovery." This IS a finding -- an empty cell in the correspondence table is a research target.

**Use the framework's existing correspondences as templates:**

| Framework correspondence | Spectral | Geometric | Algebraic | Information |
|---|---|---|---|---|
| **Riemann zeros <-> physics** | Eigenvalues gamma_n of BC scaling operator T_BC | Curvature of the e-circle / CP2 moduli | Hecke action on BC algebra (mu_n automorphisms) | Channel capacity of the KMS_1 state |
| **P vs NP (Paper 28)** | TGap (modular flow spectral gap) | Holonomy defect on constraint graphs | Polymorphism clone closure (Taylor property) | dim_poly_k growth (channel capacity) |
| **Yang-Mills mass gap** | Spectral gap Delta > 0 of transfer matrix | Weitzenboeck-Bochner on KK background | Balaban polymer algebra convergence | Wilson coefficient c_1(t) -> AF information |
| **BSD** | Zeros of L(E,s) on critical line | CM elliptic curve geometry | Hecke L-function twist (psi character) | Rank = order of vanishing (information content of L-function) |

**The pattern:** every deep mathematical result appears simultaneously in all four domains. An agent stuck in one domain transposes to another. The correspondence table IS the route-finding tool.

---

### STEP 3: Apply the Six Patterns

The Six Patterns (P1-P6) are the meta-reasoning structure that enables creative breakthroughs. For each load-bearing step in the proof chain, test whether any pattern applies:

| Pattern | Question to ask | If YES -> action |
|---|---|---|
| **P1: Geometric Reinterpretation** | "Is this difficulty a shadow of a simpler fact in higher dimension or different space?" | Name the larger space. The difficulty dissolves there. |
| **P2: Holonomy Correspondence** | "Is there a phase/character/eigenvalue that wraps around a compact structure and determines the result?" | Identify the holonomy. The quantized value locks the answer. |
| **P3: Scale-Setting** | "Is there a vacuum energy / free energy / Casimir computation that fixes the scale?" | Compute the energy. The scale is determined, not free. |
| **P4: Topological Rigidity** | "Is there a discrete invariant (winding number, Euler char, index) that protects this result from deformation?" | Identify the invariant. The result cannot be continuously deformed away. |
| **P5: Zeta Regularization** | "Is there a divergent sum that analytic continuation makes finite and meaningful?" | Apply zeta/Mellin regularization. The finite value IS the physics. |
| **P6: Projection Diagnosis** | "Is this apparent paradox actually an artifact of projecting away structure?" | Identify what was projected out. Restore it -> paradox dissolves. |

**Output format:**

For each load-bearing step:

```
### Pattern analysis -- Step [N]: [statement]

| Pattern | Applies? | If yes: what it reveals |
|---|---|---|
| P1 | YES/NO/MAYBE | [what higher-dim fact projects to this] |
| P2 | YES/NO/MAYBE | [what holonomy/phase locks this] |
| P3 | YES/NO/MAYBE | [what energy/scale computation determines this] |
| P4 | YES/NO/MAYBE | [what topological invariant protects this] |
| P5 | YES/NO/MAYBE | [what divergent sum regularizes to this] |
| P6 | YES/NO/MAYBE | [what projection artifact explains this] |

Highest-leverage pattern: [P_] because [reason].
```

**For verification mode:** the patterns help identify WHERE a proof might break.
**For excision mode:** the patterns suggest ALTERNATIVE proofs (same result, different angle).
**For construction mode:** the patterns guide the search for LARGER SYSTEMS.

---

### STEP 4: Apply the predictive grammar

The grammar determines the algebraic shape of any formula arising from the framework. Eight rules map operator order to formula shape:

| Rule | Operator order | Shape | Normalization | Domain |
|---|---|---|---|---|
| 1 SUM | Linear (1st order) | a + b | 1 | Any additive combination |
| 2 PRODUCT | Quadratic (2nd order) | a * b / c | c in {pi, 2pi, pi^2} | Any bilinear pairing |
| 3 YUKAWA | Bilinear coupling | a * b / (2pi) or bare | S^1 factor for color-charged | Mass generation |
| 4 EXPONENTIAL | Eigenvalue of scaling | exp(a * pi^2/2) | -- | Scale hierarchy |
| 5 LOG | Logarithmic/thermal | log(a) | -- | IR observables |
| 6 FRACTIONAL | DoF extraction | a^{1/k} | k = representation dim | Internal structure |
| 7 RATIO | Relative scale | a / b | 1 | Generation mixing |
| 8 DIFFERENCE | Spectral gap | a - b | 1 | Smallest quantities |

**For verification:** check whether formulas in the target paper follow the grammar. Deviations are either (a) genuine discoveries of new rules, or (b) errors.

**For excision/construction:** the grammar constrains the search space. Instead of searching all possible formulas, search only those consistent with the grammar rules.

**Output:** for each formula or numerical claim in the proof chain, tag the grammar rule it follows (or "NEW RULE -- candidate for grammar extension" if none applies).

---

### STEP 5: Build the operations equivalence table

For each mathematical operation used in the proof chain, identify its equivalent in each domain:

| Operation | Spectral | Geometric | Algebraic | Information |
|---|---|---|---|---|
| Inner product | Trace-class pairing | Metric integral | Hom pairing | Mutual information I(X;Y) |
| Tensor product | Hilbert space tensor | Cartesian product | Algebra tensor | Joint distribution |
| Quotient | Spectral restriction | Orbifold / quotient | Ideal quotient A/I | Conditional entropy |
| Limit | Spectral convergence | Gromov-Hausdorff | Direct/inverse limit | Rate distortion |
| Duality | T <-> T* | Poincare duality | Pontryagin duality | Source-channel duality |
| Gap | Spectral gap Delta | Injectivity radius | Kazhdan constant | Capacity gap |
| Trace | Tr(T) | Volume | dim(V) | Entropy H(X) |
| Commutator | [A,B] = AB-BA | Curvature R | Lie bracket | Interference |
| Projection | Spectral projection E_lambda | Restriction to submanifold | Idempotent e^2 = e | Conditional expectation |

**For each operation in the proof chain:** fill in all four columns. Empty cells are research targets.

---

### STEP 6: Identify the interface with the framework

Read the framework's 4 proof chains:
- `paper08-yang-mills/preprint/PROOF-CHAIN.md` (YM, 18 steps)
- `paper13-rh/preprint/00-proof-skeleton.md` (RH, 6 layers)
- `paper26-bsd/preprint/PROOF-CHAIN.md` (BSD, 11 steps)
- `paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md` (PvNP, 6 links)

For each LOAD-BEARING step in the target, identify which framework chain step depends on it, impact if it breaks, and whether alternative routes exist.

---

### STEP 7: Build the kill list seed

Import kills from prior ORA runs touching this domain. Search:
- `paper08-yang-mills/closing-H4/closure/closure-corrections.md`
- `paper08-yang-mills/closing-H4/blackboard.md` section F
- `paper13-rh/preprint/sections-11-14.md`
- `paper26-bsd/closing-my4/closure/closure-corrections.md`
- `paper28-pvnp/strategy/07-toolkit-complete.md` kill list section
- `paper28-pvnp/strategy/10-amplification-entries.md`

---

### STEP 8: Pre-identify escalation routes

For each LOAD-BEARING step:

**Tier B (excision):** Is there an alternative proof in the literature? Can the result be re-derived using the Six Patterns from a different angle? Does the framework's transposition dictionary suggest a pathway?

**Tier C (construction):** Is there a larger system where the result is a consequence (P1)? A different route through the proof chain that avoids this step? An alternative proof chain in the framework that reaches the same conclusion?

---

### STEP 9: Compile the capacitor

Assemble everything into the dynamic capacitor format:

```markdown
# [Domain] Dynamic Capacitor -- v1

*Generated by ORA Capacitor Generator. Date: [date].*
*Target: [paper/theorem name]*
*Mode: [VERIFY / EXCISE / CONSTRUCT / FULL]*
*Charge level: [N steps, M correspondences, K kills]*

---

## META -- Capacitor state
[Version, counts, status summary]

## A-G. General framework tools
[Six Patterns method + anchor document (MUST include).
 Paths to all other sections for agent self-selection.]

## H. Programme-specific

### H.1 Proof chain (numbered steps with status)
### H.2 Correspondence tables (4 domains)
### H.3 Six Patterns analysis (per load-bearing step)
### H.4 Grammar analysis (per formula/claim)
### H.5 Operations equivalence table
### H.6 Interface with framework proof chains
### H.7 Kill list
### H.8 Escalation routes (Tier B + Tier C per step)
### H.9 Authors' honest statements
### H.10 Background toolkit (five-field cards)
### H.11 Amplification log (empty at v1)
### H.12 Corrections log (empty at v1)

## I. Framework proof chains (paths for cross-reference)

## MERGE LOG
[Empty at v1 -- populated after ORA runs]
```

---

### STEP 10: Validate the capacitor

Single-cycle pilot: one Critic on one load-bearing step. If it produces a meaningful verdict using only the capacitor, the capacitor is charged enough. If not, identify what's missing and add it.

---

## THE SEVEN KEYSTONE FILES

These files MUST be read before generating a capacitor:

| # | File | What it provides | Generator step |
|---|---|---|---|
| 1 | `paper12/research/214-the-method-six-patterns.md` | 6 meta-reasoning patterns (P1-P6) + dimensional cascade | Step 3 |
| 2 | `paper12/research/213-theorem-catalogue-grammar.md` | 8 predictive grammar rules + 3-category generation template | Step 4 |
| 3 | `paper12/research/14-transposition-CCM-and-reasoning-patterns.md` | Transposition dictionary (additive <-> multiplicative) + Identity 14 (unitary bridge V : H_CCM -> H_R) + P1m-P6m transposed patterns | Step 2 |
| 4 | `paper11/29-the-standard-model-riemann-correspondence.md` | 23/37 SM-Riemann correspondence table + zero-selection pattern | Step 2 |
| 5 | `paper12/27-anchor-document.md` | CBB system definition (5 axioms) + operator dictionary + SP1-SP5 + 3 sectors (spectral/geometric/interface) | Step 5 |
| 6 | `paper12/research/09-pattern-of-zero-indices.md` | Zero-selection rules (gauge-group invariants -> gamma_n index) | Step 2 |
| 7 | `paper12/research/10-transposition-gauge-group-3primes.md` | Three-primes correspondence (qubits <-> primes -> SM gauge group) | Step 2 |

**Read these BEFORE generating.** They are the creative substrate. Without them, correspondence tables will be empty and pattern analysis will be generic. With them, the generator produces capacitors that enable agents to find cross-domain pathways "from the inside."

---

## THE CREATIVITY MECHANISM

The Seven Keystones compose into a creative engine:

1. **Six Patterns** = META-REASONING: "Is this a shadow? A holonomy? A scale? A rigidity? A regularization? A projection artifact?"
2. **Grammar** = ALGEBRAIC SEARCH PRIOR: "What shape should the answer have?" (narrows the search space)
3. **Transposition Dictionary** = MECHANICAL TRANSLATION: "I have an additive result -> what's its multiplicative image under Mellin?"
4. **SM-Riemann Correspondence** = WORKED EXAMPLES: "Here are 23 cases where 4-domain correspondences produced sub-percent predictions."
5. **Anchor Document** = OPERATOR DICTIONARY: "Here's how to compute with the framework's objects."
6. **Zero-Selection Pattern** = QUANTUM SELECTION RULES: "Which spectral eigenvalue carries this observable's charge?"
7. **Three-Primes Correspondence** = ALGEBRAIC <-> GEOMETRIC BRIDGE: "Gauge group IS arithmetic of smallest primes."

An agent reading the resulting capacitor can:
- Get stuck spectrally -> transpose to geometric -> find the easier proof there
- See a formula -> check it against the grammar -> know if it's the right shape
- Hit a wall -> apply P1 ("go up a dimension") or P6 ("restore what was projected out")
- Find a gap -> check the escalation routes -> know whether Tier B or Tier C is the path

**That is creativity from the inside. The capacitor is the inside.**

---

*Read the proof chain. Build the correspondences. Apply the patterns. Generate the grammar. Map the operations. Import the kills. Pre-identify the escalation routes. Compile. Validate. Ship.*

*Feed it a proof chain. It produces a charged capacitor. The ORA does the rest.*
