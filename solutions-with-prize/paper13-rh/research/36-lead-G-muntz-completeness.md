# Research 36 -- Lead G: Muntz-Szasz / Beurling-Malliavin Completeness

*Date: 2026-04-09*
*Status: PROMISING for collective statement, GAP remains for individual SPO. Feasibility 5/10.*

---

## 1. The Muntz-Szasz theorem (L^2 version)

Let 0 < lambda_1 < lambda_2 < ... be a sequence of positive reals. The system {x^{lambda_k}} is complete in L^2[0,1] if and only if

    sum_{k=1}^infty 1/lambda_k = infty.

For the classical case lambda_k = k (monomials), the sum diverges (harmonic series) and we recover Weierstrass approximation. Muntz's original theorem (1914) handled C[0,1]; the L^2 extension is due to Szasz (1916).

## 2. The Beurling-Malliavin theorem

For a real sequence Lambda = {lambda_k}, the exponential system {e^{i lambda_k x}} is complete in L^2[-L, L] if and only if the Beurling-Malliavin effective density satisfies

    D_BM(Lambda) >= L/pi.

The BM density is defined via a regularised exterior density involving logarithmic integrals of n(t)/t, but for "well-distributed" sequences it reduces to the simpler asymptotic density:

    D(Lambda) = lim_{T -> infty} #{lambda_k in [0,T]} / T.

When this limit exists and is finite, it equals D_BM. When the counting function grows superlinearly, D_BM = +infty and the system is complete on EVERY interval [-L, L].

## 3. Application to {cos(x log p) : p prime}

The frequencies are Lambda = {log p : p prime}. We compute the counting function:

    N(T) = #{log p <= T} = #{p <= e^T} = pi(e^T).

By the prime number theorem, pi(e^T) ~ e^T / T. Therefore:

    N(T)/T ~ e^T / T^2 -> infty as T -> infty.

The counting function grows SUPERLINEARLY. The BM density is infinite. The system {e^{i (log p) x}} is complete in L^2[-L, L] for every L > 0.

Since cos(x log p) = Re(e^{i (log p) x}), and completeness of the real parts follows from completeness of the full exponentials (by taking real and imaginary parts), the system {cos(x log p) : p prime} is complete in L^2[0, L] for every L > 0.

## 4. What completeness gives us

**Collective orthogonality is impossible.** If f in L^2[0,L] satisfies

    <f, cos(x log p)> = 0  for ALL primes p,

then f = 0 a.e. In matrix terms: no eigenvector phi_k of B can be orthogonal to ALL prime vectors v_p simultaneously. There is no "silent mode" that avoids every prime.

## 5. The gap: collective vs individual

SPO requires: for each eigenvector phi_k and each prime p, we have <phi_k | v_p> != 0. Completeness gives only: for each phi_k, there EXISTS at least one p with <phi_k | v_p> != 0. The gap is between "at least one overlap" and "every overlap is nonzero."

This gap is real. In finite dimensions, a vector can be orthogonal to one element of a complete system while having nonzero overlap with the rest.

## 6. Minimality and the removal argument

A system {f_k} in a Hilbert space is MINIMAL if no element lies in the closed span of the others: f_j notin cl(span{f_k : k != j}).

**Key fact:** removing one element from a complete system with infinite BM density leaves the system complete. Proof: removing one frequency reduces the counting function by 1, which does not change the superlinear growth.

Attempted argument for SPO:
- Suppose phi_k is orthogonal to v_{p_0} for a specific prime p_0.
- Then phi_k lies in the orthogonal complement of v_{p_0}.
- But {v_q : q != p_0} is still complete in L^2[0,L].
- So phi_k is in the closed span of {v_q : q != p_0}.
- This does not yield a contradiction: phi_k can be in span{v_q : q != p_0} and still be orthogonal to v_{p_0}.

The removal argument fails to close the gap.

## 7. The one-dimensional complement approach

Let V = cl(span{v_q : ALL primes q}) = L^2[0,L] (by completeness). Let V_0 = cl(span{v_q : q != p_0}). Since V_0 is also complete, V_0 = L^2[0,L] as well. So V_0 = V, and the "unique information" of v_{p_0} is already contained in the remaining system.

This means v_{p_0} does NOT carry unique information in the L^2 sense -- it is redundant. There is no one-dimensional complement to exploit.

The argument would work if the system were an EXACT system (complete and minimal but NOT a basis). For exact systems, removing one element breaks completeness, and the biorthogonal functional detects the unique direction. But with infinite density, the system is far from exact -- it is massively overcomplete.

## 8. What WOULD close the gap

To go from completeness to individual SPO, one needs:

- (a) **Algebraic independence:** the eigenvectors phi_k of B have algebraically structured components (involving log p values), and <phi_k | v_p> = 0 forces an algebraic relation among logs of primes that violates Baker/Schanuel. This is Lead E territory.
- (b) **Genericity/measure theory:** show that {phi : <phi | v_p> = 0} has codimension 1 in the eigenspace, and the eigenvalues of B do not lie on the (countably many) hypersurfaces where an overlap vanishes. Requires understanding the parameter dependence of B.
- (c) **Quantitative completeness:** use the Riesz basis property (if the Gram matrix is bounded and boundedly invertible) to get LOWER BOUNDS on |<f, v_p>| for functions with controlled norm. If phi_k has unit norm, a Riesz bound gives |<phi_k, v_p>| >= c > 0 uniformly.

Option (c) is the most promising continuation: compute the Gram matrix of {v_p} and check its spectral bounds.

## 9. Feasibility assessment

| Aspect | Feasibility | Notes |
|--------|-------------|-------|
| Completeness proof | 9/10 | BM density is clearly infinite. The collective statement is solid. |
| Individual SPO via completeness alone | 2/10 | The gap is structural. Completeness cannot distinguish individual overlaps. |
| Riesz basis / Gram matrix route | 5/10 | Computationally testable. If the Gram matrix is well-conditioned, quantitative bounds may follow. See code: muntz_completeness_test.py. |
| Combined with algebraic structure | 6/10 | Completeness + Baker-type arguments might close the gap for structured eigenvectors. |

**Recommendation:** The completeness result is a solid SUPPORTING fact -- it eliminates pathological "silent mode" scenarios. The gap to individual SPO should be attacked via the Gram matrix / Riesz basis route (computational check) or combined with the algebraic structure of B's eigenvectors.

---

*Next step: Gram matrix computation and Riesz basis check (muntz_completeness_test.py).*
