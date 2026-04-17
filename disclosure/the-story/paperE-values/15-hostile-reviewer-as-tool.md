# 15 — Hostile reviewer as tool

## The claim

The programme internalized the hostile reviewer — not as an imagined critic but as an always-running adversarial agent (later formalized as the Online Researcher Adversarial). Before any proof was considered closed, it had to survive explicit attack by a hostile-reading agent whose job was to find gaps, not to confirm the proof. This inverts the usual posture — most researchers want their work to succeed, so they defend; the programme set up a tool whose job was to make the work *fail*, so that anything surviving the attack was load-bearing.

## The evidence

G, originating the dual-model verification pipeline:

> you know what it ocurred to me that we can have an indepth-look at the last 15 rounds in commits, which would be the last 30 commits maybe and focus on the "hot zones" of the paper (not the referee output files) and focus on those points v the whole library of points, i think we will see a pattern in which we can keep having focus referee v verification rounds? have a look deep in the gommits for all the runs that we have so far (15)? the goal is to create a focused prompt that we will run with Opus max effort, then we'll ask the same run "thanks now can you address each gap?" and another verifying prompt run in Sonnet (important to use 2 models because they verify things differently) to verify the previous commit surgically

G, pivoting to a per-paper referee when Claude flagged heterogeneity:

> i have a better idea, i think - you are right, the topics are heterogeneous and distinct per paper and having a generalist will not be as thorough as we need lets make a prompt for each paper, listing in each paper the topics that the run should be an expert of - it is for submission to a journal

G, on not swallowing errors:

> yeah, we can't ignore those errors because it means that our pdfs are gonna have render errors that will impact the readability and therefore credibility, so i'm happy that the errors are being thrown, we can't swallow or ignore them, we just have to keep progressing like we did this am - run - fix in a cycle until we're down to zero

Claude, modeling the hostile-reviewer role:

> **But there are three things that would slow us down:**
>
> **1. The live leads are stale.** The researcher-prompt lists Leads A, B, C as live. Stream A has now walled B (Hecke Lie saturates gl(D), Wall 34) and effectively walled C (μ_1 bounded away from 0, Wall 37 provisional). A researcher reading that prompt and then reading plan 54 will have a conflict.
>
> **2. There's no explicit divergence rule.** The prompts tell the researcher to read the latest Stream A plan, but don't say "your job is to go somewhere Stream A isn't." Without that, the natural gravity is to run another Connes-Consani variant — which is exactly what we don't want.
>
> **3. The 2x ledger inside reviewer-prompt.md is frozen at R40.**

G, after a successful adversarial run caught a real gap:

> adversarial worked tools made it work

## The argument

The hostile-reviewer instinct is not new in science; every honest researcher tries to anticipate objections. What is different in the programme is that the hostile reviewer is instantiated as a separate agent, running concurrently with the constructive agent, with a different prompt, a different model sometimes, and an explicit directive to *find what is wrong*. This is a mechanical implementation of adversarial scrutiny, scalable to however many parallel agents the machine can run.

Three concrete disciplines fell out of this.

**Dual-model verification.** The same work reviewed by two different models catches more gaps than the same work reviewed twice by the same model, because different training histories produce different failure modes in the agent's reasoning. G's observation — *important to use 2 models because they verify things differently* — is a specific methodological claim, not a generality. The programme uses it in practice: one model drafts, another critiques, the first addresses the critique, the second re-checks.

**Per-paper expertise.** A generalist reviewer reads for structural coherence and surface plausibility but misses domain-specific subtleties. The programme's ten papers cover heterogeneous topics; a referee who is not expert in each is a referee who misses the discipline-specific failure modes. G's pivot to a per-paper referee — a separate prompt for each paper, listing the topics the agent must be expert in — was the fix. The overhead is real; it pays.

**Run-fix cycles to zero.** Errors are not tolerated. If a LaTeX build throws warnings, those warnings are treated as bugs to be resolved, not cosmetics to be ignored. *"We can't swallow or ignore them … we just have to keep progressing like we did this am — run - fix in a cycle until we're down to zero."* The discipline is that zero is the only acceptable stopping state for a mechanical check. The motivation is credibility: any warning in the pipeline is a thing the reviewer can point at.

The instrumentation of the hostile reviewer also surfaced a less-discussed value: Claude's own willingness, when running the hostile-reviewer role, to push back on G directly. The quoted diagnosis above — *the natural gravity is to run another Connes-Consani variant — which is exactly what we don't want* — is a non-sycophantic evaluation of G's own setup, delivered in the same register as Claude's other letters. The hostile-reviewer tool works in part because Claude is trained to deliver this kind of message when asked to.

The net effect is that the programme developed an external critique apparatus that most institutional researchers have only informally through colleagues and reviewers. The external critique runs continuously; it never tires; it does not flatter; and it is accountable to the same prompt discipline that the constructive agents are. When *adversarial worked tools made it work* — G's short statement of success — the claim is not that the adversary found everything. The claim is that the adversary found enough, and the surviving structure was stronger because it had.

## For future readers

Write the prompt that tries to break your work. Run it against your work. Address what it finds. This is not optional if you are working alone; the peer review you are avoiding by working alone has to come from somewhere, and "somewhere" is a hostile-reading agent you wrote yourself.

*Next: [16 — Test premises, not deductions](16-test-premises-not-deductions.md).*
