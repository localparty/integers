# Agent L — Pin #6 audits (2026-04-14)

## Audits as originally specified

### Audit A — Paper 13 "CP-violating capacitor diagonal" — **NO**

Full ripgrep across `paper13-rh/{preprint,research,referee,nodes,strategy,ccm-bypass,sources}/` for CP.violat / CP-viol / CP violat: **zero matches**. Paper 13 has no CP-violation section, no Jarlskog discussion, and no "CP-violating capacitor diagonal."

CKM mentions in Paper 13 are peripheral:
- `paper13-rh/preprint/sections-11-14.md:732` — CKM listed as downstream prediction requiring γ_n ∈ ℝ.
- `paper13-rh/preprint/sections-01-05.md:232` — abstract notes "full CKM matrix within 0.6σ of PDG 2024."

Neither defines a CBB diagonal coefficient. The actual Paper 13 bridge diagonal is `c_n^{(k)} = (1/k)(1 − w^k)/(1 − w)` with `w = exp(−2πi/k) · p^{−(1/2+iγ_n)}` (referee/latest-run/points/C1-dark-states/01-bound.md:3) — a geometric series in `p^{−iγ_n}`, NOT a `log γ_1`-weighted entry.

### Audit B — Paper 26 Step 4 J_CKM vertex — **NO**

Paper 26 Step 4 is the twisted cocycle shift bound:

    |Δc^ψ(δ)| = |1 − ψ(𝔭) N(𝔭)^{−2δ}| / |N(𝔭) − ψ(𝔭) N(𝔭)^{−2δ}|
    ⇒ |Δc^ψ(δ)| < 1/(k+1) for (k,N) ∈ {(2,13),(3,13),(4,41),(6,29)}

An INEQUALITY used in a reductio via Hasse-Brauer-Noether. It is NOT a numerical formula whose evaluation produces `log(γ_1) · ζ(3)`.

- `J_CKM | Jarlskog | 3.184` across `paper26-bsd/preprint/` and `paper26-bsd/nodes/`: zero matches.
- J_CKM hits in `paper26-bsd/code/*.py` are local Python variables in unrelated scripts.
- The `(4,41)` row in E-cocycle-shift.md:72 is a Gaussian-prime Brauer bridge over ℚ(i), not a CKM-generating vertex.

Paper 26 contains no CKM-sector language anywhere.

## The TRUE structural anchors (revised audit)

Agent L found the actual load-bearing documents at `paper12/research/102-derive-Jarlskog-CKM.md`:

1. **ζ(3) source**: Agent G's Cycle-2 Mercedes 4D derivation (three independent routes, 30-digit precision). ✓ CLOSED.
2. **log γ_1 source**: Mellin duality `H_BC = log T_BC` gives log γ_1 as the BC ground-state energy — see `paper12/research/102 §3.1`, built on `paper12/research/02`. ✓ CLOSED.

## Remaining OPEN items (from paper12/research/102 §6.3)

The real audit items, correctly stated:
- **O1**: ζ(3) origin from 3-loop QFT — **CLOSED by Agent G (2026-04-14)**.
- **O2**: Exact 10⁻⁵ normalization origin — **OPEN**.
- **O3**: Why the direct formula `log(γ_1) · ζ(3)` beats the factored 4-Wolfenstein computation 18× in precision — **OPEN**.

## Recommendation

**Pin #6 stays THEOREM-pending-audit** but with corrected audit items. The original items (Paper 13 CP-violation + Paper 26 Step 4 vertex) describe content that does not exist. The actual audit should be:

1. O2: derive the 10⁻⁵ factor (normalization of J_CKM in the CBB dictionary).
2. O3: explain the 18× precision gain vs factored 4-Wolfenstein.

Both items are in `paper12/research/102` §6.3 and are genuine research — neither has been addressed by Paper 13, Paper 26, or the Cycle-2 agents.

## Surprise findings

1. **Paper 13 has no CP-violation section**. For a paper cited in CKM predictions, this is striking.
2. **Paper 26's (4,41) bridge row is NOT the CKM k=4 vertex** — terminology coincidence, not hidden identity.
3. **18× precision gain** of the direct `log(γ_1) · ζ(3)` formula over the factored computation is the genuine structural clue worth investigating.
4. Directory `paper1/code/pin6-audits/` created empty by subagent; this FINDINGS.md written by parent after return.
