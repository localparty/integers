# Research Note 197 — Round 2 / Agent E (log-only ideas)

*Sub-agent note spawned by research/193 (convergence round 2).*
*Date:* 2026-04-09.
*Mode:* **log-only** per patched prompt §Phase 3 Agent E. No new
postulate is tested; none of the CBB system's 5 axioms is touched.

## Three ideas for future cycles

1. **Upgrade Σm_ν from one-sided bound to posterior band.**
   DESI Y3 + Planck NPIPE will produce a joint likelihood that
   replaces the <0.12 eV upper bound with a proper posterior. At
   that point the framework's prediction (from research/108) needs
   a likelihood-ratio test, not a Gaussian σ. Pre-write the
   conversion formula so round N can drop it in.

2. **Split 1/α_3(M_Z) σ_exp into world-average vs lattice-only.**
   Round 2 used the PDG24 world-average σ = 0.038. FLAG22's
   lattice-only σ is closer to 0.010. If the FLAG24 release tightens
   further, the framework's raw 8.43049 could move from <2σ to >3σ
   tension. Worth carrying both σ bands in `sigma-exp-table.md` and
   letting Agent B report both.

3. **Pre-register the λ_CKM = 56/(57√19) falsification stake.**
   Research/186 names this as the most dangerous prediction. A
   standalone note that carries the current Belle II + LHCb
   uncertainty trajectory and the σ projection for 2028–2032 would
   let each round drop it straight into the tally with a
   "falsification watch" label.

## Axiom check

None of these violate the 5 CBB axioms. All three are data-layer
refinements (σ_exp bookkeeping, likelihood treatment, pre-registered
tracking) — not structure-layer changes. No flag to G; no Agent G
spawn.

## Status

Logged. Not tested. Available for G to pick up as standalone
research notes if desired.
