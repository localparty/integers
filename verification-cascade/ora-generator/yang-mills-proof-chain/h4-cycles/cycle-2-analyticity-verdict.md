# Cycle 2: Analyticity Verdict -- Resolving the Agent A / Agent B / Tier C Dispute

*ORA Critic agent. Date: 2026-04-13.*
*Task: adjudicate the disagreement on whether (B1) closes H4.*
*Sources examined: cycle-1-k0-sector.md (Agent A), cycle-1-polymer-content.md (Agent B), 05-construction-verdict.md (Tier C), 06-capacitor-patch.md (Tier C self-criticism), Appendix H (preprint), PROOF-CHAIN.md.*

---

## 0. Executive summary

**Agent B is correct on the core technical point.** (B1) is analyticity in the field variable V, not in the coupling g_k. Agent A's argument contains a load-bearing error at the point where it asserts K_k(X,V) is "analytic in g_k^2 on a disk |g_k^2| < rho" -- this is not what (B1) says, and the claim is not established by Balaban's construction.

**However, the Tier C refined argument (after self-criticism in 06-capacitor-patch.md) is substantially sound**, though it requires tightening at two specific points. The refined argument avoids the analyticity-in-g_k claim entirely and works at fixed g_k with polymer bounds + Reisz matching. This is the correct path.

**Confidence in the refined Tier C argument: 0.60.** The main risk is not a structural error but insufficient rigor in the matching step (Question 2 below).

---

## 1. What does (B1) actually say?

Reading the preprint's Appendix H (file: `H-balaban-analyticity.md`), the statement is unambiguous:

> **(B1)** The small-field effective action S_k[V] is analytic in the block link variables V_l, with k-independent radius of analyticity.

Section 2.1 of Appendix H elaborates: Balaban's Main Estimate (CMP 109, Theorem 1) gives |K_k(X,V)| <= e^{-kappa|X|} with kappa independent of k. The analyticity is in V (the gauge field configuration), with the radius rho determined by invertibility of S_k^{(2)}[V], convergence of the Mayer expansion, and the averaging kernel geometry -- all k-independent.

Section 5.1 of Appendix H provides an honest inventory. Under "What Balaban's papers explicitly contain":
- Propagator analytic in V in small-field region: ESTABLISHED
- Polymer activities analytic in link variables: IMPLICIT in construction
- Analyticity radius k-independent: IMPLICIT

Nowhere does Balaban, or the preprint's extraction of Balaban, claim analyticity in g_k or g_k^2 as a complex parameter. The coupling g_k appears in the effective action as the coefficient 1/g_k^2 of S_YM[V] -- it parametrizes the theory, not the domain of K_k.

**Verdict on Question 1: (B1) is analyticity in V. Agent A's restatement of (B1) as "analytic in g_k^2 on |g_k^2| < rho" is an error.**

---

## 2. Does the functional integral introduce an essential singularity in g_k?

**Yes.** Agent B's analysis (Section 3.1 of cycle-1-polymer-content.md) is correct on this point. The Boltzmann weight is:

e^{-S_k[V]} = e^{-S_YM[V]/g_k^2} * e^{-sum_X K_k(X,V)}

The factor e^{-S_YM[V]/g_k^2} has an essential singularity at g_k = 0. For any gauge field configuration V with S_YM[V] > 0 (which is generically true), this factor is not analytic in g_k at the origin. The functional integral inherits this non-analyticity.

Agent A's counter-argument (Section 1.7 of the k0-sector analysis) attempts to circumvent this by claiming that the RG construction absorbs the 1/g_k^2 factor step by step, so that the effective action at each scale is analytic in g_k^2. This is the central error in Agent A's reasoning. Let me dissect it.

### Agent A's error in detail

In Section 1.4, Agent A writes:

> From (B1), the polymer activities K_k(X,V) are analytic in g_k^2 on a disk |g_k^2| < rho, with rho > 0 independent of k.

This is NOT what (B1) says. (B1) says K_k(X,V) is analytic in V. Agent A then applies Cauchy estimates in the g_k^2 variable to get remainder bounds -- but the Cauchy estimates are in the wrong variable.

In Section 1.8, Agent A attempts to argue that the RG composition preserves analyticity in g_k^2:

> Each RG step maps analytic functions to analytic functions. [...] (B1) says: the radii do NOT shrink.

But (B1) says the radii in V do not shrink. Agent A has silently substituted "analyticity in g_k^2" for "analyticity in V" and then applied (B1)'s k-independence claim to the wrong variable.

In Section 4.4, Agent A acknowledges the subtlety ("the disk of analyticity in g_0^2 shrinks with the number of RG steps K") but then argues the issue is resolved by working with the renormalized coupling g_R^2 instead of the bare coupling. This is a valid observation about the physics but does not establish analyticity in g_R^2 -- it merely parametrizes the unknown radius of analyticity (if any) in terms of a different coupling.

### The key confusion

Agent A conflates two distinct objects:

1. The Taylor expansion of K_k(X,V) in powers of (V - 1), which converges by (B1).
2. The Taylor expansion of K_k(X,V) in powers of g_k^2, which would require a separate proof.

The former is established. The latter is what H4 needs (after functional integration). These are not the same expansion, and convergence of one does not imply convergence of the other.

**Verdict on Question 2: Agent B is correct. The e^{-S_YM/g_k^2} factor introduces a genuine essential singularity. Agent A's claim that the Balaban RG absorbs this singularity is not substantiated by (B1).**

---

## 3. Is the Tier C refined argument sound?

The Tier C analysis (05-construction-verdict.md) initially makes the SAME error as Agent A -- claiming analyticity in g_k^2 from (B1). However, the self-criticism in 06-capacitor-patch.md catches this error explicitly:

> **WAIT.** This is a serious concern. The e^{-(1/g_k^2) S_YM} factor in the Boltzmann weight introduces a non-analytic dependence on g_k at g_k = 0.

The revised argument in 06-capacitor-patch.md then pivots to a different strategy that does NOT require analyticity in g_k. The revised chain is:

1. Balaban RG gives g_k -> 0 (Steps 12-14, unconditional).
2. Balaban polymer bounds give |K_k(X,V)| <= e^{-kappa|X|} (Step 3, unconditional).
3. Gradient-flow coupling g_GF^2(t) defined at each t > 0 (Steps 15-16, unconditional).
4. Tree-level + Reisz matching: g_GF^2(c a_k^2) = g_k^2 [1 + O(g_k^2) + O(e^{-kappa})].
5. Trace anomaly: gamma = -beta/g (L.3(v), unconditional).
6. Callan-Symanzik: S_2 ~ |x|^{-8} (g^2(1/|x|))^{-1} (structural).

**This is a fundamentally different argument from the original Tier C claim.** It works at FIXED g_k at each RG scale and never claims analyticity of any observable in g_k as a complex variable.

### Assessment of each step

**Step 1 (g_k -> 0):** Unconditional. Proved in the proof chain. No dispute.

**Step 2 (polymer bounds):** Unconditional. This is Balaban's main estimate. No dispute.

**Step 3 (gradient-flow coupling exists):** Unconditional. Steps 15-16 of the proof chain. No dispute.

**Step 4 (matching): THIS IS THE LOAD-BEARING STEP.** The claim is:

> g_GF^2(c a_k^2) = g_k^2 [1 + O(g_k^2) + O(e^{-kappa})]

This requires three things:
(a) At tree level (g_k = 0, Gaussian theory), the gradient-flow action density <E(t)> gives g_GF^2 = g_k^2. This is a Gaussian computation and is standard.
(b) The O(g_k^2) correction is the one-loop perturbative correction. By Reisz's power-counting theorem, the lattice one-loop correction matches the continuum one-loop correction. This is ESTABLISHED.
(c) The O(e^{-kappa}) correction comes from polymer contributions beyond perturbation theory. These are controlled by the polymer decay bound.

**Concern with (c):** The polymer decay bound |K_k(X,V)| <= e^{-kappa|X|} bounds the activity of each cluster. To get the contribution to <E(t)>_k, one needs to evaluate the functional integral with the polymer-modified Boltzmann weight. The claim that the non-perturbative contribution to <E(t)>_k is O(e^{-kappa}) relies on:
- The polymer clusters that modify the action at the measurement point are exponentially suppressed.
- The functional integral over the remaining field configurations is Gaussian to leading order.

This is plausible and consistent with the standard constructive QFT framework, but the step from "polymer activities are bounded" to "expectation values have bounded non-perturbative corrections" requires a cluster expansion argument for the correlator itself, not just for the action. The Balaban framework provides the tools for this, but the argument needs to be made explicitly.

**My assessment: CLOSABLE but not yet closed. The gap is technical, not structural.**

**Step 5 (trace anomaly):** This is an operator identity proved unconditionally in L.3(v). No dispute.

**Step 6 (Callan-Symanzik):** The non-perturbative Callan-Symanzik equation requires:
(a) A smooth running coupling g(mu). The gradient-flow coupling provides this for t > 0 (hence mu > 0). Verified.
(b) The RG equation holds non-perturbatively. This follows from the Ward identity associated with scale transformations in the Balaban-renormalized theory. Standard.
(c) The anomalous dimension is determined by the trace anomaly. Unconditional from L.3(v).

**My assessment: SOUND. The Callan-Symanzik equation is structural.**

### Overall assessment of the refined Tier C argument

The argument avoids Agent A's error (no analyticity in g_k claimed) and avoids Agent B's wall (no need to bridge V-analyticity to g-analyticity). It works within the Balaban framework using only:
- Polymer bounds (unconditional)
- RG flow (unconditional)
- Reisz matching (literature)
- Trace anomaly (unconditional)

**The one genuine gap is Step 4(c): controlling the non-perturbative correction to the gradient-flow coupling via the polymer expansion.** This is a cluster expansion argument within Balaban's framework. It is not trivial, but it uses established techniques. I classify it as CLOSABLE.

**Verdict on Question 3: The refined Tier C argument is substantially sound. It avoids both agents' concerns. The residual gap (Step 4(c)) is technical, not structural, and is closable within Balaban's framework.**

---

## 4. Is the "Wilsonian PT vs standard PT" distinction valid?

Agent A (Section 4.4 and onward in the k0-sector analysis) makes a distinction between:
- Standard perturbation theory in the bare coupling g_0 (expected divergent, IR renormalons, n! growth)
- Wilsonian perturbation theory at scale k in the running coupling g_k (claimed convergent by (B1))

**This distinction is physically meaningful but Agent A draws the wrong mathematical conclusion from it.**

The physical content: In the Wilsonian effective theory at scale k, all modes below the cutoff Lambda_k have been integrated out. The effective action S_k includes their effects non-perturbatively (via the polymer expansion). The remaining degrees of freedom are UV modes, which are weakly coupled when g_k is small.

Agent A's claim: the Wilsonian effective action K_k is analytic in g_k^2 (a convergent power series in g_k^2). This would mean the Wilsonian perturbative expansion converges, unlike the standard perturbative expansion.

**The problem:** Even in the Wilsonian framework, the effective action at scale k contains the factor 1/g_k^2 multiplying S_YM. When computing expectation values, this produces the same e^{-S_YM/g_k^2} essential singularity that plagues standard perturbation theory. The Wilsonian framework REORGANIZES the perturbative expansion (improving its behavior at each order) but does not make it convergent in g_k as a complex variable.

What IS true: At each RG step, the integration over one momentum shell is a convergent operation (the Gaussian integral with polymer corrections is well-defined). The output K_{k+1} depends on g_k in a controlled way. But "controlled" does not mean "analytic in g_k on a disk." It means the polymer activities have uniform bounds at each fixed value of g_k.

**Verdict on Question 4: The Wilsonian vs standard PT distinction is physically valid and mathematically meaningful. But Agent A's conclusion -- that Wilsonian PT converges as a power series in g_k^2 -- is the same error discussed in Questions 1-2. The Wilsonian framework provides better bounds at each fixed g_k; it does not provide analyticity in g_k.**

---

## 5. Where each agent goes wrong

### Agent A (k=0 sector): ERROR at the foundation

The entire argument rests on the claim "(B1) gives analyticity of K_k in g_k^2." This is false. (B1) gives analyticity in V. The rest of the argument (Cauchy estimates, convergent perturbative expansion, continuum limit interchange) follows logically FROM the false premise but is therefore unsound.

Agent A's self-examination (Section 4.3, "Critical evaluation") identifies the right worry ("Potential gap 2: Correlator analyticity from polymer analyticity") but then dismisses it too quickly. The argument that "the RG beta function gives g_k^2 = g_0^2/(1 + ...) which IS analytic in g_0^2 for |g_0^2| small" is correct for the COUPLING RECURSION but does not establish that EXPECTATION VALUES are analytic in g_0^2. The coupling recursion is a finite-dimensional (one-variable) recursion; the expectation value is an infinite-dimensional functional integral.

**Confidence in Agent A's original claim: <= 0.05.** The core assertion is wrong.

### Agent B (polymer content): CORRECT diagnosis, OVERLY PESSIMISTIC conclusion

Agent B correctly identifies the variable-mismatch obstruction and correctly assigns low probability (p <= 0.03) to the "analyticity in g_k" route. The structural diagnosis (Section 5.2) is precise and well-argued.

However, Agent B concludes with "The wall stands" -- implying that NO route from polymer analyticity to H4 exists. This is too strong. Agent B did not consider the possibility (discovered by Tier C's self-criticism) of working at FIXED g_k with polymer bounds and Reisz matching, without ever claiming analyticity in g_k.

Agent B's framing locks onto the question "can we get analyticity in g_k?" and, having shown the answer is no, declares all approaches blocked. But the question H4 actually needs answered is "does g_GF^2(t) -> 0 with the correct rate and does this transfer to the correlator?" -- which does not require analyticity in g_k.

**Confidence in Agent B's structural diagnosis: 0.95.** The variable-mismatch obstruction is real.
**Confidence in Agent B's pessimistic conclusion ("the wall stands"): 0.30.** The refined Tier C argument sidesteps the wall.

### Tier C (construction verdict + self-criticism): MOSTLY CORRECT after self-repair

The initial Tier C argument (05-construction-verdict.md) makes the same error as Agent A: claiming "analyticity in g_k kills non-perturbative corrections." Confidence in the initial claim: <= 0.10.

The self-criticism (06-capacitor-patch.md) correctly identifies the error, correctly diagnoses why the initial claim is too strong, and correctly pivots to the refined argument (polymer bounds + Reisz matching at fixed g_k). The self-criticism is a model of honest assessment.

The refined argument is substantially sound but has the CLOSABLE gap at Step 4(c) (non-perturbative correction to the gradient-flow coupling via cluster expansion).

**Confidence in the refined Tier C argument: 0.60.**

The 0.40 uncertainty decomposes as:
- 0.15: Step 4(c) might be harder than it looks (the cluster expansion for correlators, as opposed to the action, might have complications in the gradient-flow context).
- 0.10: The Callan-Symanzik argument at the non-perturbative level might have subtleties in the lattice-to-continuum passage.
- 0.10: The Reisz matching might require more than just power-counting (scheme-dependent finite renormalizations could affect the rate).
- 0.05: Unknown unknowns.

---

## 6. Final verdict

| Agent | Core claim | Verdict | Confidence in their claim |
|-------|-----------|---------|--------------------------|
| A (k=0 sector) | (B1) gives analyticity in g_k^2, hence convergent PT | **WRONG** -- (B1) is analyticity in V, not g_k | <= 0.05 |
| B (polymer content) | Variable mismatch blocks all polymer routes to H4 | **RIGHT on diagnosis, WRONG on conclusion** -- the refined argument avoids the mismatch | 0.95 on diagnosis, 0.30 on "wall stands" |
| Tier C (initial) | Analyticity in g_k kills non-perturbative corrections | **WRONG** -- same error as Agent A | <= 0.10 |
| Tier C (refined) | Fixed-g_k polymer bounds + Reisz matching gives AF | **SUBSTANTIALLY SOUND** with one CLOSABLE gap | 0.60 |

### Recommendation

**Adopt the refined Tier C argument as the working candidate for Step 18'.** Do NOT use the "analyticity in g_k" framing anywhere in the preprint -- it is wrong. The correct framing is:

> The Balaban polymer bounds and the Reisz power-counting theorem together control the matching between the gradient-flow coupling and the Balaban running coupling at each RG scale. The AF behavior of g_k (proved unconditionally) transfers to g_GF^2(t) with sub-leading corrections. The trace anomaly and Callan-Symanzik equation then give the short-distance OPE.

The remaining work is to close Step 4(c): a cluster expansion argument showing that the non-perturbative contribution of the polymer activities to the gradient-flow action density is O(e^{-kappa}) relative to the perturbative value. This is a standard constructive QFT calculation within the Balaban framework.

### Status of H4

**Upgraded from BLOCKED to CLOSABLE.** The refined Tier C argument provides a viable path that avoids all identified walls. The path requires one technical step (Step 4(c)) that is within the scope of Balaban's machinery but has not been written out.

**NOT YET UNCONDITIONAL.** The argument is not yet a proof. It is a detailed proof strategy with one CLOSABLE gap. Claiming it is unconditional at this stage would be premature.

---

## 7. Corrections to prior documents

| Document | Correction needed |
|----------|------------------|
| 05-construction-verdict.md | The core argument (Section "Proof chain", point 1) falsely claims "expectation values are analytic functions of g_k^2 with convergent Taylor series." This must be excised. Replace with the refined argument from 06-capacitor-patch.md. |
| 05-construction-verdict.md | Card 15 ("Balaban analyticity kills non-perturbative corrections") must be DOWNGRADED or KILLED. The claim that "there are no corrections of the form e^{-c/g_k^2} because such functions are not analytic at g_k = 0" is wrong -- the full theory IS non-analytic at g_k = 0 due to the Boltzmann weight. |
| 05-construction-verdict.md | Card 16 ("Effective vs bare PT distinction") is a valid observation but its conclusion ("effective PT is convergent by Balaban") must be weakened to "effective PT has controlled errors at each fixed g_k by Balaban polymer bounds." |
| cycle-1-k0-sector.md | The entire argument is built on a false premise (analyticity of K_k in g_k^2). It should be marked as SUPERSEDED by the refined Tier C argument. The self-critical sections (4.3, 4.4) correctly identify the subtleties but resolve them incorrectly. |
| 06-capacitor-patch.md | The revised assessment is correct. The honest caveats (Critic Questions 1-3) are well-posed and the resolutions are sound. This document should be promoted to the primary reference for Step 18'. |

---

## 8. Kill list update

| Kill # | Name | Reason |
|--------|------|--------|
| K-5 | Analyticity in g_k from (B1) | (B1) is analyticity in V, not g_k. The Boltzmann weight e^{-S_YM/g_k^2} introduces an essential singularity at g_k = 0 that is not controlled by the polymer expansion. Agent A's argument and the initial Tier C argument both fail at this point. Any future argument that claims "(B1) implies analyticity in g_k" should be immediately rejected. |

### Re-entry gate for K-5

Could be reopened ONLY if someone proves that the Balaban effective action (after integrating out all modes, i.e., the full partition function) is Borel-summable in g^2 and the Borel sum equals the non-perturbative answer. This would require a constructive proof of resurgence within the Balaban framework -- a major independent advance with no precedent.

---

*Cycle 2 complete. Dispute resolved: Agent B wins on the diagnosis, Tier C (refined) wins on the constructive path forward. The wall identified by Agent B is real but can be walked around, not through.*
