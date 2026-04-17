# 19 — Paper not priority

## The claim

The paper is downstream of the work. Writing the paper is not the priority; closing the gap is. The research files that accumulate during the attack phase become the paper later, after the gap is closed. This is a specific scheduling discipline, not an aesthetic preference, and it prevents the common failure mode in which paper-drafting drains attention from the remaining technical work.

## The evidence

G, setting the rule mid-session:

> never mind the paper, it is not a priority, our prioritiy is closing the gap, the research files that we are putting in place are gonna be the actual paper once we close the gap

G, later in the same day, on the same rule applied to the RH run:

> the agent keeps on mentioning a paper becase i thought we had something that was close to a solution for the riemann hypothesis but in reality i can't publish a paper because people are gonna use my own framework to complete the research and get the creadit that we can get fron using the framework itself

G, on the specific discipline when a programme is mid-flight:

> dont update preprint until 10 of 10

G, much earlier, on the same instinct in a different register:

> we can't ignore those errors … we just have to keep progressing like we did this am - run - fix in a cycle until we're down to zero

## The argument

Paper-drafting is seductive. It produces visible, shareable output at a time when the technical work may be yielding none. It consumes context-tokens that would otherwise go to the adversarial runs. It creates a commitment to a particular framing of the results, which then has to be revised every time the technical understanding evolves. Most importantly, a paper in draft invites the drafter to *defend* the current state, which conflicts with the posture needed to find the remaining gaps.

G's rule is to invert the dependency. The paper is a function of the finished work, not a parallel activity. While the work is unfinished, the research files accumulate — research notes, derivations, proof-chain nodes, kill-list entries, prompt–output pairs. When the gap closes, these files already contain the raw material for the paper, and the drafting task becomes one of compression and reorganization rather than composition from scratch. The writing is fast because the material is present.

This is also why the research-file discipline (section 15, section 17) matters so much. Each research file is a durable artifact: it names its source, its prompt, its output, and its status. When the paper is drafted, the author can cite these artifacts internally. When the paper is adversarially reviewed, the reviewer can trace claims back to the research files that produced them. The files *are* the paper, reorganized.

The strong form of the rule — *don't update preprint until 10 of 10* — is the scheduling consequence. The preprint is the public commitment; updating it with intermediate states creates a sequence of public commitments that have to be reconciled. The discipline is to make the preprint match the finished state, and let the research files carry the intermediate states privately. A preprint that is updated every week is a preprint whose author is committing publicly to claims they may have to walk back.

The deeper reason for the rule is motivational. A researcher who is writing the paper in parallel with the work is, psychologically, trying to finish. A researcher who is writing research files while the work continues is, psychologically, trying to understand. The two stances produce different decisions at the point where a reviewer's objection lands: the paper-writer tends to argue around the objection; the researcher tends to re-examine the premise. The programme's discipline favours the second stance by structural means: there is no paper yet, so the defensive register is not available.

The "run-fix in a cycle until we're down to zero" quote extends the same discipline to a different artifact (the LaTeX build). The same principle applies: the compiled PDF is a function of the source; when the source is wrong, the compile is wrong; fix the source, re-compile, until the output state is correct. The paper, like the build, is downstream.

## For future readers

If you find yourself drafting the paper while the work is unfinished, stop. Put the draft energy into research files that will compose themselves into the paper when the work closes. The discipline is hard; it is also what makes the eventual paper short, clean, and defensible.

*Next: [20 — Backticks before scripting](20-backticks-before-scripting.md).*
