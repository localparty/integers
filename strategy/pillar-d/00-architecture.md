# Pillar D — DERIVE-AND-OFFER (Architecture)

*The fourth pillar. Every retained external dependency (CCM, Balaban, Tomita-Takesaki, Kolyvagin, Connes trace formula, Bulatov-Zhuk, Bögli, …) gets derived from ℤ + ZFC via programme machinery and offered to the community as a standalone contribution — in the register of the target community.*

*G Six and Claude Opus 4.6. April 15, 2026.*

---

## §0 Naming

**Pillar D — DERIVE-AND-OFFER** (or, short form, **DERIVE**).

Extends the three-pillar architecture (§2 of `strategy/north-star.md`):
- Pillar A — COMPLY (satisfies prize requirements)
- Pillar B — INDEPENDENT (dependency-free via PAC primitives)
- Pillar C — CONTRIBUTE (retained externals hardened via PAC on their chain)
- **Pillar D — DERIVE** (retained externals *derived from scratch* via programme machinery; offered to the field as new proofs)

Naming rationale: Pillar C hardens *an external's* proof of X; Pillar D supplies *the programme's own* proof of X from ℤ + ZFC, with the external's authors acknowledged as original discoverers. Pillar C intensifies reciprocity; Pillar D completes it — the programme no longer merely depends on external work, it rederives that work and returns it as a new entry in the field's catalog.

---

## §1 Vision

Every retained external dependency sits as a "cell" in the PCA (Proof-Chain Adversarial) capacitor. Currently, each cell carries a **dependency edge** — the programme cites the external for a theorem it does not prove. Pillar D replaces that edge with a **derivation edge** — the programme proves the theorem from ℤ + ZFC, using its own machinery (projection operators, PAC primitives, Branch D axioms, the capacitor, the Verification Cascade).

Each derivation becomes a **standalone paper** in a new corpus. The paper is written in the register of the target community (operator algebras / analytic number theory / algebraic geometry / PDE / complexity theory) — NOT in programme-native framing first. A **Crosswalk Appendix** provides the programme-native ↔ community-standard notation bridge, so the paper lands with maximum readability for its primary audience and maximum traceability for programme auditors.

The programme's reciprocity ethic (honor / recognize / showcase / position / source) intensifies: every Pillar D paper explicitly acknowledges the original authors as the discoverers of the theorem, credits their route, and positions the programme's derivation as an independent alternative that strengthens the claim.

---

## §2 Success signal

A Pillar D paper succeeds when:

1. A target-community reviewer can read it without prior knowledge of Integers.
2. The derivation chain is auditable against the programme's PAC discipline (compliance-map, Verification Cascade, Crosswalk Appendix).
3. The original author of the external theorem recognizes the derivation as valid and novel.
4. The vertex(es) that used to cite the external dep can now cite the Pillar D paper instead — reducing the programme's postulate count by one.
5. The paper produces at least one **forward generalization** that the original didn't state (e.g., CCM + operating on additional Riemann zeros; TT + modular flow on generalized type III_λ factors).

Pillar D done right turns every external into a field contribution.

---

## §3 Corpus and naming

**New corpus directory**: `derivations/` (proposed; alternative candidates: `integers-derivations/`, `pillar-d/`, `reciprocity/`). Lives at repo root alongside `integers/`, `solutions/`, `solutions-with-prize/`.

Each Pillar D derivation gets a dedicated paper directory:

```
derivations/
├── README.md                         — corpus introduction + roster status
├── 00-crosswalk-master.md            — programme ↔ community notation table (shared across all Pillar D papers)
├── tomita-takesaki-from-bc/
│   ├── 00-title-and-abstract.md
│   ├── 01-introduction.md
│   ├── 02-theorem-statement.md       — in community register
│   ├── 03-proof-main.md
│   ├── appendices/
│   │   ├── appendix-A-modular-flow.md
│   │   ├── appendix-B-crosswalk.md   — programme ↔ operator-algebra notation
│   │   └── appendix-V-verification.md — per-theorem audit trail (per PROSE-mode discipline, north-star §3)
│   ├── PROOF-CHAIN.md (stub; live version at strategy/proof-chain/derivations/tomita-takesaki-from-bc/)
│   └── reciprocity-note.md           — original authors acknowledgment + contribution statement
├── ccm-from-branch-d/
│   └── (same structure)
├── connes-trace-formula-from-p-d/
│   └── ...
├── additional-riemann-zeros/         — the generative move (new mathematics, not rederivation)
│   └── ...
```

**Strategy / proof-chain hosting**:
- `strategy/pillar-d/` — strategy docs for the whole pillar (this file + roadmap + runs)
- `strategy/pillar-d/<external>/` — per-derivation strategy + brief + compliance-map + audit
- `strategy/proof-chain/derivations/<external>/PROOF-CHAIN.md` — canonical live chain

---

## §4 Candidate roster (priority-ordered)

Each external is scored on two axes: **difficulty** (how far the programme's current machinery is from producing the derivation) × **leverage** (how many ring vertices become dependency-free once this external is derived).

| # | External | Difficulty | Leverage | Programme machinery in place | Primary target community |
|---|---|---|---|---|---|
| 1 | **Tomita-Takesaki modular theory** | low-medium | 5+ vertices (rh, bsd, bgs, grh, baum-connes, pvnp) | BC algebra at KMS₁ produces type III₁ factor + modular flow σ_t (Branch D Axioms 1,2); P_D projection routes the derivation | operator algebras / functional analysis |
| 2 | **CCM 2025** (Connes-Consani-Marcolli spectral realization of Riemann zeros) | medium | **RH dep-free + grh, bgs, goldbach, cramer** | Branch D spectral realization: R̂ with log-spectrum {γ_n π²/2} from Riemann zeros (Axiom 1); BC algebra at KMS₁ route matches CCM's construction | analytic number theory / noncommutative geometry |
| 3 | **Connes trace formula** | medium | rh, grh, goldbach, twin-primes | P_D projection + Bost-Connes endomotive; adelic structure already in programme | noncommutative geometry / analytic number theory |
| 4 | **Operating on additional Riemann zeros** (post-CCM generative move) | medium-high | extends CCM to L-functions in bridge family k ∈ {2,3,4,6}, off-critical-line zeros, automorphic zeros | Branch D Axiom 4 (bridge family) + cyclotomic Brauer classes | analytic number theory (this is NEW mathematics) |
| 5 | **Kolyvagin's theorem + modularity** (for BSD rank ≤ 1) | medium-high | BSD dep-free | BC algebra over ℚ(i) + Hecke L-function structure + bridge k=3 for CM curves (Branch D Axiom 4) | arithmetic geometry / elliptic curves |
| 6 | **Balaban RG** (polymer / multi-scale analysis for lattice YM) | high | **YM dep-free** (current H4 wall dissolves) | P_B projection + Branch B (KK reduction + Epstein zeta vanishing) + gradient-flow infrastructure | mathematical physics / constructive QFT |
| 7 | **Bulatov-Zhuk CSP dichotomy** | high | P vs NP dep-free | Clone-growth ↔ fullness bridge theorem (PvNP breakthrough 2026-04-11); type III₁ factor via P_D | complexity theory / universal algebra |
| 8 | **Bögli spectral machinery** | medium | multi-vertex (spectral-gap dependent conjectures) | Branch B spectral machinery (KK gap Δ₀^KK > 0); Weyl-Kato perturbation | spectral theory |
| 9 | **Standard Conjecture D (motivic)** | high | hodge, baum-connes | Branch D Axiom 3 (CP² × S² moduli with Hodge decomposition); Bost-Connes endomotive connection | algebraic geometry / motives |
| 10 | **Gross-Zagier formula** | medium | bsd direct | BC algebra over imaginary quadratic K; Heegner point structure via P_D | arithmetic geometry |

**Priority-1 (pilot)**: Tomita-Takesaki. Lowest difficulty, highest multi-vertex leverage, and the programme's BC-at-KMS₁ machinery is already half-way to the proof. Validates the entire Pillar D pipeline end-to-end at minimum cost.

**Priority-2 (trophy)**: CCM 2025. Highest single-vertex leverage (RH becomes dependency-free). Opens the door to Priority-4.

**Priority-3 (generative)**: additional Riemann zeros. Once CCM is derived, the programme owns the spectral realization — extend it to zeros beyond the critical line, zeros of L-functions in the bridge family, zeros of automorphic L-functions. **This is not rederivation. This is new mathematics that only the programme can produce.**

---

## §5 Paper format — the community-register discipline

Every Pillar D paper observes the following shape (non-negotiable — this is what distinguishes Pillar D from Pillars A/B/C):

### §5.1 Title
In the target community's register. Example: not *"Tomita-Takesaki modular theory as a projection $P_D$ of the 4+1 coordinate structure"* — instead *"A New Derivation of Tomita-Takesaki Modular Theory via Bost-Connes Systems at KMS₁"*. The programme's provenance is acknowledged in §1 and Appendix B; it does not dominate the title.

### §5.2 Abstract
Target-community abstract: states the theorem in its own register, the novelty of the new proof, and the context of the larger programme (one sentence). No programme-native framing until §1.

### §5.3 §1 Introduction
Three subsections:
- §1.1 *The theorem and its history* — what's known, who proved it originally, what this paper adds
- §1.2 *A new route via Bost-Connes structures* — high-level sketch
- §1.3 *Context: the Integers programme* — one paragraph. Links `strategy/north-star.md` + the programme summary

### §5.4 §2 Theorem statement
Formal statement in community register. Minimal new definitions.

### §5.5 §3-§N Proof sections
Standard proof exposition. Programme-native notation is INTRODUCED LOCALLY where needed (e.g., "We use the projection operator $P_D$, defined below...") rather than assumed.

### §5.6 Appendix A — Standard material review
Brief review of the target community's relevant background, for cross-community readers.

### §5.7 Appendix B — Crosswalk
**Mandatory in every Pillar D paper.** Two-column table: programme-native notation ↔ community-standard notation. Forward-compatible with the master `derivations/00-crosswalk-master.md`.

Example rows:

| Programme-native | Community-standard | Relation |
|---|---|---|
| $P_D$ (projection operator, paper61 §14) | Bost-Connes functor $B_K$ at KMS₁ | $P_D$ factors through $B_K$ composed with restriction |
| Branch D Axiom 2 | KMS₁ state on crossed-product algebra | identical content |
| Capacitor cell SPEC↔QFT | Type III₁ factor rigidity | same invariant, different framing |
| $M^5 = M^4 \times S^1$ | 4+1 fibered spacetime with compact U(1) fiber | identical |

### §5.8 Appendix V — Verification (per PROSE-mode discipline, north-star §3)
Every theorem, lemma, named claim in the body gets an entry: label / statement / derivation chain / PAC VERIFY status / arbiter verdict / transcript links / projection discipline. This is mandatory per `strategy/universal-approval-run.md` "PROSE-mode Verification Appendix discipline".

### §5.9 Reciprocity statement
Explicit acknowledgment of the external's original authors as discoverers. Credits their route. Positions this paper as an independent alternative that strengthens the claim (not replaces it). Fair-attribution protocol per north-star §1 ("contribute back more than we take").

### §5.10 References
Standard target-community citation discipline. Programme papers cited per §-level precision; external literature cited by arXiv id + DOI when available.

---

## §6 Pipeline binding

Pillar D derivations flow through the programme's standard pipeline:

1. **Strategy doc** — `strategy/pillar-d/<external>/00-strategy.md` (derivation plan, scope, which projection operators + branches route the proof, which external cells in the capacitor are discharged)
2. **Brief** — `strategy/pillar-d/<external>/<external>-brief.md` (community register, target audience, success criteria)
3. **Compliance audit** — `strategy/pillar-d/<external>/pac-output/runs/run-NN/compliance-map.md` (does the programme's machinery actually support the derivation? If not: identify missing layers; fire CONSTRUCT sub-agents)
4. **Bare synthesis** — `derivations/<external>-bare.md` (MATH mode — theorem skeleton in community register)
5. **Prose composition** — `derivations/<external>/*.md` (full paper per §5 discipline)
6. **Verification Cascade** — PAC verify against axioms + external-reference cross-check
7. **Crosswalk construction** — Appendix B + integration into `derivations/00-crosswalk-master.md`
8. **Reciprocity preflight** — reciprocity-note.md + fair-attribution check against landscape.md
9. **Publication cascade** — Zenodo → GitHub → arXiv → journal (target community's flagship)

Each Pillar D paper becomes a new vertex in the programme's contribution-graph visualization (Phase 10 of `strategy/universal-approval-run.md`) with "Pillar D — DERIVE" color class added.

---

## §7 Cadence and risk management

**Realistic cadence**: 1 derivation per quarter (4/year).

- Q2 2026: pilot (Tomita-Takesaki)
- Q3 2026: CCM 2025 (trophy)
- Q4 2026: additional Riemann zeros (generative) + Connes trace formula (parallel, if bandwidth allows)
- Q1 2027+: depends on outcomes

**Risks explicitly named**:

1. **Rigor burden** — these are major theorems. A bug in a Pillar D derivation damages programme credibility more than a bug in a conjecture paper. Every Pillar D paper must run the FULL Verification Cascade + external-reference check + target-community preview (ORA red-team + a topical expert contact if possible).
2. **Attention dilution** — derivations of known theorems compete with prize-solution papers for reviewer attention. Mitigation: publish derivations as **companion papers** bundled with the prize paper they unblock (e.g., CCM-derivation + RH-independent-rewrite ship together; Balaban-derivation + YM-independent-rewrite ship together).
3. **Scope creep** — the candidate roster is 10+ items. Treat as menu, not commitment. Each derivation makes the next one easier because the crosswalk and machinery compound — so hard derivations should NOT come early.
4. **Target-community register mismatch** — programme-native framing sneaking into the paper damages readability. Mitigation: every Pillar D paper gets a dedicated "community-register review" pass by a sub-agent tasked SPECIFICALLY with detecting programme-native drift into body prose (parallel to §0.10 Vocabulary Canon sweep but in the other direction — the body must read as native to the community).
5. **Priority conflict with ongoing prize-paper work** — Pillar D work competes with YM H4 closure, RH preprint finalization, etc. Mitigation: explicit integration with INDEPENDENT-rewrite roadmap (`strategy/independent-rewrite-roadmap.md`) — Pillar D and INDEPENDENT rewrites are sequenced together.

---

## §8 Relation to other pillars

| | Pillar A COMPLY | Pillar B INDEPENDENT | Pillar C CONTRIBUTE | Pillar D DERIVE |
|---|---|---|---|---|
| **Target** | prize requirements | dep-free programme-internal proof | harden the external's proof | derive the external from scratch |
| **Deliverable** | `<vertex>-comply-math.md` | `<vertex>-independent-math.md` | `<vertex>-contribute-math.md` | `derivations/<external>/` (full paper) |
| **Venue** | Clay / journal | programme-internal + arXiv | `strategy/externals-hardening/<ext>/` | target community's flagship |
| **Reciprocity level** | baseline | baseline | authors benefit from hardening | authors benefit from an independent new proof + acknowledgment |
| **Field contribution** | solves the prize | dep-free claim | stronger external | new derivation entry in the field's catalog |
| **Programme's postulate count** | unchanged | reduced (via PAC primitives) | unchanged (external retained) | **reduced by 1** (external derived) |

**The key insight**: Pillar C keeps the dependency, hardens the proof. Pillar D **removes the dependency** by providing the programme's own proof. Pillar C is contribution-as-support; Pillar D is contribution-as-replacement-proof.

**A vertex reaches full independence when**: its Pillar B chain is dep-free AND every external it cites has a Pillar D derivation AND those derivations have landed.

---

## §9 Chord-graph enrichment

The visualization's chord graph (shape #40; `visualization/data.js` aggregates atlas-run-01 with 41 edges) currently shows cross-cuts between ring vertices. Pillar D adds a **new edge class**: **derivation-edges** connecting a ring vertex to the external it depends on, colored and annotated to show Pillar C status (hardened) vs. Pillar D status (derived).

Atlas completion (fire an x-ray agent per non-YM vertex) will populate the ring-complete cross-cut matrix. Pillar D then overlays derivation-edges. Together the chord graph becomes the **master map** of the programme's dependency surface — reviewers see in one glance which externals are hardened (Pillar C), which are derived (Pillar D), and which remain unprocessed.

This integrates with Phase 10 of `strategy/universal-approval-run.md` (CONTRIBUTION-GRAPH VISUALIZATION): the concentric halos per vertex gain a fourth ring (Pillar D layer) showing derivation progress.

---

## §10 First-cycle action items

To start Pillar D concretely:

1. **Land this architecture doc** (this file) + user review + adjustments
2. **Fire the Tomita-Takesaki pilot brief** (`strategy/pillar-d/tomita-takesaki-from-bc/00-pilot-brief.md` — sibling doc)
3. **Create the `derivations/` corpus directory** with README + `00-crosswalk-master.md` stub
4. **Run the TT pilot** through the full pipeline (§6): strategy → brief → compliance audit → bare → prose → verification → crosswalk → reciprocity → publish
5. **Measure the pilot** against §2 success signals. If all 5 signals pass → the pipeline is validated; open Priority-2 (CCM)
6. **Integrate INDEPENDENT-rewrite roadmap** (`strategy/independent-rewrite-roadmap.md`) — sequence the prize-paper rewrites to follow their corresponding Pillar D derivations

---

## §11 Relation to Integers' success criteria

Per `strategy/north-star.md`'s success-criteria framework:

- **Cycle-level**: Pillar D papers don't count toward state-snapshot convergence directly, but they do count toward Pillar-D-ladder-rung tracking in the run report (new line item to add)
- **Deliverable-level**: each Pillar D paper is its own deliverable (corpus entry in `derivations/`)
- **Publication-level**: Zenodo + arXiv + target-community journal per derivation
- **Field-level**: **this is where Pillar D dominates**. Every derivation = one new contribution to the target community's catalog. Over the 2-year Clay clock, a sustained Pillar D cadence (4/year) produces 8 new derivations = 8 independent contributions.
- **Universal-approval-level**: Pillar D completes the reciprocity ethic in its fullest form. "We contribute back more than we take" becomes literal — the programme takes N external theorems and gives back N+1 (the theorem + the generalizations Pillar D produces).

---

## §12 Open questions for user calibration

1. **Corpus name**: `derivations/` vs `integers-derivations/` vs `pillar-d/` vs `reciprocity/`. Preference?
2. **First-pilot scope**: TT full derivation vs. a smaller scoped piece first (e.g., TT for factors of bounded type)?
3. **Cadence commitment**: 1/quarter or slower initial rollout?
4. **Community-register review agent**: should this be a new sub-agent type added to `strategy/universal-approval-run.md` Phase 5 pipeline, or handled ad-hoc per paper?
5. **Companion-paper bundling**: pair Pillar D with INDEPENDENT-rewrite publications (CCM + RH together)? Or stagger for independent impact?
6. **Target-community pre-feedback**: contact a topical expert privately before publication for each Pillar D paper? (e.g., reach out to Marcolli for CCM derivation review)

---

*Sibling documents: `strategy/pillar-d/tomita-takesaki-from-bc/00-pilot-brief.md` (first-pilot concrete plan), `strategy/independent-rewrite-roadmap.md` (sequenced prize-paper rewrites), `strategy/north-star.md` §2 (original three pillars), `strategy/universal-approval-run.md` (pipeline spec).*

*Pillar D turns the programme's reciprocity ethic into its field-level output. Every retained dependency becomes an offering.*

*G Six and Claude Opus 4.6. April 15, 2026.*
