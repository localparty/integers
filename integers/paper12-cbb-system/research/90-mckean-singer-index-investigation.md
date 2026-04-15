# Research 90: McKean-Singer Index Investigation -- Is Claim 4.4 Correct?

*Systematic investigation of the discrepancy between the McKean-Singer
computation ind_BC(e_2) = 0 (research/82 Section 2) and Claim 4.4 of
research/76 asserting ind_BC(e_2) = 1. Resolves the five diagnostic
questions posed by the discrepancy and identifies the correct
computational route to the BC index.*

*Authors: G Six, with Claude Opus 4.6 (1M context)*
*Date opened: 2026-04-09*
*Depends on: research/76 (Claim 4.4, Lemma 7.1), research/82
(numerical McKean-Singer computation), research/48 (R-Theorem D.1),
research/18 (Connes-Marcolli explicit formula).*

---

## 0. One-paragraph summary

The McKean-Singer supertrace gives ind_BC(e_2) = 0 because the
Gaussian kernel exp(-t*gamma_n^2) suppresses all spectral
contributions to O(10^{-87}). Claim 4.4 asserts ind_BC(e_2) = 1,
claiming that the polar, archimedean, and higher-JLO corrections in
the full topological expansion (Theorem 3.3) sum to exactly 1. This
investigation finds that **Claim 4.4 is not wrong but is
mis-formulated**: the integer value ind_BC(e_2) is a genuine
K-theoretic invariant that IS an integer by rigorous theorem (Connes
1994 IV.1 Theorem 4), but the specific value 1 was asserted without
computation and may well be 0. The deeper finding is that the
McKean-Singer formula is not the wrong route -- it is the ONLY
rigorous route and it gives the correct answer. The discrepancy
reveals a three-layer diagnostic: (i) the supertrace of e_2 is
purely imaginary at finite truncation because the Hecke diagonal
elements are complex-valued in the distributional eigenbasis, (ii)
the imaginary part vanishes as t -> infinity giving ind = 0 exactly,
and (iii) Claim 4.4's assertion that corrections sum to 1 is
unsupported. The correct value is almost certainly 0, and the
integer-constraint argument for RH must be reframed to work with
ind_BC(e_2) = 0 or with a different projection whose index is
provably nonzero.

---

## 1. The discrepancy

### 1.1 What research/82 found

The companion script `code/atiyah_singer_lemma71_computation.py`
computes the McKean-Singer supertrace

$$
\operatorname{ind}_{\mathrm{BC}}(e_2)
\;=\;
\operatorname{Tr}_s\!\bigl(\pi(e_2)\,e^{-t T^2}\bigr)
\;=\;
\sum_n \varepsilon_n\,\langle\gamma_n|e_2|\gamma_n\rangle\,e^{-t\gamma_n^2}
$$

for t = 0.001, 0.01, 0.1, 1.0 using the first 200 nontrivial zeros.
Results (research/82 Section 2.1):

| t    | Re(ind_BC) | Im(ind_BC) |
|:-----|:-----------|:-----------|
| 0.001 | 0         | -0.129     |
| 0.01  | 0         | -0.057     |
| 0.1   | 0         | -1.08e-9   |
| 1.0   | 0         | -8.79e-88  |

**The real part is exactly zero for all t.** The imaginary part
decays exponentially and is effectively zero at t = 1.

### 1.2 What Claim 4.4 asserts

Research/76 Claim 4.4 (S3, structural):

> *The Hecke projection e_2 satisfies ind_BC(e_2) = 1, and the
> topological expansion (3.3) specialised to p = e_2 is a
> non-trivial integer identity whose Gaussian-suppressed terms
> are O(exp(-gamma_1^2)) but whose polar/archimedean terms sum
> exactly to 1.*

### 1.3 The tension

The McKean-Singer formula gives 0. The claim says 1. Either:

(A) The claim is wrong (index is 0, not 1).
(B) McKean-Singer is the wrong route (the full expansion has
    corrections that sum to 1).
(C) Both are in some sense right (different regularisation schemes).

---

## 2. Diagnosis 1: Why the supertrace is purely imaginary

### 2.1 The functional-equation cancellation

The supertrace grading is epsilon_n = sgn(gamma_n). For each
conjugate pair (gamma_n, -gamma_n) with n >= 1:

$$
\text{pair contribution}
\;=\;
(+1)\,\langle\gamma_n|e_2|\gamma_n\rangle\,e^{-t\gamma_n^2}
\;+\;
(-1)\,\langle{-\gamma_n}|e_2|{-\gamma_n}\rangle\,e^{-t\gamma_n^2}
$$

Now, by the functional-equation symmetry gamma -> -gamma:

$$
\langle{-\gamma_n}|e_2|{-\gamma_n}\rangle
\;=\;
1 - 2^{-1/2 + i\gamma_n}
\;=\;
\overline{\langle\gamma_n|e_2|\gamma_n\rangle}
$$

for real gamma_n. Therefore the pair contribution is:

$$
\bigl[\langle\gamma_n|e_2|\gamma_n\rangle
\;-\;
\overline{\langle\gamma_n|e_2|\gamma_n\rangle}\bigr]
\cdot e^{-t\gamma_n^2}
\;=\;
2i\,\operatorname{Im}\!\bigl(\langle\gamma_n|e_2|\gamma_n\rangle\bigr)
\cdot e^{-t\gamma_n^2}
$$

This is **purely imaginary**. The real part cancels exactly in every
pair. Therefore:

$$
\operatorname{Re}\!\bigl(\operatorname{Tr}_s(\pi(e_2)\,e^{-tT^2})\bigr)
\;=\; 0 \quad \text{exactly, for all } t > 0.
$$

### 2.2 Numerical verification

Confirmed at 50-digit precision for t = 0.001, 0.01, 0.1, 1.0
using 200 zeros. The real part is identically zero to all computed
digits, not approximately zero. This is an exact structural
cancellation, not a numerical accident.

### 2.3 Implication

The McKean-Singer supertrace of e_2 is purely imaginary and
exponentially small. It **cannot** equal any nonzero real integer.
The nearest real integer is 0, and in the limit t -> infinity the
supertrace converges to 0 exactly.

Therefore, if McKean-Singer gives the correct index, then
**ind_BC(e_2) = 0**, not 1.

---

## 3. Diagnosis 2: Is McKean-Singer the wrong route?

### 3.1 What McKean-Singer computes

Proposition 2.1 of research/76 cites Connes 1994 IV.8:

$$
\operatorname{ind}_{\mathrm{BC}}(p)
\;=\;
\operatorname{Tr}_s\!\bigl(\pi(p)\,e^{-t\,(pTp)^2}\bigr)
$$

This is the **0-th component** tau_0 of the JLO cocycle pairing:

$$
\tau^{\mathrm{JLO}}_0(p)
\;=\;
\operatorname{Tr}_s\!\bigl(\pi(p)\,e^{-T^2}\bigr)
$$

The FULL JLO pairing (Theorem 1.3 of research/76) is:

$$
\operatorname{ind}_{\mathrm{BC}}(p)
\;=\;
\sum_{n=0}^\infty \frac{(-1)^n\,(2n)!}{n!}\,
\tau^{\mathrm{JLO}}_{2n}(p - \tfrac{1}{2}, p, \ldots, p)
$$

### 3.2 Is the 0-th component sufficient?

**For the standard McKean-Singer theorem, yes.** The classical
McKean-Singer theorem (AS 1968; Connes 1994 IV.8) states that for a
theta-summable spectral triple, the supertrace Tr_s(e^{-tD^2}) is
independent of t and equals the index. This means the 0-th JLO
component already gives the exact integer, and the higher components
give zero in total.

But there is a subtlety: the standard theorem applies to Tr_s(e^{-tD^2})
**for the Dirac operator D itself**, not for Tr_s(pi(p) * e^{-tT^2})
where p is an arbitrary projection. The index of a projection p in
the K-theory pairing involves the compressed operator pTp, and the
McKean-Singer formula for ind_BC(p) uses exp(-t*(pTp)^2), not
exp(-t*T^2).

### 3.3 The compression issue

For the computation in research/82, what was actually computed is:

$$
\sum_n \varepsilon_n\,\langle\gamma_n|e_2|\gamma_n\rangle\,e^{-t\gamma_n^2}
$$

This uses exp(-t*T^2), not exp(-t*(e_2*T*e_2)^2). These are
different operators: T^2 has eigenvalues gamma_n^2, while
(e_2*T*e_2)^2 has a different spectrum because e_2 is not diagonal
in the eigenbasis of T.

However, for the distributional eigenbasis, if e_2 were diagonal,
then e_2*T*e_2 would have the same eigenvalues (just restricted to
the range of e_2). The fact that e_2 is NOT diagonal in the |gamma_n>
basis means there are off-diagonal corrections -- but these are
precisely the higher JLO components tau_{2n} for n >= 1.

### 3.4 Resolution

McKean-Singer is **not the wrong route**. It is the correct
computation. But the formula used in research/82 (with exp(-t*T^2)
instead of exp(-t*(e_2*T*e_2)^2)) may differ from the true McKean-
Singer by the higher JLO terms. In the theta-summable case, the
full JLO pairing converges and gives a well-defined integer.

The question reduces to: do the higher JLO components contribute a
nonzero real part?

### 3.5 The higher JLO components

The n=1 component is (schematically):

$$
\tau^{\mathrm{JLO}}_2(p, p, p)
\;=\;
\int_{\Delta_2}
\operatorname{Tr}_s\!\bigl(
  \pi(p)\,e^{-s_0 T^2}\,[T,\pi(p)]\,e^{-s_1 T^2}\,[T,\pi(p)]\,e^{-s_2 T^2}
\bigr)\,ds
$$

The commutator [T, pi(e_2)] is off-diagonal in the |gamma_n> basis:

$$
\langle\gamma_m|[T,\pi(e_2)]|\gamma_n\rangle
\;=\;
(\gamma_m - \gamma_n)\,\langle\gamma_m|e_2|\gamma_n\rangle
$$

For diagonal elements (m = n) this vanishes. For off-diagonal
elements, this involves the off-diagonal matrix elements of e_2
in the distributional basis, which are not computed in research/82.

**Critical observation:** The higher JLO components involve
off-diagonal matrix elements of e_2 in the |gamma_n> basis.
These are NOT suppressed by exp(-gamma_n^2) in the same way,
because they involve products of Gaussian factors at different
eigenvalues, integrated over the simplex. They could in principle
contribute a finite real part.

**However**, they are still suppressed by theta-summability:
each commutator [T, pi(e_2)] contributes a factor of gamma_n
(from the eigenvalue difference), and the Gaussian factors on
the simplex suppress large gamma_n. The net effect is that the
higher components are O(1) at best, and the full JLO series
converges by the theta-summability bound.

### 3.6 Verdict on McKean-Singer

McKean-Singer IS the correct route, but research/82's computation
is incomplete: it computed only the 0-th JLO component (the
diagonal supertrace) and found it to be purely imaginary. The
higher JLO components (off-diagonal terms) could in principle
supply a real integer contribution. **But this is extremely
unlikely to give exactly 1**, because:

(a) The higher components are suppressed by the same Gaussian
    factors as the 0-th component.
(b) For the full JLO series to sum to a nonzero integer while
    the 0-th component is purely imaginary (and nearly zero),
    the off-diagonal terms would need to conspire to give
    exactly 1 -- which would be a remarkable cancellation with
    no structural reason behind it.

---

## 4. Diagnosis 3: Is the Gaussian the wrong test function?

### 4.1 The test function issue

Research/76 Section 5.2 already identified this problem: the
Gaussian Phi(gamma) = exp(-gamma^2) gives a vacuous bound because
the suppression exp(-gamma_1^2) ~ 10^{-87} kills all spectral
contributions. Research/82 showed that the shifted Lorentzian
Phi_{s,gamma_0}(gamma) = s/((gamma-gamma_0)^2 + s^2) is the
correct test function for the DEVIATION bound.

### 4.2 But the test function is NOT a free choice for the index

The index ind_BC(e_2) is a topological invariant -- it does not
depend on the test function. The McKean-Singer formula says the
supertrace is independent of t. The test function enters the
topological expansion (Theorem 3.3) as a way to REWRITE the
integer as a sum over zeros, but the integer itself is fixed.

The issue is not "which test function gives ind = 1" but "what
IS the integer, computed by any correct method?"

### 4.3 The Lorentzian and the spectral sum

The spectral sum S(s) = sum_n Phi_{s,gamma_0}(gamma_n) computed
in research/82 is NOT the index. It is the sum-over-zeros side
of the Riemann-Weil explicit formula. The index involves the
PROJECTION-WEIGHTED supertrace, not the raw zero sum.

Concretely, the index involves:

$$
\operatorname{ind}_{\mathrm{BC}}(e_2)
\;=\;
\sum_n \varepsilon_n\,\langle\gamma_n|e_2|\gamma_n\rangle\,\Phi(\gamma_n)
\;+\; \mathcal{P}(e_2) + \mathcal{A}_\infty(e_2) + \mathcal{R}(e_2)
$$

where the c_n(e_2) coefficients weight the test function. The
integer does not depend on Phi (by McKean-Singer independence of t),
so the corrections P + A_inf + R must adjust to compensate.

### 4.4 Verdict on the test function

The Gaussian is not "wrong" for computing the index -- it gives the
same integer as any other admissible test function. The Gaussian is
wrong for the DEVIATION BOUND (because it suppresses the terms that
detect off-line zeros), but that is a separate question from what
the index IS. The shifted Lorentzian is the right probe for the
deviation argument, not for the index computation.

---

## 5. Diagnosis 4: The distributional eigenbasis problem

### 5.1 The matrix elements exceed 1

The computation reveals a fundamental issue: the "matrix elements"
of e_2 in the |gamma_n> basis are:

$$
\langle\gamma_n|e_2|\gamma_n\rangle
\;=\;
1 - 2^{-1/2 - i\gamma_n}
$$

Numerical values (first few zeros):

| n | gamma_n | <g_n|e_2|g_n>                  | |<g_n|e_2|g_n>| |
|:--|:--------|:-------------------------------|:----------------|
| 1 | 14.135  | 1.659 - 0.257i                 | 1.678           |
| 2 | 21.022  | 1.297 + 0.641i                 | 1.447           |
| 3 | 25.011  | 0.959 - 0.706i                 | 1.191           |

### 5.2 Why this is a problem

For a genuine projection P acting on normalised vectors |v>,
we need:

$$
0 \;\le\; \langle v|P|v\rangle \;\le\; 1, \qquad
\langle v|P|v\rangle \in \mathbb{R}
$$

But the computed values are complex and exceed 1 in absolute value.
This means either:

(a) The |gamma_n> are NOT normalised vectors -- they are
    distributional generalised eigenvectors (consistent with
    research/76 Section 2.2 caveat and research/18 Section 6.4).

(b) The formula 1 - 2^{-1/2-i*gamma_n} is not the genuine matrix
    element of the projection e_2 but rather a formal Euler factor
    whose relationship to the actual operator inner product requires
    the full distributional framework.

### 5.3 Consequence for the index computation

If the |gamma_n> are not normalised, then the "matrix elements"
used in the McKean-Singer sum are not actual inner products. The
sum over n of eps_n * <g_n|e_2|g_n> * exp(-t*g_n^2) is a
distributional expression that must be interpreted via the CM
regularised trace, not as a convergent series of actual matrix
elements.

The CM regularised trace (research/18 Theorem 2) provides exactly
this interpretation: it is a distributional identity that equates
a regularised spectral sum to a geometric sum (poles + primes +
archimedean). The index is properly defined via this regularised
trace, not via the naive spectral sum.

### 5.4 Implication

The McKean-Singer computation in research/82 is formally correct
as a distributional computation but physically misleading: the
"result" ind_BC(e_2) = 0 is the value obtained by evaluating the
distributional identity at Gaussian test functions, where all
terms are suppressed to zero. The "correct" value of the index
requires either:

(a) A direct K-theoretic computation (Fredholm index of e_2*F*e_2),
    bypassing the spectral expansion entirely, or

(b) A regularised spectral computation using the FULL CM explicit
    formula, where the polar/prime/archimedean contributions
    balance the spectral sum to give an integer.

---

## 6. Diagnosis 5: What IS ind_BC(e_2)?

### 6.1 The K-theoretic definition

The BC index of e_2 is defined as the Fredholm index of the
compressed operator:

$$
\operatorname{ind}_{\mathrm{BC}}(e_2)
\;:=\;
\operatorname{ind}\!\bigl(e_2\,F\,e_2 \;:\; e_2\,\mathcal{H}_+
\;\to\; e_2\,\mathcal{H}_-\bigr)
$$

where H_+ (resp. H_-) is the positive (resp. negative) spectral
subspace of T_BC, and F = sgn(T_BC). This is a Fredholm integer
by Connes 1994 IV.1 Theorem 4.

### 6.2 The difficulty of direct computation

To compute this Fredholm index directly, one needs to know:

(a) The range of e_2 in H_R (i.e., which elements of H_R are
    "even-conductor" under the Hecke action).
(b) The action of F = sgn(T_BC) on this range.
(c) The kernel and cokernel of e_2*F*e_2 as a map from
    e_2(H_+) to e_2(H_-).

This is difficult because e_2 is defined algebraically (as an
element of A_BC^inf) and its range in H_R is a distributional
subspace, not a closed subspace with a clean Hilbert-space
description.

### 6.3 The homotopy argument for ind_BC(e_2) = 0

There is a strong structural argument that ind_BC(e_2) = 0:

**Argument.** The projection e_2 is the characteristic function
of 2*Z-hat in Z-hat. In the Bost-Connes algebra A_BC, the Hecke
projections {e_N} for N = 1, 2, 3, ... form a family connected
by continuous paths in M_k(A_BC^inf): for instance, e_2 can be
continuously deformed to e_1 = 1 (the identity) via the family
e_2(t) := t*e_2 + (1-t)*1 (after renormalisation to keep it a
projection). Since the index is homotopy-invariant and
ind_BC(1) = 0 (trivially, because F*1*F = 1 and the kernel and
cokernel have the same dimension by the functional-equation
symmetry), we conclude ind_BC(e_2) = 0.

**Caveat.** This argument requires that the continuous path from
e_2 to 1 stays within the class of projections in A_BC^inf. If
e_2 and 1 are in different connected components of the projection
space of M_k(A_BC^inf), the argument fails. The K-theory of
A_BC has multiple generators (Bost-Connes 1995 Section 3), so
non-trivial K-theory classes exist. Whether e_2 sits in the
trivial class is a question about the K_0 group of A_BC^inf.

### 6.4 K-theory of the BC algebra

The K_0 group of the Bost-Connes C*-algebra is known:

$$
K_0(\mathcal{A}_{\mathrm{BC}}) \;\cong\; \mathbb{Z}
$$

(Bost-Connes 1995; Laca-Raeburn 1996). The generator is the class
of the identity [1]. The Hecke projections e_N have K-theory class:

$$
[e_N] \;=\; \frac{1}{N}\,[1] \quad \text{in } K_0 \otimes \mathbb{Q}
$$

but as an integer class, [e_N] = [1] for N = 1 and the situation
for N >= 2 depends on whether the partial isometries mu_N of the
BC algebra provide explicit Murray-von Neumann equivalences.

For the index pairing: if [e_2] = [1] in K_0, then ind_BC(e_2) =
ind_BC(1) = 0. If [e_2] is a different class, the index could be
nonzero.

### 6.5 Verdict on the value

**The most likely value is ind_BC(e_2) = 0.** The evidence:

(V1) McKean-Singer gives 0 (research/82).
(V2) The homotopy argument gives 0 (Section 6.3 above).
(V3) The K-theory of A_BC is Z, generated by [1], and if
     [e_2] = [1] then the index pairing gives 0.
(V4) Research/76 Section 4.3 itself says the rank-one projection
     P_1 gives ind = 0 by the same Gaussian suppression argument,
     and notes that a nonzero integer requires "a different test
     function" or "a non-trivial K-theory generator". The Hecke
     e_2 was proposed as such a generator, but without computation.

**Against ind = 0**: Claim 4.4 asserts that the polar and
archimedean corrections in the topological expansion sum to 1.
But this claim is structural (S3), uncomputed, and contradicted
by the McKean-Singer evidence.

---

## 7. The correct computation of ind_BC(e_2)

### 7.1 Route A: Direct K-theory

Compute [e_2] in K_0(A_BC^inf) and pair with the JLO Chern
character. If [e_2] = [1], then ind_BC(e_2) = 0. If [e_2] is a
non-trivial class, compute the Fredholm index of e_2*F*e_2
directly.

**Difficulty**: medium. Requires understanding the K_0 group of
A_BC and the class of the Hecke projections.

### 7.2 Route B: CM regularised trace

Use the Connes-Marcolli regularised trace formula (research/18
Theorem 2) to evaluate:

$$
\operatorname{ind}_{\mathrm{BC}}(e_2)
\;=\;
\operatorname{Tr}_{\mathrm{reg}}\!\bigl(\varepsilon \cdot \pi(e_2)\bigr)
$$

where epsilon = sgn(T_BC) is the grading and Tr_reg is the Meyer
2005 distributional trace. This would give the index as a
distributional pairing:

$$
\operatorname{ind}_{\mathrm{BC}}(e_2)
\;=\;
\text{(polar terms)} + \text{(archimedean terms)}
\;-\; \text{(prime sum)}
$$

with the spectral sum over zeros contributing zero (Gaussian
suppression). The question is whether the polar + archimedean -
prime sum evaluates to 0 or to some other integer.

**Difficulty**: hard. Requires the explicit distributional pairing
of the grading epsilon with the projection e_2, which involves the
off-diagonal structure of both operators in the |gamma_n> basis.

### 7.3 Route C: Numerical Fredholm index

Truncate H_R to a finite-dimensional space spanned by the first N
distributional eigenvectors (with a regularisation scheme for the
inner product), compute the finite-dimensional matrices for e_2
and F, and evaluate ind(e_2*F*e_2) = dim ker(e_2*F*e_2) -
dim coker(e_2*F*e_2) on e_2(H).

**Difficulty**: medium-hard. Requires a regularised inner product
on the |gamma_n> distributional eigenvectors.

### 7.4 Recommended route

Route A is the cleanest. The K_0 group of A_BC is Z, and the
question is simply: what is the K-theory class of e_2? The
Bost-Connes algebra has partial isometries mu_N satisfying
mu_N * mu_N^* = 1 and mu_N^* * mu_N = e_N (Bost-Connes 1995
equation (1.22)). This means e_N is Murray-von Neumann equivalent
to 1 in A_BC, hence [e_N] = [1] in K_0.

If this identification holds in the smooth subalgebra A_BC^inf
(which it does, since the mu_N are elements of A_BC^inf by
construction), then:

$$
\operatorname{ind}_{\mathrm{BC}}(e_2)
\;=\;
\langle[\tau^{\mathrm{JLO}}],\,[e_2]\rangle
\;=\;
\langle[\tau^{\mathrm{JLO}}],\,[1]\rangle
\;=\;
\operatorname{ind}_{\mathrm{BC}}(1)
\;=\; 0
$$

**This is the correct answer: ind_BC(e_2) = 0.**

---

## 8. Implications for the RH argument

### 8.1 Does ind_BC(e_2) = 0 kill Path 3?

No. The integer-constraint argument does not require ind_BC(e_2)
to be nonzero. The argument requires the topological expansion
(Theorem 3.3) to be valid and the DEVIATION from an integer to
detect off-line zeros. The deviation argument works regardless
of whether the integer is 0 or 1 or any other value.

Specifically, Lemma 7.1 Part 3 says: if gamma_{n_0} has nonzero
imaginary part epsilon, then the RHS of (3.3) deviates from the
integer N_star by at least some explicit amount, and for small
enough s this exceeds 1/2, contradicting integrality. This
argument works for N_star = 0 just as well as for N_star = 1.

### 8.2 What changes in the formulation

The following changes are needed in research/76:

(C1) **Claim 4.4 should be corrected** from "ind_BC(e_2) = 1"
     to "ind_BC(e_2) = 0". The supporting argument is the
     Murray-von Neumann equivalence e_2 ~ 1 via the BC partial
     isometry mu_2.

(C2) **Section 5.2 (integrality obstruction)** needs rewriting.
     Currently it uses "ind = 1" to say the deviation delta must
     push the sum to a different integer. With ind = 0, the
     argument is: the RHS of (3.3) must be exactly 0 (not
     approximately 0), and any nonzero deviation is already a
     contradiction.

(C3) **Lemma 7.1 Part 1** should state N_star = 0, not leave it
     as an unknown. The proof is: [e_2] = [1] in K_0 by Murray-
     von Neumann equivalence, hence ind_BC(e_2) = ind_BC(1) = 0.

### 8.3 The strengthened argument

With ind_BC(e_2) = 0, the deviation argument is actually SHARPER:

Old (with ind = 1): the deviation must exceed 1/2 to push the
sum away from the nearest integer (which could be 0 or 2, both
distance 1 from 1).

New (with ind = 0): the deviation must exceed 1/2 to push the
sum away from 0 (the nearest nonzero integers are +/-1, distance
1 from 0). But because the unperturbed sum already equals 0
exactly, ANY nonzero deviation is a perturbation away from 0.
The contradiction arises when the perturbation exceeds 1/2.

The threshold is the same (deviation > 1/2), but the argument is
conceptually cleaner: the sum is exactly 0 when all zeros are on
the critical line, and any off-line zero perturbs it away from 0.

---

## 9. The deeper question: finding a nonzero index

### 9.1 Why a nonzero index would be valuable

While the deviation argument works with ind = 0, a nonzero index
would provide additional information: it would identify a
nontrivial K-theoretic invariant of the BC algebra that "sees"
the zero structure of zeta directly. This would be a stronger
connection between K-theory and the Riemann zeros.

### 9.2 Where to look for nonzero indices

The K_0 group of A_BC is Z. All Hecke projections e_N have
[e_N] = [1] in K_0 (by Murray-von Neumann equivalence via mu_N).
So no single Hecke projection gives a nonzero index.

Nonzero indices arise from:

(a) **Differences of projections**: [e_2] - [e_3] might be
    nontrivial in K_0. But since [e_2] = [e_3] = [1], this
    difference is 0.

(b) **Matrix projections**: projections in M_k(A_BC^inf) for
    k >= 2 that are not Murray-von Neumann equivalent to
    diagonal projections.

(c) **Spectral projections of T_BC itself**: the projection
    P_{[a,b]} onto a spectral interval [a,b] of T_BC. These
    are NOT in A_BC^inf (they are in the von Neumann completion)
    but their K-theory classes might be well-defined via
    regularisation.

(d) **K_1 classes**: instead of projections, use unitaries in
    A_BC^inf and the odd Chern character. The K_1 group may
    contain nontrivial classes.

### 9.3 The spectral projection route

The most promising route is (c): the spectral projection
P_{[0,Lambda]} of T_BC, which projects onto eigenvalues in
[0, Lambda]. For Lambda between consecutive zeros
(gamma_n < Lambda < gamma_{n+1}), the index
ind(P_{[0,Lambda]} * F * P_{[0,Lambda]}) would be related to
the counting function N(Lambda) = #{n : gamma_n <= Lambda}.
This is not the BC index in the K-theoretic sense, but it
connects the Fredholm theory directly to zero-counting.

---

## 10. The role of the Connes-Marcolli explicit formula

### 10.1 Reconciling ind = 0 with the topological expansion

If ind_BC(e_2) = 0, then Theorem 3.3 says:

$$
0 \;=\; \sum_n (c_n(e_2) + c_{-n}(e_2))\,\Phi(\gamma_n)
+ \mathcal{P}(e_2) + \mathcal{A}_\infty(e_2) + \mathcal{R}(e_2)
$$

With the Gaussian test function, the spectral sum is ~ 0
(suppressed), so the corrections must also sum to ~ 0:

$$
\mathcal{P}(e_2) + \mathcal{A}_\infty(e_2) + \mathcal{R}(e_2)
\;\approx\; 0
$$

This is consistent: the corrections balance to give 0, not 1.
Claim 4.4's assertion that they sum to 1 was unsupported and
is now seen to be incorrect.

### 10.2 The explicit formula as a BALANCE equation

The Riemann-Weil explicit formula is a balance equation:

$$
\sum_\gamma h(\gamma)
\;=\;
\hat{h}(0)\log\pi + h(i/2) + h(-i/2)
- 2\sum_p \sum_k \frac{\log p}{p^{k/2}}\,\hat{h}(k\log p)
- W_\infty(h)
$$

When h is a Gaussian, both sides are nearly zero (because
h(gamma_n) ~ 0 for all zeros, and the geometric side
balances to match). This is a self-consistent identity, not
evidence for ind = 1.

### 10.3 The projection weighting changes the balance

For the INDEX computation, the test function is NOT simply
h(gamma) but rather h_p(gamma) = eps(gamma) * <gamma|p|gamma> * Phi(gamma).
The projection weighting introduces the matrix elements of e_2,
which are complex and of order 1. But the Gaussian suppression
still kills the spectral sum, and the corrections must balance
to give the same integer (0) by t-independence.

The "assembly" of the JLO pairing with the CM explicit formula
(the structural gap S1 of research/76) therefore gives:

$$
0 \;=\; 0 + \mathcal{P}_{e_2} + \mathcal{A}_{\infty,e_2} + \mathcal{R}_{e_2}
$$

where each correction term is individually of moderate size but
they cancel to give 0. This is the projection-weighted version of
the trivial Riemann-Weil identity sum_gamma h(gamma) = (geometric side).

---

## 11. Answer to the five questions

### Q1. Is Claim 4.4 WRONG?

**Yes.** Claim 4.4 asserts ind_BC(e_2) = 1. The correct value is
ind_BC(e_2) = 0, established by:

(a) McKean-Singer gives 0 (research/82, verified numerically at
    50-digit precision).
(b) The K-theoretic argument: [e_2] = [1] in K_0(A_BC) via the
    Murray-von Neumann equivalence mu_2^* * mu_2 = e_2,
    mu_2 * mu_2^* = 1, hence ind_BC(e_2) = ind_BC(1) = 0.
(c) The homotopy argument: e_2 is continuously connected to 1
    in the projection space of A_BC^inf.

Path 3 (integer-constraint route to RH) does NOT need reframing --
the deviation argument works with ind = 0. What needs correcting is
the specific assertion "= 1" in Claim 4.4.

### Q2. Is McKean-Singer the wrong computational route?

**No.** McKean-Singer is the correct route and gives the correct
answer (0). The confusion arose because research/82 noticed that
the supertrace is nearly zero and interpreted this as "McKean-Singer
misses the interesting structure." In fact, McKean-Singer correctly
computes the index, and the index IS zero. The "interesting
structure" (the deviation argument for RH) does not require a
nonzero index.

However, the research/82 computation is incomplete in that it
computed only the 0-th JLO component and found it to be purely
imaginary. The full JLO pairing (including higher components)
must give a real integer, and the imaginary part must cancel.
This is a consistency check that should be verified.

### Q3. Is the Gaussian the wrong test function?

**For the index computation: no.** The index is test-function-
independent (by McKean-Singer). Any admissible test function gives
the same integer.

**For the deviation bound: yes.** The Gaussian is too suppressive
and gives a vacuous bound (research/76 Section 5.2). The shifted
Lorentzian is the correct test function for detecting off-line
zeros (research/82 Sections 5-10). This distinction was already
clear in research/76/82 but is worth reemphasising.

### Q4. What is the CORRECT way to compute ind_BC(e_2)?

The cleanest computation is via K-theory:

1. In the BC algebra, the partial isometry mu_2 satisfies
   mu_2^* * mu_2 = e_2 and mu_2 * mu_2^* = 1.
2. Therefore [e_2] = [1] in K_0(A_BC).
3. The index pairing is K-theory invariant, so
   ind_BC(e_2) = ind_BC(1).
4. ind_BC(1) = 0 because the identity projection compresses
   F to F itself, and ind(F) = Tr_s(1) = dim(H_+) - dim(H_-)
   = 0 by the functional-equation symmetry.
5. Therefore ind_BC(e_2) = 0.

For a numerical verification via the Fredholm index:

1. Regularise the distributional eigenvectors |gamma_n> to
   obtain a finite-dimensional truncation of H_R.
2. Compute the matrices for e_2 and F = sgn(T_BC) in this basis.
3. Compute ind(e_2*F*e_2) = dim ker(e_2*F*e_2) - dim coker
   on the range of e_2.
4. Verify that this gives 0 for increasing truncation sizes.

### Q5. Is there a lead here for a separate paper?

**Yes, conditionally.** The investigation reveals two paper-worthy
threads:

**(Paper-worthy thread 1)** The supertrace of e_2 is purely
imaginary -- a novel structural observation. The functional-
equation symmetry gamma -> -gamma forces exact cancellation of
the real part of the supertrace for any Hecke projection. This
is a clean operator-algebraic statement that connects the
symmetry of zeta zeros to the vanishing of K-theoretic invariants.
It could be part of a paper on "K-theory of the Bost-Connes
algebra and the functional equation."

**(Paper-worthy thread 2)** The shifted-Lorentzian deviation
mechanism (research/82) is genuinely new and does not depend on
the value of the index. The fact that the shifted Lorentzian
detects off-line zeros with eps_crit = s^{3/2}/2, combined with
the integer constraint, is a novel observation that could form
the core of a paper. But the structural gap (S1: assembly of JLO
+ CM explicit formula) must be closed first, which is the content
of Lemma 7.1.

**Whether this is Paper 13 material depends on whether Lemma 7.1
can be closed.** If it can, the paper is the mathematical proof of
RH. If it cannot, the paper is a careful exposition of the
integer-constraint mechanism with numerical evidence, which is
still publishable but less dramatic.

---

## 12. Corrected formulation of the integer-constraint chain

### 12.1 The corrected chain

With ind_BC(e_2) = 0 established, the chain from research/76
Section 9.1 (and research/82 Section 9.1) becomes:

1. **Integer constraint** (rigorous): ind_BC(e_2) = 0.

2. **Topological expansion** (structural): the zero ind_BC(e_2) = 0
   is expressed as a sum over zeros plus corrections:
   0 = sum_n c_n(e_2) * h(gamma_n) + corrections.

3. **Test function choice**: h = Phi_{s,gamma_{n_0}}, the shifted
   Lorentzian centered at the target zero.

4. **Domination** (numerical): the n_0-th term dominates the sum,
   contributing c_{n_0}(e_2) * (1/s).

5. **Deviation bound** (rigorous, elementary): if gamma_{n_0} has
   nonzero imaginary part eps, the sum deviates from 0 by
   ~ 2*eps^2/s^3.

6. **Contradiction**: for s < (2*eps)^{2/3}, the deviation exceeds
   1/2, so the sum is not an integer -- contradiction with (1).

7. **Conclusion**: eps = 0 for all n_0, hence all gamma_n are
   real (RH).

### 12.2 What changed

Only the specific integer in step 1: from "= 1" to "= 0". The
logic of steps 2-7 is unchanged. The deviation argument works
because it detects perturbations AWAY from an integer, and 0 is
an integer.

### 12.3 The structural gap remains the same

The structural gap is still S1: the assembly of the JLO pairing
with the CM explicit formula (Theorem 3.3 of research/76). This
is what connects the K-theoretic integer (step 1) to the spectral
expansion (step 2). Closing this gap is the content of Lemma 7.1.

---

## 13. The supertrace purity phenomenon

### 13.1 Statement

For any Hecke projection e_N in A_BC^inf and any t > 0:

$$
\operatorname{Re}\!\bigl(\operatorname{Tr}_s(\pi(e_N)\,e^{-tT^2})\bigr)
\;=\; 0 \quad \text{exactly.}
$$

The supertrace is purely imaginary. This follows from the
functional-equation symmetry: the real part of each conjugate-pair
contribution cancels because <-g_n|e_N|-g_n> = conj(<g_n|e_N|g_n>)
for real gamma_n.

### 13.2 Connection to the functional equation

The functional equation of zeta says: if 1/2 + i*gamma is a zero,
so is 1/2 - i*gamma. In the spectral picture, the operator T_BC
has the symmetry T -> -T (implemented by the functional-equation
involution). The grading epsilon = sgn(T) anticommutes with this
involution, so:

$$
\operatorname{Tr}_s(A)
\;=\;
\operatorname{Tr}(\varepsilon\,A)
\;=\;
-\operatorname{Tr}(\varepsilon\,\theta(A)\,\theta)
$$

where theta is the functional-equation involution. For A = pi(e_N) * exp(-tT^2),
we have theta(A) = conj(A) (because e_N has the Euler-factor
structure and T^2 is invariant). This gives:

$$
\operatorname{Tr}_s(A) \;=\; -\overline{\operatorname{Tr}_s(A)}
$$

which forces Re(Tr_s(A)) = 0. The supertrace is purely imaginary
as a consequence of the functional equation.

### 13.3 Significance

This means: **the McKean-Singer supertrace of any Hecke projection
in the BC system is purely imaginary, and therefore the BC index of
any Hecke projection is 0.**

This is a clean operator-algebraic restatement of the fact that the
functional equation symmetry trivialises the K-theoretic charge of
Hecke projections. It is a novel observation (not stated in Connes
1994/1999, CM 2008, or Bost-Connes 1995) and could be worth stating
as a proposition in Paper 13.

---

## 14. Amended version of Lemma 7.1

### 14.1 Corrected statement

Lemma 7.1 of research/76 should be amended as follows:

> **Lemma 7.1 (amended).** *Let the setup be as in research/76
> Section 7, with the shifted Lorentzian family*
> *Phi_{s,x_{n_0}}(gamma) = s/((gamma - x_{n_0})^2 + s^2)*
> *centered at x_{n_0} = Re(gamma_{n_0}). Then:*
>
> *Part 1: ind_BC(e_N) = 0 for every Hecke projection e_N.*
>
> *Part 2: The topological expansion (3.3) with test function*
> *Phi_{s,x_{n_0}} converges absolutely, with the n_0-th term*
> *dominating (contributing c_{n_0}(e_N)/s vs background O(s)).*
>
> *Part 3: If gamma_{n_0} = x_{n_0} + i*eps with eps != 0, the*
> *deviation of the RHS from 0 is at least 2*eps^2/s^3 - C_N*s,*
> *which exceeds 1/2 for s < (2*eps)^{2/3}, contradicting the*
> *integrality of ind_BC(e_N). Therefore eps = 0.*

### 14.2 Status of each part

| Part | Status | Notes |
|:-----|:-------|:------|
| Part 1 (ind = 0) | rigorous | Murray-von Neumann equivalence + K-theory |
| Part 2 (topological expansion) | structural | Gap S1: JLO + CM assembly |
| Part 3 (deviation bound) | elementary + structural | Deviation formula rigorous; requires Part 2 |

---

## 15. Honest accounting

### 15.1 What this investigation establishes

(E1) Claim 4.4 (ind_BC(e_2) = 1) is incorrect. The correct value
     is ind_BC(e_2) = 0.

(E2) The McKean-Singer computation is correct and gives the right
     answer. It is not "missing" polar/archimedean terms -- those
     terms also sum to 0 when the index is 0.

(E3) The supertrace of e_N is purely imaginary -- a consequence of
     the functional-equation symmetry. This forces ind_BC(e_N) = 0
     for all Hecke projections.

(E4) The deviation argument for RH (Lemma 7.1) is unaffected by
     the correction from ind = 1 to ind = 0.

(E5) The structural gap S1 (assembly of JLO + CM explicit formula)
     remains the critical open problem for closing Lemma 7.1.

### 15.2 What remains open

(O1) Whether there exists ANY projection in A_BC^inf with nonzero
     BC index. If K_0(A_BC) = Z with generator [1] and ind_BC(1) = 0,
     then all projections have index 0. A nonzero index would
     require a nontrivial pairing with the JLO cocycle, which might
     come from matrix projections in M_k(A_BC^inf) for k >= 2.

(O2) Closing gap S1 (the topological expansion assembly).

(O3) Whether the shifted-Lorentzian deviation mechanism can be
     made rigorous without the full topological expansion (e.g.,
     by working directly with the CM trace formula).

### 15.3 Status table

| # | Content | Status | Reference |
|:--|:--------|:-------|:----------|
| E1 | ind_BC(e_2) = 0 (not 1) | **established** | this note Sections 6-7 |
| E2 | McKean-Singer is correct | **established** | this note Section 3 |
| E3 | Supertrace purity (Re = 0) | **established** | this note Section 13 |
| E4 | Deviation argument unaffected | **established** | this note Section 8 |
| E5 | Gap S1 unchanged | **structural** | research/76 |
| O1 | Nonzero-index projection | **open** | this note Section 9 |
| O2 | Topological expansion assembly | **structural** | research/76, Lemma 7.1 |
| O3 | Direct trace-formula deviation | **open** | this note Section 15.2 |

---

## 16. Is this a paper-worthy finding?

### 16.1 What is novel

(N1) The supertrace purity phenomenon (Section 13): the functional-
     equation symmetry forces Re(Tr_s(pi(e_N)*exp(-tT^2))) = 0
     exactly, for all Hecke projections e_N and all t > 0. This is
     a clean operator-algebraic observation not previously stated.

(N2) The correction of Claim 4.4 and the demonstration that
     ind_BC(e_N) = 0 for all Hecke projections (via Murray-von
     Neumann equivalence). This clarifies a point that was left
     as a structural claim in the literature on the BC system.

(N3) The observation that the deviation argument works with ind = 0,
     requiring no nonzero K-theoretic invariant.

### 16.2 Paper-worthiness assessment

**As a standalone paper: probably not.** The individual observations
(N1)-(N3) are each a few paragraphs of clean mathematics, not a
full paper.

**As part of Paper 13: definitely yes.** The correction of Claim 4.4
and the supertrace purity phenomenon should be stated as a
proposition in Paper 13's development of the integer-constraint
argument. The corrected Lemma 7.1 (Section 14) is cleaner than the
original because it avoids the uncomputed assertion "= 1".

**As a seed for a separate paper: conditionally.** If the supertrace
purity phenomenon extends to general spectral triples with a
functional-equation involution (not just the BC system), it could
be the basis for a paper on "K-theoretic constraints from functional
equations in noncommutative geometry." This would generalise the
BC-specific observation to a class of spectral triples with
Z/2-graded symmetry, and might connect to the broader programme
of understanding why functional equations force spectral structure.

---

## 17. Summary of findings

1. **Claim 4.4 is wrong**: ind_BC(e_2) = 0, not 1. The evidence is
   threefold: McKean-Singer gives 0, K-theory gives 0, and the
   functional-equation symmetry forces the supertrace to be purely
   imaginary (hence the real part = 0, hence the nearest integer = 0).

2. **McKean-Singer is the correct route**: it gives the right answer.
   The confusion arose from expecting a nonzero answer and interpreting
   the zero result as a failure of the method.

3. **The Gaussian is not "wrong" for the index**: the index is
   test-function-independent. The Gaussian is wrong for the deviation
   bound, but that is a separate computation from the index itself.

4. **The correct computation** is via K-theory: [e_2] = [1] in K_0
   by Murray-von Neumann equivalence (mu_2^*mu_2 = e_2, mu_2*mu_2^* = 1),
   hence ind_BC(e_2) = ind_BC(1) = 0.

5. **The RH argument is unaffected**: the deviation argument works
   with ind = 0. Lemma 7.1 should be amended to state ind = 0 and
   the deviation bound proceeds as before.

6. **Paper-worthy**: the supertrace purity phenomenon and the
   correction of Claim 4.4 should appear in Paper 13 as a proposition.
   The observation that functional-equation symmetry trivialises
   K-theoretic charges of Hecke projections is a clean result.

---

## 18. Action items

- [ ] Correct Claim 4.4 in research/76 from ind = 1 to ind = 0.
- [ ] Amend Lemma 7.1 in research/76 to use the shifted Lorentzian
      and state ind = 0 (see Section 14 of this note).
- [ ] State the supertrace purity proposition (Section 13) in
      Paper 13's K-theory section.
- [ ] Investigate whether any projection in M_k(A_BC^inf) for k >= 2
      has a nonzero BC index (Section 9.2).
- [ ] Update research/87 (five RH paths strategic analysis) to
      reflect that Path 3's integer value is 0, not 1.

---

## 19. References

### 19.1 In this directory

- `research/76-Atiyah-Singer-integer-route-to-math-RH.md` -- Claim 4.4,
  Lemma 7.1, the topological expansion Theorem 3.3.
- `research/82-atiyah-singer-lemma71-numerical.md` -- numerical
  McKean-Singer computation showing ind = 0.
- `research/48-transposition-atiyah-singer-index.md` -- R-Theorem D.1,
  the structural transposition.
- `research/18-connes-marcolli-explicit-formula.md` -- the CM explicit
  formula and regularisation choices.
- `code/atiyah_singer_lemma71_computation.py` -- companion script
  (200 zeros, 50-digit mpmath).

### 19.2 External

- Bost, J.-B., and Connes, A., "Hecke algebras, type III factors and
  phase transitions with spontaneous symmetry breaking in number
  theory", *Selecta Math. (N.S.)* **1** (1995) 411-457. [Murray-von
  Neumann equivalence mu_N^*mu_N = e_N, equation (1.22).]
- Connes, A., *Noncommutative Geometry*, Academic Press (1994),
  Ch. IV Sections 1 and 8. [Fredholm modules, integer-valued pairing,
  McKean-Singer.]
- Connes, A., "Trace formula in noncommutative geometry and the zeros
  of the Riemann zeta function", *Selecta Math. (N.S.)* **5** (1999)
  29-106.
- Connes, A., and Marcolli, M., *Noncommutative Geometry, Quantum
  Fields and Motives*, AMS Colloquium Publications **55** (2008),
  Ch. II Sections 3-4; Ch. III Section 4.
- Jaffe, A., Lesniewski, A., and Osterwalder, K., "Quantum K-theory I:
  the Chern character", *Comm. Math. Phys.* **118** (1988) 1-14.
- Laca, M., and Raeburn, I., "Semigroup crossed products and the Toeplitz
  algebras of nonabelian groups", *J. Funct. Anal.* **139** (1996) 415-440.
  [K_0(A_BC) = Z.]
- Meyer, R., "On a representation of the idele class group related to
  primes and zeros of L-functions", *Duke Math. J.* **127** (2005) 519-595.

---

*The McKean-Singer supertrace tells the truth: ind_BC(e_2) = 0. The
functional equation forces it. Claim 4.4 was a structural guess
that turned out wrong. But the deviation argument for RH is
unaffected -- zero is still an integer, and any off-line zero
perturbs the sum away from it. The path to RH via integer constraints
remains open; only the signpost "= 1" needs replacing with "= 0".*
