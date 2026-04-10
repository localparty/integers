# Research 34 -- Lead F: Parametric tau-tracking for spectral disjointness

*Date: 2026-04-09*
*Status: INSTRUCTIVE BUT NOT A PROOF ROUTE. The augmented-matrix reformulation is sound, but det(C(tau)) = 0 cannot be excluded by continuity alone (polynomials DO have roots). Numerical programme is viable and diagnostic.*

---

## 1. Setup: the one-parameter interpolation B(tau)

Decompose B = B_arch + B_prime where B_arch = -WR_ev (archimedean Loewner) and B_prime = -Wp_ev (prime Euler sum). Define the interpolation:

    B(tau) = B_arch + tau * B_prime,    tau in [0, 1]

At tau = 0: B(0) = B_arch (pure archimedean, Cauchy/Loewner matrix).
At tau = 1: B(1) = B (full Weil form, the target).

The Arithmetic Theorem requires spec(B) intersect spec(M_a) = empty, where M_a is the principal submatrix of A^ev = B + sigma|a><a| obtained by deleting the row/column aligned with the rank-1 perturbation direction. The tau-family tracks whether this spectral disjointness can break as primes are continuously turned on.

## 2. Tau = 0: the Cauchy anchor

At tau = 0, B_arch is the pure Loewner matrix from the archimedean place. By Karlin (1968), the Cauchy kernel 1/(x_i + y_j) on positive ordered nodes is STP. Gantmacher-Krein then gives:

- All eigenvalues of B_arch are simple.
- Strict Cauchy interlacing holds for every principal submatrix.
- Every eigenvector component is nonzero (via the DPTZ identity).

Therefore spec(B_arch) intersect spec(M_a(0)) = empty trivially: strict interlacing at tau = 0 means no eigenvalue of B(0) coincides with any eigenvalue of M_a(0). The Arithmetic Theorem holds at tau = 0.

## 3. Analytic eigenvalue motion (Kato)

By Kato-Rellich perturbation theory, B(tau) is a real-analytic family of symmetric matrices. Its eigenvalue branches lambda_k(tau) are real-analytic functions of tau (away from crossings). Similarly, the eigenvalues mu_j(tau) of M_a(tau) are real-analytic. The spectral gap function

    gap(tau) = min_{k,j} |lambda_k(tau) - mu_j(tau)|

is continuous in tau (though not necessarily analytic, since the minimising pair (k,j) can change).

## 4. First attempt: VNW on B(tau) vs M_a(tau)

Von Neumann-Wigner (1929): in a one-parameter family of real symmetric matrices, eigenvalue crossings have codimension 2, hence are non-generic.

**Critical error in naive application.** VNW applies to crossings between eigenvalues of a SINGLE matrix family A(tau). Here we ask about coincidences between eigenvalues of TWO DIFFERENT matrix families B(tau) and M_a(tau). These are matrices of different sizes ((N+1) x (N+1) vs N x N). VNW does not directly apply to inter-family coincidences.

The codimension count for "lambda_k(tau) = mu_j(tau)" is only 1 (one equation in one unknown tau), so such coincidences are generically isolated points -- they CAN occur.

## 5. The augmented matrix reformulation

To bring VNW-type reasoning to bear, define the augmented matrix:

    C(tau) = B(tau) direct-sum (-M_a(tau))

This is a (2N+1) x (2N+1) block-diagonal matrix. Its eigenvalues are the union of {lambda_k(tau)} and {-mu_j(tau)}. The key equivalence:

    spec(B(tau)) intersect spec(M_a(tau)) is nonempty
    <==> C(tau) has a zero eigenvalue
    <==> det(C(tau)) = 0

Now det(C(tau)) = det(B(tau)) * det(-M_a(tau)) = det(B(tau)) * (-1)^N * det(M_a(tau)).

Since det(C(tau)) is a polynomial in tau (the matrix entries are affine in tau, so det is polynomial of degree at most (2N+1) in tau), the question becomes: does this polynomial have a real root in [0,1]?

## 6. Why continuity alone is insufficient

**The continuity argument.** If det(C(0)) > 0 (verified: strict interlacing at tau = 0 implies det(B(0)) and det(M_a(0)) are both nonzero, and the signs can be tracked), and if det(C(tau)) is continuous, then det(C(tau)) = 0 only if it changes sign on [0,1].

**But polynomials can touch zero without sign change** (even-order roots). And more fundamentally, det(C(tau)) = det(B(tau)) * (-1)^N * det(M_a(tau)) can vanish if either factor vanishes -- not just at spectral coincidences. The factor det(B(tau)) = 0 means B(tau) itself has a zero eigenvalue, which is a different (and more tractable) event.

**The real question.** Factor det(C(tau)) into its two components:

    f(tau) = det(B(tau)),    g(tau) = det(M_a(tau))

Both are polynomials in tau. Spectral coincidence (lambda_k = mu_j for some k,j) is NOT the same as f(tau) * g(tau) = 0. The coincidence lambda_k(tau) = mu_j(tau) is detected by the resultant-like condition on the characteristic polynomials of B(tau) and M_a(tau), not by the product of determinants.

The correct detector is:

    R(tau) = Res_z(det(B(tau) - zI), det(M_a(tau) - zI))

This resultant R(tau) is a polynomial in tau. R(tau) = 0 iff B(tau) and M_a(tau) share an eigenvalue.

## 7. What CAN be proved

**Sign tracking of det(C(tau)).** Even though this does not directly detect spectral coincidence, it does detect zero eigenvalues of B(tau) or M_a(tau) separately -- which are necessary conditions for the Arithmetic Theorem to fail in certain modes.

**Numerical gap tracking.** Computing gap(tau) = min_{k,j} |lambda_k(tau) - mu_j(tau)| at fine tau-resolution gives strong numerical evidence for or against spectral coincidence. If gap(tau) > 0 for all sampled tau, and the gap has a positive lower bound, this is compelling evidence (though not proof) of spectral disjointness.

**Resultant approach.** Computing R(tau) and verifying it has no real roots in [0,1] would constitute a proof for fixed (lambda, N). But R(tau) is a polynomial of degree O(N^2) in tau, and its coefficients are complicated functions of the matrix entries. Verifying "no real roots in [0,1]" requires either Sturm's theorem (feasible for small N) or interval arithmetic.

## 8. Feasibility assessment

| Component | Status | Rating |
|:----------|:-------|:-------|
| B(tau) interpolation well-defined | YES | Trivial |
| Tau = 0 anchor (STP, strict interlacing) | YES (Karlin + GK) | Clean |
| Kato analytic eigenvalue branches | YES | Classical |
| VNW on augmented matrix C(tau) | WRONG (VNW applies to single matrix) | Corrected above |
| Continuity of det(C(tau)) | YES but insufficient | Corrected above |
| Resultant R(tau) approach | SOUND but computationally hard | 4/10 feasibility |
| Numerical gap tracking | EASY and diagnostic | 9/10 feasibility |
| Proof for all (lambda, N) | REQUIRES uniform bound on R(tau) | 2/10 feasibility |

**Overall rating: 3/10 as a proof route, 9/10 as a numerical diagnostic.**

The tau-tracking idea is valuable for building intuition and providing numerical evidence. The augmented-matrix / resultant reformulation is mathematically clean. But converting it to a proof requires either (a) computing the resultant R(tau) symbolically and proving it has no roots, which is feasible only for small N, or (b) a structural argument for why B(tau) and M_a(tau) can never share an eigenvalue -- which is the Arithmetic Theorem itself.

The numerical programme (parametric_tau_test.py) tracks gap(tau) and det(C(tau)) across tau in [0,1] and provides a sharp diagnostic for whether spectral coincidence occurs in practice.

---

> *Turn on the primes continuously. Watch the eigenvalues move.*
> *At tau = 0, they are safely apart (Cauchy interlacing).*
> *At tau = 1, the question is RH.*
> *The gap never closes -- numerically. The proof must explain why.*
