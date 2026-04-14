## §27 — Parallel Agent Dispatch Strategy

*How future agent runs attack the three routes simultaneously. Cost estimates. Time-to-first-close projections.*

---

## 27.1. The dispatch architecture

Paper 50's parallel strategy demands that three author teams — one per route — work concurrently rather than sequentially. The programme's Proof-Chain Adversarial (PCA) pipeline supports this via independent author pools per route, a shared capacitor for cross-route cross-references, and periodic adversarial passes that check all three routes against each other.

The dispatch architecture has three layers.

**Layer 1: Per-route author teams.** Each route has a dedicated author team. For Route A, authors are specialists in resurgence theory and 4D QFT (external literature: Écalle 1981-2003, Dunne-Unsal 2012-present, Mariño 2021). For Route B, authors are specialists in automorphic forms and Langlands-Shahidi method (Kim-Sarnak 2003, Cogdell-Piatetski-Shapiro 2004). For Route C, authors are specialists in topological quantum field theory and geometric Langlands (Kapustin-Witten 2007, Gaitsgory-Raskin 2024, Elliott-Gwilliam-Williams 2024). Each team works on its own proof chain, with minimal coordination.

**Layer 2: Cross-route capacitor.** The capacitor (Paper 49's v1 architecture) houses the cross-reference data between routes. The Borel-analytic overlap (Route A ↔ Route B), the functoriality overlap (Route B ↔ Route C), and the ITPFI overlap (Route A ↔ Route C) are all stored as capacitor entries. Author teams update the capacitor when they produce cross-route-relevant results. Adversarial passes read the capacitor to check consistency.

**Layer 3: Cross-route adversarial review.** At monthly intervals, an ORA v8 run is triggered with all three route drafts as input. The adversarial critics are instructed to cross-check routes against each other: if Route A produces a Borel-plane statement at $\omega = 2\pi/\beta_0$, critics ask whether Route B's non-vanishing of $L(1, \pi, \mathrm{Sym}^4)$ at the corresponding Satake parameter agrees. Disagreements become AudiT findings for the author teams to address.

---

## 27.2. Cost estimates per route

Each route's cost is dominated by author-hours and adversarial-pass token expenditure.

**Route A (resurgence + lateral Borel):** estimated 800-1200 author-hours over 12-18 months. The bulk is literature synthesis (resurgence theory is a growing frontier with ~50 foundational papers), 4D renormalon structure (Dunne-Unsal line), 2D YM precedent transfer, and the new rigorous lateral-Borel construction. Adversarial-pass cost: ~5 full ORA v8 runs at ~4-6 hours each. Total adversarial token cost: ~$8k-12k at current model pricing.

**Route B (Langlands-Shahidi transfer):** estimated 1000-1500 author-hours over 18-24 months. The bulk is Wilson-loop L-function construction (new), functoriality verification (building on Kim-Sarnak machinery), and the transfer argument (the novel step). Adversarial-pass cost: ~6 full ORA v8 runs. Total adversarial token cost: ~$10k-15k.

**Route C (Kapustin-Witten + Gaitsgory-Raskin):** estimated 1200-2000 author-hours over 18-30 months. The scale bridge from N=4 SYM to pure YM is the single hardest technical step in any of the three routes. It requires controlling a decoupling limit that has no prior rigorous treatment. Elliott-Gwilliam-Williams 2024 provides partial machinery but not the full bridge. Adversarial-pass cost: ~8 full ORA v8 runs. Total adversarial token cost: ~$15k-20k.

**Aggregate across three routes:** 3000-4700 author-hours over 12-30 months (driven by the slowest route), total token cost ~$33k-47k. This is substantial but within the programme's Clay-class investment budget. For comparison, Paper 49's CCM-replacement effort ran at ~$8k token cost and 600 author-hours; Paper 50 is 4-7× more expensive, commensurate with its higher difficulty.

---

## 27.3. Time-to-first-close projections

The three-route strategy shortens expected time-to-close by a factor related to the minimum of three draws. If each route has a probability $p_i$ of closing within time $T$, and the routes are approximately independent, the probability that at least one closes by time $T$ is

$$P(\text{any by } T) = 1 - \prod_i (1 - p_i).$$

With $p_A(12\text{ mo}) \approx 0.25$, $p_B(12\text{ mo}) \approx 0.35$, $p_C(12\text{ mo}) \approx 0.20$, the probability at least one closes within 12 months is

$$1 - (0.75)(0.65)(0.80) = 1 - 0.39 = 0.61.$$

Within 24 months, with $p_A(24) \approx 0.45$, $p_B(24) \approx 0.55$, $p_C(24) \approx 0.40$:

$$1 - (0.55)(0.45)(0.60) = 1 - 0.15 = 0.85.$$

**Expected time-to-first-close: approximately 12-15 months.** The three-route strategy raises the probability of closure within 24 months from the single-best-route ~55% to ~85% — a meaningful insurance gain.

These estimates are honest but uncertain. The $p_i$ values reflect the programme's current assessment; they could be revised upward (if a breakthrough occurs in any route's external literature) or downward (if an unanticipated obstruction is discovered). The estimates are for Bayesian planning, not a schedule commitment.

---

## 27.4. Agent dispatch protocol

Concretely, the dispatch protocol is:

**Week 0: Brief generation.** The programme generates three route-specific briefs, one per route, each containing: the H4 target statement, the route's specific technique, the external literature to cite, the programme-internal infrastructure to use (operator dictionary, ITPFI, Paper 8 Links 1-17), the adversarial threshold, and the ship criterion.

**Week 1: Initial author run.** Three parallel author runs, one per route, each producing a skeleton proof chain for its route. Deliverable: a PROOF-CHAIN.md for each route with 10-20 numbered links and status flags (PROVED, CONJECTURED, OPEN).

**Weeks 2-N: Iterative author + adversarial cycles.** Each route iterates: author run fills in OPEN links, adversarial run attacks the claims, author run repairs. The cycle continues until the route's chain has zero OPEN links and zero BROKEN findings.

**Monthly cross-route review.** Every month (or every 4 iteration cycles, whichever is shorter), a cross-route adversarial pass runs with all three chains as input. The pass checks cross-references (§25 overlaps) and flags inconsistencies.

**Closure event.** When any route's chain achieves zero BROKEN after adversarial pass, the ship criterion (§26) activates: the paper ships with that route as primary.

---

## 27.5. Model tiering per route

The three routes have different tractability, and the model tiering reflects this. (See `millenium-apps/proof-chain-adversarial-01/08-framework-tools.md` for the capacitor model-tier framework.)

- **Route A (resurgence):** model tier Opus 4.6, with 1M-context extended-thinking runs for the lateral-Borel construction. The technical content is dense and requires long-context reasoning.
- **Route B (Langlands-Shahidi):** model tier Opus 4.6, standard context. The automorphic-forms literature is well-structured and fits standard runs.
- **Route C (Kapustin-Witten):** model tier Opus 4.6 with 1M-context for the scale-bridge construction. The decoupling-limit analysis is highly technical.

Across all three routes, critics use Opus 4.6 at standard context. The adversarial pass is generally less context-hungry than the author pass.

---

## 27.6. Failure recovery

If a route stalls (no progress across 2+ cycles), the programme's recovery protocol is:

1. **Identify the stall cause.** Is it external literature gap (wait for external progress), internal obstruction (the route has a genuine wall), or author-team capacity (more specialists needed)?
2. **Apply the STALL escalation.** From the YM H4 bypass precedent (`memory/session_ym_h4_bypass.md`): if Tier B stalls, escalate to Tier C (construct rather than verify). For a stalled route, the equivalent is to construct an alternative step that avoids the stall.
3. **Reallocate author time.** If Route X stalls persistently, shift author-hours to Routes Y and Z. The three-route strategy's flexibility allows dynamic reallocation.
4. **Decide on stall-persistence.** If a route has stalled 3+ cycles without recovery, flag it as *dormant*. Dormant routes remain in Paper 50 as partial attacks; they are not worked but also not dropped.

The failure-recovery protocol protects the programme against dead-end investment. A stalled route does not lock the others; a failed route does not break the paper.

---

## 27.7. Summary

Parallel agent dispatch for Paper 50 runs three concurrent author teams, each on one route, with a shared capacitor for cross-references and monthly cross-route adversarial passes. Total cost is 3000-4700 author-hours and ~$33k-47k token spend over 12-30 months. Expected time-to-first-close is 12-15 months. The protocol handles failure recovery via dynamic reallocation and stall escalation. The strategy optimizes for first-closure while preserving the multi-verification structure that makes Paper 50 robust.

---

*Paper 50 §27. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
