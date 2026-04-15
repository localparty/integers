# Research Note 207 — Convergence Round 4, Agent E (creative log)

*Log-only. No postulates tested. CBB 5 axioms untouched.*

## Round-4 ideas (2, none trigger Agent G)

1. **Escalation-rule generalisation.** The rule now fires once, for
   m_Z and v. But the only other row likely to stale for ≥3 rounds
   is ξ (1.4σ, but `raw`, not `raw+stale`). Worth codifying what
   distinguishes `raw+stale` from `raw` precisely enough that no
   future row accidentally enters the gap bucket. Proposal for a
   future prompt revision: `raw+stale` is defined as `|σ| > 3σ_exp
   AND correction channel is known`. Leave for G.

2. **laurent-shifted preview computation.** Even without porting
   (a, b) into research/23, round 5 could do a *preview*: compute
   the shifted m_Z and v with (a, b) in Agent A and report them
   alongside the raw tally, without modifying research/23. This
   would de-risk the port by showing whether the shift closes both
   rows to <1σ or leaves one residual. Adds ~10 minutes to Agent A.
   Not urgent; flagging for G.

## Not triggered

No finding this round demands a new postulate test. Agent G stays
dormant. The framework remains fixed at 5 axioms.
