# Research 38 -- Lead I: Explicit Cauchy Eigenvectors + Inductive Baker

*Date: 2026-04-09*
*Status: INTERESTING BUT BLOCKED. Base case is clean; inductive step hits cancellation control. Feasibility 4/10.*

---

## 1. Explicit eigenvectors of the Cauchy matrix

B_0 is the Cauchy matrix C_{ij} = 1/(x_i + x_j) with distinct positive nodes x_1 < ... < x_n. Eigenvector components have the closed form:

    phi_k[i] = 1/(x_i + theta_k) * prod_{j=1}^{n} (x_i + x_j) / prod_{j != i} (x_i - x_j)

where theta_k satisfies the secular equation sum_i w_i/(x_i + theta) = lambda with w_i = prod_{j != i}(x_i + x_j) / prod_{j != i}(x_i - x_j). For distinct positive x_i, every component phi_k[i] is nonzero -- no factor vanishes. This also follows from STP + Gantmacher-Krein, but the explicit formula makes it transparent.

---

## 2. SPO_0: Lindemann-Weierstrass at the base case

The overlap is <phi_k^0 | v_p> = sum_i phi_k^0[i] * cos(x_i log p). With algebraic nodes x_i, the coefficients phi_k^0[i] are algebraic (rational functions of the x_i), all nonzero by GK. The arguments beta_i = x_i log p are distinct (x_i distinct, log p != 0).

**If x_i are Q-linearly independent:** Lindemann-Weierstrass gives algebraic independence of e^{i*beta_1}, ..., e^{i*beta_n}, so no nontrivial algebraic combination of cos(beta_i) vanishes. Hence <phi_k^0 | v_p> != 0. SPO_0 is proved.

**Caveat for integer grids:** if x_i = i, then beta_i = i log p are Q-linearly dependent. LW gives algebraic independence of e^{i log p} but not of cos(i log p) for different i. Baker does not apply either (sum of cosines, not linear form in logs). SPO_0 on integer grids needs a refined argument, though each term is nonzero and the phases are distinct.

---

## 3. SPO_1: the first inductive step

B_1 = B_0 + alpha_2 v_2 v_2^T. By the secular equation (Research 33), eigenvectors of B_1 are:

    phi_k^1[i] = sum_j c_{kj} phi_j^0[i],    c_{kj} = <phi_j^0|v_2> / (lambda_j^0 - mu_k^1)

The new overlap <phi_k^1 | v_3> = sum_i [sum_j c_{kj} phi_j^0[i]] cos(x_i log 3).

**Problem.** The eigenvalue mu_k^1 is a root of the secular equation involving <phi_j^0|v_2> (which contains cos(x_i log 2)) and alpha_2 = log 2/sqrt{2}. So c_{kj} involves transcendentals. The overlap becomes a sum of products of transcendental coefficients times cos(x_i log 3). Baker (which requires algebraic coefficients) does not apply.

---

## 4. The inductive structure

At step K -> K+1, the overlap is:

    <phi_k^{K+1} | v_{p_{K+2}}> = sum_i F_i^{(K+1)} * cos(x_i log p_{K+2})

where F_i^{(K+1)} is a rational function of all previous eigenvalues and overlaps (involving log p_1, ..., log p_K and their cosines). The fresh ingredient is cos(x_i log p_{K+2}), with log p_{K+2} Q-linearly independent of all previous log p_m (fundamental theorem of arithmetic). Nonvanishing requires that F_i^{(K+1)} does not conspire to cancel the new cosine terms exactly.

---

## 5. The obstacle: Baker controls linear forms, not sums of products

The overlap at K >= 1 is sum_i f_i cos(g_i) with f_i, g_i transcendental. This is an algebraic independence question. Known tools fall short:
- **Baker:** controls b_1 log a_1 + ... + b_n log a_n with algebraic b_i. Coefficients f_i are transcendental at K >= 1.
- **Nesterenko (1996):** proves specific algebraic independence results (pi, e^pi, Gamma(1/4)). Not general enough.
- **Schanuel's conjecture:** would imply the overlap is nonzero (maximal transcendence degree). But Schanuel is unproved.

---

## 6. Possible rescue: sign control via Gantmacher-Krein

If all terms have the same sign, the sum cannot vanish.

**K = 0, k = 1:** GK gives phi_1^0[i] > 0 for all i (first eigenvector, all positive). If cos(x_i log p) > 0 for all i (holds when max_i x_i * log p < pi/2), every term is positive. SPO_0 is trivially nonzero for the leading eigenvector under this condition.

**K >= 1:** The secular coefficients c_{kj} have a determined sign pattern (denominators alternate by interlacing, overlaps have known sign). But phi_k^{K+1}[i] = sum_j c_{kj} phi_j^K[i] is a signed sum whose net sign depends on magnitudes, not just the sign pattern. Sign tracking becomes intractable for general k and K.

---

## 7. Feasibility

| Component | Status |
|:----------|:-------|
| Cauchy eigenvector formula | Explicit, classical -- Done |
| SPO_0 for Q-lin. indep. nodes | Proved (Lindemann-Weierstrass) |
| SPO_0 for integer grids | Hard -- refined transcendence needed |
| SPO_1 (K=0 -> K=1) | Blocked -- coefficients transcendental |
| General SPO_K | Open -- cancellation control beyond Baker |
| Sign rescue (GK) | Partial -- works for k=1, K=0 only |

### Overall: 4/10

Base case is a real advance over Research 33 (which noted Baker at K=0 as "plausible" without the argument). Inductive step hits the same wall as Research 35: sums of products of transcendentals are beyond current theory. Sign control from GK is a new idea but covers limited cases.

---

*The Cauchy eigenvector formula makes K = 0 explicit. Lindemann-Weierstrass closes the base.*
*At K >= 1, eigenvector components become transcendental. Baker loses grip.*
*Sign control from Gantmacher-Krein is the new idea. It works partially.*
*The inductive step needs either Schanuel or a structural miracle.*
