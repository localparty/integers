# 10 — The Dynamic Capacitor: Self-Adjust, Trim, Amplify

---

## A capacitor that learns

A static capacitor is useful. A dynamic capacitor is powerful. The difference: a static capacitor contains what was known BEFORE the run. A dynamic capacitor contains what was known before the run PLUS everything discovered DURING the run, with honest corrections applied and successful methods amplified across programmes.

The dynamic capacitor runs a three-phase update cycle after each ORA wave:

## Phase 1: Self-Adjust

After each wave returns, the capacitor absorbs new knowledge:

**New five-field cards** for results discovered during the wave. When an Author finds a new structural identification, or a Critic produces a verification verdict, or a Synthesis agent identifies a cross-lead pattern — each of these becomes a new card. The card starts with STATUS = PENDING and is upgraded to VERIFIED / WEAKENED / BROKEN after the next Critic pass.

**Updated statuses** on existing cards. A card that was PENDING at wave-open may be SURVIVED at wave-close (the Critic verified it). A card that was VERIFIED at wave-open may be WEAKENED at wave-close (the re-verification found an issue). Status flows in both directions — up (PENDING -> VERIFIED) and down (VERIFIED -> WEAKENED). Both directions are documented.

**New kill list entries.** Every approach that was tried and failed during the wave becomes a kill with pattern category, root cause, and re-entry gate. The kill list grows monotonically — kills are never removed, only extended with re-entry conditions if new evidence justifies retrying.

**New correspondence entries.** When an Author discovers a cross-domain correspondence (a spectral fact that has a geometric image, or an algebraic structure that has an information-theoretic interpretation), the correspondence table gains a row. Empty cells that are FILLED during a run are among the most valuable outputs — they open new pathways that didn't exist before.

**New escalation routes.** When a step is found WEAKENED, the runner identifies excision and construction candidates. These are added to section H.8 of the capacitor for future waves.

The self-adjust phase is AUTOMATIC — it happens as part of the cycle-close checklist. The runner writes the blackboard updates AND the capacitor updates in the same cycle. The capacitor is not updated "later" or "at session-close" — it is updated IN THE CYCLE WHERE THE DISCOVERY HAPPENS. This is the BSD lesson: G's projector was too valuable to defer.

## Phase 2: Trim

Not everything in the capacitor stays at its original value. The trim phase removes or downgrades stale knowledge:

**Killed approaches move to the kill list.** If a wave's Author tries an approach and the Critic kills it, the approach moves from "active strategy" to "kill list entry." The card is not deleted — it is RECLASSIFIED. Its STATUS changes from "candidate" to "KILLED" with a WHY field. Future Authors see the kill and don't re-attempt.

**Weakened results get honest corrections.** This is the PvNP v4 pattern. During the P vs NP programme's retroactive verification (April 12, 2026), three results were downgraded:

- **Q5-RIEMANN** went from "VERIFIED — 3-SAT complexity exponent equals 2/(gamma_6 - gamma_5) at 0.001%" to "WEAKENED — formula unique (1/3780 among tested Riemann-zero formulas) but fitted alpha = 0.383 +/- 0.142 (1-sigma includes 0.43 but not clean)." The measurement was real. The precision claim was overstated. The correction preserves the finding (the formula is unique) while honestly downgrading the confidence (the numerical fit is noisy at small n).

- **Q6-OUTDIM** went from "VERIFIED 6/6 — polymorphism space dimension separates P from NPC perfectly" to "PARTIALLY VERIFIED — NPC collapse bulletproof (0 in 2M samples); P-time growth confirmed only for 2-SAT at 50k tuples; Horn/Dual-Horn/XOR NOT reproduced at k=5 with rigorous checking." The NPC side held. The P-time side weakened. The correction splits the card into what's solid and what needs more work.

- **O8-PARTITION** went from "VERIFIED 5/5 — Lee-Yang zeros separate P from NPC" to "DOWNGRADED 1/5 — violation entropy gap confirmed (5.24%) but Lee-Yang spacing does NOT reproduce (seed-dependent). V2 was statistical fluctuation." The original verification was flawed. The retroactive check caught the flaw. The card now says: "Do NOT cite O8 as verified. Only violation entropy (V1) is robust."

These corrections are the capacitor's IMMUNE RESPONSE. A finding that survives re-verification is strengthened. A finding that doesn't is honestly downgraded. The corrections themselves are documented in section H.12 — the reader can see exactly what changed, when, and why.

**Superseded correspondence logic is replaced.** When a new wave discovers a better correspondence (a more direct spectral-to-geometric mapping, or a correspondence that works at higher precision), the old correspondence is replaced. The old version is preserved in the corrections log as a historical note, not deleted — the evolution of understanding is part of the record.

The trim phase requires HONESTY. It is easier to leave a card at VERIFIED than to downgrade it to WEAKENED. It is easier to keep a killed approach as "maybe try again" than to move it to the kill list with a HARD CONSTRAINT. The trim phase is where the anti-overfit discipline meets the capacitor: every downgrade is an honest negative, and honest negatives are the programme's credibility (Signature 2).

## Phase 3: Amplify

When a verification, excision, or construction succeeds, the method and findings amplify across tiers:

**Method amplification.** If the Tier 4 pilot (Boegli + Teschl verification) succeeds, the verification METHOD — the brief format, the capacitor structure, the dispatch pattern, the 6-step verification loop — is validated. That validated method amplifies to Tier 1 (CCM verification) with confidence. The pilot doesn't just verify Boegli; it validates the architecture.

**Finding amplification.** If the CCM verification finds that Theorem 4.2 (self-adjointness of D_N) survives adversarial review, the self-adjointness result becomes AVAILABLE to other programmes as a verified external tool. Paper 26 (BSD) doesn't depend on CCM directly, but if a future BSD extension needs spectral operator methods, the verified CCM card is available in the cross-tier amplification log.

**Kill amplification.** If the Balaban verification finds a weakness in a specific kind of convergence argument, that weakness PROPAGATES as a warning to any other tier that uses convergence arguments. Kill K-1 from the H4 closure (CCM -> YM port is Wrong-space) was a kill that affected Tier 1 (CCM verification) — the verification Authors need to know that CCM's "perturbation" means rank-one operator perturbation, not QFT perturbation theory. Kills amplify across tiers because the same failure pattern can appear in different domains.

**Technique amplification.** If an excision (Tier B) in one tier produces an independent proof using a specific technique (say, Kato-Rellich perturbation theory instead of Caratheodory-Fejer), that technique becomes a CANDIDATE for excision in other tiers. The technique doesn't need to apply directly — the PATTERN might apply. "Replace a complex construction with a simpler perturbation-theoretic argument" is a technique pattern that could work for CCM (replace CF with KR), for Balaban (replace full RG with targeted convergence bounds), or for Boegli (replace generalized strong resolvent convergence with a direct KLMN bound).

The amplify phase is where the verification cascade becomes MORE THAN THE SUM OF ITS PARTS. Four independent verifications would produce four independent results. Four verifications with cross-tier amplification produce a NETWORK of results where each verification strengthens all the others.

## The connection to Agentic Context Engineering (ACE)

The dynamic capacitor's three-phase cycle maps directly to Microsoft Research's ACE framework (arXiv:2510.04618, presented at ICLR 2026):

> *"ACE treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation, and prevents collapse with structured, incremental updates that preserve detailed knowledge."*

| ACE concept | Dynamic capacitor equivalent |
|---|---|
| Evolving playbook | The capacitor file itself |
| Generation | Self-adjust: new cards from wave results |
| Reflection | Trim: honest downgrades, kill updates |
| Curation | Amplify: cross-tier transfer of successful methods |
| Structured incremental updates | One update per wave, version-numbered |
| Prevents collapse | Kill list prevents re-entry; honest downgrades prevent overclaiming |
| No labeled supervision needed | The capacitor learns from execution feedback (SURVIVED / WEAKENED / BROKEN verdicts) not from human labeling |

ACE reports +10.6% improvement on agent tasks and +8.6% on domain-specific reasoning when contexts evolve through this generate-reflect-curate cycle. The dynamic capacitor applies the same principle to mathematical research: the "context" is compiled mathematical knowledge, the "evolution" is wave-by-wave verification/excision/construction results, and the "curation" is the honest trim phase that removes or downgrades what doesn't hold up.

The key insight from ACE that validates the dynamic capacitor architecture: **evolving contexts outperform static contexts precisely because they incorporate execution feedback.** A static capacitor is a snapshot of knowledge at build time. A dynamic capacitor is a living knowledge base that improves with every wave. The improvement is not speculative — ACE measured it on agent tasks, and the ORA's own history (BSD projector discovery, PvNP retroactive corrections) demonstrates it on mathematical research.

## Versioning: the capacitor's audit trail

Every capacitor has a version number that increments after each phase update:

- **v1**: the generator's initial output (before any ORA run)
- **v2**: after the first verification run's findings are merged (self-adjust + trim)
- **v3**: after the second run, or after a Tier B excision's findings are merged
- **v4**: after a cross-tier amplification adds findings from another tier
- ...

The version number IS the audit trail. A referee looking at `tier1-ccm-capacitor-v4.md` can read the MERGE LOG at the bottom of the file and see:

```
| Date | Run | Cards added | Cards updated | Kills added | Escalations | Notes |
|---|---|---|---|---|---|---|
| 2026-04-14 | CCM-ver-wave-1 | 8 | 0 | 0 | 0 | Initial verification: 8 CCM steps tested |
| 2026-04-14 | CCM-ver-wave-2 | 2 | 3 | 1 | 1 | Thm 5.10 WEAKENED; escalated to Tier B |
| 2026-04-15 | CCM-exc-wave-1 | 1 | 1 | 0 | 0 | Independent re-derivation of Thm 5.10 |
| 2026-04-16 | Tier 4 amplify | 0 | 0 | 0 | 0 | Boegli method amplified; no CCM impact |
```

The MERGE LOG tells the story of the programme's learning. Each row is a wave. Each column is a kind of knowledge change. The sequence of rows shows how the capacitor grew — what was added, what was corrected, what was amplified. The log is the capacitor's MEMORY OF ITS OWN EVOLUTION.

---

*Self-adjust: absorb new findings immediately, in the cycle where they happen. Trim: honestly downgrade what doesn't hold up — the corrections ARE the credibility. Amplify: transfer successful methods and findings across tiers — four verifications become a network. Version the capacitor after every phase. The merge log is the audit trail. The dynamic capacitor learns from every wave. It never forgets a finding. It never hides a correction. It grows.*
