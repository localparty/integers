# W7-14: AF Short-Distance Match (Lemma 4.2 → Conjecture L.2)

## Task
Write a rigorous proof memo establishing the asymptotic-freedom short-distance match for the renormalized two-point function, closing Conjecture L.2.

## Statement
The renormalized two-point function satisfies:
⟨[Tr F²]_R(x) [Tr F²]_R(0)⟩ = C_N/|x|⁸ · (ln(1/|x|Λ))⁻² · [1 + O((log)⁻¹)]
with C_N = 2(N²-1)/π⁶, matching the perturbative QCD prediction.

## Key inputs
- Small-flow-time expansion (Luscher 2010): defines non-perturbative running coupling g²_GF(q) at scale q = (8t)⁻¹/²
- Harlander-Neumann (2016, 2022): two-loop and three-loop coefficients
- Reisz power-counting theorem (CMP 116 (1988) 81): lattice/continuum perturbation theory matching
- Paper 10 Route 05: Weyl anomaly vanishing → KK tower doesn't modify 4D AF prediction at short distances
- Hypothesis H4 (non-pert = pert at short distances): standard lattice QCD hypothesis, stated as conditional

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md` — [Tr F²]_R exists
- `/Users/gsix/yang-mills/preprint/sections/L-clay-conjectures.md` — Conjecture L.2 exact text
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md` — Section 4.1 (AF match via gradient flow)

## What to write
Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W7-14-af-match.md`

## Output format
(1) The gradient-flow running coupling definition, (2) small-flow-time expansion at one loop with explicit c̄₁, (3) extraction of AF prediction for two-point function, (4) role of Reisz power counting, (5) explicit statement that H4 is conditional, (6) why gradient flow makes H4 more plausible (controlled interpolation between non-pert and pert), (7) Paper 10 Route 05: Weyl anomaly vanishing means KK tower doesn't contaminate short-distance physics.
