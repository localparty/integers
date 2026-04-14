# T8 Vertex: Lindelof L3 -- beta mismatch repair attempt

**Target:** L3 claims |zeta(1/2+it)| = |omega_1(sigma_t(.))| but conflates beta=1 (KMS_1 state) with beta=1/2 (critical line). Three repair routes attempted.

---

## Route A: Analytic continuation to omega_{1/2}

**Verdict: BLOCKED.**

The BC system has a phase transition at beta=1. For beta < 1, there is a unique KMS state (high-temperature phase). So omega_{1/2} exists and is unique. However, the partition function Z_BC(1/2) = sum n^{-1/2} = zeta(1/2), which DIVERGES. The high-temperature KMS_{1/2} state is not normal with respect to the trace -- it lives on a different GNS representation. The formal evaluation omega_{1/2}(mu_n* mu_m) = delta_{nm} n^{-1/2} gives a non-normalizable state. The pointwise identification |zeta(1/2+it)| = |omega_{1/2}(sigma_t(.))| inherits this divergence: the right-hand side is not well-defined as a number because the state is not a state (not normalized, not even sigma-finite in the GNS sense). One cannot continue from the convergent regime beta > 1 through the phase transition at beta=1 into beta=1/2 while preserving the trace formula.

## Route B: Moments rather than pointwise

**Verdict: SPECULATIVE.**

L2 establishes: Lindelof iff int_0^T |zeta(1/2+it)|^{2k} dt = O(T^{1+eps}) for all k >= 1. On the BC side, |zeta(1/2+it)|^2 = sum_{m,n} (mn)^{-1/2} (m/n)^{it}, which is formally Tr(Delta_1^{-1/2} Delta_1^{-it} . Delta_1^{-1/2} Delta_1^{it}) -- a trace involving Delta_1^{-1/2} as a "weight insertion" rather than a temperature. The integral int |zeta|^{2k} dt would become a trace of a 2k-fold product with Delta_1^{-1/2} insertions, integrated over the flow parameter. This avoids the divergent partition function (the t-integral provides regularization) and stays at beta=1 for the GNS representation. However: (i) the formal trace sum_{m,n} (mn)^{-1/2} is itself divergent before t-integration; (ii) the t-integral provides delta(m-n) which reduces to zeta(1), still divergent; (iii) making this rigorous requires a cutoff scheme (Cesaro, Riesz, or physical) that has not been constructed. Promising direction but currently without a rigorous framework.

## Route C: Matrix element of Delta_1^{it} at beta=1

**Verdict: VIABLE (with caveats).**

Stay entirely at beta=1. The GNS space H_1 has basis |n> = mu_n Omega_1 with Delta_1|n> = n|n> (research/121, eq. 2.8). Define the vector:

  xi = sum_{n=1}^{infty} n^{-1/4} |n>

Then ||xi||^2 = sum n^{-1/2} = zeta(1/2), which diverges. So xi is NOT in H_1.

Alternative: use a REGULARIZED vector xi_s = sum n^{-s/2} |n> for Re(s) > 1, so ||xi_s||^2 = zeta(s) < infty. Then:

  <xi_s, Delta_1^{it} xi_s> = sum n^{-s} n^{it} = zeta(s - it).

At s = 1/2 this would give zeta(1/2 + it) -- but xi_{1/2} is not in H_1. However, the FUNCTION s -> <xi_s, Delta_1^{it} xi_s> = zeta(s - it) is analytic for Re(s) > 1 and admits meromorphic continuation to all s. The Lindelof hypothesis becomes a growth statement about this analytically continued matrix element at s = 1/2.

This works because: (a) Delta_1^{it} is bounded (unitary), so the only issue is whether xi_s is in H_1; (b) zeta(s-it) is well-defined by meromorphic continuation regardless of whether xi_s converges; (c) the growth bound |zeta(1/2+it)| = O(t^eps) is a statement about the continued function, not about the literal inner product.

**Caveats:** The repair replaces a literal operator identity with an analytic continuation of a matrix element. This is mathematically precise but conceptually weaker: L3 would say "the zeta function on the critical line IS the analytic continuation of a matrix element of the modular unitary Delta_1^{it}" rather than "the zeta function IS a KMS amplitude." The operator-algebraic content is thinner.

---

## Repaired L3 (if Route C adopted)

| Link | Statement | Status |
|---|---|---|
| 3' | For Re(s) > 1, zeta(s+it) = <xi_s, Delta_1^{it} xi_s> with xi_s = sum n^{-s/2} \|n> in H_1. By meromorphic continuation in s, zeta(1/2+it) is the value at s=1/2 of this matrix element. Lindelof says: this continued matrix element grows sub-polynomially in t. | PROVED (the identity for Re(s)>1) + ANALYTIC CONTINUATION (to s=1/2) |

**Net effect:** L3 upgrades from CONJECTURED to PROVED-WITH-CONTINUATION. The beta mismatch is resolved: we never leave beta=1. The price is that the critical-line statement is not a literal inner product but its meromorphic continuation. The moments connection (L2) remains the stronger independent handle.

---

*T8 repair attempt. 2026-04-14. Route C viable, Routes A/B blocked/speculative.*
