# Research Index — Scheme-Independence of Epstein Vanishing

**Project:** QG5D Paper Series  
**Question:** Is the UV finiteness of 5D linearized gravity on M⁴ × S¹/Z₂ scheme-independent?  
**Status:** Active research — 5 parallel routes

## Background

Paper 1 proves UV finiteness via: KK mode sums → Epstein zeta functions → Universal Epstein
Vanishing theorem → perturbative UV finiteness of 5D linearized gravity. The proof uses
zeta regularization. The open honesty (stated in Paper 1 Appendix U): scheme-independence
has not been proved.

This research directory collects five parallel explorations of scheme-independence, each
pursuing a different mathematical route. Every file pair (prompt + output) is a self-contained
research record suitable for inclusion as an appendix.

## Files

| # | Prompt | Output | Route | Status |
|---|--------|--------|-------|--------|
| 01 | 01-prompt.md | 01-number-theoretic-zeta-zeros.md | Trivial zeros of ζ_R | — |
| 02 | 02-prompt.md | 02-heat-kernel-seeley-dewitt.md | Seeley-DeWitt coefficients | — |
| 03 | 03-prompt.md | 03-z2-parity-cancellation.md | Z₂ even/odd parity | — |
| 04 | 04-prompt.md | 04-poisson-dimreg.md | Poisson resummation in dim-reg | — |
| 05 | 05-prompt.md | 05-weyl-anomaly-kk-tower.md | Weyl anomaly from KK tower | — |
| 06 | — | 06-synthesis.md | Synthesis across all routes | — |

## Code

Each route has a corresponding Python environment at:
`/Users/gsix/quantum-geometry-in-5d-latex/code/<route-name>/`

Environments contain: computation scripts, results output, venv. Results are
embedded in the research memo for each route.

## Canonical values (do not contradict these)

- R₀ = 10.1 μm (Casimir constraint, corrected with mirror sector)
- ξ = 0.432 (from Ω_DM/Ω_b = 5.36)
- m_ν = 49.7 ± 0.5 meV (framework prediction, CMB-S4 test at 5–8σ)
- 5/2 identity: m_ν/m_KK|_{GUT} = 5/2 = 3 − 1/2 — numerical coincidence, not topological theorem
- Goroff-Sagnotti counterterm: R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} — the 2-loop obstruction in 4D gravity
