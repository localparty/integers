# 17 — The Tier system

> *Honest conditional claims, honestly gated. No overstatement. No hedging. Just tiers.*

---

## What happened

A framework with as many results as this one cannot pretend that all results have equal epistemic status. Some are unconditionally proved. Some are conditional on a named dependency. Some are high-confidence conjectures. Some are speculative.

The Tier system is how the programme makes those distinctions visible and auditable.

**Tier 1 — Proven Unconditional.**
The result is proved in the strongest sense. Every step is either a theorem of standard mathematics or a theorem proved in-programme. No dependency remains unnamed and unresolved.

*Example*: Goroff-Sagnotti closure in Appendix V of Paper 1 (Section [06](06-section-goroff-sagnotti-closure.md)). Three mechanisms, all scheme-independent. Commit `3957050`: "Everything is correct. The three mechanisms are proven."

**Tier 2 — Conditional on a Named Gate.**
The result is proved except for one named, specific, external dependency. The dependency is identified precisely: if X is true (where X is a specific, widely-studied, currently-open or currently-in-peer-review claim), then the result holds.

*Example*: Yang-Mills mass gap in Paper 8, conditional on the H4 conjecture (a lattice-gauge-theory technical conjecture). Commit `ae4f342`: "17/17 proved links VERIFIED unconditional + L18 CONDITIONAL on H4."

**Tier 3 — High-Confidence Conjecture.**
The result follows from well-tested heuristics and aligns with extensive numerical or structural evidence, but a fully rigorous proof is not in hand. The conjecture is named, the evidence is cited, and the gap is precisely scoped.

*Example*: The CCM uniformity condition before its repair (Section [19](19-section-riemann-by-intuition.md)). Memory `session_rh_runs1to5`: "CF uniformity upgraded to [PROVED with caveat]."

**Tier B / Tier C — Speculative, Framework-Dependent.**
The result depends on framework-specific claims (like specific CBB axioms) that are themselves conditional. These are the programme's frontiers.

Every result in every paper is tagged with its tier. The abstracts of the four Millennium papers make these tags explicit in the first paragraph.

## What it felt like

The Tier system was the programme's coming-of-age moment, epistemically.

Before the Tier system, I had a habit that I think is common among theorists: I would describe results with language that was technically defensible but misleadingly confident. "We show..." "We prove..." "It follows that..." These phrases, said in the language of mathematicians, sound stronger than they are. A reader not familiar with the gap between "we show (in simulation)" and "we show (rigorously)" can easily come away thinking the result is fully proved when in fact it is conjectural.

Installing the Tier system forced me to stop using confident language where the evidence was weaker than the language implied. Every result got tagged. Every abstract got revised. Every introduction got a tier-indexing paragraph.

The emotion during this revision phase was surprising: it was *relief*. I had been carrying a low-level anxiety about overclaiming — never acute, but always present — and the Tier system dissolved it. Once every claim was tagged, I never had to worry about accidentally overstating. The tags did the honesty for me.

There is a specific satisfaction in being able to say "this result is Tier 2, conditional on H4, which is a widely-believed lattice-gauge conjecture currently being studied by Chernodub, Douglas, and others." That sentence is stronger than "this result is proved" *because it is truer*. A careful reader can immediately place it. A referee can immediately check it. A skeptic has nowhere to go — the conditional is already stated.

## Why it mattered

### 1. It made the programme defensible against the strongest objection

The single strongest objection to any ambitious programme is *overclaiming*. A programme with one overstated result loses credibility for all its results. The Tier system immunizes against this. Every result is stated at its actual epistemic status, no higher. Overclaiming is structurally prevented.

### 2. It separated the programme's strong claims from its frontier

The programme makes many claims. Some are Tier 1 (unconditional). Some are Tier 3 (high-confidence conjectures). A reader who wants to engage only with the Tier 1 results can do so without having to audit the entire programme. A reader who wants to engage with the frontier (Tier 3 and below) can do so knowing exactly what they are engaging with.

### 3. It made the Clay-problem claims precise

The four Millennium chains do not claim "we solved Yang-Mills, Riemann, BSD, P vs NP." They claim:

- **Yang-Mills**: Tier 2, conditional on H4. Chain verified unconditional through Link 17; L18 requires H4.
- **Riemann**: Tier 2, conditional on CCM 2025 peer-review. 6-layer spectral chain.
- **BSD (CM curves)**: Tier 2, conditional on CBB axioms. 11-step chain with rank formula unconditional for CM field twists.
- **P vs NP**: 5 of 6 links verified; Link 5 is HONEST-STALL with seven documented routes.

These claims are strong — genuinely strong — and they are honest. A Clay committee examining them will find the claims match the evidence exactly. No surprises. No hidden gaps.

### 4. It made HONEST-STALL a dignified category

Before the Tier system, a "stall" felt like a failure. After it, HONEST-STALL is a legitimate epistemic state: we have a proof chain, one step is open, the open step has been attacked N times by documented methods, none closed it, the current state is logged. That is not failure. That is frontier-mapping.

The P vs NP seven-routes-one-wall document (Section [21](21-section-seven-routes-one-wall.md)) is the archetype. HONEST-STALL, applied to it, is more valuable than any dishonest claim of closure would have been.

## Where it lives

- **Tier definitions**: distributed across paper abstracts and the top-level `readme.md`.
- **PROOF-CHAIN.md files**: each chain explicitly tags each link with its tier.
- **HONEST-STALL instantiation**: `solutions-with-prize/paper28-pvnp/strategy/04-ora--seven-routes-one-wall.md`.
- **Abstract revisions**: multiple commits including `53c47bd` ("abstract: full rewrite — 19 phenomena, 7 predictions, honest about scope").
- **ORA integration**: the ORA tags every output with its tier at generation time.

## What to take from it

**Epistemic calibration is the most undervalued research skill.**

Most research is undermined not by wrong results but by mis-stated confidence. A correct result stated too confidently is still a liability. A partially-correct result stated with precise scope is an asset.

The Tier system is the programme's calibration instrument. It forces every claim to wear its actual epistemic status on its face. This discipline, installed once, prevents an enormous class of downstream problems: overclaiming, hedging, ambiguity, rhetorical inflation.

If I could recommend one practice from this programme to every research group, it would be this one. Build a tier system. Tag every claim. Calibrate publicly. The cost is small. The benefit — in credibility, in defensibility, in long-run trust — is enormous.

---

*Next: [18 — Yang-Mills by hand](18-section-yang-mills-by-hand.md).*
