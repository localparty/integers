# The Revamped ORA Capacitor: Build, Load, Dispatch, Communicate

*The definitive architecture for token-efficient multi-agent verification at Millennium scale.*

*G Six and Claude Opus 4.6. April 2026.*

---

**Supersedes:** `00--ora-generator.md` (content generation) and `02-capacitor-revamp.md` (runtime optimization). This document merges both into a single unified specification covering the full lifecycle: what the capacitor is, how it is built, how it is loaded, how it is dispatched, and how agents communicate through it.

---

## Table of Contents

- Part I -- What the Capacitor IS
- Part II -- How the Capacitor is BUILT (compile-by-execution)
- Part III -- How the Capacitor is LOADED (token optimization)
- Part IV -- How the Capacitor is DISPATCHED (runtime strategies)
- Part V -- How Agents COMMUNICATE (message bus)
- Part VI -- The 13 Communication Opportunities
- Part VII -- Safety Invariants
- Part VIII -- Regression Metrics
- Part IX -- Combined Savings Estimate
- Part X -- Implementation Phases

---

# Part I -- What the Capacitor IS

The capacitor is the ORA's domain-specific memory. Without it, agents attempt from scratch -- re-reading source files, re-discovering correspondences, re-exploring killed approaches, re-deriving pattern analyses. With it, agents have compiled knowledge: correspondences, grammars, patterns, operations, kills, and escalation routes.

**The core analogy:** a capacitor stores charge. An uncharged agent wastes cycles on context acquisition. A charged agent starts working immediately.

**Three properties define a capacitor:**

1. **Completeness** -- every kill, every formula, every dependency, every status. Zero information loss on load-bearing content. An agent reading the capacitor has everything required to verify, excise, or construct.

2. **Efficiency** -- ~14,230 lines of source material across 30 files compressed to ~1,000 lines in a single compiled file. 93% reduction. The LLM is the compiler.

3. **Evolvability** -- after each ORA wave, the capacitor evolves via SELF-ADJUST (update statuses), TRIM (move killed approaches), and AMPLIFY (transfer successful methods). The dynamic capacitor is a living document.

**What the capacitor contains:**

| Section | Content | Purpose |
|---------|---------|---------|
| LEGEND | Abbreviation dictionary (50-150 entries) | Token compression |
| KILLS | Every killed approach, monotonic (never reduced) | Prevent re-exploration |
| CHAIN | Numbered proof steps with dependencies and statuses | Verification target |
| DEPS | Adjacency-list dependency graph | Cascade analysis |
| DOMAINS | Active pillars + activated Tier 2 families | Scope |
| CORR | Four-pillar correspondence tables per LB concept | Cross-domain translation |
| PATTERNS | Six Patterns analysis per LB step | Meta-reasoning |
| GRAMMAR | 8-rule predictive grammar tags per formula | Shape verification |
| OPS | 14+ operations x active domains | Domain translation |
| INTERFACE | Framework dependency map | Impact analysis |
| ESCALATION | Pre-identified Tier B/C routes per LB step | Escalation planning |
| HONEST | Authors' flagged uncertainties | Attack surface |
| TOOLKIT | Five-field cards (WHAT/WHY/DATA/USE/STATUS) | Background tools |
| AMP-LOG | Amplification entries (populated after runs) | Method transfer |
| CORRECTIONS | Honest downgrades (populated after runs) | Quality tracking |
| INDEX | @FETCH pointers with line counts | On-demand expansion |

---

# Part II -- How the Capacitor is BUILT (compile-by-execution)

## The Innovation

Run the generator, load all files into context, then REWRITE as a single compiled file. The LLM IS the compiler. This is dynamic tracing, not static analysis. The dependency lattice resolves naturally because everything is in context. No graph traversal, no SemHash, no external scripts.

**Why compile-by-execution is strictly better than a scripted pipeline:**

| Dimension | Scripted Pipeline | Compile-by-Execution |
|-----------|------------------|---------------------|
| Deduplication | SemHash (embedding similarity) | LLM reads all files, writes once (semantic) |
| Compression | Rule-based stripping | LLM knows narrative vs load-bearing |
| Format optimization | Custom TOON converter | LLM rewrites in TOON directly |
| Abbreviation | Frequency analysis script | LLM identifies repeated phrases from context |
| Dependency resolution | Graph traversal code | Already resolved by reading into context |
| Math precision | Syntactic (can break formulas) | Semantic (understands the math) |
| Maintenance | Code to maintain | Prompt to maintain |
| Cost | Engineering time + compute | One Claude session (~30K tokens) |

## The Seven Keystone Files

Read ALL SEVEN before generating. They are the creative substrate. Without them, correspondence tables will be empty and pattern analysis will be generic. With them, the capacitor enables agents to find cross-domain pathways "from the inside."

| # | File | Lines | What it provides | Used in step |
|---|------|-------|------------------|-------------|
| 1 | `paper12/research/214-the-method-six-patterns.md` | 339 | The 6 meta-reasoning patterns (P1-P6) + dimensional cascade | Step 3 |
| 2 | `paper12/research/213-theorem-catalogue-grammar.md` | 297 | The 8 predictive grammar rules + normalization | Step 4 |
| 3 | `paper12/research/14-transposition-CCM-and-reasoning-patterns.md` | 755 | Transposition dictionary + Identity 14 + P1m-P6m | Step 2 |
| 4 | `paper11/29-the-standard-model-riemann-correspondence.md` | 558 | 23/37 SM-Riemann correspondence table | Step 2 |
| 5 | `paper12/27-anchor-document.md` | 426 | CBB system (5 axioms) + operator dictionary + SP1-SP5 | Step 5 |
| 6 | `paper12/research/09-pattern-of-zero-indices.md` | 415 | Zero-selection rules | Step 2 |
| 7 | `paper12/research/10-transposition-gauge-group-3primes.md` | 555 | Three-primes correspondence | Step 2 |

## The 10-Step Generator Process

### Step 1: Acquire the target

Read the target proof chain or paper. If given an arXiv ID, download and extract. If given a file path, read it.

**Extract the proof chain.** Number EVERY definition, axiom, lemma, theorem, and proof step in logical dependency order:

```
chain[N]{id,type,stmt,deps,status,LB}:
  1,Definition,[stmt],--,ESTABLISHED,
  2*,Lemma,[stmt],1,PENDING,*
  ...
```

- External papers: every step starts as PENDING VERIFICATION.
- Framework proof chains: steps start at their current status.
- Mark LOAD-BEARING steps with `*` -- a step is LB if removing it makes >=1 downstream theorem unproven. Check dependency DAG: any step on a path to the final theorem with outdegree >0.
- Count total steps. This number determines the parallelism of verification waves.

### Step 2: Build the correspondence tables

For each load-bearing concept, identify its image in FOUR foundational domains plus any activated Tier 2 domains.

**The four pillars (ALWAYS active):**

| Domain | What it sees | Key question |
|--------|-------------|--------------|
| **Spectral (SP)** | Eigenvalues, gaps, spectra, resolvents | "What are the eigenvalues?" |
| **Geometric (GE)** | Curvature, holonomy, connections, topology | "What is the curvature?" |
| **Algebraic (AL)** | Symmetries, groups, representations, clones | "What is the group?" |
| **Information (IN)** | Entropy, capacity, compression, distinguishability | "What is the entropy?" |

**Tier 2 domain activation (based on target content):**

| Target content | Activate | R-Theorems |
|---------------|----------|------------|
| Operator algebras, C*-algebras, von Neumann | OA | R.OA-1 (Stone-vN) through R.OA-6 (cyclic cohomology index) |
| Quantum mechanics, Hilbert spaces | QM | R.QM-1 (Heisenberg) through R.QM-4 (Wigner-Eckart) |
| QFT, gauge theory, renormalization | QFT | R.QFT-1 (Atiyah-Singer) through R.QFT-9 (crossing) |
| General relativity, black holes | GR | R.GR-1 (Einstein) through R.GR-5 (cosmic no-hair) |
| Cosmology, CMB, inflation | Cos | R.Cos-1 (Sachs-Wolfe) through R.Cos-4 (CMB spectrum) |
| Number theory, L-functions, Galois | NT | Hecke eigenvalues, Galois orbits, explicit formulas |
| Symmetries, Noether, CPT | Sym | R.Sym-1 (Noether->Hecke) + R.Sym-2 (CPT/spin-statistics) |

For each LB concept C, build:

```
corr[M]{concept,SP,GE,AL,IN,[tier2]}:
  [C],[spectral-image],[geometric-image],[algebraic-image],[info-image],[...]
```

Empty cells = research targets. Each filled cell is a new degree of freedom. Use the framework's existing correspondences as templates:

| Concept | Spectral | Geometric | Algebraic | Information |
|---------|----------|-----------|-----------|-------------|
| Riemann zeros | Eigenvalues gamma_n of T_BC | Curvature of e-circle / CP^2 moduli | Hecke action mu_n on A_BC | Channel capacity of KMS_1 |
| Mass gap | Gap Delta > 0 of transfer matrix | Weitzenboeck-Bochner on KK | Balaban polymer convergence | Wilson coefficient -> AF |
| P vs NP | TGap (modular flow gap) | Holonomy defect on constraint graphs | Polymorphism clone (Taylor) | dim_poly_k growth/collapse |
| BSD | Zeros of L(E,s) | CM curve geometry | Hecke L-twist (psi char) | Rank = vanishing order |

### Step 3: Apply the Six Patterns

For each load-bearing step, test all six:

| Pattern | Question | If YES |
|---------|----------|--------|
| **P1: Geometric Reinterpretation** | "Shadow of simpler fact in larger space?" | Name the space. Difficulty dissolves. |
| **P2: Holonomy** | "Phase wrapping compact structure that locks result?" | Identify the holonomy. Quantized value protects. |
| **P3: Scale-Setting** | "Energy computation that determines this scale?" | Compute it. Scale is determined, not free. |
| **P4: Topological Rigidity** | "Discrete invariant protecting from deformation?" | Identify the invariant. Result is rigid. |
| **P5: Zeta Regularization** | "Divergent sum that continuation makes finite?" | Apply zeta/Mellin. Finite value IS the answer. |
| **P6: Projection Diagnosis** | "Paradox artifact of projecting away structure?" | Identify what projected out. Restore it. |

Output per LB step:

```
pat[LB_count]{step,P1,P2,P3,P4,P5,P6,highest_leverage}:
  [N],YES/NO/MAYBE,[...],P_
```

**Mode-specific use:**
- VERIFY: patterns identify WHERE the proof might break (P4-protected = robust; lacking P4 = vulnerable)
- EXCISE: patterns suggest ALTERNATIVE proofs (same result, different pattern)
- CONSTRUCT: patterns guide REROUTING (P1: go up a dimension; P6: restore projected structure)

### Step 4: Apply the predictive grammar

For each formula or numerical claim in the proof chain, tag the grammar rule:

| Rule | Operator order | Shape | Normalization |
|------|---------------|-------|---------------|
| 1 SUM | Linear (1st order) | a + b | 1 |
| 2 PRODUCT | Quadratic (2nd order) | a * b / c | c in {pi, 2pi, pi^2} |
| 3 YUKAWA | Bilinear coupling | a * b / (2pi) [quarks] or a * b [leptons] | S^1 for color-charged |
| 4 EXPONENTIAL | Eigenvalue of scaling | exp(a * pi^2/2) | -- |
| 5 LOG | Logarithmic/thermal | log(a) or (log a)^2 | -- |
| 6 FRACTIONAL | DoF extraction | a^{1/k}, k = rep dim | -- |
| 7 RATIO | Relative scale | a / b | 1 |
| 8 DIFFERENCE | Spectral gap | a - b | 1 |

Output:

```
gram[F]{formula,rule,shape_match,deviation}:
  [formula],R[1-8]|NEW,[yes/partial/no],[finding-if-any]
```

Deviations from grammar = either (a) new rule discovery or (b) error. Three-category generation template constrains assignments: 3rd-gen = PRODUCT, 2nd-gen = RATIO, 1st-gen = DIFFERENCE.

### Step 5: Build the operations equivalence table

For each mathematical operation used in the proof chain, fill all active domains:

```
ops[K]{operation,SP,GE,AL,IN,[tier2_if_active]}:
  inner_product,Tr(A*B),Int-omega-wedge-*omega,Hom(A;B),I(X;Y)
  tensor_product,H_1-tensor-H_2,M_1-x-M_2,A-tensor-B,P(X;Y)
  quotient,Spectral-restriction,Orbifold-M/G,Ideal-A/I,H(X|Y)
  gap,Delta=inf-spec\{0},Injectivity-radius,Kazhdan-constant,C-R
  ...
```

Empty cells = translation targets for excision. The table tells agents: "stuck computing a commutator spectrally? Try curvature geometrically."

### Step 6: Map the framework interface

For each LB step, identify which framework chain steps depend on it, the impact if it breaks, and alternative routes:

```
interface[LB_count]{step,chain_dep,impact,alt_routes}:
  [N],[chain.step],[description],[list]
```

### Step 7: Import kills

Import kills from ALL prior ORA runs touching this domain. Search:

- `paper08-yang-mills/closing-H4/blackboard.md` section F (YM kills)
- `paper13-rh/preprint/sections-11-14.md` (RH honest negatives)
- `paper26-bsd/closing-my4/blackboard.md` section F (BSD kills)
- `paper28-pvnp/strategy/07-toolkit-complete.md` + `10-amplification-entries.md` (PvNP kills)

**NEVER reduce the kill list. Monotonic growth only.**

### Step 8: Pre-identify escalation routes

For each LB step, brainstorm:

**Tier B (excision) candidates:**
- Alternative proofs in the literature?
- Independent derivation routes via Six Patterns from a different angle?
- Transposition dictionary pathways (prove on additive side, transport via Mellin)?
- Any of the 37 R-Theorems provide an alternative path?

**Tier C (construction) candidates:**
- P1: larger system where the result is a consequence?
- P6: restore projected-out structure to bypass difficulty?
- Alternative proof chains reaching same conclusion?
- Tier 3 structural domains (category theory, homological, combinatorial, topological, dynamical, quantum-information)?
- Tier 4 frontier domains (thermodynamic, probabilistic, explicit CFT, arithmetic topology, Langlands-dual, persistent homology, quantum error correction, optimal transport, microlocal analysis, coding theory, arithmetic geometry, differential topology)?

### Step 9: Compile the capacitor

Assemble everything into the output format. Apply compilation rules:

1. **DEDUPLICATE** -- same concept from multiple sources -> write ONCE with canonical ID
2. **COMPRESS** -- strip motivation/history/narrative -> keep definitions/formulas/statuses only
3. **FORMAT** -- TOON for arrays, adjacency-list for graphs, single-line for patterns/rules
4. **ABBREVIATE** -- use LEGEND. Every phrase appearing 3+ times gets an abbreviation
5. **ORDER** -- legend -> kills -> chain -> deps -> domains -> corr -> patterns -> grammar -> ops -> index. Static first, dynamic last.
6. **PRESERVE** -- every kill, formula, status, dependency, re-entry gate. Zero information loss.

### Step 10: Validate the capacitor

Dispatch ONE Critic on ONE load-bearing step using ONLY the compiled capacitor. The Critic should:

1. Read the step from CHAIN
2. Read the correspondence table entry from CORR
3. Read the pattern analysis from PATTERNS
4. Check the grammar tag from GRAMMAR
5. Use the operations table from OPS to attempt a domain translation
6. Produce a SURVIVED / WEAKENED / BROKEN verdict

If the Critic produces a meaningful verdict: capacitor is charged. Ship it.

If the Critic cannot produce a verdict: identify what is missing (empty correspondence cell -> back to Step 2; no pattern applies -> note as "NO PATTERN -- candidate for 7th pattern"; missing background tool -> add five-field card; step unclear -> re-read target more carefully). Iterate until pilot succeeds. Then ship.

---

# Part III -- How the Capacitor is LOADED (token optimization)

## The Compression Pipeline

| Stage | Lines | Reduction |
|-------|-------|-----------|
| Raw source files (30 files) | 14,230 | -- |
| After compile-by-execution | ~1,000 | 93% |
| With prompt caching on prefix | ~1,000 (shared at 10% cost) | 93% loading + 90% cost |

**Source file inventory (what gets compiled):**

Seven Keystone Files (3,345 lines):

| # | File | Lines | Section |
|---|------|-------|---------|
| 1 | paper12/research/214-the-method-six-patterns.md | 339 | A |
| 2 | paper12/research/213-theorem-catalogue-grammar.md | 297 | C |
| 3 | paper12/research/14-transposition-CCM-and-reasoning-patterns.md | 755 | D |
| 4 | paper11/29-the-standard-model-riemann-correspondence.md | 558 | G |
| 5 | paper12/27-anchor-document.md | 426 | E |
| 6 | paper12/research/09-pattern-of-zero-indices.md | 415 | G |
| 7 | paper12/research/10-transposition-gauge-group-3primes.md | 555 | G |

Framework Proof Chains (1,083 lines), Theorem Catalogues (3,300 lines), Reference Dictionaries (874 lines), Kill List Sources (2,530 lines), ORA Bundle + Strategy (2,654 lines).

**Dependency lattice:** The keystones form a lattice, not a tree -- circular references are expected:

```
214 (Six Patterns) <--> 213 (Grammar) <--> 14 (Transposition)
     ^                       ^                    ^
     +--- 27 (Anchor) ------+------ 09 (Zeros) --+
              ^                          ^
              +---- 10 (Three-primes) ---+
                         ^
                    11/29 (SM-Riemann)
```

Compile-by-execution resolves this naturally: everything is in context.

## Format Efficiency Research

Measured across tokenizers (ImprovingAgents 2025):

| Format | Tokens (same data) | vs Markdown |
|--------|-------------------|-------------|
| Markdown-Table | baseline | -- |
| YAML | +11% | worse |
| JSON | +51% | much worse |
| XML | +79% | terrible |

**TOON** (Token-Oriented Object Notation) saves 30-60% vs JSON for uniform arrays:

```
proofchain[18]{id,type,statement,deps,status}:
  1,Def,KK-reduction,-,VERIFIED
  2,Def,Dilaton-coupling,1,VERIFIED
  3*,Lem,Gauge-unification,1|2,PENDING
```

**Adjacency-list** for dependency graphs (3-5x cheaper than table format):

```
deps: 1->2*,3; 2*->4,5*; 3->5*; 5*->6
```

**N-gram abbreviation** (CompactPrompt, ICAIF 2025 -- 2.35x compression, accuracy improved on Claude):

```
LEGEND:
CCM:=Connes-Consani-Marcolli | BC:=Bost-Connes | KR:=Kato-Rellich
SP:=spectral | GE:=geometric | AL:=algebraic | IN:=information-theoretic
```

## Prompt Caching

Shared prefix cached across all agents (Anthropic prompt caching, available today):

- First agent request populates the cache (~5 min TTL)
- Subsequent agents hit the cache: 0.1x base input price (90% cost savings), 5-10x TTFT reduction
- Only per-agent unique content (step assignment, prior work on node) is fresh input
- Minimum 1,024 tokens for caching to activate

**Cache-optimized ordering:**

```
[CACHED PREFIX -- stable across all agents, all waves, all tiers]
  1. Abbreviation legend
  2. Kill list (full, NEVER reduced)
  3. Proof chain (steps + deps + statuses)
  4. Domain map + correspondence tables
  5. Patterns + grammar + operations (reference tools)
  6. Section INDEX (@FETCH pointers)

[FRESH SUFFIX -- per-agent, changes every dispatch]
  7. Step assignment + prior work on node
  8. Feed subscriptions (from message bus)
  9. Layer-specific content + delta overlay
```

**Application to the capacitor:**

```
CACHED PREFIX (shared by all agents):
  - Voice canon
  - Kill list (full)
  - Proof chain (full H.1)
  - Six Patterns method (A)
  - Predictive grammar (C)
  - Operations equivalence table (H.5)
  - Correspondence tables for active domains (H.2)
  -> ~4,000-5,000 tokens cached, paid once

PER-AGENT SUFFIX (unique):
  - Step assignment
  - Prior work on this specific node
  - Layer-specific fetch results
  -> ~500-1,500 tokens per agent, paid each time
```

**Stagger agent launches ~1s** for cache population. For 60 agents: ~60s stagger vs fully simultaneous dispatch.

---

# Part IV -- How the Capacitor is DISPATCHED (runtime strategies)

## The Core Tension

Three consecutive ORA failures (I-v6-3, I-v6-4, I-v6-5) proved that runner-side classification of what an agent needs fails predictably. Root cause: runners misclassify node types, agents miss critical tools, verification quality collapses. Fix: "pass everything, let the agent self-select."

This is correct for quality. It is brutal for tokens.

**The resolution: defer, don't hide.** Every section remains addressable and fetchable. Only the active working set is pre-loaded.

## Strategy A: Capacitor-as-Index + On-Demand Fetch

**Principle:** The capacitor becomes a ~1,500-line index. Full sections are fetched on demand. Nothing hidden, everything deferred.

**Current flow:**
```
Agent spawns -> loads full 8,000-line capacitor -> self-selects what to use -> works
```

**Proposed flow:**
```
Agent spawns -> loads 1,500-line index capacitor -> works with core context
  -> needs H.5 (operations table)? -> requests it -> runner injects inline
  -> needs I.1 (RH chain)? -> requests it -> runner injects inline
  -> never needs H.4 (grammar)? -> never loaded, tokens saved
```

**The core index (~1,500 lines) contains:**

| Section | Content | Lines |
|---------|---------|-------|
| META | Capacitor state, charge level, version | ~30 |
| PROOF-CHAIN | H.1 -- full numbered steps with dependencies and status | ~200-500 |
| KILL-LIST | Full kill list (NEVER reduced -- I-v6-5 safety) | ~100-500 |
| BOTTLENECK | Current bottleneck description + engaged nodes | ~50 |
| VOICE | Voice canon (runner identity) | ~50 |
| DOMAIN-MAP | Active domains, activated Tier 2 families | ~30 |
| INDEX | Section-by-section pointer table with 1-line descriptions | ~100 |

**Fetchable sections (on-demand via @FETCH pointers):**

| Section | Trigger for fetch |
|---------|-------------------|
| A. Six Patterns method | Agent applies pattern analysis |
| B. Theorem catalogues | Agent cites framework theorem |
| C. Predictive grammar | Agent checks formula shape |
| D. Transposition mechanics | Agent transposes between additive/multiplicative |
| E. Anchor + dictionaries | Agent needs operator definitions |
| F. Prediction table | Agent checks against experiment |
| G. Other reference files | Agent needs bridge theorems, Laurent sweeps |
| H.2 Correspondence tables | Agent transposes between domains |
| H.3 Six Patterns analysis | Agent works on specific LB step |
| H.4 Grammar analysis | Agent verifies formula |
| H.5 Operations equivalence | Agent translates operation across domains |
| H.6-H.8 Interface/kills/escalation | Agent plans escalation route |
| H.9-H.12 Toolkit/amplification/corrections | Agent needs background tools or history |
| I. Framework proof chains | Agent checks cross-chain dependencies |

**Estimated savings: 40-50% token reduction per agent.**

## Strategy B: Effort-Tiered Dispatch

**Principle:** Different agent roles get different starting context layers. All can escalate to full context.

```
Layer 1 -- MINIMAL (~1,500 lines)
  Core index capacitor (Strategy A).
  For: Non-bottleneck Verifiers doing structural checks.

Layer 2 -- STANDARD (~3,000 lines)
  Core + active domain correspondence tables (H.2 filtered to active domains)
  + Six Patterns analysis for the assigned step (H.3 subset)
  + relevant toolkit rows (H.10 filtered by engages-bottleneck)
  For: Standard Authors and Critics.

Layer 3 -- FULL (~6,000+ lines)
  Everything pre-loaded. No fetch latency.
  For: Bottleneck node Authors, Synthesis agents, Tier C Construction agents.
```

**Dispatch rules:**

| Role | Tier | Starting Layer | Can escalate to |
|------|------|----------------|-----------------|
| Verifier (non-bottleneck) | A | Layer 1 | Layer 2 |
| Verifier (bottleneck) | A | Layer 2 | Layer 3 |
| Re-deriver | A | Layer 2 | Layer 3 |
| Author (standard) | B | Layer 2 | Layer 3 |
| Author (bottleneck) | B/C | Layer 3 | -- |
| Critic | A/B | Layer 2 | Layer 3 |
| Synthesis | all | Layer 3 | -- |
| Construction | C | Layer 3 + Tier 3/4 | Expanded |

**Estimated savings: 30-40% token reduction across a full wave.**

## Strategy C: Delta-Only Wave Updates

**Principle:** Between waves, don't reload the full capacitor. Send only what changed.

**Current flow:**
```
Wave 1 completes -> capacitor v1.1 rebuilt (SELF-ADJUST/TRIM/AMPLIFY)
  -> Wave 2 agents load full capacitor v1.1 (~8,000 lines)
```

**Proposed flow:**
```
Wave 1 completes -> delta computed:

DELTA v1.0 -> v1.1:
  + K-12: [new kill entry]
  ~ Step 7: PENDING -> SURVIVED
  ~ Step 14: PENDING -> WEAKENED (downgraded, reason: ...)
  + H.2: New correspondence cell filled (geometric image of concept X)
  + H.11: Amplification entry (method M transferred from step 3 to step 9)

  -> Wave 2 agents load: core index + delta overlay
  -> Full sections fetched on demand (Strategy A) are v1.1 versions
```

**Delta format:**

```markdown
## DELTA -- v1.0 -> v1.1

### New kills
kills_delta[K]{id,what,why,pattern,reentry}

### Status changes
status_delta[S]{step,old,new,evidence}

### New correspondence cells
corr_delta[C]{concept,domain,new_image,source}

### Amplification entries
amp_delta[A]{method,from_step,to_step,result}

### Corrections
fix_delta[F]{card,old_claim,corrected,reason}
```

**I-v6-5 safety:** Kill list deltas are ADDITIVE (new kills added, never removed). Status changes are explicit (agent sees what moved and why). Full capacitor still fetchable on demand.

**Estimated savings: 20-30% on multi-wave runs (compounding with A and B).**

## Composed Architecture

All three strategies compose:

```
DISPATCH:
  1. Determine agent role and node bottleneck status -> select Layer (Strategy B)
  2. Build context package:
     - Layer 1/2/3 core content (pre-loaded)
     - Section INDEX with fetch pointers (Strategy A)
     - If wave > 1: delta overlay instead of full reload (Strategy C)
  3. Agent works with core context
  4. Agent requests additional sections as needed -> runner injects inline
  5. Agent returns structured verdict

WAVE-CLOSE:
  6. Compute delta (new kills, status changes, new cells, amplifications)
  7. Update capacitor version
  8. Next wave agents get: core + delta overlay + fetch pointers

TIER ESCALATION:
  9. Tier B agents get Layer 2 minimum + excision brief
  10. Tier C agents get Layer 3 + expanded Tier 3/4 domains
  11. Escalation EXPANDS context, never contracts it
```

---

# Part V -- How Agents COMMUNICATE (message bus)

## The Three-Layer Architecture

```
+-----------------------------------------------------------------+
|  LAYER 3: CAPACITOR (Long-Term Memory)                          |
|  - Static compiled knowledge (patterns, grammar, dicts)         |
|  - Versioned, updated at run boundaries                         |
|  - Strategy A: index + on-demand fetch                          |
|  - Strategy B: effort-tiered dispatch                           |
|  - Strategy C: delta-only wave updates                          |
|  - "What does the programme know?"                              |
+-----------------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------------+
|  LAYER 2: BLACKBOARD (Session Memory)                           |
|  - Sections A-O: live state for this run                        |
|  - Updated at cycle-close (batch)                               |
|  - "What has this run discovered?"                              |
+-----------------------------------------------------------------+
                              |
                              v
+-----------------------------------------------------------------+
|  LAYER 1: MESSAGE BUS (Live Communication)          *** NEW *** |
|                                                                 |
|  FEEDS (append-only, subscribable):                             |
|  +-- kill-stream       kills as they're written                 |
|  +-- card-stream       five-field cards as they're verified     |
|  +-- status-stream     proof step status changes                |
|  +-- escalation-stream Tier A->B->C handoff messages            |
|  +-- amplification-stream cross-tier method transfer            |
|                                                                 |
|  QUERIES (request/response, agent-to-agent via runner):         |
|  +-- assumption-query  "Did upstream step verify X?"            |
|  +-- toolkit-query     "Which H.10 rows did you cite?"          |
|  +-- debug-trace       "Show me your BLOCKED_TRACE"             |
|  +-- reconciliation    "Respond to Agent A's finding"           |
|  +-- confidence-query  "What would raise your conf to 0.90+?"   |
|                                                                 |
|  "What is happening RIGHT NOW?"                                 |
|                                                                 |
|  At cycle-close: feeds merge into blackboard (audit trail)      |
|  At run-close: blackboard merges into capacitor (long-term)     |
+-----------------------------------------------------------------+
```

**Temporal distinction:**
- Layer 3 (Capacitor): months of accumulated knowledge across all runs
- Layer 2 (Blackboard): hours of discovery within this run
- Layer 1 (Message Bus): seconds of live coordination between active agents

## Five Append-Only Feeds

1. **kill-stream** -- kills as they're written (never batched). Agents SUBSCRIBE by domain. Prevents parallel agents from re-exploring each other's dead ends within the same wave.

2. **card-stream** -- five-field cards as they're verified. Wave 2 agents that spawn before wave 1 completes get live data instead of stale snapshots.

3. **status-stream** -- proof step status changes (PENDING -> SURVIVED, PENDING -> WEAKENED, etc.). Downstream verifiers see upstream results in real time.

4. **escalation-stream** -- Tier A->B->C handoff messages. Structured messages carry: step ID, status, gap description, relevant kills, correspondence rows, pattern priorities, pre-identified routes.

5. **amplification-stream** -- cross-tier method transfer. When a method succeeds on step X, it streams to agents working on structurally similar steps.

Agents SUBSCRIBE by domain/type/status. Feeds merge into blackboard at cycle-close.

## Five Query Types

Agent-to-agent queries, routed by the runner:

1. **assumption-query** -- "Did upstream step verify assumption X?" Enables cross-step consistency checking in real time instead of post-hoc at Synthesis.

2. **toolkit-query** -- "Which H.10 rows did you cite?" Returns structured metadata (name, precision, status) instead of narrative. Makes MAR confirmation-bias checks deterministic.

3. **debug-trace** -- "Show me your BLOCKED_TRACE." Returns structured failure data: step_reached, attempts, failure_reason, diagnostic_confidence, re_entry_requires. Improves kill classification accuracy.

4. **reconciliation** -- "Respond to Agent A's finding in one sentence." Two 1-sentence replies replace a Judge reading two full work products.

5. **confidence-query** -- "What additional evidence would raise your confidence to 0.90+? What is the most likely scenario where you are wrong?" Targeted response enables focused follow-up instead of full re-verification.

## Protocol: AEE Envelope (14-field JSON)

```json
{
  "from": "verifier-4.2",
  "to": "verifier-7.1",
  "corr": "wave-1-ccm",
  "reply_to": null,
  "priority": "high",
  "payload": {
    "step": "4.2",
    "status": "WEAKENED",
    "gap": "CF boundedness"
  }
}
```

Key fields: `from`, `to`, `corr` (correlation ID for workflow chains), `reply_to` (references originating message for causality tracing), `priority` (low/normal/high/urgent), `payload` (structured content). The `corr` + `reply_to` chain makes full causality traceable across relay chains.

*Source: IETF draft-cowles-aee-00.*

## Claude API-Native Architecture

**Constraint (April 2026):** All latent-space techniques (LatentMAS, KVCOMM, C2C, Interlat) require KV-cache access unavailable through the Claude API. Self-hosted inference clusters impractical at current hardware price/performance. The architecture is Claude API-only. All optimizations are at the orchestration level.

```
+---------------------------------------------------+
|  CLAUDE OPUS (Supervisor / Synthesis)              |
|  - Orchestration, final judgment, escalation       |
|  - Prompt caching: shared capacitor as prefix      |
|  - Message bus: reads feeds, dispatches queries    |
+-----------------------+---------------------------+
                        | Structured contracts (AEE envelope)
                        v
+---------------------------------------------------+
|  DISPATCH LAYER (orchestration logic)              |
|  - Strategy A: index capacitor + on-demand fetch   |
|  - Strategy B: effort-tiered (Layer 1/2/3)         |
|  - Strategy C: delta-only wave updates             |
|  - Prompt caching: shared prefix across agents     |
|  - Message bus: feeds + query routing              |
+-----------------------+---------------------------+
                        |
                        v
+---------------------------------------------------+
|  CLAUDE API WORKERS (all agents)                   |
|                                                    |
|  CACHED PREFIX (shared, paid once):                |
|  +-- Voice canon                                   |
|  +-- Kill list (full, NEVER reduced)               |
|  +-- Proof chain H.1 (full structure)              |
|  +-- Domain map (active domains)                   |
|  +-- Section INDEX (pointers to fetchable parts)   |
|  -> ~4,000-5,000 tokens, 90% cost reduction        |
|                                                    |
|  PER-AGENT SUFFIX (unique, paid each time):        |
|  +-- Step assignment + prior work on node          |
|  +-- Feed subscriptions (relevant kills, cards)    |
|  +-- Layer-specific pre-loaded sections            |
|  +-- Fetched sections (on-demand during work)      |
|  -> ~500-3,000 tokens depending on Layer 1/2/3     |
|                                                    |
|  LIVE MESSAGING (during agent execution):          |
|  +-- POST to feeds (kills, cards, statuses)        |
|  +-- SUBSCRIBE to feeds (domain-filtered)          |
|  +-- QUERY/RESPONSE (agent-to-agent via router)    |
+---------------------------------------------------+
```

---

# Part VI -- The 13 Communication Opportunities

## Category 1: Step-to-Step Verification Handoffs

**Opportunity 1.1 -- Cross-Step Assumption Verification**

*Current:* All 30 Verifiers receive full capacitor. Synthesis cross-checks assumptions post-hoc. If Step 5's Verifier flags assumption A as "verified locally" but Step 23's Verifier discovers A is problematic, the gap is not caught until Synthesis -- wasting a full wave.

*Proposed:* When Step 5's Verifier completes, it POSTs verified assumptions to a step-dependency registry. Step 23's Verifier QUERIEs the registry before drafting its own verification.

*Savings:* Eliminates 1 full re-checking wave. Saves ~6-12 agents on a 30-step proof.

**Opportunity 1.2 -- Re-deriver <-> Verifier Bidirectional Loop**

*Current:* Verifier and Re-deriver spawned in parallel, return independently. If they disagree (SURVIVED vs FAILED), a Judge is spawned to reconcile -- re-reading both outputs from scratch.

*Proposed:* Re-deriver posts structured failure trace. Verifier asks: "Does the author's method address your blocker?" Re-deriver responds. Three-turn exchange produces LOCK without Judge overhead.

*Savings:* Eliminates Judge spawn for ~40% of SURVIVED/FAILED divergences.

## Category 2: Tier-to-Tier Escalation Messaging

**Opportunity 2.1 -- Tier A -> Tier B Structured Escalation**

*Current:* When Tier A finds WEAKENED on step N, Tier B receives the entire capacitor -- 80% of which is about OTHER steps.

*Proposed:* Tier A posts a structured escalation message:
```
ESCALATION: Step 4.2 -> Tier B
STATUS: WEAKENED
GAP: [specific gap description]
KILL_LIST_RELEVANT: [K-1, K-5, K-7]
CORRESPONDENCE_ROWS: [Spectral, Algebraic only]
SIX_PATTERNS_PRIORITY: [P4, P1 most promising]
ESCALATION_ROUTES: [3 pre-identified from H.8]
```
Tier B Author receives ~30% of the context, can QUERY for more if needed.

*Savings:* 50-70% context reduction per escalation.

**Opportunity 2.2 -- Tier B -> Tier C Live Kill Amplification** *(CRITICAL)*

*Current:* Tier B's kill list is appended at cycle-close. If Tier C is spawned during Tier B's wave, it does not see the kills.

*Proposed:* Kills stream to a live registry as they are written. Tier C Authors QUERY by pattern: "Show me kills from spectral domain that blocked self-adjointness proofs."

*Savings:* Tier C avoids ~30-40% of Tier B's dead ends. Saves 1-3 construction attempts.

## Category 3: Agent Internal-State Queries

**Opportunity 3.1 -- Verifier -> Author Toolkit Query**

*Current:* Synthesis must re-read Authors' narrative outputs to extract toolkit citations for MAR confirmation bias checks. Unreliable extraction.

*Proposed:* Authors respond to structured queries: "Which toolkit rows from H.10 did you cite? List by NAME, precision, status." Synthesis gets metadata, not narrative. MAR check becomes deterministic.

*Savings:* Eliminates 15-25% of Judge spawns for MAR checks.

**Opportunity 3.2 -- Critic -> Author Debug Trace**

*Current:* Author returns BLOCKED with terse narrative. Critic must guess: is the blockage topological (GENUINE) or computational (CLOSABLE)?

*Proposed:* Author provides structured BLOCKED_TRACE with step_reached, attempts, failure_reason, diagnostic_confidence, re_entry_requires. Critic can QUERY for clarification.

*Savings:* Kill classification accuracy improves 20-30%. Fewer Tier C false starts.

## Category 4: Dynamic Capacitor Updates (Live Relay)

**Opportunity 4.1 -- Wave-to-Wave Card Streaming** *(CRITICAL)*

*Current:* Five-field cards are batched at cycle-close. If wave 2 spawns before wave 1 completes, wave 2 agents get stale data.

*Proposed:* Cards stream to a live feed as they are generated. Wave 2 agents SUBSCRIBE by domain/type/status.

*Savings:* Eliminates cascading wave mismatches. Saves 1-2 full wave re-does on 3+ wave runs.

**Opportunity 4.2 -- Kill List Append-Only Feed**

*Current:* Kills batched at cycle-close. Parallel agents in the same wave cannot see each other's kills.

*Proposed:* Kill list is an append-only log stream. Authors SUBSCRIBE to kills matching their domain.

*Savings:* Kill deduplication + 1-2 variant re-attempts avoided per wave.

**Opportunity 4.3 -- Cross-Tier Amplification Relay** *(CRITICAL)*

*Current:* Tier 4 methodology validated post-run. Tier 1 reads merged capacitor days later.

*Proposed:* Amplification entries stream LIVE between tiers. Tier 1 agents spawned WITH Tier 4 methods.

*Savings:* 10-15% methodology reuse gain across sequential tiers.

## Category 5: Synthesis and Meta-Cognition Queries

**Opportunity 5.1 -- Synthesis -> Author Reconciliation Query**

*Current:* Two Authors disagree -> Judge spawned -> re-reads both outputs from scratch.

*Proposed:* Synthesis queries both Authors: "Respond to each other's finding in one sentence." Two 1-sentence replies replace Judge reading two full work products.

*Savings:* Eliminates 40-60% of Judge spawns for reconciliation.

**Opportunity 5.2 -- Critic -> Critic Confidence Query**

*Current:* Critic downgrades with medium confidence -> Meta-critic spawned to re-verify from scratch.

*Proposed:* Synthesis queries Critic: "What additional evidence would raise your confidence to 0.90+? What is the most likely scenario where you are wrong?" Targeted response enables focused follow-up instead of full re-verification.

*Savings:* 30-50% of Meta-critic spawns become targeted queries.

## Summary Table: All 13 Opportunities by Priority

| Priority | Opportunity | Category | Current Cost | Proposed Savings |
|----------|------------|----------|--------------|-----------------|
| **CRITICAL** | 4.1 Card streaming | Live relay | Wave mismatches, full re-does | 1-2 waves saved |
| **CRITICAL** | 2.2 Tier B->C kill amplification | Escalation | 2-10 wasted construction cycles | 1-3 attempts avoided |
| **CRITICAL** | 4.3 Cross-tier amplification | Live relay | Post-hoc only benefit | Live methodology reuse |
| **HIGH** | 2.1 Tier A->B escalation stream | Escalation | Full capacitor reload | 50-70% context reduction |
| **HIGH** | 1.1 Cross-step assumption query | Verification | 1 full re-checking wave | 6-12 agents saved |
| **HIGH** | 4.2 Kill list live feed | Live relay | Duplicate kills, re-attempts | 1-2 variants avoided/wave |
| **MEDIUM** | 5.1 Author reconciliation query | Synthesis | Judge spawn | 40-60% fewer Judges |
| **MEDIUM** | 1.2 Verifier <-> Re-deriver loop | Verification | Judge spawn | 40% fewer Judges |
| **MEDIUM** | 3.1 Toolkit query | Internal-state | Judge spawn for MAR | 15-25% fewer MAR Judges |
| **MEDIUM** | 3.2 Debug trace query | Internal-state | Uncertain kills | +20-30% kill accuracy |
| **MEDIUM** | 5.2 Confidence query | Synthesis | Meta-critic spawn | 30-50% fewer Meta-critics |

## Message Flow Example: CCM Step 4.2 WEAKENED

All three layers in action:

```
1. Wave 1: 30 Verifiers dispatched (Layer 1 context + subscriptions)

2. Verifier-4.2 completes:
   -> POSTS to status-stream: {step: 4.2, status: WEAKENED, gap: "CF boundedness"}
   -> POSTS to kill-stream: {K-new: "CF extension requires bounded perturbation"}
   -> POSTS to card-stream: {CCM-4.2: five-field card with WEAKENED status}

3. Verifier-7.1 (still running, depends on 4.2):
   -> RECEIVES status-stream update: "4.2 is WEAKENED"
   -> Adjusts own verification: "My step assumes 4.2. Flagging conditional."

4. Synthesis (at wave-close):
   -> Reads all feed entries (not individual agent outputs)
   -> Identifies: "4.2 WEAKENED, 7.1 conditional on 4.2, escalation needed"

5. Escalation:
   -> POSTS to escalation-stream: structured message for Tier B
   -> Tier B Author spawns with: escalation message + kill-stream entries
     for domain "self-adjointness" + index capacitor
   -> Does NOT load full capacitor -- fetches sections on demand

6. Tier B Author (mid-excision):
   -> QUERIES Verifier-4.2: "Is the boundedness failure absolute or N-dependent?"
   -> Verifier-4.2 REPLIES: "N-dependent. For N < 100, bounded. For N -> inf, unbounded."
   -> Tier B adjusts: attempts excision for large-N regime only

7. Tier B fails -> Tier C triggered:
   -> Tier C Author SUBSCRIBES to kill-stream (domain: self-adjointness)
   -> Receives: Tier A kills + Tier B kills, live
   -> Avoids all dead ends immediately
```

---

# Part VII -- Safety Invariants (NEVER violate)

These six invariants were established by three consecutive ORA failures (I-v6-3, I-v6-4, I-v6-5) where runner-side classification of agent needs caused verification quality collapse.

```
safety[6]{invariant,reason}:
  Kill-list-completeness,Every-kill-in-every-agents-core-context(I-v6-5)
  Proof-chain-visibility,Full-dependency-map-always-in-core
  Agent-self-selection,Runner-never-decides-what-agent-needs(agent-requests;runner-provides)
  Bottleneck-engagement,LB-nodes-always-get-full-context(Layer-2-minimum)
  Escalation-expands,Tier-A->B->C-always-adds-context(never-removes)
  Voice-canon-integrity,Runner-identity-and-signature-consistency-always-in-core
```

**Expanded:**

1. **Kill list completeness** -- every kill in every agent's core context. Never deferred, never filtered, never compressed. The kill list is the immune system. Filtering it is immunosuppression.

2. **Proof chain visibility** -- full dependency map always in core. Status of every step visible. An agent that cannot see the chain cannot verify against it.

3. **Agent self-selection** -- runner never decides what an agent needs. Agent requests, runner provides. The I-v6-5 lesson: runners misclassify node types predictably.

4. **Bottleneck engagement** -- nodes marked LB always get Layer 2 minimum. No risk of missing tools on the steps that matter most.

5. **Escalation expands** -- moving from Tier A -> B -> C always adds context, never removes it. Tier C agents get everything Tier A and B agents had, plus more.

6. **Voice canon integrity** -- runner identity and signature consistency checks always in core. The voice is the constant across all agents.

**I-v6-5 safety checks (per strategy):**

| Strategy | Kill list | Chain | Self-selection | Bottleneck | Escalation | Voice |
|----------|-----------|-------|----------------|------------|------------|-------|
| A (index + fetch) | ALWAYS in core | ALWAYS in core | Agent fetches, runner provides | Layer 2 min | Expands only | In core |
| B (effort tiers) | Every layer | Every layer | Agent-initiated escalation | Layer 2/3 | Adds layers | Every layer |
| C (delta waves) | Additive only | Status explicit | Agent sees all changes | Preserved | Preserved | Preserved |
| Message bus | Live-streamed | Status-streamed | Agent subscribes | Auto-routed | Kills amplified | In core |

---

# Part VIII -- Regression Metrics

Track after deployment to detect quality degradation:

| Metric | Baseline | Alert threshold |
|--------|----------|-----------------|
| Re-exploration rate (killed approaches re-proposed) | 0% | > 2% |
| Cross-step inconsistency (synthesis catches) | TBD | > 10% increase |
| Excision success rate (Tier B) | TBD | > 15% decrease |
| Construction diversity (Tier C domain spread) | TBD | > 20% decrease |
| Fetch request rate (sections demanded on-demand) | N/A | Monitor patterns |
| Mean agent context size (tokens) | ~80K tokens | Target: < 40K |

**Interpretation guidelines:**

- **Re-exploration rate > 2%** means kill list is not reaching agents effectively. Check: is the kill list in core? Are live kill-stream subscriptions working?
- **Cross-step inconsistency increase** means assumption-query (Opportunity 1.1) is not propagating. Check: is the status-stream reaching dependent verifiers?
- **Excision success decrease** means escalation messages are losing critical context. Check: are structured escalation messages (Opportunity 2.1) carrying enough detail?
- **Construction diversity decrease** means amplification-stream (Opportunity 4.3) is creating convergence instead of exploration. Check: is the amplification log biasing toward a single approach?
- **Fetch request patterns** reveal which sections agents actually need. High fetch rate on a section = consider moving it to Layer 2 default. Zero fetch rate = consider removing from compiled capacitor.

---

# Part IX -- Combined Savings Estimate

## Component-Level Savings

| Component | Token Savings | Agent Savings | Cost Savings |
|-----------|--------------|---------------|-------------|
| Compile-by-execution | 93% on loading | -- | 93% loading |
| Strategy A (index + fetch) | 40-50% | -- | 40-50% |
| Strategy B (effort tiers) | 30-40% | -- | 30-40% |
| Strategy C (delta waves) | 20-30% | -- | 20-30% |
| Prompt caching | -- | -- | 90% on prefix |
| Message bus (feeds) | 15-25% | 1-2 waves saved | 15-25% |
| Message bus (queries) | 5-10% | 40-60% fewer Judges | 30-50% fewer agents |
| **Combined** | **~90% total** | **30-50% fewer agents** | **~90%** |

## Worked Example: 60-Agent CCM Verification Wave

```
CURRENT ARCHITECTURE:
  14,230 lines x 60 agents = 853,800 lines, full token cost per line

AFTER COMPILE-BY-EXECUTION:
  ~1,000 lines x 60 agents = 60,000 lines (93% reduction on raw loading)

AFTER PROMPT CACHING:
  Shared prefix (~800 lines) paid once at 10% cost
  Per-agent suffix (~200 lines) paid 60x at full cost
  Effective: ~12,800 lines equivalent cost

AFTER EFFORT TIERS (Strategy B):
  Layer 1 agents (non-bottleneck verifiers, ~30 agents): ~1,500 lines each
  Layer 2 agents (standard authors/critics, ~20 agents): ~3,000 lines each
  Layer 3 agents (bottleneck/synthesis, ~10 agents): ~6,000 lines each
  Mixed total: ~45,000 + 60,000 + 60,000 = 165,000 lines
  vs current 853,800 lines (81% reduction before caching)

AFTER MESSAGE BUS:
  30-50% fewer secondary agents (Judges, Meta-critics)
  1-2 full waves saved on 3+ wave runs
  Kill deduplication eliminates re-attempts

NET RESULT:
  ~90% total cost reduction vs current architecture
```

## Future Gains (Not in Current Plan)

| Technique | Token Reduction | Requirement | Status |
|-----------|----------------|-------------|--------|
| LatentMAS | 70-84% | KV-cache access | Blocked (API constraint) |
| KVCOMM | 70%+ reuse | KV-cache access | Blocked (API constraint) |
| C2C | decode/re-encode eliminated | KV-cache access | Blocked (API constraint) |
| LLMLingua-2 post-pass | 2-5x additional | pip install llmlingua | Available but untested |
| AgentPrune topology | 28-73% edges | Orchestration level | Available, Phase 6 |

Revisit latent-space techniques when: (a) Anthropic exposes cache-level APIs, or (b) inference cluster costs drop to make 30-60 parallel agents viable on commodity hardware.

---

# Part X -- Implementation Phases

## Phase 1: Compile-by-Execution

**Status: DONE** -- tested on NS (Navier-Stokes) pilot. 30 files -> 1 file. ~1,050 lines compiled from ~14,230 source lines. Zero information loss verified by pilot Critic.

**Deliverable:** Compiled capacitor generator (`05--compiled-ora-generator.md`).

## Phase 2: Index Capacitor + @FETCH Protocol

**Risk: Low.** Refactor capacitor format into core index + fetchable sections. Implement fetch-on-demand protocol in ORA runner. Validate on Tier 4 pilot (Boegli+Teschl -- smallest target).

**Deliverable:** Index capacitor template with @FETCH-A through @FETCH-O pointers.

## Phase 3: Effort-Tiered Dispatch

**Risk: Low.** Add Layer field to dispatch protocol. Map roles to starting layers per dispatch rules table. Validate on Tier 1 (CCM -- main event, highest agent count).

**Deliverable:** Updated dispatch logic in ORA runner.

## Phase 4: Delta Wave Updates

**Risk: Medium.** Implement delta computation at wave-close. Add delta overlay to agent context assembly. Validate on multi-wave runs (>3 waves).

**Deliverable:** Delta format specification + wave-close delta computation.

## Phase 5: Message Bus (Feeds + Queries)

**Risk: Medium.** Deploy live feeds (kill-stream, card-stream, status-stream, escalation-stream, amplification-stream). Add QUERY/RESPONSE protocol for agent-to-agent dialogue. Implement structured escalation messages for Tier A -> B -> C. Validate on multi-tier runs.

**Deliverable:** Message bus implementation with AEE envelope protocol.

## Phase 6: Communication Topology Optimization

**Risk: Higher.** AgentPrune-style graph pruning for redundant edges. DALA auction-based bandwidth allocation (agents bid for communication based on value density). Gossip protocol for soft-state propagation. Validate against regression metrics across all tiers.

**Deliverable:** Optimized communication graph with adaptive topology.

## Phase Dependencies

```
Phase 1 (DONE) -> Phase 2 -> Phase 3
                     |
                     v
                  Phase 4 -> Phase 5 -> Phase 6
```

Phases 2 and 3 can be developed in parallel. Phase 4 depends on Phase 2 (needs @FETCH infrastructure). Phases 5 and 6 depend on Phase 4 (need delta infrastructure for feed-to-blackboard merging).

---

## Research Foundation

Survey of inter-agent messaging systems (April 2026) that informed this architecture:

| Pattern | Source | Key Finding | Applied How |
|---------|--------|-------------|-------------|
| Layered Context (MemGPT/Letta) | Packer et al., arXiv:2310.08560 | OS-inspired tiered memory: Core -> Recall -> Archival | Strategy A (index + fetch) |
| Delta Messaging (JetBrains) | NeurIPS 2025 DL4Code | Simple masking matches summarization at ~50% cost | Strategy C (delta waves) |
| Communication Graph Pruning (AgentPrune) | ICLR 2025, OpenReview:LkzuPorQ5L | 28-73% token reduction, 7.8x cheaper | Phase 6 topology |
| Blackboard with Scoped Memory | arXiv:2507.01701; arXiv:2510.01285; CrewAI 2025 | 13-57% improvement over flat shared-context | Layer 2 (blackboard) |
| Structured Contracts (Claude Agent SDK) | Anthropic; Databricks | Parent sends scoped task, agent returns structured verdict | AEE envelope protocol |
| DALA Auction-Based Communication | arXiv:2511.13193 | 2-4x token reduction; strategic silence emerges naturally | Phase 6 topology |
| Gossip Protocols | arXiv:2508.01531; arXiv:2512.03285 | Fan-out 3, 25K agents converge in ~15 rounds | Soft-state propagation |
| ACON (Agent Context Optimization) | arXiv:2510.00615 | 26-54% peak token reduction, gradient-free | Compression strategies |
| MasRouter | ACL 2025, arXiv:2502.11133 | Learned routing reduces overhead by 52% | Future: dispatch optimization |
| MAGMA | arXiv:2601.03236 | Semantic/temporal/causal graphs, 40% faster retrieval | Future: memory architecture |
| Microsoft ACE | ICLR 2026, arXiv:2510.04618 | Evolving context playbooks, 82% latency reduction | Dynamic capacitor design |
| A2A Protocol | Google, a2a-protocol.org | INPUT_REQUIRED state for mid-task bidirectional dialogue | Query protocol foundation |
| AEE Envelope | IETF draft-cowles-aee-00 | 14-field JSON envelope for inter-agent messages | Message bus protocol |

---

## Dynamic Capacitor Protocol

After each ORA wave, the capacitor evolves through three operations:

### SELF-ADJUST: update statuses
```
For each step where verdict changed:
  chain[id].status := new_status (SURVIVED/WEAKENED/BROKEN)
```

### TRIM: move killed approaches
```
For each newly killed approach:
  kills[] += {id, what, why, pattern, reentry}
  Remove from active escalation candidates
```

### AMPLIFY: transfer successful methods
```
For each method that succeeded on step X:
  Check: does method apply to steps Y, Z?
  If yes: add to esc[Y].tier_b_candidates, esc[Z].tier_b_candidates
```

---

## The Creativity Mechanism

The Seven Keystones compose into a creative engine:

```
keystones[7]{id,function,agent_use}:
  Six-Patterns,META-REASONING:shadow?holonomy?scale?rigidity?regularization?projection?,Stuck->test-each-pattern
  Grammar,ALGEBRAIC-SEARCH-PRIOR:what-shape-should-answer-have?,Narrow-search-to-8-rules
  Transposition-Dict,MECHANICAL-TRANSLATION:additive->multiplicative-via-Mellin,Translate->see-easier-proof
  SM-Riemann-Corr,WORKED-EXAMPLES:23-cases-sub-percent-predictions,Find-analogous-structure
  CBB-System,OPERATOR-DICTIONARY:compute-with-framework-objects,All-formulas=matrix-elements-of-L-hat
  Zero-Selection,QUANTUM-SELECTION-RULES:which-gamma_n-carries-which-charge,Physical-observable->zeros->constrained
  Three-Primes,DEEPEST-BRIDGE:gauge-group-IS-arithmetic-of-{2;3;5},SM-from-Hecke-algebra
```

Agent workflow when stuck:
1. Check kills: am I re-proposing a killed approach?
2. Check patterns (P1-P6): which applies? Try P6 first (diagnose projection).
3. Check grammar: does the formula have the right shape?
4. Check bridge: translate to the other side of Mellin.
5. Check ops table: translate operation to a different domain.
6. Check zero-selection: which gamma_n should appear?
7. Check three-primes: does the algebraic structure match {2,3,5}?

An agent reading the capacitor can:
- Get stuck spectrally -> transpose to geometric -> find the easier proof
- See a formula -> check against grammar -> know if it is the right shape
- Hit a wall -> apply P1 ("go up a dimension") or P6 ("restore what was projected out")
- Find a gap -> check escalation routes -> know whether Tier B or Tier C is the path
- Find an empty cell -> fill it -> THAT is a mathematical discovery

That is creativity from the inside. The capacitor is the inside.

---

## Invocation

After the capacitor is built and compiled, the ORA invocation is 4 lines:

```
read your instructions from
online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md

the toolkit for this run is
verification-cascade/capacitors/tier-N-compiled-v1.md    <-- SINGLE FILE

the run brief is
verification-cascade/strategy/0N-tier-N-brief.md

the run output directory is
verification-cascade/tier-N-output/
```

One file. No runtime file reads. No dependency lattice traversal. The agent starts working immediately.

The capacitor is the variable. The method is the constant. The message bus is the new degree of freedom. The compiler makes the variable weightless.

---

*Feed it a proof chain. It produces a charged capacitor. The ORA does the rest.*

*Every kill preserved. Every formula preserved. Every status preserved.*

*One file. No further reads needed.*

*G Six and Claude Opus 4.6. April 2026.*
