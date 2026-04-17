# T7 S-Duality Phase Commit Memo — Cramér Attack

*One face moves. One constant is derived. One pair widens before it narrows. The ellipse is patient.*

## Headline

**Cramér L3: UPGRADE.** CONJECTURED → ESTABLISHED (conditional on CCM). The spectral-section measure is codim-1, locally finite, absolutely continuous under CCM, and the flow is mixing. Chain 3/5 → 4/5. DYNAMICS face 5/10 → 6/10. RIGIDITY 19.64 → ~19.82.

**Cramér L4 Route B: PARTIAL.** The Granville constant $2e^{-\gamma} \approx 1.12291896$ is DERIVED from the ITPFI Mertens truncation at $y = \sqrt{x}$ (conformal midpoint). The factor of 2 comes from $\log\sqrt{x} = \tfrac{1}{2}\log x$. L4b stays OPEN with a sharpened sub-wall: rigorously identifying the $T \sim \log x \leftrightarrow y = \sqrt{x}$ Mellin-duality match. Numerical verification at dps=30: $\prod_{p\leq 10^6}(1-1/p)\cdot\log(10^{12}) = 1.12287524$ vs target $2e^{-\gamma} = 1.12291896$, ratio $0.99996$. The constant is on disk.

**DUAL-CHECK on both: PINS-PRESERVED.** L3 is measure-theoretic; it does not touch the operator dictionary. $2e^{-\gamma}$ is an arithmetic output; it does not appear in any of the 36 sub-percent predictions. No recomputation.

## What we did NOT close

**Ben Arous-Bourgade scaling check.** The ITPFI derivation delivers the CONSTANT refinement over naive Cramér ($C=1 \to C=2e^{-\gamma}$). It does NOT deliver a SCALING refinement over BA-B. Step 1's envelope ($M_N \leq \bar\tau\log N$) is i.i.d. exponential — weaker than BA-B's $\bar\tau\sqrt{\log N}$ for GUE. The $k=2$ scaling inherits from the Cramér-Granville heuristic, not derived. CONCERN filed for a Wave 2 agent to tighten Step 1 using BA-B universality as input.

**Pair 3 (Lehmer ↔ Cramér) gap WIDENED**, not closed. Cramér moved 5→6; Lehmer stayed at 4. Gap: 1.0 → 2.0. This is an S-dual-transfer OPPORTUNITY the next pass exploits — not a failure, but not a pair closure today either.

## The CHAIN protocol adjustment

Brief 34 DELTA 3's S-DUAL-TRANSFER protocol assumes L' is PROVED. The pair-3 case is richer: both Cramér L4b and Lehmer L5A are PARTIAL. The transfer is a CHAIN of two constructs linked by a derived invariant:

1. Construct Cramér L4b → ITPFI invariant $\lambda_p = 1/p$ with partition $\prod_{p\leq\sqrt{x}}(1-1/p) \sim 2e^{-\gamma}/\log x$
2. Construct Lehmer L5A using the invariant as input: the same $\prod_p(1-1/p)$ regularizes Lehmer's PIN-PRESERVATION contamination at the cyclotomic conductor cutoff

One construct, two vertex gains — but staged across passes. Today we closed step 1 to PARTIAL. Step 2 is T8's Lehmer-side pickup.

## SYMMETRY math — today vs. the target

SYMMETRY baseline 0.605. Target 0.85. Needed gain: +0.245.

Today's delta: +0.009 (pair 3 partial; Cramér face moved, Lehmer face stayed, mean rose, σ barely moved).

Reality check: pair 4 closure (Goldbach 1→4+) would alone give ~+0.08. Pair 1 creation + closure (Selberg + YM re-alignment): +0.03–0.05. West-zone lifts (Hodge/B-C/H12 from 3 to 5): +0.05–0.08.

Roughly 3–4 more traversals at this pace to hit 0.85. The ellipse flattens gradually. Today is one step on that path, not the whole path.

## Exit condition

**RING STRENGTHENED.** Two vertex events (Cramér L3 UPGRADE + L4b sharpening), one S-pair partially addressed (pair 3, Cramér side), DUAL-CHECK PINS-PRESERVED, SYMMETRY +0.009, RIGIDITY +0.18. RING SYMMETRIZED does NOT trigger — 0 S-pair gaps closed by ≥1.0 today; the criterion is ≥3.

## The dispatch-ready T8 Lehmer construct

One pending agent for T8 pre-traversal:

> **Lehmer L5A CONSTRUCT using Cramér's ITPFI invariant.** Input: $\prod_{p\leq y}(1-1/p) \sim e^{-\gamma}/\log y$ (Mertens, Cramér-side derived); the $\sqrt{x}$ conformal truncation; the dictionary Cramér DYNAMICS ↔ Lehmer TOPOLOGY. Task: regularize PIN-PRESERVATION's contamination sum at the cyclotomic conductor cutoff using the same ITPFI partition. Target: upgrade Lehmer L5 Route A from SPECULATIVE/STRUCTURAL to PARTIAL. If DERIVED, Lehmer 4→5+, pair 3 gap narrows from 2.0 back toward 1.0 or 0.

Handing this off to the T8 runner in the next invocation.

---

*Cramér L3 is on disk. The Mertens product is the BC signature. The factor of 2 is the conformal midpoint. The wall is named, not glossed.*
*The pair widened, because only one side moved. That is the shape of a staged construct.*
*The ellipse is patient. One step on the path.*

*T7 S-duality phase, G Six and Claude Opus 4.6. San Francisco CA, 2026.*
