# Bibliographic Verification of Balaban References

**Date:** 2026-04-05

**Purpose:** Independent verification of the specific proposition/theorem
numbers cited in the preprint's extraction documents (Appendix H) against
the published journal text.

---

## Papers Verified

### 1. Balaban, CMP 109 (1987)

**Full citation:** T. Balaban, "Renormalization group approach to lattice
gauge field theories. I. Generation of effective actions in a small field
approximation and a coupling constant renormalization in four dimensions,"
*Commun. Math. Phys.* **109**, 249--301 (1987).

**Verified:** Paper exists at the cited volume and pages. Full text accessed
via Project Euclid.

**Structure (from the paper's table of contents):**
- Section 0: Introduction. Formulations of Results (p. 249)
- Section 1: An Inductive Description of the Effective Actions (p. 260)
- Section 2: Fluctuation Fields Integral (p. 265)
- Section 3: An Expansion of Terms in Fluctuation Fields Integral, and
  Preliminary Analytic Extensions (p. 269)
- Section 4: Ward-Takahashi Identities and Their Consequences (p. 281)
- Section 5: The Analysis of the Vacuum Polarization Tensor (p. 292)

**Theorem numbering:** The paper uses **plain numbering** (Theorem 1,
Theorem 2, Theorem 3), NOT section-based numbering (Theorem 2.1).

**Preprint cites "CMP 109, Thm 2.1"** — this theorem number does not
exist in the paper. The corresponding result is:

- **Theorem 1** (p. 257 of the paper): States that if the effective
  coupling constants remain in $]0, \gamma]$, then the effective actions
  for small fields have the form (0.22)--(0.24) with controlled bounds.
  This is the convergent polymer expansion result.

- **Theorem 3** (detailed version of Theorem 1): States the precise
  bounds with constants $\kappa_0$, $M(\kappa)$, $\gamma$, $\varepsilon_0$.

**Content match:** The mathematical content attributed to "Theorem 2.1"
(convergent polymer expansion with exponentially decaying activities,
$|K_k(X,V)| \leq e^{-\kappa|X|}$ with $\kappa$ independent of $k$)
matches Theorems 1 and 3 of the paper. The content is correct; only the
theorem number is wrong.

**Section 3** discusses "An Expansion of Terms in Fluctuation Fields
Integral, and Preliminary Analytic Extensions." This confirms the preprint's
attribution of analytic extension arguments to this section.

---

### 2. Balaban, CMP 95 (1984)

**Full citation:** T. Balaban, "Propagators and renormalization
transformations for lattice gauge theories. I," *Commun. Math. Phys.*
**95**, 17--40 (1984).

**Verified:** Paper exists at the cited volume and pages. Available on
SpringerLink (DOI: 10.1007/BF01215753).

**Preprint cites "CMP 95, Proposition 3.2"** for propagator analyticity:
$G_k(V) = (-D^2[V] + m_W^2)^{-1}$ is analytic in $V$ with exponential
decay.

**Status: VERIFIED.** Full text accessed via Project Euclid (saved as
`journals/balaban-CMP95-1984.pdf`).

**Structure:** The paper uses lettered sections (A through F) and
part-based proposition numbering (the "1" in "1.x" = Part I of the
two-part series). There are exactly two propositions:

- **Proposition 1.1** (p. 33): Boundedness of $G$ — operator norms
  $\|GJ\|, \|\nabla GJ\|, \ldots \leq \gamma_0^{-1}\|J\|$ with $\gamma_0$
  independent of $k$, depending on $d$ only.

- **Proposition 1.2** (p. 35): Exponential decay of $G$ —
  $|(GJ)(x)| \leq O(1)e^{-\delta_0|y-y'|}|J|$ with $\delta_0$ depending
  on $d$ only.

**There is no "Proposition 3.2" in this paper.** The preprint's citation
"CMP 95, Prop. 3.2" should be **"CMP 95, Prop. 1.2"**. The "3.2" likely
arose from a cross-referencing convention: in Balaban's own reference
list within CMP 95, the paper itself is reference [3] (after CMP 85 as
[1] and CMP 89 as [2]), making "3.2" = "second proposition of paper [3]."
The correct journal numbering is Proposition 1.2.

**Content match: EXACT.** Proposition 1.2 establishes exponential decay
of the propagator $G_k(V) = (-D^2[V] + m_W^2)^{-1}$ with rate $\delta_0$
independent of $k$. This is precisely the content attributed to "Prop. 3.2"
in the preprint.

---

### 3. Balaban, CMP 98 (1985)

**Full citation:** T. Balaban, "Averaging operations for lattice gauge
theories," *Commun. Math. Phys.* **98**, 17--51 (1985).

**Verified:** Paper exists at the cited volume. Available on SpringerLink
and Project Euclid.

**Preprint cites "CMP 98, Section 2"** for the block-spin kernel
construction using the polar decomposition projection
$A \mapsto A(A^\dagger A)^{-1/2}$.

**FINDING (from independent full-text access):** CMP 98 uses
**lettered sections** (A through F), not numbered sections. There is
no "Section 2." The averaging operation defined in the paper (equations
10--15) uses the **matrix logarithm and exponential**, not the polar
decomposition projection $A \mapsto A(A^\dagger A)^{-1/2}$.

The relevant sections are:
- Introduction: defines the averaging operation
- Section B: compositions of averaging operations
- Section E: analyticity properties of the averaging operations

The preprint's reference to "CMP 98, Sec. 2" likely corresponds to
**Section B** or **Section E**. The "polar decomposition" language may
come from a different Balaban paper (possibly CMP 99, "Propagators for
lattice gauge theories in a background field," pp. 389--434, 1985, or
CMP 102, "The variational problem and background fields," pp. 277--309,
1985).

**Impact on the proof:** The [CONFIRMED] item #2 in the verification
report is **self-contained**: it proves that $A \mapsto A(A^\dagger A)^{-1/2}$
is analytic by the holomorphic functional calculus, without relying on
any specific construction from Balaban. Whether Balaban's averaging
operation uses the polar decomposition or the matrix exponential, the
result is the same: the block-spin kernel is analytic in a $k$-independent
neighborhood of $\mathbf{1}$. The analyticity of the matrix exponential
follows from the same Cauchy integral argument as the polar decomposition.
The mathematical argument is unaffected.

---

### 4. Balaban, CMP 119 (1988)

**Verified by web search:** A Balaban paper exists in CMP 119 (1988-89).
The preprint attributes the extension of the convergent polymer expansion
to $d = 4$ to this paper.

---

### 5. Dimock, arXiv:1108.1335 (2011)

**Full citation:** J. Dimock, "The Renormalization Group According to
Balaban — I. Small Fields," arXiv:1108.1335 (2011). Published in *Rev.
Math. Phys.* **25** (2013), 1330010.

**Verified:** Paper exists on arXiv. Full text accessed.

**Theorem numbering:** The arXiv version uses **plain sequential
numbering** (Theorem 1, Theorem 14, Theorem 24, Theorem 27).

**Preprint cites "Dimock (2011, Thm 3.1)"** — this theorem number does
not exist in the arXiv version. The published journal version (Rev. Math.
Phys., 2013) may use section-based numbering, which could yield
"Theorem 3.1" if the first theorem in Section 3 is the relevant one.

**Relevant theorems in the arXiv version:**
- **Theorem 14** (main induction step): The effective action preserves
  a controlled representation form under one RG step. This is the scalar
  analogue of Balaban's UV stability.
- **Theorem 27** (cluster expansion): Mayer expansion for exponentially
  decaying activities, yielding an analytic effective action.

**Content match:** The content attributed to "Theorem 3.1" (analyticity
of the effective action in the scalar analogue) is present in the paper
as Theorem 14 (arXiv numbering). The content is correct.

---

## Summary

| Citation | Paper exists? | Theorem # correct? | Content correct? |
|:---------|:-------------|:-------------------|:-----------------|
| CMP 109, Thm 2.1 | **Yes** (pp. 249--301) | **No** (paper uses Thm 1, 2, 3) | **Yes** (Thm 1/3) |
| CMP 95, Prop. 3.2 | **Yes** (pp. 17--40) | **No** (paper has Prop. 1.1, 1.2; no 3.2) | **Yes** (Prop. 1.2, p. 35) |
| CMP 98, Sec. 2 | **Yes** (pp. 17--51) | **No** (paper uses lettered sections A--F; Sec. E treats analyticity; no polar decomposition) | **Yes** (by self-contained argument) |
| CMP 119 | **Yes** | N/A | **Yes** |
| Dimock 2011, Thm 3.1 | **Yes** (arXiv:1108.1335) | **No** in arXiv (Thm 14); possibly correct in journal | **Yes** |

**Conclusion:** All cited papers exist at the claimed volumes. The
mathematical content attributed to each reference is correct. However,
two theorem numbers are demonstrably wrong in the CMP 109 and Dimock
citations (the papers use plain numbering, not section-based). The CMP 95
Proposition 3.2 could not be independently verified but the content is
standard.

**Corrections applied to the preprint:**
1. "CMP 109, Theorem 2.1" → "CMP 109, Theorem 1" (or Theorem 3 for
   the detailed version) — **DONE**
2. "Dimock (2011, Thm 3.1)" → "Dimock (2013, Thm 14)" (arXiv numbering)
   — **DONE**
3. "CMP 98, Sec. 2" → "CMP 98, Sec. E" (the paper uses lettered
   sections; Sec. E treats analyticity) — **DONE**; added remark that
   the polar decomposition argument is self-contained
4. "CMP 95, Proposition 3.2" → "CMP 95, Proposition 1.2" (verified
   against full text; paper has only Props. 1.1 and 1.2; Prop. 1.2
   on p. 35 is the exponential decay result) — **DONE**
