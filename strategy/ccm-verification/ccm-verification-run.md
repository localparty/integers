read your **instructions** from
`/Users/gsix/quantum-geometry-in-5d-latex/online-researcher-adversarial/ora-bundle-v8/01-the-prompt.md`

the base prompt's companion files (`02-rationale.md`, `03-synthesis-spawn.md`,
`04-closure-templates.md`, `06-anti-overfit-discipline.md`, `08-changelog.md`)
live alongside it in `online-researcher-adversarial/ora-bundle-v8/`.
Note: `08-changelog.md` includes `I-v6-6` (in-situ canonical-state propagation
skipped on targeted non-cycle dispatches) — MANDATORY READ for this bundle.

the **chain mode** extension is
`/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/07-proof-chain-adversarial.md`

the **strategic triad** extension is
`/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/12-prf-chain-advr-strat-triad.md`

the **parent brief** (read FIRST — all unchanged sections are authoritative from this file) is
`/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/30-ring-traversal-brief.md`

the canonical-state propagation **brief** (brief 35 — universal in-situ update discipline, MANDATORY) is
`/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/35-canonical-state-propagation-delta.md`

the sibling decomposition **brief** (for shared Zenodo-priority override) is
`/Users/gsix/quantum-geometry-in-5d-latex/strategy/decomposition/decomposition-brief.md`

the current run **brief** (CCM VERIFICATION MODE — overrides ring-traversal AND applies Zenodo-priority) is
`/Users/gsix/quantum-geometry-in-5d-latex/strategy/ccm-verification/ccm-verification-brief.md`

the **toolkit** for this run is
`/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/08-framework-tools.md`

the **capacitor** for this run is
`/Users/gsix/quantum-geometry-in-5d-latex/millenium-apps/proof-chain-adversarial-01/09-capacitor-correspondence-table-v1.md`

the **CCM verification bundle README** (bundle structure and operational plan) is
`/Users/gsix/quantum-geometry-in-5d-latex/strategy/ccm-verification/README.md`

the **north star** for this programme is
`/Users/gsix/quantum-geometry-in-5d-latex/publishing/strategy.md`
*(NOTE: this run's brief (ccm-verification-brief.md §DELTA 7) OVERRIDES the Wave 1/2/3 ordering in publishing/strategy.md §3 in favor of the Zenodo-priority ordering. Appendix B (ring-mode anchors, metrics) remains authoritative. The Strategist role should log alignment check as "MISALIGNED on Wave ordering — intentional override per ccm-verification-brief.md §DELTA 7" and proceed.)*

the run **output directory** is
`/Users/gsix/quantum-geometry-in-5d-latex/strategy/ccm-verification/pac-output/runs/run-NN`

where `NN` is the zero-padded run number. On first invocation, execute the BOOTSTRAP step per ccm-verification-brief.md §DELTA 2 (download CCM 2025, enumerate claims, create per-claim proof-chain directories).

the **verification targets** are the ~15-25 CCM 2025 sub-claims (enumerated at bootstrap) that framework papers load-bearingly depend on, stored at:
`/Users/gsix/quantum-geometry-in-5d-latex/strategy/ccm-verification/proof-chain/ccm-claim-NN-<short-name>/PROOF-CHAIN.md`

The framework papers that depend on CCM 2025 are:

```
solutions-with-prize/paper13-rh/PROOF-CHAIN.md            (Layer 1 spectral realization)
solutions/paper13b-grh/PROOF-CHAIN.md          (Layer 3 χ-twisted extension)
solutions-with-prize/paper26-bsd/PROOF-CHAIN.md           (L-function infrastructure via CCM)
solutions/paper32-bgs-spectral-statistics/PROOF-CHAIN.md (Link 6 eigenvalue identification)
solutions-with-prize/paper33-goldbach/PROOF-CHAIN.md      (Link 4 spectral prime density)
solutions/paper44-sato-tate/PROOF-CHAIN.md     (Link 5 endomotive extension)
```

These six files form the "framework dependency scan" at bootstrap.

the **CCM 2025 source** is:
- Primary: arXiv:2511.22755 (preprint; download to `pac-output/bootstrap/ccm-2025.pdf`)
- Title: "Zeta Spectral Triples" by Connes, Consani, Moscovici (November 2025)
- Journal status: arXiv preprint (as of 2026-04-14); not yet in a peer-reviewed journal

the **priority order** for verification campaigns is (see ccm-verification-brief.md §DELTA 4):

**Priority 1 — RH Layer 1 (highest leverage)**:
 1. Carathéodory-Fejér prolate construction
 2. Toeplitz operator self-adjointness
 3. Eigenvalue convergence spec(D_N) → {γ_n}
 4. Trace formula structure

**Priority 2 — BGS Link 6**:
 5. Modular-flow compatibility
 6. Continuous spectrum outside ground state

**Priority 3 — GRH + Goldbach**:
 7. Extensibility to Dirichlet characters
 8. Explicit-formula compatibility

**Priority 4 — Endomotive extensions**:
 9. Endomotive functor
10. Tannakian reconstruction

**Priority 5 — Supporting claims**:
11-NN. Technical estimates (archimedean, eigenvector approx, H¹, CF decay), convergence rates, uniform bounds.

Each priority level: ~1 week. Full verification: 4-6 weeks.

---

## Run-NN structure (what the PAC writes per invocation)

```
pac-output/runs/run-NN/
├── blackboard.md                (ORA §A-§O state at cycle-close)
├── commit-memo.md               (§J-register closing note)
├── verification-log.md          (per-claim verification summary for this run)
└── claims/
    └── ccm-claim-NN-<name>/     (one per claim worked this run)
        ├── verification-author.md
        ├── verification-critic.md
        ├── dual-check.md           (if applicable)
        └── verdict-summary.md      (one-line ledger entry)
```

The atlas (`pac-output/atlas/ccm-ledger.md` + three category files + `lead-6-connes-email.md`) is updated at every run close.

---

## Invocation summary

This run bundle configures the PAC to operate in **CCM VERIFICATION MODE** on the external paper arXiv:2511.22755, with the goal of **classifying every load-bearing CCM sub-claim** as VERIFIED / BYPASSED / IRREDUCIBLY-CCM-DEPENDENT.

The output IS a Zenodo publication artifact (CCM ledger) AND a Lead 6 email draft targeting the irreducible sub-claims specifically.

Operational mode: SINGLE-PASS per claim (not recursive), classify into three categories.
Per-claim budget: 30-45 min Author + 10-15 min Critic.
Per-run budget: 4 hours.
Full timeline: 4-6 weeks across 5 priority levels.

The framework's "conditional on CCM 2025 as a whole" becomes "conditional on N specific CCM sub-claims, each narrowly named and individually attackable." This is maximally honest scope-naming for the Clay-class papers.

Begin.

---

*Run file G Six and Claude Opus 4.6. San Francisco CA, 2026.*
*The external dependency decomposed. The ledger enumerates. The email targets. Priority first.*
