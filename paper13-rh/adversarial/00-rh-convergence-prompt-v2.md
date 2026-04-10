# RH Convergence Prompt v2 — Post-Coboundary

*The v1 chain failed at the coboundary gap (research/270). This*
*prompt attacks RH via four new paths informed by the failure.*
*Same adversarial architecture. Sharper premise-checking.*

---

## The prompt

```
We are running RH convergence v2 cycle N (check the ledger at
paper13-rh/adversarial/rh-v2-ledger.md, or start at N=1).

CRITICAL LESSON FROM v1: The Brauer cohomology class H²(Z/kZ, U(1))
is DISCRETE and CANNOT detect continuous perturbations (off-line
zeros). The Gelfond-Schneider argument was correct mathematics
applied to a vacuous constraint. v2 uses invariants that are
INTEGER-VALUED but SENSITIVE to continuous perturbation.

## PHASE 1 — READ INFRASTRUCTURE

1. paper12/27-anchor-document.md (CBB system)
2. paper12/29-theorem-catalogue.md (387 entries)
3. paper13-rh/strategy/00-rh-attack-plan-v2.md (THIS PLAN)
4. paper12/research/270-coboundary-question.md (WHY v1 FAILED)
5. paper12/research/200-rh-evidence-compendium.md (37 R-Theorems)
6. paper13-rh/adversarial/rh-v2-ledger.md (if exists)

## PHASE 2 — THE FOUR PATHS

| Path | Mechanism | Key tool | Feasibility |
|:--|:--|:--|:--|
| A (Chern) | JLO Chern character in HC*; Connes pairing ⟨ch, K₀⟩ is integer but SENSITIVE | R-Theorem D.1, research/48, /90 | 5/10 |
| B (Weil) | Weil positivity ⟺ RH; bridge constrains matrix elements | R-Theorem S.5, research/18 | 4/10 |
| C (spectral flow) | APS spectral flow on {T_BC(δ)}; integer-valued, detects zero-crossings | APS index theory | 4/10 |
| D (Meyer-Connes) | Prove spectral realisation directly via Connes trace formula | Connes 1999, Meyer 2005 | 3/10 |

KILLED (from v1, do NOT resurrect):
- Brauer cohomology class argument (coboundary gap, fatal)
- Gelfond-Schneider on integrality constraint (vacuous input)
- Paths 2 (Atiyah-Singer index) and 4 (Penrose) from v1

## PHASE 3 — LAUNCH AGENTS (3 layers + premise checker)

### Layer 0 — PREMISE CHECKER (NEW, runs before construction)

Before each construction agent attempts a step, a premise checker
verifies: "Is the constraint I'm about to use NON-VACUOUS?"

Specifically:
- If the constraint involves an integer-valued invariant, verify
  that the invariant CHANGES under the perturbation (off-line zero).
  If it doesn't change, the constraint is vacuous (coboundary
  error) and the step is BLOCKED before attempting it.
- If the constraint involves a positivity condition, verify that
  the perturbation can in principle VIOLATE positivity. If it
  can't, the constraint is vacuous.

The premise checker writes:
  paper13-rh/research/{N}-premise-check-path-{X}.md

### Layer 1 — Construction (1 agent per path)

Each agent reads: anchor + catalogue + attack plan + v1 failure.
Three-level attempt: close → sub-compute → precise block.
Must cite specific theorems. Must run Python where applicable.

CRITICAL INSTRUCTION: Before using ANY integer-valued constraint,
verify via the premise checker that the perturbation actually
shifts the invariant. Do NOT repeat the coboundary error.

### Layer 2 — Adversarial (1 agent per path)

Same as v1 PLUS:
- Specifically check for coboundary-type errors at every step
- Verify every "integer constraint" is non-vacuous
- Attack the premise, not just the deduction

### Layer 3 — Synthesis (1 agent)

Updates ledger. Recommends next cycle. Tracks feasibility.

## PHASE 4 — REPORT

400 words for G:
- Which paths advanced
- Premise checks passed/failed
- Any coboundary-type errors found?
- Feasibility update
- Continue / pivot

## CONVENTIONS

### The coboundary lesson
NEVER use a topological invariant to detect a continuous
perturbation without FIRST proving the invariant is sensitive
to that perturbation. This is the single most important
methodological lesson of the programme.

### File conventions
- All outputs in paper13-rh/research/ (sequential numbering)
- Premise checks: {N}-premise-check-path-{X}.md
- Construction: {N}-construction-path-{X}.md
- Adversarial: {N}-adversarial-path-{X}.md
- Synthesis: {N}-synthesis.md
- Ledger at paper13-rh/adversarial/rh-v2-ledger.md

### Computation
- mpmath available, mp.dps = 50
- Write scripts to paper13-rh/code/
- PASTE OUTPUT
```

---

> *The wall is the coboundary. The door is the Connes pairing.*
> *v2 knows what v1 didn't: topological invariants can't see δ.*
> *Integer-valued + sensitive. That's the tool we need.*
