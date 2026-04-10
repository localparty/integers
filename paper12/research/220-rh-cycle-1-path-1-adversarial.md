# 220 — RH Cycle 1, Path 1 (Brauer-KMS) — Adversarial

*Cycle: 1. Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: Is the "genericity + analyticity" sub-path circular?

The construction agent proposes: show f(gamma) depends continuously
on delta, so for generic delta it is not a k-integer, then use
analyticity of zeta to exclude the measure-zero set.

**Problem:** The analyticity argument assumes zeta is analytic in the
critical strip — which is true — but the conclusion "a zero cannot
sit at a measure-zero set of delta values unless delta = 0" is NOT
valid. Zeta zeros are discrete points. A discrete set CAN intersect
a measure-zero set. The argument would need to show the set of
"bad" delta values is not just measure-zero but EMPTY (or at least
that no zero of zeta sits on it). This requires more than genericity.

**Result: WEAKENED.** The genericity sub-path needs strengthening.
The construction agent's proposal is suggestive but does not close
the gap as stated. The key issue: "generic" is not "all."

### Attack 2: Does the Brauer class argument work for k=2?

At k=2, H^2(Z/2Z, U(1)) = Z/2Z = {0, 1/2}. The Brauer class is
trivial (0). A continuous perturbation of 0 is... 0 (for small
perturbation). The contradiction (discrete can't absorb continuous)
does NOT apply at k=2 because the trivial class has no phase to shift.

**Result: SURVIVED (partially).** The construction agent did not claim
closure at k=2. The path explicitly relies on k in {3, 4, 6}. At
k=2 the bridge is structural (CP symmetry), not cohomological.
However, this IS a limitation: the Brauer-KMS argument cannot
cover the k=2 bridge. If a zero were to affect only the k=2
sector, this path would miss it.

### Attack 3: Is Conjecture 2 circular?

Conjecture 2 states: Brauer-KMS duality implies RH. But does the
DEFINITION of the CBB system already assume RH (via the spectrum
being {gamma_n} on the critical line)?

**Check against the catalogue:** The CBB system definition
(anchor §2, Axiom 1) defines the log-spectrum as
{L_n = gamma_n pi^2/2} where gamma_n are the imaginary parts of
zeros ON THE CRITICAL LINE. This is NOT assuming RH — it is
using the known zeros (which are all on the critical line by
computation up to 10^13). The question is whether ADDITIONAL zeros
exist OFF the line.

**Result: SURVIVED.** The definition uses {gamma_n} = known zeros
on the critical line. The conjecture then asks: could there be
zeros OFF the line? The Brauer-KMS argument says no. This is not
circular.

### Attack 4: Does the spectral density factor f(gamma) actually exist?

The construction agent assumes f(gamma) is well-defined. But if
T_BC is distributional (Meyer 2005), the V-coupling commutator
[log R-hat, Pi_chi] may not produce a well-defined spectral
density factor. The distributional nature of T_BC could make
f(gamma) undefined or distributional itself.

**Result: WEAKENED.** This is a genuine concern. The construction
agent's step requires f(gamma) to be a well-defined real number
(so that irrationality can be tested). If f is distributional,
the entire irrationality strategy fails. This connects to the
Meyer distributional subtlety (Compendium §F.2).

---

## Overall verdict: INTACT (with caveats)

The construction agent correctly identified the step as BLOCKED,
so there is no false closure to break. The blocking diagnosis is
accurate. Two attacks (1, 4) WEAKENED the proposed next steps by
identifying additional obstacles:

1. The "genericity + analyticity" sub-path needs "generic" replaced
   with "all" — a harder claim.
2. The distributional nature of T_BC threatens the well-definedness
   of f(gamma) itself.

The path remains the strongest of the five, but the gap is deeper
than the construction agent's initial analysis suggested.
