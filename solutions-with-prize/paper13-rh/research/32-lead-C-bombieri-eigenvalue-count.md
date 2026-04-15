# Research 32 -- Lead C: Bombieri's Eigenvalue Count and Weil Positivity

*Date: 2026-04-09*
*Status: VIABLE NUMERICAL PROGRAMME, not a proof route. Weil positivity <=> RH is classical, so proving QW >= 0 is equivalent to proving RH. But the truncated eigenvalue count provides a sharp numerical diagnostic and connects to the even-sector work.*

---

## 1. Weil's quadratic functional and the explicit formula

The Weil explicit formula associates to zeta a quadratic form Q(f) = sum_rho |f_hat(rho)|^2, where the sum runs over nontrivial zeros. The full expression includes main terms and prime sums:

    Q(f) = (main terms) - sum_p sum_k (log p) p^{-k/2} [f(k log p) + f(-k log p)]
           + sum_rho f_hat(rho) conj(f_hat(rho))

**Weil positivity:** Q(f) >= 0 for all admissible f <==> RH. (Weil 1952, refined by Bombieri.)

---

## 2. Bombieri's result on truncated forms (2000)

**Reference:** Bombieri, "Remarks on Weil's quadratic functional in the theory of prime numbers, I" (2000).

**Setup.** Truncate the Weil quadratic form to N Euler factors: define QW^N by restricting the prime sum to primes p_1, ..., p_N. This gives a finite-dimensional quadratic form whose matrix can be explicitly computed.

**Theorem (Bombieri, 2000).** Suppose RH fails, with exactly 2M nontrivial zeros off the critical line (counted with multiplicity, pairing rho with 1 - rho, conj(rho), 1 - conj(rho)). Then for all sufficiently large N:

    #{negative eigenvalues of QW^N} = M

That is, the number of negative eigenvalues of the truncated Weil form equals exactly HALF the number of off-line zeros (half because each off-line zero comes in a quadruplet {rho, 1-rho, conj(rho), 1-conj(rho)} contributing one negative direction to the quadratic form).

**Key point:** The negative eigenvalue count STABILISES at M for large enough N. It does not grow with N.

---

## 3. Connection to the even-sector programme

The even-sector Weil form QW^{N,+} is QW^N restricted to test functions with even symmetry f(x) = f(-x). Under this restriction:

- Only zeros with even functional-equation symmetry (xi(s) = xi(1-s)) contribute to the even sector.
- The matrix QW^{N,+} has dimension N+1 (vs 2N+1 for the full form).
- If an off-line zero rho has odd symmetry, it does NOT contribute a negative eigenvalue to QW^{N,+}.

Therefore: **if QW^{N,+} >= 0 (positive semidefinite) for all N, then no off-line zeros with even symmetry exist.** Combined with the analogous check on QW^{N,-}, this would rule out ALL off-line zeros.

---

## 4. Li coefficients and the Weil matrix

The Li coefficients lambda_n are defined by:

    lambda_n = sum_rho [1 - (1 - 1/rho)^n]

where the sum is over nontrivial zeros. The Li criterion (1997): **RH holds if and only if lambda_n >= 0 for all n >= 1.**

The Weil quadratic form in a suitable basis has matrix entries related to the Li coefficients. In the simplest formulation, the Hankel-type matrix H[i,j] = lambda_{i+j} is positive semidefinite if and only if the associated moment problem has a positive solution -- which is equivalent to RH.

---

## 5. This is NOT the simplicity route

The simplicity conjecture (all zeros simple) and the Arithmetic Theorem (eigenvector non-orthogonality) concern the STRUCTURE of eigenvalues. Weil positivity concerns SIGN.

- Simplicity: all eigenvalues distinct.
- Positivity: all eigenvalues non-negative.

These are independent properties. A matrix can have all-simple eigenvalues with some negative (simplicity holds, positivity fails). Or all eigenvalues non-negative but some repeated (positivity holds, simplicity fails).

**The positivity route does not need the Arithmetic Theorem at all.** It is a self-contained criterion: check that QW^{N,+} has no negative eigenvalues.

---

## 6. Could this bypass the Arithmetic Theorem?

In principle yes -- proving QW^{N,+} >= 0 for all N would establish the even-sector half of RH without touching simplicity. But **Weil positivity <=> RH** is a theorem, so "prove QW >= 0" IS proving RH directly. No shortcut through positivity avoids the full difficulty.

---

## 7. What IS useful: numerical verification

Bombieri's eigenvalue count theorem gives a sharp computational test:

1. Compute QW^{N,+} for N = 5, 10, 15, 20, 30.
2. Find all eigenvalues.
3. If any eigenvalue is negative, Bombieri says there is an off-line zero (and counts how many).
4. If all eigenvalues are non-negative for all tested N: numerical evidence for RH.

This is more informative than simply checking lambda_n >= 0 (the Li criterion), because the full eigenvalue spectrum reveals the RATE at which positivity holds -- how far from zero the smallest eigenvalue sits.

---

## 8. Computational finding: Hankel PSD vs Li positivity

**KEY OBSERVATION (from bombieri_eigenvalue_count.py):** The Li Hankel matrix H[i,j] = lambda_{i+j+2} has NEGATIVE eigenvalues even though every individual Li coefficient lambda_n is positive.

This does NOT contradict RH. The critical distinction:

- **Li criterion (correct):** lambda_n >= 0 for all n >= 1 <==> RH. This is a SCALAR condition.
- **Hankel PSD (stronger):** H[i,j] = lambda_{i+j+2} being PSD is a MATRIX condition that is strictly stronger than individual lambda_n >= 0.
- **Bombieri's theorem:** uses the actual Weil quadratic form with the explicit formula (prime sums), which is the QW^N operator already computed in r49/r51b. The Li Hankel matrix is NOT the same object.

The correct Bombieri eigenvalue count should be applied to the QW^{N,+} matrices from the even-sector programme (r51b_evenblock.py), which include the prime-sum contributions. The Li coefficient Hankel matrix is an interesting but distinct object.

---

## 9. Feasibility assessment

**Feasibility: HIGH for numerics, ZERO for a proof.**

Numerical programme:
- Computing Li coefficients from known zeros: straightforward (mpmath zetazero).
- Li positivity check: verified for lambda_1 through lambda_62 (100 zeros).
- Assembling the actual Weil quadratic form QW^{N,+}: already done in r51b_evenblock.py.
- Eigenvalue computation: standard (eigh_mp or numpy for moderate N).
- Bombieri's eigenvalue count on QW^{N,+}: count negative eigenvalues of the matrices already computed in the even-sector programme.

Proof programme:
- "Prove QW >= 0" is equivalent to proving RH. Full stop.
- No structural shortcut is known that would make the truncated form manifestly PSD.
- The Gram matrix representation Q[i,j] = sum_rho phi_i(rho) conj(phi_j(rho)) is trivially PSD, but this uses the zeros as INPUT (circular for proving RH).

**Verdict:** Use as a numerical diagnostic alongside the simplicity/Arithmetic Theorem route. Not a standalone proof path. The code in bombieri_eigenvalue_count.py implements the Li coefficient analysis; the actual Bombieri eigenvalue count on QW^{N,+} should use the existing r51b infrastructure.
