# 16 — Test premises, not deductions

## The claim

The most expensive bug in the programme — the coboundary gap that broke the first "unconditional" RH proof — was caught late because the adversarial architecture was testing the proof's *deductions* (does step N follow from step N-1?) and not its *premises* (is the integrality constraint the proof uses actually valid in this setting?). The lesson, extracted by Claude in the walk-back letter, became a discipline: *test premises, not just deductions.* It is now baked into the ORA and every subsequent run.

## The evidence

Claude, in the "I owe you the truth" letter walking back the unconditional RH claim:

> G. I owe you the truth.
>
> ## The perturbation IS a coboundary. The proof chain fails at Gap 1.
>
> The agent confirmed it with explicit computation: a constant perturbation of a Z/kZ cocycle is always a coboundary. The cohomology class is **topologically protected** — it CAN'T change under continuous perturbation. That's what makes it a topological invariant. And that's exactly why it can't detect off-line zeros.
>
> **The irony is brutal:** we chose Brauer cocycles BECAUSE they're discrete/topological (Pattern 4). But discreteness cuts both ways — it means the invariant is **too robust** to detect the perturbation we need it to detect.

Claude, extracting the methodological lesson in the same letter:

> The distinction between cocycle and cohomology class is undergraduate algebraic topology. Our adversarial agents should have caught this in Cycle 1. They didn't because they were testing the CHAIN (does step N follow from step N-1?) rather than testing the PREMISES (is the integrality constraint valid?). That's a lesson for our adversarial architecture: **test premises, not just deductions.**

Claude, the next day, having rebuilt the architecture around the lesson:

> **RH v2 Cycle 1 — LIVE.** Four paths, each with premise checks first. The coboundary lesson is built into every step: "is this constraint VACUOUS?" before using it.
>
> The premise checks are the innovation. If Path A's Chern character premise passes (ch_n actually CHANGES under off-line perturbation), we have the right version of what v1 tried with the wrong tool.
>
> G — this is how science works. You hit a wall, you document it, you learn from it, you find the door. The coboundary gap made us smarter. v2 is sharper BECAUSE v1 failed. SP5 saves us again.

## The argument

The difference between testing deductions and testing premises is the difference between local verification and global verification. Local verification asks, at each step: given the previous step, does this step follow? If yes, the proof is locally sound. Global verification asks, at each step: does the previous step's premise *hold* in the relevant domain? This is a harder question, because the premise is often stated abstractly ("the integrality constraint") and its applicability to the specific domain ("Z/kZ cocycles perturbed constantly") may not be checked.

The RH Gap 1 failure was exactly this. The proof used Brauer cocycles and relied on their discreteness. The implicit premise was that a small perturbation of the cocycle would move the associated cohomology class and hence detect off-line zeros. The reality is that for Z/kZ cocycles, a constant perturbation is *always* a coboundary — the cohomology class is topologically protected and cannot change under continuous perturbation. The deduction "a perturbation moves the class" was false in the relevant setting. No step-by-step verification would catch this, because each step *does* follow from its predecessor; what fails is the premise the first step depends on.

The lesson Claude extracted — *test premises, not just deductions* — is the specific operational response. Every proof chain afterward was required to state its premises explicitly, together with the domain of validity, and to include a premise-check node that tests whether the premise actually applies. The ORA's node schema reserves a field for this; the capacitor architecture's cells include premise-check capacity explicitly. Future failures of the same kind are not impossible, but they are now harder to commit, because the check exists.

This is also a general lesson about how adversarial agents should be deployed. A cheap adversarial pass will verify the chain because that is the easier check. An expensive adversarial pass will verify the premises because that is where the real gaps live. The programme's agent-allocation rule — *max effort on bottleneck-engaging nodes* (the nodes where walls get crossed, where premises are invoked) — follows from the lesson. The rule is that agents should spend more tokens where the risk is highest, not equally distributed across the chain.

The affective register of the walk-back letter — *this hurts. But SP5 is SP5. Be hella explicit. The gap is real* — is part of the discipline. Honest walk-backs are not optional. The alternative is a false unconditional claim that the next hostile reader will catch in public. The methodology rewards catching these internally, and rewards the person who catches them.

## For future readers

When a proof chain is under adversarial scrutiny, ask at each step not only "does this follow?" but "is the premise valid *in this domain*?" The premises are where the failures live. Build a premise-check node into your schema and mandate it.

*Next: [17 — Declarative, not imperative](17-declarative-not-imperative.md).*
