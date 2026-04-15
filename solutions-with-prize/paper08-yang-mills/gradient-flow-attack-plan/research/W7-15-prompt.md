# W7-15: Leading-Order Operator Product Expansion (Lemma 4.3 → Conjecture L.4)

## Task
Write a rigorous proof memo establishing the leading-order OPE for [Tr F²]_R, closing Conjecture L.4 at leading order.

## Statement
[Tr F²]_R(x) [Tr F²]_R(y) ~ C^1(x-y)·1 + C^O(x-y)·[Tr F²]_R(y) + Σ_{k: d_k≥6} C^k(x-y)·O_k(y)
with identity-channel coefficient C^1(x-y) = C_N/|x-y|⁸ · (ln(1/|x-y|Λ))⁻² · [1 + O((log)⁻¹)].

## Key inputs
- At t > 0: O_t(x)·O_t(y) is UV-finite for ALL x,y including coincident (flow smearing)
- Gradient-flow OPE coefficients D_k^{(t)}(x-y) are smooth (not distributional) at t > 0
- Taking t → 0 recovers distributional OPE coefficients
- dev ≥ 2 at dimension ≥ 6 (Lemma 3.3, W1-04): controls subleading channels
- Perturbative coefficients known to 3 loops: Zoller-Chetyrkin JHEP 12 (2012) 119; JHEP 10 (2014) 169
- The full non-perturbative OPE (all channels, all orders) remains open — state this honestly

## What to read
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W5-10-cauchy-estimate-and-extraction.md` — [Tr F²]_R exists
- `/Users/gsix/yang-mills/preprint/sections/L-clay-conjectures.md` — Conjecture L.4 exact text
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/l1-gradient-flow-attack-plan.md` — Section 4.3 (OPE via gradient flow)
- `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-04-established-lemmas-pack.md` — Lemma 3.3 (dev ≥ 2)

## What to write
Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W7-15-ope-leading.md`

## Output format
(1) Gradient-flow OPE at t > 0 (smooth coefficients), (2) t → 0 limit recovers distributional OPE, (3) identity-channel coefficient from AF prediction, (4) subleading channels controlled by dev ≥ 2, (5) operator basis at dimension ≤ 6 (Kluberg-Stern-Zuber), (6) honest statement: full OPE at all orders is open, leading order is proved. Reference Zoller-Chetyrkin for perturbative coefficients.
