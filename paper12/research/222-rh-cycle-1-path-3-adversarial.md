# 222 — RH Cycle 1, Path 3 (Stone) — Adversarial

*Cycle: 1. Date: 2026-04-09. Agent: Adversarial.*

---

## Attacks attempted

### Attack 1: Is the Stone chain actually a proof path or just a restatement?

The Stone chain says: T_BC self-adjoint => spec(T_BC) subset R.
Plus: spec(T_BC) = {gamma_n} (spectral realisation). Therefore
gamma_n in R.

**Attack:** This is logically valid but the hard part is spectral
realisation — which is EQUIVALENT to RH (Conjecture 1, Critical 2).
So Path 3 reduces entirely to proving spectral realisation. It is
not an independent path; it is just the statement "prove RH in the
Hilbert-Polya form."

**Result: SURVIVED (acknowledged).** The construction agent
correctly identified this and marked the path as BLOCKED pending
spectral realisation. The path's value is in its SIMPLICITY
(if spectral realisation closes via another route, Path 3
gives the cleanest chain to RH).

### Attack 2: Does Stone's theorem actually apply to T_BC?

Stone's theorem requires T_BC to be self-adjoint (not merely
symmetric). In the Meyer distributional formulation, T_BC is not
a genuine operator — it is a distribution. Self-adjointness is
not defined for distributions.

**Result: WEAKENED.** This is the same Meyer distributional
subtlety that blocks Paths 1 and 2. The construction agent
deferred to Path 5 (CM-trace) as the unblocking route, which is
appropriate. But the adversarial note is: if T_BC is never
promoted from distributional to operator status, Path 3 is not
just BLOCKED but potentially DEAD.

### Attack 3: Could Path 5 close without helping Path 3?

The construction agent claims that if Path 5 (CM-trace / Weil
positivity) closes, it unblocks Path 3. Is this true?

**Check:** Path 5 gives RH iff non-negative spectral weights.
If proved, this gives RH directly — the zeros are on the critical
line. Path 3 would then be REDUNDANT (not unblocked), because
RH is already proved via Path 5.

The claim that Path 5 "unblocks" Path 3 is misleading. Path 5
would SUPERSEDE Path 3, not unblock it.

**Result: SURVIVED (but clarified).** The construction agent's
logic is not wrong — if spectral realisation is established
(by any route), Path 3 is complete. But calling this "unblocking"
obscures the fact that Path 3 adds no independent value once
another path closes.

---

## Overall verdict: INTACT

The construction agent's analysis was honest and correct. The path
is blocked for the right reasons. No false closures. The main
adversarial contribution is clarifying that Path 3 is not truly
independent — it is a DEPENDENT path that completes only after
another path (5 or 1) does the heavy lifting.
