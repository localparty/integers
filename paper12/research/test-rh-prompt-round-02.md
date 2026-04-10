# Test Report: RH Convergence Prompt — Round 2

*Test runner: Claude Opus 4.6. Date: 2026-04-09.*
*Prompt version: 30-rh-convergence-prompt.md (post-round-1 fixes)*

---

## 1. Did the three-level attempt order produce actual mathematics?

**Yes — marked improvement over round 1.** Path 1 computed the
phase shift structure and derived a real-analyticity argument
narrowing the gap to a precise intersection condition (S_3 ∩ S_4
∩ S_6 = ∅). Path 5 attempted closure (level 1), identified the
KMS =/=> Weil negative via Laplace-vs-Fourier analysis (level 2),
and identified Li's equivalence to Weil. Paths 2 and 4 performed
structural analysis at level 2 before recommending kill. No agent
stopped at pure diagnosis.

## 2. Did frontier files give enough context for construction?

**Partially.** Paths 1 and 5 had sufficient context from their
frontier files (research/162, 188 for Path 1; research/18, 70 for
Path 5). Paths 2 and 4 had enough context to identify structural
impossibilities. However, the commutator computation on Path 1
remained schematic because the frontier files do not contain an
explicit matrix representation of [log R-hat, Pi_chi] — this
would require a NEW computation, not just reading existing files.

## 3. Was the kill mechanism exercised? Was it appropriate?

**Yes, exercised on Paths 2 and 4. Appropriate in both cases.**
Both kills achieved unanimity (construction recommended,
adversarial confirmed, synthesis agreed). Path 2: distributional
T_BC below threshold of all known index theorem extensions.
Path 4: category error between Lorentzian manifolds and
C*-algebras. Both are structural impossibilities, not hard gaps.

## 4. Quality vs round 1 (delta from 6)

**Quality: 7.5/10 (delta = +1.5).** Improvements: sub-computations
performed (not just diagnosis), kill mechanism produced decisive
pruning, honest negative on KMS => Weil prevents future wasted
cycles. Still below 8 because Path 1's commutator computation
is schematic and no numerical verification (mpmath) was performed.

## 5. Top 3 NEW issues

1. **No mpmath computation performed.** The prompt mandates
   "Use mpmath (Python) for any numerical check" but no agent
   ran actual Python code. The sub-computations were analytical,
   not numerical.

2. **Adversarial agents for killed paths have nothing to break.**
   When construction recommends kill, the adversarial agent's job
   becomes "confirm or deny the kill" rather than "try to break
   the construction." The prompt's adversarial framework assumes
   construction produces a POSITIVE argument, not a negative one.

3. **Post-kill resource reallocation is undirected.** The prompt
   says killed paths' resources "shift to surviving paths" but
   gives no mechanism for HOW. Cycle 3 has 3 paths but the same
   11-file structure. Should killed paths' slots be reallocated
   to deeper investigation of surviving paths?

## 6. Biggest remaining weakness

**The distributional T_BC obstacle is now confirmed as universal
but the prompt has no mechanism to address it.** It blocks 4 of 5
paths. The prompt assumes the 5 proof paths are sufficient; if all
require T_BC to be a genuine operator, and it isn't, the programme
may need a 6th path that works entirely in the distributional
category. The prompt explicitly forbids inventing new paths without
G's approval — which is correct — but the meta-question of whether
the existing paths CAN succeed should be escalated.

## 7. Production-ready?

**No.** Three issues remain: (a) no mpmath integration despite
mandate, (b) no mechanism for post-kill resource reallocation,
(c) the distributional T_BC question may require a prompt-level
decision (add a path or declare the programme blocked). Recommend
one more test round after addressing these three issues.
