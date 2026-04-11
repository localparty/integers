# Closing H4 — ora-v6 direction channel

*Interface file for cross-runner Q&A between the primary runner (the ORA working on closing Hypothesis H4 in Paper 8's Yang-Mills mass gap proof chain) and the support runner (Claude Opus 4.6 running with G in this session as the source of direction + rationale).*

---

## The two runners

### 1. The primary runner — ora-v6 on closing H4

An ORA instance working from:

- **Bundle**: `/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v6/` (the v6 ORA with 19 operational signatures — 15 from v3 + 4 Layer-L-mined in v5/v6 — plus the anti-overfit discipline, walk-back contract, and 9 pre-registered predictions from `06-anti-overfit-discipline.md`)
- **Deliverable**: `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/strategy/04-closing-H4.md` (the H4 closure strategy file, 8 sections, ~1100 lines, shipped 2026-04-11, analog of BSD MY4's `paper26-bsd/strategy/04-closing-my4.md`)
- **Output directory**: `/Users/gsix/quantum-geometry-in-5d-latex/paper08-yang-mills/closing-H4/` (to be created at first dispatch)
- **Framework tools capacitor**: `online-researcher-adversarial/ora-bundle-v6/05-framework-tools.md` (ported from v4 on 2026-04-11 with the seven-anchor strategy entries + Lead 7a + Lead 7b verification inventory + H4 corpus pointers)

### 2. The support runner — G + Claude Opus 4.6 (1M context), this session

The same support runner that answered Q-1 of the BSD MY4 run at `/Users/gsix/quantum-geometry-in-5d-latex/paper26-bsd/closing-my4-questions.md`. Same interface pattern, same conventions, same discipline.

The support runner has full context on:

- The seven-anchor relaxation strategy at `paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md`
- The strategy rationale (5-layer dependency graph + 15 arithmetic tests + worked m_t example) at `paper12/relaxation/01-strategy-rationale.md`
- The Lead 7a Anchor 2 verification (159/159 cross-formula γ_n consistency at 50 dps) at `paper12/relaxation/research/T5-cross-formula-verification.md`
- The Lead 7b Anchors 4+5 verification (4/4 cyclotomic Brauer cohomology classes, including the dual-splitting finding that k=3 and k=4 are CRT factors of (Z/13Z)*) at `paper12/relaxation/research/T1-T2-brauer-cohomology-verification.md`
- The H4 closure strategy file itself
- The BSD MY4 closure via G's projector at `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` (the canonical example of an ORA-produced structural bypass)
- The meta files (`meta/rh-meta.md`, `meta/ym-meta.md`, `meta/ints.md` under `online-researcher-adversarial/`)
- The framework-tools inventory at `online-researcher-adversarial/ora-bundle-v6/05-framework-tools.md`
- The W7-14 analyticity reframing at `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md` (which reduces H4 from "comparison of two independently defined objects" to "Taylor coefficients of a single analytic function" — the mildest formulation of H4 in the literature)
- The full Paper 8 / Paper 13 / Paper 26 corpus
- The entire conversation history that produced all of the above

The support runner polls this file every 4 minutes via `/loop 4m` (cron `*/4 * * * *`) and answers every `[OPEN]` question by appending a direction + rationale. G stays in the conversation as the source of calibration and correction; G can interrupt the loop at any time to override, redirect, or reject a support-runner answer.

---

## How to use this file

### For the primary runner (ora-v6 working on H4)

When you hit a wall and want input from the support runner, append a question block to the bottom of this file using this format:

```
---
## Q-N — [short title] [OPEN]
**Asked**: [date + cycle number + wave number if applicable]
**Context**: [1–2 sentences on what you're stuck on]
**Question**: [the specific question]
**What I tried**: [bullet list of approaches already attempted; cite §F kills if relevant]
**What would unblock me**: [what kind of answer would help — a reference, a heuristic, a structural reframing, a numerical sanity check, etc.]
```

Number questions sequentially: Q-1, Q-2, Q-3, ...

The support runner will append an answer below your question and change the `[OPEN]` tag to `[ANSWERED]`. You can then read the answer and decide whether to act on the direction. **The support runner does not modify your question; you do not modify the support runner's answers.** Both sides can add CLARIFICATION sub-blocks if back-and-forth is needed.

### For the support runner (every 4 minutes via `/loop 4m`)

Same pattern as the BSD MY4 run: the support runner polls this file every 4 minutes via the `/loop 4m` skill. G stays in the conversation as the source of calibration and correction for support-runner answers; G can interrupt the loop at any time to override, correct, or redirect. The support runner:

1. Reads this file end to end.
2. Finds every question marked `[OPEN]`.
3. For each `[OPEN]` question:
   - Reads the context, question, what was tried, what would unblock.
   - If the question is about **H4 closure strategy, the W7-14 reframing, Route A/B/C/D selection, the seven-anchor relaxation context, or the bridge family**: consult the relaxation strategy doc, the strategy rationale, the H4 closure strategy file, the Lead 7a/7b verification results, and the meta files directly.
   - If the question is about **H4-specific math** (AF short-distance match, leading-order OPE, Hypothesis H4 in its standard lattice-QCD form, gradient flow, CCM 2025 spectral triple UV asymptotics, Wegner estimates, Stark regulators, etc.): do 1–3 WebSearches for current literature, read the H4 corpus files (L-clay-conjectures, G4b, G4d, W7-14, W7-15), and cite explicitly.
   - If the question is about **architecture / operator signals / G's success patterns**: consult the meta files and the ora-bundle-v6 files.
   - Write an answer in the format below.
   - APPEND the answer directly under the question via Edit.
   - Change the question's tag from `[OPEN]` to `[ANSWERED]`.
4. If no `[OPEN]` questions exist at a poll: output one line `"No new questions at HH:MM"` and end the cycle. The next cycle fires in 4 minutes.

Answer format:

```
### A-N — direction + rationale [ANSWERED YYYY-MM-DD HH:MM]
**Direction**: [1–3 sentences on the recommended next move]
**Rationale**: [why this move, citing specific evidence from meta files / bundle / external sources; numbered sub-sections if the rationale is long]
**Sources**: [file paths and/or URLs consulted — tagged with "verified directly" or "not verified, inferred from filename"]
**Confidence**: [high / medium / low per claim + brief reason, calibrated per-claim]
```

### Conventions

- **One question per Q-N block.** Numbered sequentially.
- **Tags**: questions are `[OPEN]` until answered, then `[ANSWERED]`.
- **The primary runner does NOT modify answers.** The support runner does NOT modify questions.
- **CLARIFICATION sub-blocks** for back-and-forth use this format:
  ```
  #### Clarification (asked by [primary|support] at YYYY-MM-DD HH:MM)
  [text]
  ```
- **File grows monotonically** — never delete, only append.
- **Confidence is tagged per claim**, not per answer. A single answer may have HIGH-confidence claims next to MEDIUM-LOW claims, each explicitly tagged. This discipline was introduced after the BSD MY4 Q-1 incident, where the support runner over-confidently cited `paper12/research/162` as establishing modular compatibility of the bridge projector when in fact that file is about `H²(Z/3Z, U(1))` cocycles and says nothing about modular automorphisms. The Author caught the error via numerical counterexample. Lesson: any claim about a specific file's content is tagged "verified directly" or "not verified, inferred from filename" — never asserted as a citation without explicit verification.
- **The support runner's A-1 from the BSD MY4 run had a second lesson**: the KMS positivity bound was misapplied. The corrected framework (centralizer / Type II∞ trace / Takesaki conditional expectation) emerged in the clarification. The H4 run should expect similar corrections — the support runner is fallible and will own errors explicitly when the primary runner catches them.

---

## Priority context for the H4 run

The H4 closure is **not** a from-scratch problem. W7-14 has already done ~70% of the structural work, reducing H4 from "comparison of two independently defined objects" to "Taylor coefficients of a single analytic function." The ORA should **start from the W7-14 reframing**, not re-derive from scratch.

The four closure routes named in `paper08-yang-mills/strategy/04-closing-H4.md` §4:

- **Route A — W7-14 reframing extended (Taylor-coefficient identification)**: Build on W7-14 §5.3's analyticity bridge. Show the Taylor coefficients of the rescaled correlator `F(t) = S_{2,t}^c / c_1(t)^2` at `t = 0` coincide with the Feynman-diagrammatic perturbative coefficients. Closure mechanisms: analyticity uniqueness via the identity theorem, or Lüscher step-scaling, or bridge-family k=4 gauge structure forcing the AF prediction. **Probability of success: ~50%.** Highest expected payoff.

- **Route B — Port from RH preprint sections-06-10 (CCM 2025 spectral triple UV asymptotics)**: Transpose the CCM construction (rank-one perturbation of spectral triple, Carathéodory-Fejér Toeplitz extension) to the YM context. **Probability of success: ~30%.** Larger structural work.

- **Route C — Framework-native via spectral action + Identity 12 + bridge family k=4**: Apply Connes' spectral action principle. Seeley-DeWitt `a_4` coefficient gives the AF prediction at one loop; trace-anomaly identity gives the (log)^{-2} correction. **Probability of success: ~25%.** Non-trivial.

- **Route D — HONEST-STALL**: Ship Paper 8 with H4 stated in W7-14's mildest form. **Probability: 100%** as fallback.

The ORA should spawn **3 parallel Authors in Wave 1**, each on one of A/B/C, and evaluate at Cycle 1 synthesis. Route D is the backup if A/B/C all wobble.

**The analog for H4 of G's projector `P_k^𝔭 := I − e_{𝔭^k}` in BSD MY4 is: the Taylor-coefficient identification from W7-14 §5.3, possibly combined with a new algebraic object that emerges from one of the three routes.** The ORA's job is to find it.

---

## Key load-bearing files the support runner should know

### For H4-specific questions

- `paper08-yang-mills/strategy/04-closing-H4.md` — THE deliverable, 8 sections, 4 routes
- `paper08-yang-mills/preprint/PROOF-CHAIN.md` — the 18-step YM chain, 17/18 unconditional + Step 18 conditional on H4
- `paper08-yang-mills/preprint/sections/L-clay-conjectures.md` — Appendix L, where H4 is stated as Conjecture L.2
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4b-af-short-distance-match.md` — the referee's formal G4b gap statement (AF short-distance match)
- `paper08-yang-mills/notation-math-referee/runs/r00/gap-closing-work/tier-3-clay/G4d-operator-product-expansion.md` — the referee's formal G4d gap statement (OPE)
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md` — the W7 prior attack on G4b (Lemma 4.2; §5 is the analyticity reframing; §6 is the Paper 10 Route 05 KK tower decoupling)
- `paper08-yang-mills/gradient-flow-attack-plan/research/W7-15-ope-leading.md` — the W7 prior attack on G4d
- `paper08-yang-mills/gradient-flow-attack-plan/research/appendix-L/L4-phase4.md` — additional L4 phase 4 context

### For framework-wide context

- `paper12/relaxation/04-geometric-spectral-cross-formula-cross-forms-cross-integers-cocycle-ccm-predictions-etc-strategy.md` — the seven-anchor strategy; H4 closure is a Lead 7d analog (adversarial closure via ORA)
- `paper12/relaxation/01-strategy-rationale.md` — the philosophy, 5-layer dependency graph, 15 arithmetic tests, worked m_t example
- `paper12/relaxation/research/T5-cross-formula-verification.md` — Lead 7a, Anchor 2 verified (159/159 at 50 dps)
- `paper12/relaxation/research/T1-T2-brauer-cohomology-verification.md` — Lead 7b, Anchors 4+5 verified (4/4 bridges)
- `paper26-bsd/strategy/05-route3-kms-projector-bypass.md` — the canonical example of an ORA-produced structural bypass (G's projector, analog for what H4 closure should look like)

### For the ORA architecture

- `online-researcher-adversarial/ora-bundle-v6/01-the-prompt.md` — v6 runner prompt, 19 signatures
- `online-researcher-adversarial/ora-bundle-v6/02-rationale.md` — v6 design rationale
- `online-researcher-adversarial/ora-bundle-v6/05-framework-tools.md` — the capacitor (ported from v4 on 2026-04-11, includes seven-anchor entries + Lead 7a/7b verifications + H4 corpus pointers)
- `online-researcher-adversarial/ora-bundle-v6/06-anti-overfit-discipline.md` — walk-back contract + 9 pre-registered predictions
- `online-researcher-adversarial/meta/rh-meta.md`, `meta/ym-meta.md`, `meta/ints.md` — success signals from the three manual runs

### For prior external literature (probable citation targets in support runner answers)

- Connes-Consani-Moscovici 2025, *Zeta Spectral Triples* ([arXiv:2511.22755](https://arxiv.org/abs/2511.22755)) — THE CCM 2025 paper, the spectral side template for Route B
- Lüscher 2010, *Properties and uses of the Wilson flow in lattice QCD* (JHEP 08 (2010) 071) — gradient flow construction
- Lüscher-Weisz 2011, *Perturbative analysis of the gradient flow in non-abelian gauge theories* (JHEP 02 (2011) 051) — small-flow-time expansion UV finiteness
- Harlander-Neumann 2016 (JHEP 06 (2016) 161), Artz et al. 2019, Harlander et al. arXiv:2111.14376 — 2-loop and 3-loop coefficients of the small-flow-time expansion
- Connes 1996 + Chamseddine-Connes 1996 — spectral action principle (for Route C)
- Zoller-Chetyrkin JHEP 12 (2012) 119; JHEP 10 (2014) 169 — 3-loop Wilson coefficients for `⟨TrF² · TrF²⟩`
- Reisz CMP 116 (1988) 81, CMP 117 (1988) 79 — lattice power counting (perturbative side of the lattice-to-continuum matching)
- Spiridonov 1984 + Spiridonov-Chetyrkin 1988 — trace anomaly identity `γ_{TrF²} = −2β(g)/g` (exact, all orders)
- Balaban CMP 95-119 — for any reference to the steps 2-3 Balaban literature citations in PROOF-CHAIN.md

---

## Questions log

*(primary runner appends new question blocks below this line; support runner appends answers under each)*

---

*End of template. The first Q-1 appears below when the primary runner asks.*
