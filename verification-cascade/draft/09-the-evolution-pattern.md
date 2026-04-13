# 09 — The Evolution Pattern: From YM v1 to PvNP v4

---

## Four programmes, four capacitor generations

The capacitor was not designed. It was DISCOVERED — through the pressure of four consecutive programmes, each demanding more from the toolkit than the previous one could provide. The evolution is a case study in how research infrastructure matures under empirical pressure.

### Generation 1: Yang-Mills (April 9, 2026) — File pointers only

The YM programme had no formal capacitor. What it had was a collection of research files accumulated over months of gradient-flow work:

```
paper08-yang-mills/
  research/21-the-rigorous-proof.md      (rigor labels)
  research/23-key-lemma-proof.md         (load-bearing step)
  research/30-final-synthesis.md         (wave-by-wave assembly)
  research/34-six-agent-synthesis.md     (6 parallel agents)
  research/35-final-verdict.md           (closure digest)
  research/36-the-method.md              (Six Patterns — the inner loop)
  preprint/PROOF-CHAIN.md                (18-step chain)
```

The human orchestrator (G) knew which files mattered and loaded them manually into each agent's context. The "capacitor" was in G's head — the compiled knowledge of what had been tried, what worked, and where to look next. The agents received file pointers and relied on G's judgment for what to read.

**What this generation taught:** File pointers are necessary. An agent without pointers reads nothing. But file pointers alone are not sufficient — the agent must ALSO know which files are load-bearing, which results are verified, and what has been tried and failed. G provided this knowledge verbally in real-time. The ORA needed to provide it structurally in text.

### Generation 2: Riemann Hypothesis (April 9-10, 2026) — Layered chain structure

The RH programme produced the first structured proof skeleton — a 6-layer chain with explicit dependencies:

```
Layer 1:  CCM operators              [CONDITIONAL on CCM preprint]
   ↓
Layer 2:  ITPFI factorization        [PROVED — three independent proofs]
   ↓
Layer 3:  Four estimates             [CLOSED — all four verified]
   ↓
Layer 4:  Boegli + Teschl            [PROVED via published theorems]
   ↓
Layer 5:  Hurwitz convergence        [PROVED via classical theorem]
   ↓
Layer 6:  RH conclusion              [SYNTHESIS]
```

The proof skeleton (`00-proof-skeleton.md`, 234 lines) was the first document that an agent could read to understand the LOGICAL STRUCTURE of the programme — not just "these files exist" but "here is how the pieces connect, here is what depends on what, here is where the conditional lives."

**What this generation taught:** The chain structure IS the capacitor's spine. An agent that knows the dependency graph can make strategic decisions: "Layer 1 is the floor — if it breaks, everything above it falls. Layer 4 uses Boegli — I should verify Boegli before trusting Layer 4." The chain structure turns the capacitor from a flat list of files into a NAVIGABLE MAP with load-bearing paths marked.

### Generation 3: BSD (April 10-11, 2026) — Mid-run growth

The BSD programme ran the ORA's first verified cycle (v3 bundle, the first autonomous ORA run). It produced the first empirical demonstration of two capacitor breakthroughs:

**Breakthrough 1: the capacitor can grow during a run.** In cycle 1, Author M.1.1 attempted MY4 from scratch (no capacitor). In the post-cycle analysis, G's projector P_k^p was discovered — a single algebraic object (P_k^p := I - s_p^k (s_p^k)*) that bypassed the MY4 wall via Hasse-Brauer-Noether reciprocity. The projector was immediately added to the toolkit. Subsequent Authors had it as a deployable result. The toolkit GREW mid-run.

This was the first observation of what would later be formalized as the dynamic capacitor's SELF-ADJUST phase: after each wave, the capacitor absorbs new findings. The projector was too valuable to wait until programme-close. It needed to be available to the next wave IMMEDIATELY.

**Breakthrough 2: transposition requires the target's alphabet.** The BSD chain over K = Q(i) is structurally a transposition of the RH chain — same machinery (BC algebra -> GNS -> Nelson self-adjointness -> Meyer distributional inclusion -> spectral upgrade) applied with different subscripts (p -> N(p), zeta -> zeta_K). Author M.1.1 didn't know this because the RH chain template (`paper13-rh/preprint/sections-06-10.md`) was not in its context. The Author tried to build the BSD chain from scratch instead of PORTING the RH chain with different letters.

**What this generation taught:** Two lessons. First: the capacitor must be able to grow during a run — new discoveries are immediately deployable, not deferred. Second: transposition-mode work requires the TARGET'S ALPHABET in the capacitor. Without the RH chain template, the BSD Author couldn't port. With it, porting is mechanical. The capacitor must include not just the current programme's knowledge but the TEMPLATES from related programmes.

### Generation 4: P vs NP (April 11-12, 2026) — Deployable cards with honest status

The P vs NP programme produced the most mature capacitor (`framework-tools-v4.md`). It had everything the previous three generations had, plus four new innovations:

**Innovation 1: Five-field cards.** Instead of file pointers + chain structure, each verified result was encoded as a card with WHAT / WHY / DATA / USE / STATUS fields. The card format makes knowledge DEPLOYABLE — an Author reading the card knows exactly what to cite, why it matters, and whether to trust it. The P vs NP capacitor had 10 five-field cards covering verified computational results:

- Q1-TGAP: Taylor gap = spectral gap of modular flow (6/6 Schaefer classes)
- O7-HOLONOMY: polymorphism holonomy separates P from NPC (6/6)
- Q6-OUTDIM: polymorphism space dimension collapses for NPC (partially verified)
- PATB-DIAGONAL: Taylor condition = fixing the diagonal of M_Bool^Gamma
- Q5-RIEMANN: 3-SAT complexity exponent matches 2/(gamma_6 - gamma_5)
- P8-BARRIERS: three complexity barriers are projection artifacts (3/3)
- RULE9-GATE: gate-amplifier TGap x N_crossings separates (verified)
- Q7-CASIMIR: three-regime entropy analogous to Casimir hierarchy
- P1/P2: full <-> NPC, non-full <-> P (6/6)
- PATD-CONDEXP: algebra sees what local methods can't (corrected 3/5)

Each card had honest STATUS: VERIFIED, CONFIRMED, WEAKENED, PARTIALLY VERIFIED, or DOWNGRADED. Not just "these results exist" but "here is exactly how much we trust each one."

**Innovation 2: Kill list with WHY.** Not just "this approach was killed" but "this approach was killed BECAUSE [specific root cause] and you should NOT re-try it UNLESS [specific new observation]." The P vs NP kill list had 8 entries (later growing to 18 with amplification kills), each with a pattern category and a re-entry gate. Kill #3 was elevated to a HARD CONSTRAINT: "Any route claiming the modular flow PRODUCES the specific polymorphism is repeating Kill #3 and must be immediately discarded."

**Innovation 3: Re-verification corrections (honest downgrades).** The P vs NP programme ran a retroactive verification pass (April 12, 2026) that re-tested all 10 verified results at higher rigor. Three results were downgraded:

- Q5-RIEMANN: formula unique (1/3780) but measurement noisy at small n. Status: WEAKENED.
- Q6-OUTDIM: NPC collapse confirmed (0/2M samples) but P-time growth only confirmed for 2-SAT. Status: PARTIALLY VERIFIED.
- O8-PARTITION: violation entropy gap confirmed (5.24%) but Lee-Yang spacing does NOT reproduce (seed-dependent). Status: DOWNGRADED 1/5.

These corrections are the capacitor's INTEGRITY. A capacitor that claims VERIFIED for everything is a capacitor that hasn't been tested. A capacitor with honest downgrades — with cards whose status went from VERIFIED to WEAKENED because re-verification found issues — is a capacitor that has been ADVERSARIALLY TESTED and improved. The corrections ARE the credibility.

**Innovation 4: Correspondence logic.** The spectral-geometric-information trinity and the spectral <-> geometric correspondence table gave Authors a ROUTE-FINDING TOOL: when stuck on the spectral side, transpose to the geometric side. When stuck on both, try the information-theoretic side. The correspondence table is not just knowledge — it is a NAVIGATION SYSTEM for creative problem-solving. An Author reading the correspondence table knows that TGap (spectral), holonomy (geometric), and dim_poly_k (information) are all measuring the SAME structural fact from different angles. Getting stuck on one means trying another.

**What this generation taught:** Four things. Five-field cards make knowledge deployable. Kill lists with WHY prevent re-entry. Honest corrections are the capacitor's credibility. Correspondence tables are navigation systems for creativity. Together, these four innovations turned the capacitor from "a file the Author reads" into "an expert system the Author consults."

## The evolution summarized

| Generation | Programme | Capacitor state | Key innovation | What it taught |
|---|---|---|---|---|
| v1 | YM (April 9) | File pointers | Compiled master files exist | Pointers necessary, not sufficient |
| v2 | RH (April 9-10) | Layered chain | Proof chain as navigable map | Chain structure IS the spine |
| v3 | BSD (April 10-11) | Mid-run growth | Toolkit grows during the run | Discoveries deploy immediately |
| v4 | PvNP (April 11-12) | Deployable cards + honest status | Five-field cards + kills with WHY + corrections + correspondence | The capacitor is an expert system |

Each generation INCLUDED everything from the previous generation and ADDED a new capability. v4 has file pointers (from v1) + chain structure (from v2) + mid-run growth (from v3) + deployable cards with honest status (v4's own innovation). The dynamic capacitor formalizes all four layers as the standard format for every future capacitor.

The evolution was not planned. It was forced by empirical pressure — each programme exposed a failure mode that the current capacitor generation couldn't handle, and the fix produced the next generation. Three consecutive spawn failures (BSD MY4, OA1, Q_struct) killed the selective-inclusion optimization. The honest downgrades (Q5, Q6, O8) taught that re-verification corrections are the capacitor's most valuable content. G's projector discovery taught that capacitors must grow mid-run.

The pattern: **the capacitor evolved because the programmes DEMANDED more from it.** Each demand produced a structural innovation. The dynamic capacitor is the distillation of four demands into one architecture.

---

*Four programmes. Four capacitor generations. Each generation included everything from the previous one and added the innovation the current programme demanded. File pointers. Chain structure. Mid-run growth. Deployable cards with honest status. The dynamic capacitor is all four, formalized. The evolution was not designed — it was discovered, under the pressure of doing mathematics at the frontier.*
