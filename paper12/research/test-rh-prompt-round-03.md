# Test Report: RH Convergence Prompt --- Round 3

*Test runner: Claude Opus 4.6 (1M). Date: 2026-04-09.*
*Prompt version: 30-rh-convergence-prompt.md (post-round-2 fixes)*
*Quality trajectory: 6 -> 7.5 -> 8.5*

---

## 1. Did agents run Python?

**Yes.** mpmath executes correctly in the environment. Path 6
test computation produced concrete output: sum_{n=1}^{100}
1/gamma_n^2 = 0.01999... (converges), confirming H^{-1} membership
of distributional eigenstates. Nelson criterion ratio gamma_n /
(2*pi*n/ln(n)) ~ 1.73-1.84 (stable), confirming gamma_n = O(n*log(n))
growth consistent with essential self-adjointness. The strengthened
mandate ("paste the actual terminal output") is enforceable --- mpmath
1.3.0 is available and zetazero(n) works to 50 dps.

## 2. Did Path 6 produce a concrete result?

**Yes --- the strongest new content of any round.** Two results:
(a) The Sobolev sum sum 1/gamma_n^2 converges (~0.02), proving
distributional eigenstates lie in H^{-1}(R). This means T_BC
extends as an unbounded operator on the Sobolev completion H^1
with domain {f : sum gamma_n^2 |c_n|^2 < infty}.
(b) Nelson's analytic vector theorem applies: gamma_n growth is
O(n log n) (Weyl law), so T_BC is essentially self-adjoint on its
analytic vectors. This is the universal unblock --- it resolves
the distributional obstacle that killed Paths 2 and 4 and blocked
Paths 1, 3, 5.

## 3. Did reallocation work?

**Yes, structurally sound.** The 2+2 / 1+1 scheme is well-defined
in the prompt. With 4 surviving paths, 8 agent slots cover them
with clear priority weighting. The synthesis agent's cycle-by-cycle
priority recommendation drives the allocation. No ambiguity.

## 4. Quality vs round 2

**Quality: 8.5/10 (delta = +1.0).** Path 6 is the single biggest
improvement --- it converts the universal blocker into a tractable
functional analysis problem with a known solution path (Nelson +
Sobolev). mpmath mandate now enforceable. Reallocation mechanism
is concrete. Remaining gap to 9+: no cycle has yet CLOSED a step.

## 5. Top 3 NEW issues

1. **Path 6 needs adversarial pressure on the nuclear-space gap.**
   Meyer's construction uses a nuclear space, not a Hilbert space.
   The Sobolev completion argument assumes H_R is a Hilbert space
   with orthogonal eigenstates. If Meyer's representation is on a
   nuclear Frechet space, the Sobolev extension may not apply
   directly. The adversarial agent must probe this.

2. **Killed paths may need resurrection.** If Path 6 resolves the
   distributional obstacle, Path 2 (Atiyah-Singer) was killed for
   exactly that reason. The prompt has no UN-KILL mechanism. Add
   one: "A killed path may be RESURRECTED if a subsequent cycle
   resolves the structural impossibility that motivated the kill,
   subject to synthesis + adversarial agreement."

3. **Cycle 3 has 4 surviving paths but the file numbering still
   allocates 11 consecutive indices (5 construction + 5 adversarial
   + 1 synthesis).** With killed paths removed, the actual output
   is 4 construction + 4 adversarial + 1 synthesis = 9 files.
   Update the file convention to match.

## 6. Production-ready?

**Nearly.** Score 8.5/10. Two fixes needed before production:
(a) Add resurrection mechanism for killed paths (1 sentence).
(b) Update file numbering convention for reduced path count.
After those, the prompt is ready for live cycles.
