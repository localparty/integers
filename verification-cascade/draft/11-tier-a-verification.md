# 11 — Tier A: Verification — Reading with Hostile Intent

---

## The simplest tier, the most common outcome

Most external dependencies will SURVIVE verification. Balaban's polymer expansion has been cited for 40 years without a published correction. Boegli's spectral exactness theorem is clean, focused, and published in a good journal. Bulatov and Zhuk independently proved the same classification — a natural LOCK. Even CCM 2025, despite being a preprint, is authored by a Fields medalist building on 30 years of prior work with striking numerical evidence (10^-1235 coincidence probability).

The verification cascade's Tier A is not expecting to find catastrophic errors. It is expecting to CONFIRM — and to produce the documentation that transforms "we trust this result" into "we have independently tested this result." The difference between trust and testing is the difference between a citation and a verification report.

But Tier A must be genuinely adversarial. If the verification only confirms, it is a rubber stamp, not a test. The ORA's architecture prevents rubber-stamping by construction: Critics are DIFFERENT Claude instances from Authors, the kill list prevents glossing, the honest-first stance (Signature 2) requires every gap to be named, and the Meta-critic independently classifies ambiguous gaps. The verification is real. The expectation of SURVIVED does not weaken the adversarial stance — it sets the baseline that makes WEAKENED and BROKEN findings meaningful.

## The 6-step verification loop

The ORA's standard 6-step method loop (Diagnose / Reinterpret / Unify / Lock / Compute / Verify) was designed for CONSTRUCTION — building new mathematics. For verification, the same 6 steps adapt:

| Step | Construction mode | Verification mode |
|---|---|---|
| **1. Diagnose** | "What is the bottleneck?" | "What does this proof step CLAIM?" |
| **2. Reinterpret** | "Strip the framing — what's the phenomenon?" | "Restate in my own words — do I actually UNDERSTAND the claim?" |
| **3. Unify** | "Find a toolkit element that applies" | "Identify the ASSUMPTIONS — are they stated? Are they correct? Are any hidden?" |
| **4. Lock** | "Prove it" | "Check against PRIMARY SOURCES — does the citation actually say what the proof claims it says?" |
| **5. Compute** | "Run the calculation" | "RE-DERIVE independently — do I get the same result using different methods?" |
| **6. Verify** | "Self-suspect: is my proof wrong?" | "Self-suspect: is my READING wrong? Am I missing something the author intended?" |

Steps 4 and 5 are the load-bearing steps for verification:

**Step 4 (Lock — check against primary sources)** is the I-7 + I-v6-1 discipline applied to external papers. The verifier reads the proof's citations, fetches the primary source, finds the verbatim passage, and checks two things:

1. **Paraphrase check (I-7):** Does the citation match what the primary source actually says? (Quote-level accuracy)
2. **Inference check (I-v6-1):** Does the primary source LOGICALLY ENTAIL the conclusion the proof draws from it, or does it merely NOT CONTRADICT it? (Inference-level accuracy)

The H4 closure programme discovered I-v6-1 the hard way: an Author correctly quoted Paper 13 section 1.5 verbatim but drew the OPPOSITE structural inference from the quote. The quote said "Sections 3-11 are self-contained and do not depend on the CBB axioms." The Author concluded "two-dependency (CCM + CBB)." The quote was faithful. The inference was wrong. I-7 caught the quote. I-v6-1 was born to catch the inference.

For external verification, this discipline is CRITICAL. An external paper may cite a prior result correctly at the quote level but draw a broader conclusion than the cited result supports. The verifier must check BOTH levels.

**Step 5 (Compute — re-derive independently)** is the second route that creates a LOCK. The verifier attempts to prove the same result using DIFFERENT methods — not reading the author's proof, but working from the hypothesis and conclusion alone. If the independent derivation agrees: the result has two routes (the author's and the verifier's), and the LOCK confidence lifts from 7/10 to 9/10. If the independent derivation disagrees: the discrepancy is a finding — either the author's proof has a gap, or the verifier's method has a gap, and a Reconcile primitive (Judge spawn) resolves which.

**Step 6 (Verify — self-suspect the READING)** is unique to verification mode. In construction, self-suspicion asks "is my proof wrong?" In verification, self-suspicion asks "is my READING wrong?" This is the intellectual humility check. Before declaring a step WEAKENED or BROKEN, the verifier must ask: "am I sure I understand what the author intended? Is the gap I found a real gap in the proof, or a gap in my understanding?" This check prevents false negatives — declaring a correct proof broken because the verifier misread it.

## The REFRAME in verification mode

Signature 1 (the reframing reflex) fires at every cycle-open. In construction mode, it asks: "what if the current framing is why this is HARD?" In verification mode, it asks a different question:

> "What if my reading of this proof step is why it looks WRONG?"

This is a subtle but critical shift. In construction, the reframe targets the PROBLEM's framing. In verification, the reframe targets the READER's framing. The proof's framing is the author's — it is what it is. The verifier's job is not to reframe the proof but to understand it correctly and test it honestly.

When a verification REFRAME fires, it produces one of three outputs:

1. **"My reading was wrong — the step is actually correct."** The verifier misunderstood the notation, the convention, or the logical structure. The step is re-classified as SURVIVED. This is the most common REFRAME output in verification — most "gaps" found by AI verifiers are reading errors, not proof errors.

2. **"My reading was correct — the step has a real gap."** The reframe confirms that the verifier understood the proof correctly and the gap is genuine. The step stays WEAKENED or BROKEN. This is the valuable output — a confirmed finding.

3. **"The step is correct but for a DIFFERENT reason than the author states."** The proof reaches the right conclusion via a wrong or incomplete argument. The verifier found a better argument. This is a Tier B excision candidate — the independent derivation in Step 5 may produce a cleaner proof of the same result.

## Parallel dispatch at step level

In construction mode, parallel dispatch is at the LEAD level: N open leads = N parallel Authors. In verification mode, parallel dispatch is at the STEP level: N proof steps = N parallel Verifiers.

For a paper like CCM 2025 with ~30 proof steps across 4 key theorems, the runner dispatches 30 Verifiers in one wave. Each Verifier receives:

- The specific proof step (extracted from the capacitor's H.1 proof chain)
- The capacitor's correspondence table for that step (which domain images exist)
- The capacitor's Six Patterns analysis for that step (which patterns apply)
- The capacitor's kill list (which approaches have failed in this domain)
- The background toolkit (the mathematical tools the step uses)
- The instruction: "execute the 6-step verification loop on this step. Produce SURVIVED / WEAKENED / BROKEN."

All 30 return in parallel. The Synthesis agent cross-checks for consistency: do two Verifiers that worked on adjacent steps agree on shared assumptions? Did any Verifier flag a dependency that another Verifier assumed was valid?

This is where verification outperforms serial reading. A human referee reading a 30-page paper reads sequentially — step 1, then step 2, then step 3. A cross-step inconsistency between steps 5 and 23 might be missed because by the time the referee reaches step 23, the details of step 5 have faded. The parallel ORA catches cross-step inconsistencies by CONSTRUCTION: the Synthesis agent reads all 30 verdicts simultaneously and checks every pair.

## The Verifier + Re-deriver pattern

For each LOAD-BEARING step (marked with * in the capacitor's proof chain), the runner dispatches BOTH:

- A **Verifier** (Critic role): reads the author's proof and checks it step by step using the 6-step verification loop. Goal: determine if the author's argument is correct.

- A **Re-deriver** (Author role): receives the step's hypothesis and conclusion but NOT the author's proof. Attempts to prove the same result independently, using the capacitor's Six Patterns, correspondence tables, and grammar as tools. Goal: produce an independent proof.

When both return:

| Verifier says | Re-deriver says | Combined verdict | Action |
|---|---|---|---|
| SURVIVED | Proved (same result, different method) | **LOCKED** — two independent routes | Confidence 9/10. Record both proofs. |
| SURVIVED | Failed to prove | SURVIVED but no LOCK | Confidence 7/10. The author's proof stands but has only one route. |
| WEAKENED | Proved (different method) | **EXCISION CANDIDATE** | The author's proof has a gap but an independent proof exists. Tier B may be immediate. |
| WEAKENED | Failed to prove | **WEAKENED** | The gap is real and no independent route was found. Document. Assess impact. |
| BROKEN | Proved (different method) | **CRITICAL FINDING + EXCISION** | The author's argument is fatally flawed but the result is independently provable. The dependency can be replaced. |
| BROKEN | Failed to prove | **BROKEN** | Fatal gap. No independent route. Escalate to Tier B (focused excision) or Tier C (reroute). |

The Verifier + Re-deriver pattern is the LOCK mechanism (Signature 10) applied to verification. Two independent routes to the same result — or two independent confirmations that the result breaks — produce higher confidence than either agent alone.

## What verification produces

A completed Tier A verification produces:

**1. A per-step verdict table:**

```
| Step | Type | Status | Verifier | Re-deriver | Combined | Notes |
|---:|---|---|---|---|---|---|
| 1 | Definition | SURVIVED | confirmed | n/a | SURVIVED | Standard definition, no issues |
| 2* | Theorem | SURVIVED | confirmed | proved (alt) | LOCKED | Two independent proofs |
| 3* | Lemma | WEAKENED | gap in step 3c | failed | WEAKENED | Hidden assumption about... |
| ... | ... | ... | ... | ... | ... | ... |
```

**2. A kill list for the verified domain** (any approaches the Verifiers or Re-derivers tried and abandoned).

**3. Updated correspondence table entries** (any cross-domain connections discovered during verification).

**4. An overall verdict:** SURVIVED (all load-bearing steps verified, chain is sound), WEAKENED (gaps found, repairable), BROKEN (fatal gap, chain needs repair or rerouting).

**5. Escalation assessment:** if WEAKENED or BROKEN, which steps need Tier B excision, and which pre-identified escalation routes are most promising.

All of this is merged into the capacitor (self-adjust + trim) and the capacitor version increments. The next wave — whether a re-verification of weakened steps or an escalation to Tier B — starts from the UPDATED capacitor.

---

*Verification is reading with hostile intent — but also with intellectual humility. The 6-step verification loop: diagnose the claim, restate it, identify assumptions, check sources, re-derive independently, self-suspect the reading. Parallel dispatch at step level: N steps, N verifiers, cross-step consistency checked by Synthesis. The Verifier + Re-deriver pattern: two independent routes produce LOCKed confidence. SURVIVED is the expected outcome. WEAKENED or BROKEN is the valuable finding. Either way: the result is no longer trusted — it is tested.*
