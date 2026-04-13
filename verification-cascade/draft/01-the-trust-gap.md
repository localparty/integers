# 01 — The Trust Gap in Modern Mathematics

---

## The referee bottleneck

Mathematics has a verification problem. Not a proof problem — a *trust* problem.

When Grigori Perelman posted his proof of the Poincare conjecture on arXiv in 2002-2003, the mathematical community took three years to verify it. Three separate teams — Kleiner-Lott, Morgan-Tian, and Cao-Zhu — each produced hundreds of pages of detailed verification before the Clay Institute could declare the problem solved. Perelman himself refused the prize. The proof was correct. The verification took longer than the proof.

When Andrew Wiles announced his proof of Fermat's Last Theorem in 1993, a gap was found by Nick Katz during refereeing. Wiles and Richard Taylor spent 14 months repairing the gap. The proof was eventually correct — but the repair cycle cost a year. The gap was not in Wiles's own mathematics. It was in the interaction between Wiles's methods and an external result he depended on (the Euler system argument). A dependency that nobody had independently tested before submission.

When Shinichi Mochizuki posted his claimed proof of the abc conjecture in 2012, the mathematical community has spent over a decade unable to reach consensus on whether it is correct. Peter Scholze and Jakob Stix identified what they consider a fundamental gap in Corollary 3.12 of IUT III. Mochizuki disagrees. The proof has been published in a journal Mochizuki edits. As of 2026, the community remains divided. The proof may be correct. The verification has failed — not because the mathematics is too hard, but because the trust infrastructure collapsed.

These are not isolated cases. They are symptoms of a structural problem: **as proofs grow in length, complexity, and dependency on external results, the gap between "proof exists" and "proof is trusted" widens.** The Clay Millennium Prize requires crossing that gap. A proof that cannot be verified cannot be awarded.

## The dependency problem

Every serious mathematical proof depends on prior results. Wiles depended on the modularity theorem (which itself depended on decades of work by Langlands, Tunnell, Ribet, and others). Perelman depended on Hamilton's Ricci flow programme (20 years of prior work). Any proof of the Yang-Mills mass gap depends on Balaban's polymer expansion (1984-1998, never independently verified). Any approach to RH through Connes's programme depends on CCM 2025 (a preprint, not yet peer-reviewed).

Each dependency is a **trust boundary**. When a proof says "by Theorem X of [Author]," the referee must either:

1. **Trust the citation** — accept that [Author]'s Theorem X is correct without checking it. This is how most mathematics works. It is also how errors propagate silently.

2. **Verify the citation** — read [Author]'s paper, check the proof of Theorem X, and confirm it says what the proof claims it says. This is what referees are supposed to do. It is also why refereeing a Clay submission takes years.

3. **Replace the citation** — prove Theorem X independently, eliminating the dependency entirely. This is the strongest option. It is also the rarest, because it requires the referee to do original mathematical work.

The verification cascade does all three — systematically, adversarially, and at scale.

## The cost of unverified dependencies

Consider the dependency map of the four proof chains in the QG5D framework:

| Paper | Chain length | Unconditional | Key external dependency | Status of dependency |
|---|---|---|---|---|
| Paper 8 (Yang-Mills) | 18 steps | 17 (94%) | Balaban polymer expansion (CMP 1984-98) | Published, peer-reviewed, **never independently verified in 40 years** |
| Paper 13 (Riemann Hypothesis) | 6 layers | 5 (83%) | CCM 2025 spectral realization (arXiv:2511.22755) | **Preprint, not yet peer-reviewed** |
| Paper 26 (BSD) | 11 steps | 10 (91%) | CBB axioms (Paper 23) | Framework axioms, supported by 36 zero-parameter predictions (P < 10^-89) |
| Paper 28 (P vs NP) | 6 links | 5 (83%) | Bulatov-Zhuk CSP dichotomy (FOCS 2017, JACM 2020) | Published at top venues, **never formally verified** |

Every one of these dependencies is a point where a Clay referee could say: "I cannot verify your proof because I cannot verify the result you depend on." And they would be right. The referee's job is not to trust — it is to verify.

The traditional response to this is: "well, Balaban's work is published and peer-reviewed." True. But "published and peer-reviewed" is not the same as "independently verified." Mochizuki's IUT is published and peer-reviewed. The community still does not trust it. Publication is necessary but not sufficient for trust at the frontier.

## The verification cascade as the answer

The verification cascade inverts the traditional submission model. Instead of:

> "Here is our proof. Please verify it. Please also verify every result we depend on. This will take you years."

The cascade says:

> "Here is our proof. We have ALREADY adversarially verified every result we depend on. Here are the verification reports. Here is the kill list — what we tested and how. Here is the audit trail. Check our verification, not our dependencies."

This is a fundamentally different submission. The referee's job changes from "verify everything from scratch" to "verify the verification system." The system itself is testable — its methods are documented, its predictions are pre-registered, its failures are honestly reported.

The key insight: **the cost of verification is paid once by the prover, not repeatedly by every referee.** A Clay submission with a verification cascade saves the mathematical community years of redundant effort. The prover does the hardest work — testing their own foundations — before the referees see the proof.

## What this requires

Building a verification cascade requires:

1. **An adversarial verification system** that can read mathematical papers, extract proof chains, test each step, and produce honest verdicts (SURVIVED / WEAKENED / BROKEN). This is the ORA.

2. **Domain-specific memory** that gives the verification system compiled knowledge about each dependency — what's been tried, what works, what doesn't, and where to look. This is the capacitor.

3. **Escalation capability** — when verification finds a weakness, the system can attempt independent re-derivation (excision) or find alternative routes (construction). This is the three-tier protocol.

4. **Cross-domain creativity** — the ability to find pathways between mathematical disciplines that provide fresh angles for verification and alternative proofs. This is the correspondence table engine, powered by the framework's 39+ transposed mathematical domains.

5. **Honest reporting** — every finding documented, every failure named, every correction applied. The kill list is the credibility. A verification cascade that hides its negative results is worse than no cascade at all.

No previous Clay submission has included any of these. The verification cascade is a new kind of mathematical artifact — a proof's immune system, published alongside the proof.

---

*The trust gap is real. Proofs that take years to verify are proofs that cannot be trusted in time. Dependencies that nobody checks are dependencies that can break silently. The verification cascade closes the gap — not by making proofs simpler, but by making their foundations transparent.*
