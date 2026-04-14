# Link 16 Critic Verdict

**Target:** Continuum flowed Schwinger functions: unique (not subsequential), OS0-OS4 at fixed t > 0.
**Source:** §L.2, Lemmas L.2.1–L.2.4; Appendix D.

---

## Verdict: WEAKENED (one labeling gap; no logical breaks)

---

## Attack Results

**A1 (Unique vs. subsequential convergence):** SOUND. Cauchy argument in Lemma L.2.2 gives pointwise convergence in R for each fixed f, i.e., weak-* convergence in S'. Completeness of R yields uniqueness without subsequence extraction. Topology is correct and sufficient for OS axioms.

**A2 (OS2/RP tightness as t → 0⁺):** SOUND at fixed t > 0. The Portmanteau transfer requires finite propagation speed of the heat kernel; cross-plane contamination argument degrades as t → 0⁺ but the claim is strictly at fixed t > 0. Independent Argument 2 (sum-of-squares) provides a backup.

**A3 (RP closure under weak limit):** SOUND. Sum-of-squares argument is topology-independent. The set of RP functionals is closed under weak-* limits by standard inner-product arguments.

**A4 (OS1 Euclidean covariance exact vs. approximate):** SOUND. Symanzik bound (L.2.19) with triply exponential flow enhancement ensures exact O(4) covariance in the K → ∞ limit.

**A5 (OS4 cluster rate uniform in t):** SOUND. Gap Δ∞ is a property of the measure, not the probe. K-uniform reference at §5.7(d) transfers cleanly.

**A6 (OS axiom labeling inconsistency — NEW):** WEAKENED. §L.2 Lemma L.2.3 uses the convention OS2 = reflection positivity, OS3 = symmetry. But line 164, line 2486, and §5.7 use OS3 = reflection positivity. Inside the OS2 proof block (lines 1218, 1239), the text cross-references "§5.7, OS3" for the lattice RP — pointing to the §5.7 label, not the Lemma L.2.3 label. The proof is internally consistent within §L.2 but the cross-references are ambiguous: a reader verifying via §5.7 will find OS3 = RP there, which is the OS2 slot in §L.2. No axiom is logically missing, but the inconsistency creates a verifiability gap requiring explicit disambiguation.

---

## Required Repair

Add a single parenthetical at the top of §L.2: "We use the convention OS0=temperedness, OS1=covariance, OS2=reflection positivity, OS3=symmetry, OS4=cluster; this differs from the OS3=RP convention used in §5.7 and Appendix D." Update cross-references at lines 1218 and 1239 to use the §L.2 label (OS2) or add "(OS3 in §5.7 notation)".
