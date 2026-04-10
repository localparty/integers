# Referee Report F4: Uniqueness of Continuum Limit

**Classification:** HEAVY
**Verdict:** CLOSABLE GAP
**Estimated repair:** 1 sentence (stating that uniqueness is not claimed and not required)

---

## Overview

The continuum limit is obtained as a subsequential limit via Banach-Alaoglu
compactness. Different subsequences of lattice spacings a_j -> 0 could in
principle yield different continuum QFTs. This report examines the subsequence
dependence, the universality question, the subsequence-independence of the mass
gap value, and the comparison with the Clay Millennium Prize requirements.

---

## Sub-point analysis

### (a) Subsequence dependence

The continuum Schwinger functions are obtained via Banach-Alaoglu: the
distributional bounds on S_n^{(a)} (from the OS0' estimate) imply weak-*
compactness, and a diagonal argument extracts a subsequence a_j -> 0 along
which all S_n^{(a_j)} converge. Different subsequences could, in principle,
yield different limiting distributions.

The preprint obtains the continuum limit as a subsequential limit and does NOT
claim that the limit is unique. This is the correct logical stance: proving
uniqueness of the continuum limit for an asymptotically free gauge theory is a
deep open problem closely related to constructive non-perturbative
renormalization.

Crucially, the mass gap Delta_inf > 0 is proved for EVERY subsequential limit.
The argument is: the convergence of the RG telescoping sum

    C_inf = C_0 - sum_k delta C_k

is absolute (by the geometric convergence of the delta C_k bounds established
in Parts D-E), so it is independent of any subsequence chosen for the weak
limit of the Schwinger functions. Similarly, the physical scale Lambda_inf is
determined by the RG flow (one-loop running plus controlled corrections), which
is again independent of the subsequence.

**Finding:** SOUND as stated. The preprint correctly establishes the mass gap
for every subsequential limit without claiming uniqueness.

**Impact on the claimed result:** This is sufficient for the Jaffe-Witten
problem, which requires existence of a mass gap, not uniqueness of the
continuum theory (see sub-point (d)).

### (b) Universality

The question of whether ALL subsequential limits yield the SAME continuum QFT
is the universality question for Yang-Mills theory. This is a non-trivial open
problem for asymptotically free gauge theories. Known results:

- In 2D, the Gross-Witten-Wadia model has a unique continuum limit.
- In 3D, some progress exists for gauge-Higgs models (Balaban, Brydges-Yau).
- In 4D, no complete uniqueness proof exists for any interacting gauge theory.

The preprint does not address universality. This is appropriate: uniqueness is
a separate question from existence and is not required by the problem statement.
However, the preprint should state explicitly that uniqueness is not claimed and
remains an open question.

**Finding:** CLOSABLE GAP. The preprint should include a sentence such as:
"The continuum limit is obtained as a subsequential limit; uniqueness of the
limit (universality) is not claimed and is not required by the Jaffe-Witten
problem statement." Estimated difficulty: 1 sentence.

**Impact on the claimed result:** This is a matter of precision in the claims.
Without the disclaimer, a reader could misinterpret the result as claiming
uniqueness.

### (c) Mass gap value is subsequence-independent

The physical mass gap is Delta_inf = C_inf * Lambda_inf, where:

- C_inf = C_0 - sum_{k=0}^{infinity} delta C_k is determined by the absolutely
  convergent RG telescoping sum. Each delta C_k is computed from the RG step
  at scale k, which depends only on the coupling g_k and the effective action
  at that scale. The RG flow is deterministic: given the initial coupling g_0
  and the lattice action, the entire sequence {g_k, delta C_k} is determined.

- Lambda_inf is the physical scale set by the RG flow, again determined by the
  initial conditions.

Since C_inf and Lambda_inf are both determined by the deterministic RG flow
(not by the choice of subsequence for the distributional limit), the mass gap
Delta_inf is the same for all subsequential limits.

The positivity Delta_inf = C_inf * Lambda_inf > 0 therefore holds for all
subsequences, not just the one chosen in the diagonal extraction.

**Finding:** SOUND. The mass gap value is determined by the RG flow, which is
subsequence-independent. The positivity holds universally across all
subsequential limits.

**Impact on the claimed result:** This is a strong feature of the proof: even
though the continuum QFT may not be unique, the mass gap IS unique (and
positive). All potential continuum theories arising from different subsequences
share the same mass gap.

### (d) Comparison with the Clay Millennium Prize requirements

The Jaffe-Witten problem statement (Clay Mathematics Institute, 2000) asks for
the existence of a quantum Yang-Mills theory on R^4 satisfying the Wightman
axioms (or the equivalent Osterwalder-Schrader axioms) with a strictly positive
mass gap.

The key linguistic observation: the problem uses the indefinite article "a"
throughout: "Prove that for any compact simple gauge group G, a non-trivial
quantum Yang-Mills theory exists on R^4 and has a mass gap Delta > 0." The
indefinite article "a" indicates that existence of one such theory suffices.

All subsequential limits obtained by the preprint's construction are Yang-Mills
theories in the sense required: they are derived from the Wilson lattice action
(which is the standard lattice discretization of the classical Yang-Mills
Lagrangian), they satisfy the OS axioms (by Parts F1-F2), and they have a mass
gap (by the RG argument). Each subsequential limit is therefore a valid
candidate for "a" Yang-Mills theory satisfying the prize conditions.

The question of whether different subsequential limits give the same or
different theories is the universality question (sub-point (b)), which is
separate from the prize requirement.

**Finding:** SOUND. The proof provides at least one (and potentially many)
continuum Yang-Mills theories with mass gap, which is what the Jaffe-Witten
problem requires.

**Impact on the claimed result:** The existence claim is well-matched to the
prize problem. Uniqueness, while scientifically important, is a separate
question that does not affect the validity of the existence proof.

---

## Summary

The uniqueness analysis reveals one closable gap: the preprint should state
explicitly that uniqueness of the continuum limit is not claimed and is not
required by the Jaffe-Witten problem statement. This requires 1 sentence. The
key strength of the proof is that the mass gap value Delta_inf > 0 is
subsequence-independent (determined by the deterministic RG flow), so
positivity holds for all subsequential limits. The proof correctly matches the
existence requirement of the Clay problem.
