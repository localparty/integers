# Cross-Consistency Verification Report

Referee: automated cross-check (2026-04-05)

---

## 1. Internal Consistency of Claims

### 1.1 Abstract vs. Conclusion

- [x] Both claim $SU(N)$ lattice mass gap $\Delta > 0$ at all physical couplings: **consistent**.
- [x] Both claim continuum limit $\Delta_\infty > 0$ conditional on three [VERIFY] items: **consistent**.
- [x] Both reference Section 5.6 and Appendix H for the proof chain: **consistent**.
- [x] Both describe [VERIFY] items as "reading exercises from Balaban's published construction (CMP 109, 1987)": **consistent**.
- [x] Summary tables match: lattice results marked **Proved**, continuum limit marked **Proved (conditional on [VERIFY])**: **consistent**.
- [x] Quantitative predictions (string tension 437 MeV, glueball $0^{++}$, Luscher coefficient): abstract and conclusion Section 12.5 agree.
- [x] The SU(2) independent proof via 2D Yang-Mills on $S^2$: mentioned in both abstract and conclusion.

**Verdict: Abstract and conclusion are internally consistent. No overclaims detected between them.**

### 1.2 PROOF-CHAIN.md vs. Section 5.6 (Table IV.1)

Comparing the 14-step proof chain tables side by side:

| Step | PROOF-CHAIN.md Source | Section 5.6 Source | Match? |
|:-----|:----------------------|:-------------------|:-------|
| 1 | 04-lattice-mass-gap.md | Section 4 | Equivalent (different naming convention) |
| 2 | CMP 109, 119 | CMP 109, 119 | Exact |
| 3 | CMP 109, Thm 2.1 | CMP 109, Thm 2.1 | Exact |
| 4 | Extraction from CMP 95--109 | Extraction from CMP 95--109 | Exact |
| 5 | Standard complex analysis | Standard complex analysis | Exact |
| 6 | single-step-case-b.md | Section 5.3.1 | Equivalent |
| 7 | conj-1-closing.md, Lemma 2.1 | Algebraic identity | **Minor mismatch** |
| 8 | two-deriv-spectral-lemma.md, Sec 4 | Section 5.5.4 | Equivalent |
| 9 | Part III, Sec III.3 | Part III, Sec III.3 | Exact |
| 10 | (B1) + classification | (B1) + classification | Exact |
| 11 | Spectral lemma + Step 10 | Spectral lemma + Step 10 | Exact |
| 12 | rg-preservation.md | Section 5.4 | Equivalent |
| 13 | rg-preservation.md, Sec 6 | Section 5.4.6 | Equivalent |
| 14 | 09-continuum-limit.md | Section 5.7 | Equivalent |

**FINDING (MINOR):** PROOF-CHAIN.md uses working-document filenames (e.g., `single-step-case-b.md`, `conj-1-closing.md`, `rg-preservation.md`, `09-continuum-limit.md`) while Section 5.6 uses section numbers. These appear to be the same content under different naming conventions -- the PROOF-CHAIN.md was evidently assembled from the working directory while Section 5.6 uses preprint-internal references. Step 7 shows the largest discrepancy: "conj-1-closing.md, Lemma 2.1" vs. "Algebraic identity" -- both describe the Newton decomposition result, but the labels differ. Not a logical gap, but a cosmetic inconsistency that should be harmonized before submission.

**Status columns match exactly** in all 14 steps. No status inflation between the two tables.

The IV.2 (Classification of arguments) and IV.3 (Items requiring verification) sections are **verbatim identical** between PROOF-CHAIN.md and Section 5.6.

### 1.3 [VERIFY] Items -- Cross-File Consistency

The three [VERIFY] items appear in the following files:

| File | V1: Polymer activity analyticity | V2: Kernel complexification | V3: Dim-6 projection exact | Consistent? |
|:-----|:-|:-|:-|:---|
| 00-abstract.md | "Three reading exercises from Balaban's published construction (CMP 109, 1987)" -- not itemized individually | | | Aggregate reference only |
| 05-continuum-limit.md (Sec 5.6, IV.3) | Yes, full statement | Yes, full statement | Yes, full statement | **Canonical** |
| PROOF-CHAIN.md (IV.3) | Yes, full statement | Yes, full statement | Yes, full statement | **Verbatim match** with Sec 5.6 |
| 06-referee-objections.md (Obj G) | References "Sections 5.6, Parts I-II" and "three reading exercises" | | | Aggregate reference |
| 08-conclusion.md (Sec 12.2) | Describes all three: "analyticity of individual polymer activities, $k$-independence of the analyticity radius, and exactness of the dimension-6 projection" | | | **Consistent** |
| H-balaban-analyticity.md (Sec 5.2) | Yes, all three classified with same descriptions | | | **Consistent** |

**FINDING:** The three [VERIFY] items are consistently identified everywhere they appear. The detailed statements in PROOF-CHAIN.md and Section 5.6 are verbatim identical. The abstract, conclusion, and Appendix H all describe them consistently as "reading exercises from Balaban's published construction."

**One subtlety:** PROOF-CHAIN.md IV.2 lists only **two** items as [VERIFY] in the classification table (polymer activities analytic; radius $k$-independent) while IV.3 lists **three** (adding: dimension-6 projection is exact). However, in the IV.2 table the third item ("Complexification to $\mathrm{SL}(N,\mathbb{C})$") is classified as "Standard complex analysis" rather than [VERIFY]. This is consistent with the V2 item being about the block-spin kernel specifically, not the full complexification. The distinction is correct: V2 is about a specific analytic property of the $A \mapsto A(A^\dagger A)^{-1/2}$ map, while the IV.2 complexification entry is about the general complex-analytic extension. No inconsistency.

### 1.4 Section 6 (Referee Objections) -- Resolution References

| Objection | Claimed Resolution | Verified Location | Correct? |
|:----------|:-------------------|:------------------|:---------|
| A: Vacuum subtraction | Operator identity disproved; spectral intermediate-state | Section 5.2.4 (disproved), Section 5.5 (correct mechanism) | **Yes** |
| B: Parity of $E_k$ | Theorem 6(a) proves parity vanishing | Section 5.2.3, Theorem 6(a) | **Yes** |
| C: Locality and support radius | $R_O$ is $O(1)$ in block lattice units | Section 5.6, Part I, Step (c) | **Yes** |
| D: Momentum-space convolution | Replaced by spectral intermediate-state | Section 5.5, Appendix G | **Yes** |
| E: First-order perturbation theory | RG recursion 1/4 contraction | Section 5.4 | **Yes** |
| F: Inductive stability | Recursion stable fixed point; stability of excitation number | Section 5.4, Section 5.6 Part III | **Yes** |
| G: Balaban applicability to KK theory | Status: [VERIFY] | Sections 5.6 Parts I-II, Appendix H | **Yes -- correctly flagged as [VERIFY]** |

**Verdict: All seven objection resolutions correctly reference the locations where the resolutions appear. Objection G is honestly marked [VERIFY] rather than RESOLVED.**

---

## 2. Complete Proof Chain -- No Gaps

### 2.1 Lattice Chain: Theorem 1 through Theorem 5

**Theorem 1** (Weitzenboeck spectral gap): $\mu_1 \geq 6/r_3^2$ on $\mathbb{CP}^{N-1}$.
Source: Riemannian geometry, positive Ricci curvature of Fubini-Study metric.
Status: Self-contained proof in Section 4.2. **No external dependency.**

**Theorem 1 $\to$ Theorem 2** (bond activity bound): $|g_b| \leq C_0 e^{-m_1 a}$ with $m_1 = 2\sqrt{3}/r_3$.
- [x] Theorem 2 explicitly uses $\lambda_1^{(1)} = 12/r_3^2$ from Theorem 1 (line 511 of Section 4).
- [x] The KK propagator bound $Ce^{-m_1 a}$ is derived from the spectral gap.
**Arrow verified: clear logical implication, hypotheses provided.**

**Theorem 2 $\to$ Theorem 3** (cluster expansion convergence): Kotecky-Preiss criterion.
- [x] Theorem 3 uses the bond constant $C_0$ from Theorem 2 (line 528 of Section 4).
- [x] Convergence condition $2\beta < m_1 a/6 - \ln(c_d K C_0^{1/6})$ is stated.
**Arrow verified.**

**Theorem 3 $\to$ Theorem 4** (lattice mass gap): $\sigma > 0$, $\Delta > 0$.
- [x] Theorem 4 proof part (a) invokes Theorem 1, 2, and 3 explicitly (lines 695-702).
- [x] String tension positivity follows from convergent cluster expansion.
- [x] Mass gap from Fredenhagen-Marcu theorem applied to $\sigma > 0$.
**Arrow verified.**

**Theorem 4 $\to$ Theorem 5** (IR equivalence / decoupling):
- [x] Theorem 5 uses $\sigma_{\mathrm{KK}} > 0$ from Theorem 4 and its corollary (line 829).
- [x] Transfers mass gap to standard SU(N) theory via decoupling of KK modes.
- [x] Requires $m_1 a \gg 1$, same regime as Theorem 4.
**Arrow verified.**

**Lattice chain verdict: Complete, no gaps. Each theorem explicitly references and uses the output of its predecessor.**

### 2.2 Continuum Chain

**Starting point:** $\Delta_0 > 0$ (Theorem 4, lattice proof).

**Balaban (literature) $\to$ Theorem 6(a):**
- [x] Balaban's bound $\|E_k\| \leq C g_k^4$ per site is the input.
- [x] Theorem 6(a) proves the first moment vanishes by parity (Section 5.2.3).
- [x] Theorem 6(b) (operator identity $\hat{E}_k(0) = 0$) is **correctly identified as FALSE** (Section 5.2.4).
**Arrow verified. The disproval of 6(b) is a strength, not a gap -- it shows honest self-correction.**

**Dimension-6 classification (Section 5.3):**
- [x] All non-derivative dim-6 operators ($\mathrm{Tr}(F^3)$, $d^{abc}F^3$) eliminated by $\mathcal{C}$-symmetry (exact, non-perturbative).
- [x] Only two-derivative operators survive: $\mathrm{Tr}(D_\rho F)^2$ and $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$.
**Verified: complete classification with no missing cases.**

**Spectral lemma (Section 5.5):**
- [x] Lemma states: $\mathrm{exc}(\mathcal{O}) \geq p \Rightarrow |\langle 1|\mathcal{O}|1\rangle_c| \leq C_p M \hat{\Delta}^p$.
- [x] Uses the LATTICE mass gap $\hat{\Delta}$ as an INPUT (from Theorem 4 via the transfer matrix spectrum).
- [x] Does NOT assume $\Delta_\infty > 0$.
- [x] Proof is self-contained: transfer matrix spectral decomposition with Boltzmann weights.
**Arrow verified. No circularity (see Section 3 below).**

**(B1) + (B2) $\to$ Stability of excitation number (Section 5.6, Part III):**
- [x] (B1) proved in Part I from Balaban's polymer expansion (conditional on [VERIFY] items).
- [x] (B2) proved in Part II by complexification.
- [x] Stability lemma: any $\mathcal{C}$-even, dim-6, gauge-invariant, analytic operator has $\mathrm{exc} \geq 2$.
- [x] Applied to $\delta E_k^{d=6}$, giving $\mathrm{exc} \geq 2$ non-perturbatively.
**Arrow verified.**

**Single-step bound (Section 5.6, III.5):**
- [x] Spectral lemma ($p=2$) + $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ + $\|\delta E_k^{d=6}\| \leq C g_k^4$ yields $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}} g_k^4 \hat{\Delta}_{k+1}^2$.
- [x] This discharges "Conjecture 1 at $d_O = 6$" (line 1351).
**Arrow verified.**

**RG recursion (Section 5.4):**
- [x] $C_{k+1} = C_k/4 + C_{\mathrm{new}}$: old contribution contracts by 1/4 per step.
- [x] New contribution bounded by single-step bound above.
- [x] Recursion has stable fixed point.
**Arrow verified.**

**Continuum limit (Section 5.7, Theorem 8):**
- [x] $\sum C_k g_k^4 \hat{\Delta}_k^2 < \infty$ by doubly exponential convergence.
- [x] $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$.
- [x] OS axioms verified; thermodynamic/continuum limits commute.
**Arrow verified.**

**Continuum chain verdict: Complete, conditional on the three [VERIFY] items. Every arrow has explicit logical implication with hypotheses discharged by prior steps.**

---

## 3. No Circular Reasoning

### 3.1 Does the spectral lemma use $\Delta_\infty$?

**NO.** The spectral lemma (Section 5.5.3) uses $\hat{\Delta}$ (the dimensionless gap at the CURRENT RG step), which at the starting scale is $\hat{\Delta}_0$ from the lattice proof (Theorem 4). The lemma's hypothesis (i) uses $\|\mathcal{O}\| \leq M$ and hypothesis (iii) uses $\mathrm{exc}(\mathcal{O}) \geq p$. The spectral gap $\hat{\Delta}$ appears in the CONCLUSION, not the hypothesis. It is the mass gap at scale $k$, not $\Delta_\infty$.

**Verified: no circularity.** The lemma maps (operator bound $M$ + excitation number $p$ + existing gap $\hat{\Delta}_k$) to a matrix element bound. It does not assume the gap survives.

### 3.2 Does the RG recursion assume what it's trying to prove?

**NO.** The RG recursion is a genuine induction:

- **Base case:** $\hat{\Delta}_0 > 0$ from the lattice proof (Theorem 4). The bound $C_0 g_0^4 \hat{\Delta}_0^2$ is trivially satisfied because $\hat{\Delta}_0 \sim O(1)$.
- **Inductive step:** Given $\hat{\Delta}_k > 0$, the single-step bound gives $|\delta\hat{\Delta}_k| \leq C g_k^4 \hat{\Delta}_k^2$, and the recursion yields $\hat{\Delta}_{k+1} = \hat{\Delta}_k(1 + O(g_k^4))$.
- **Convergence:** $\sum g_k^4 \hat{\Delta}_k^2 < \infty$ because $g_k^4 \sim 1/k^2$ and $\hat{\Delta}_k^2 \sim (a_k\Lambda)^2 \sim 2^{-2k}$.

The induction never assumes $\hat{\Delta}_k > 0$ for $k > k_0$ -- it PROVES it from the previous step.

**Verified: no circularity.** The structure is a standard induction with an explicit base case from an independent proof.

### 3.3 Does the stability of excitation number use the disproved operator identity?

**NO.** The stability argument (Section 5.6, Part III) proceeds by **universal classification of dimension-6 operators**, not by any operator identity. Specifically:

- It does NOT use $\hat{E}_k(0) = 0$ (which was disproved in Section 5.2.4).
- It does NOT use the Newton decomposition to extract $\hat{\Delta}$ factors from the external state (Mechanism 2, which was shown incorrect in Appendix G).
- It DOES use:
  (i) $\mathcal{C}$-symmetry to eliminate non-derivative operators (exact).
  (ii) Dimension counting to show only two-derivative operators survive.
  (iii) The spectral intermediate-state mechanism for $\mathrm{Tr}(D_0 F)^2$.

**Verified: no use of the disproved identity.** The paper correctly identifies and abandons the incorrect mechanism.

---

## 4. The Three [VERIFY] Items

### 4.1 Consistency across files

The three items are:

1. **Analyticity of individual polymer activities** -- verify Balaban CMP 109, Sections 2-4 preserve analyticity inductively.
2. **Block-spin kernel complexification** -- verify $A \mapsto A(A^\dagger A)^{-1/2}$ is analytic in a $k$-independent neighborhood of $\mathbf{1} \in \mathrm{GL}(N, \mathbb{C})$.
3. **Dimension-6 projection is exact** -- verify Balaban's coupling renormalization absorbs $\mathrm{Tr}(F^2)/g_k^2$, so $\delta E_k^{d=6}$ is genuinely dimension-6.

These are described identically (verbatim) in:
- PROOF-CHAIN.md, Section IV.3
- Section 5.6, Part IV.3
- Appendix H, Section 5.2

And described consistently (in summary form) in:
- Abstract (line 48-49)
- Conclusion Sections 12.2 and 12.6
- Section 6, Objection G

- [x] Same three items everywhere: **YES**.
- [x] Described as "reading exercises from Balaban's published construction": **YES**, in every occurrence.

### 4.2 Do any claims depend on these items being resolved?

**YES.** The continuum limit $\Delta_\infty > 0$ depends on (B1) and (B2), which in turn depend on the [VERIFY] items:

- [VERIFY] #1 and #2 feed into (B1): analyticity with $k$-independent radius.
- [VERIFY] #2 feeds into (B2): extension to $\mathrm{SL}(N, \mathbb{C})$.
- [VERIFY] #3 feeds into the stability of excitation number: the operator is genuinely dim-6.

**Is this dependency flagged?** Yes, consistently:
- Abstract: "conditional on three [VERIFY] items"
- PROOF-CHAIN.md: "Conditional on the three [VERIFY] items"
- Section 5.5.5 status table: marks the non-perturbative excitation number and $\Delta_\infty > 0$ as "**Conditional** on (B1)-(B2)"
- Conclusion: "conditional on three [VERIFY] items from Balaban's construction"

**Verdict: Properly flagged. No unacknowledged dependency.**

---

## 5. The Multi-Time-Slice Correction

### 5.1 Does Section 5.5 use the CORRECTED mechanism?

**YES.** Section 5.5 (The Two-Derivative Spectral Lemma) is built entirely on the spectral intermediate-state mechanism:

- Section 5.5.1 sets up the multi-time-slice transfer matrix representation (eq. 1-2).
- Section 5.5.2 defines minimal excitation number via intermediate states.
- Section 5.5.3 proves the lemma using Boltzmann extraction from excited intermediate states.
- Section 5.5.4 verifies explicitly for $\mathrm{Tr}(D_0 F)^2$: the factor $(e^{E_m - E_n} - 1)^2$ produces $\hat{\Delta}^2$ through the vacuum intermediate state.

Section 5.5 does NOT contain:
- Any reference to $\nabla_0$ acting on the external state.
- Any use of the disproved operator identity $\hat{E}_k(0) = 0$.
- Any claim that rigid temporal translation of the operator produces $\hat{\Delta}$ factors.

**Verified: Section 5.5 uses only the corrected (spectral intermediate-state) mechanism.**

### 5.2 Is Appendix G consistent with Section 5.5?

**YES.** Appendix G explicitly:

1. Identifies the incorrect mechanism ("Mechanism 2: $\nabla_0$ on external state gives $(e^{-\hat{\Delta}} - 1)$") and shows it gives ZERO by time-translation invariance (Section 3.1-3.3).
2. Derives the correct mechanism (Section 4): internal covariant derivative $D_0$ in the composite operator probes the spectral gap through intermediate states.
3. States the correction: "Mechanism 2 must be replaced" (Section 6.1).
4. Confirms the final bound $C g_k^4 \hat{\Delta}^2$ survives with the corrected derivation (Section 6.3).
5. Notes the multi-time-slice nature does NOT obstruct the mechanism (Section 5.3).

The final verdict of Appendix G (Section 7.3): "Conjecture 1 at $d_O = 6$ stands, but the derivation of Mechanism 2 requires correction."

**Section 5.5 implements exactly this correction.** The spectral lemma in Section 5.5 is the cleaned-up version of what Appendix G Section 4 derives. The two documents are logically consistent: Appendix G documents the error and its correction; Section 5.5 presents the corrected version.

---

## 6. Status Markers

### 6.1 Comprehensive marker inventory

| Claim | Marked Status | Correct? | Notes |
|:------|:-------------|:---------|:------|
| $\sigma > 0$ on lattice (SU(N)) | **Proved** | Yes | Theorems 1-4, complete proof |
| $\Delta > 0$ on lattice (SU(N)) | **Proved** | Yes | Fredenhagen-Marcu from $\sigma > 0$ |
| No phase transitions ($a \gg r_3$) | **Proved** | Yes | Cluster expansion convergence |
| OS axioms on lattice | **Proved** | Yes | Osterwalder-Seiler (1978) |
| Theorem 6(a): parity vanishing | **Proved** | Yes | Exact symmetry argument |
| Theorem 6(b): operator identity | **False** | Yes | Correctly disproved |
| $\mathcal{C}$-elimination of $\mathrm{Tr}(F^3)$ | **Proved** (exact) | Yes | Symmetry argument |
| Newton decomposition: $n \geq 2$ | **Proved** (exact) | Yes | Algebraic identity |
| $\mathrm{exc}(\mathrm{Tr}(DF)^2) \geq 2$ | **Proved** | Yes | Explicit spectral sum |
| Spectral lemma (general) | **Proved** | Yes | Transfer matrix + spectral gap |
| (B1): analyticity | **Proved** (Part I) | **Borderline** | See note below |
| (B2): complexification | **Proved** (Part II) | **Borderline** | See note below |
| $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ non-pert. | **Proved** / **Conditional** on (B1)-(B2) | Consistent | Sec 5.5.5 says Conditional; Sec 5.6 IV.1 says Proved |
| $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ bound | **Proved** / **Conditional** | Consistent | Same pattern |
| $\Delta_\infty > 0$ | **Proved** / **Conditional** | Consistent | Same pattern |
| RG recursion convergence | **Proved** | Yes | Standard analysis |

### 6.2 Potential overclaims

**FINDING (MODERATE):** There is a tension in the status of (B1) and (B2).

In the PROOF-CHAIN.md and Section 5.6 IV.1 table:
- Step 4 (B1): marked **Proved** (Part I)
- Step 5 (B2): marked **Proved** (Part II)
- Step 10 ($\mathrm{exc} \geq 2$ non-pert.): marked **Proved**
- Step 14 ($\Delta_\infty > 0$): marked **Proved**

But the same documents immediately follow with "Conditional on the three [VERIFY] items."

And in Section 5.5.5 (the status table at line 1066-1074):
- $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$ non-pert.: marked **Conditional** on (B1)-(B2)
- $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$: marked **Conditional** on (B1)-(B2)
- $\Delta_\infty > 0$: marked **Conditional** on (B1)-(B2)

The IV.1 table marks these as **Proved** while the Section 5.5.5 table marks them as **Conditional**. This is not a contradiction -- the IV.1 table's verdict (IV.4) explicitly says "conditional on the three [VERIFY] items" -- but the bold **Proved** in the table rows is potentially misleading if read without the caveats below.

**Assessment:** The paper handles this correctly in aggregate. The abstract says "Proved (conditional on three [VERIFY] items)," which is the most accurate formulation. The PROOF-CHAIN table should ideally mark Steps 10-14 as **Proved (conditional)** rather than bare **Proved** to avoid any ambiguity. However, the IV.4 Verdict paragraph immediately below the table makes the conditionality explicit, so this is a presentation issue rather than a substantive overclaim.

**FINDING (MINOR):** Section 5.4 (the RG recursion status table at line 842-849) lists:
- "New-operator form factor (Input 1)": **Pert: proved. Non-pert: OPEN**
- "Full non-perturbative form factor bound": **CONDITIONAL on Input 1**

This was the status BEFORE Section 5.6 discharged Conjecture 1. The text at line 851 says "The remaining problem is Conjecture 1, now sharpened..." and Section 5.6 then resolves it. So Section 5.4's status is a snapshot of the argument at that point in the exposition, not the final status. This is pedagogically appropriate (the paper tells the story in order) but a reader who stops at Section 5.4 would get an incomplete picture. Not an error.

### 6.3 Is anything marked [PROVED] that should be [VERIFY] or [CONDITIONAL]?

**No substantive overclaims found.** The key conditional results are consistently flagged:

1. Every file that mentions $\Delta_\infty > 0$ qualifies it with "conditional on [VERIFY] items."
2. The [VERIFY] items themselves are never marked as [PROVED] -- they are consistently flagged with the [VERIFY] marker.
3. The lattice results (Theorems 1-5) are marked [PROVED] and this is justified: they do not depend on any [VERIFY] items.

**One item deserving scrutiny:** Appendix H (Section 5.3) notes that Balaban's papers say (B1) and (B2) are "consequences of Balaban's CMP 109, not stated results." The correction: "(B1) and (B2) are stated results in Balaban's CMP 109" appearing in the spectral lemma document is "slightly too strong." This is flagged honestly in Appendix H itself.

---

## 7. Overall Assessment

### Strengths

1. **Honest self-correction.** The paper identifies and corrects its own errors (the disproved operator identity in Section 5.2.4; the incorrect nabla_0-on-external-state mechanism documented in Appendix G). This is rare and increases confidence in the remaining claims.

2. **Clean separation of proved and conditional.** The lattice proof (Theorems 1-5) is fully self-contained. The continuum limit is clearly separated and honestly flagged as conditional on [VERIFY] items.

3. **No circular reasoning detected.** The spectral lemma uses $\hat{\Delta}_k$ (current gap, not the target $\Delta_\infty$). The RG is a genuine induction with base case from an independent proof. The stability argument avoids the disproved identity.

4. **Complete proof chain.** Every arrow in both the lattice and continuum chains has explicit logical content. No step is hand-waved or deferred without flagging.

5. **Consistent [VERIFY] identification.** The three items are the same everywhere, consistently described, and all downstream claims are appropriately conditioned.

### Weaknesses / Items Requiring Attention

1. **(Moderate) Status table ambiguity.** The PROOF-CHAIN.md and Section 5.6 IV.1 tables mark Steps 10-14 as bold **Proved** while the Section 5.5.5 table marks the same claims as **Conditional**. The conditionality is stated in the accompanying text, but the table headers should be harmonized for clarity. Recommended fix: mark Steps 10-14 as "**Proved** (conditional on [VERIFY])" in the IV.1 table.

2. **(Minor) Source reference mismatch.** PROOF-CHAIN.md uses working-document filenames; Section 5.6 uses section numbers. These should be unified before submission.

3. **(Minor) Theorem 7 is referenced but never formally stated.** Section 5.2.5 says Conjecture 1 is "Proved perturbatively to all orders (Theorem 7)" and Section 5.4 references "Perturbative (Theorem 7) is proved," but no boxed "Theorem 7" statement appears in the sections I reviewed. It may be stated elsewhere in the working documents, but its absence from the main preprint sections is a gap in the exposition (not the logic).

4. **(Minor) Appendix H correction.** Section 5.3 of Appendix H identifies that the spectral lemma document says "(B1) and (B2) are stated results in Balaban's CMP 109" when they are actually consequences, not stated theorems. The paper should incorporate this correction.

### Verdict

**The proof chain is internally consistent and the logic is unbroken, conditional on the three explicitly identified [VERIFY] items.** No circular reasoning, no unacknowledged gaps, and no substantive overclaims were detected. The paper is honest about its limitations and correctly flags all conditional claims. The issues found are presentational, not logical.
