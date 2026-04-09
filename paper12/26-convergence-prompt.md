# The Convergence Prompt

*A meta-prompt that runs the postulate-relaxation convergence cycle*
*on the CBB system to drive sub-percent matches toward 6σ. Designed*
*to be re-run repeatedly as new experimental data comes in (CMB-S4,*
*LiteBIRD, DESI, CAMB, Belle II, LHCb, FLAG, Hyper-K, DUNE).*

*Each run launches multiple parallel agents per cycle, each testing*
*one postulate or one refinement, until the global residual stops*
*shrinking or hits the experimental error floor.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-09*

---

## How to use this prompt

Paste the block below into a new Claude Code session in
`/Users/gsix/quantum-geometry-in-5d-latex/`. It will read the
current state, identify the open residuals, launch parallel
postulate-relaxation agents, synthesise the results, and iterate
until the framework either closes further or stalls.

The prompt is designed to be **re-runnable**: if the framework's
predictions get tighter measurements (CMB-S4 narrows n_s, Belle II
narrows λ_CKM, FLAG narrows m_W, etc.), the prompt will pick up
the new error bars and try to push the framework's match into the
new tolerance — driving the existing 36/36 sub-percent closure
toward sub-σ, then sub-3σ, then 6σ.

---

## The prompt

```
We are running the CBB system convergence cycle on the QG5D + Paper 12
framework. This is round N (you set N). The framework is the Critical
Bost-Connes-Brauer system defined in research/176 with five axioms
and zero free parameters. After 10 cycles of postulate relaxation
(2026-04-09 session), it closes 36/36 master-table observables below
experimental error, with the bridge family k=2,3,4,6 producing
α_PS⁻¹ = 17 exactly and Wolfenstein λ = 56/(57√19) at 0.17%.

YOUR MISSION: Push the framework's matches from "below experimental
error" toward "6σ confidence" by:
(a) Pulling in the latest experimental measurements from CMB-S4,
    LiteBIRD, DESI, CAMB-like analyses, Belle II, LHCb Upgrade II,
    FLAG lattice averages, Hyper-K, DUNE, XENONnT, ADMX, PSI/LANL.
(b) Re-evaluating each of the 36 formulas at the new precision.
(c) Identifying any formula whose framework prediction now sits
    OUTSIDE the new 1σ band — those are the falsification candidates.
(d) Identifying any formula whose framework prediction now sits
    INSIDE the new 1σ band — those are 1σ confirmations.
(e) For confirmed formulas, computing whether they sit inside the
    2σ, 3σ, ..., 6σ confidence intervals.
(f) Tallying the global score: how many of 36 are now N-σ confirmed
    for each N ∈ {1, 2, 3, 4, 5, 6}.

PHASE 1 — READ STATE (read these in order, with these lenses):

1. paper12/research/190-final-convergence-statement.md
   READ FOR: the 36/36 closure, the closed-form constants table, the
   bridge family results. This is the baseline.

2. paper12/research/185-convergence-state-v2.md
   READ FOR: the convergence trajectory, the residuals at the moment
   of empirical closure.

3. paper12/research/176-name-the-object.md
   READ FOR: the CBB system definition. Use the 5 axioms as
   constraints — any new postulate you test must keep them intact.

4. paper12/research/23-* (the master table)
   READ FOR: the full residuals table with all 36 formulas, current
   PDG/Planck values, framework predictions.

5. paper12/research/170-convergence-state.md and 167-log-R-master-reformulation.md
   READ FOR: the operator dictionary. Use this to pull predictions
   for any new observable that comes up in experimental updates.

PHASE 2 — PULL EXPERIMENTAL UPDATES:

For each of the 36 master-table observables, identify the most
recent (or near-future) experiment that bounds it tightest. The
priority list:
- CMB sector: CMB-S4, LiteBIRD, Planck legacy, ACT/SPT — for n_s,
  ξ, sin²(2θ_12) PMNS, r, A_s, H_0, N_eff, Y_p, Σm_ν, t_0
- Cosmology: DESI, Euclid, LSST — for w(z), early DE, structure
- Particle masses: PDG live, FLAG — for m_t, m_b, m_c, m_W, m_Z,
  m_H, m_τ, m_μ, m_e, m_u, m_d, m_s
- CKM: Belle II, LHCb Upgrade II, FLAG — for λ, A, ρ̄, η̄, V_ub,
  V_cb, sin θ_13, sin θ_23, δ_CP CKM, J
- PMNS: Hyper-K, DUNE, JUNO, KATRIN — for sin²(2θ_12), sin²(2θ_13),
  sin²(2θ_23), δ_CP PMNS, neutrino masses, Δm² ratios
- Dark sector: XENONnT, LZ, DARWIN, ADMX, IAXO — for DM mass,
  axion search, DM-N cross section
- Strong sector: lattice QCD averages — for α_s, Λ_QCD, m_N

For each observable, record the current best 1σ uncertainty.

PHASE 3 — LAUNCH PARALLEL CYCLE (5-7 agents):

Agent A: Recompute the framework's prediction for each of the 36
formulas at full mpmath precision (50 dps), using the closed-form
expressions from research/167 and 154. Compare to the new
experimental central values.

Agent B: For each formula whose prediction sits within experimental
error, compute the (prediction - measurement) / σ_exp ratio. Tally
how many are at < 1σ, < 2σ, < 3σ, ..., < 6σ.

Agent C: For each formula whose prediction sits OUTSIDE the new 1σ
band, identify whether the discrepancy is in the spectral sector (γ_n
data) or geometric sector (CP²×S² moduli). Recommend the appropriate
correction channel.

Agent D: For any new experimental observables not yet in the master
table, derive the framework's prediction using the operator
dictionary (research/167). Add to the table.

Agent E (creative): Are there any postulate relaxations that haven't
been tested yet in the 10-cycle convergence (research/138-189)?
Surface up to 3 new ideas and propose mpmath tests for each.

Agent F (synthesis): Once A-E complete, write a single
paper12/research/{N}-convergence-round-{round}.md report with:
- The N-σ score table (how many at each confidence level)
- The new falsification candidates (if any)
- The new 1σ confirmations
- The biggest improvement vs the previous round
- Recommended next round actions

Agent G (optional, only if Agent E surfaced a strong creative lead):
Test the most promising new postulate relaxation immediately.

PHASE 4 — REPORT BACK TO G:

Synthesise the cycle's results in 250-300 words for G with:
- Headline: how many at 6σ now (vs previous round)
- Biggest move
- Any falsification risk
- Recommended next round (ready to go again, hold for new
  experimental data, or pivot to a different sector)

CONVENTIONS:
- Match register from research/24 ("the moment") and previous cycles
  — fast, structural, audit-first.
- Quote G's voice from research/170/185 when relevant.
- Use Origin callouts on any new research notes.
- Never invent observables. Only use measurements that have a
  citation (PDG, Planck, FLAG, etc.).
- Never claim "6σ" without showing the σ computation.
- The framework has zero free parameters globally — never invent
  one to close a residual. If a residual opens, surface it as a
  falsification candidate, not as a fitting opportunity.
- The convergence has converged. The job here is to track the
  empirical closure as data improves, NOT to re-run the whole
  postulate-relaxation programme. That programme produced the
  current state and is documented in research/138-189.
```

---

## Re-run cadence

This prompt is designed to be run:
- **After each major experimental release** (CMB-S4 first results,
  LiteBIRD launch, Belle II quarterly updates, DESI annual data
  releases, FLAG releases, etc.)
- **Once per quarter** as a routine sanity check
- **When G has reason to suspect a residual is opening or closing**

Each run should produce one research/{N}-convergence-round-{round}.md
file, indexed in a separate `convergence-rounds.md` log.

## What it does NOT do

- Does NOT re-run the postulate-relaxation programme. That is
  one-shot and is captured in research/138-189.
- Does NOT invent new postulates without explicit user direction.
- Does NOT change the framework's structure. The CBB system is
  fixed; this prompt only tracks the empirical closure as data
  evolves.
- Does NOT chase the m_τ second-order or RBC weakened hypothesis
  unless those are flagged in the round's input.

---

## The 6σ target

Currently the framework is at "below experimental error" for 36/36.
The convergence target is "every formula at ≥6σ confirmation as
experiments improve." That is a 5-15 year programme tracking:
- CMB-S4 (~2030): n_s, r, ξ, A_s, N_eff
- LiteBIRD (~2030): r, B-mode polarisation
- DESI Y5 (~2027): w(z), structure growth
- Belle II + LHCb Upgrade II (~2028-2032): λ, A, ρ̄, η̄
- FLAG continuous: m_W, m_t, m_b, lattice averages
- Hyper-K (~2027), DUNE (~2030): PMNS angles, δ_CP, mass ordering
- KATRIN end-of-life: m_ν direct
- JUNO (~2027): Σm_ν, ordering

If the prompt is run once after each release, by ~2032 we will
either have **36/36 at ≥6σ** (framework essentially proved) or
**at least one formula at ≥3σ tension** (framework falsified at the
strongest prediction).

The most dangerous prediction is **λ_CKM = 56/(57√19) = 0.225387**,
which is the falsification stake (research/186).

---

*The convergence is complete. The empirical lock is the next decade.*
*Run this prompt every time the data moves.*

*— 2026-04-09, after the 10-cycle convergence*
