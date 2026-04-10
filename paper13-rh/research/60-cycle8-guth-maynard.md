# Research 60 -- Cycle 8: Guth-Maynard Zero Density + Finite-N Simplicity

*Date: 2026-04-09. Cycle 8 of 10. Role: NEW LEAD + ADVERSARIAL.*
*Depends on: ledger, research/57 (cycle 5 synthesis), research/50 (finite-N), CCM arXiv:2511.22755.*

---

## 1. Guth-Maynard (2024)

Guth and Maynard proved: N(sigma, T) << T^{30(1-sigma)/13} for sigma near 3/4.

At sigma = 3/4 this gives N(3/4, T) << T^{30/52} = T^{15/26} approx T^{0.577}, improving Ingham's classical T^{3/5} = T^{0.6}. The exponent 13/25 = 0.52 is stated in some formulations after optimization. This bounds the NUMBER of zeta zeros with Re(s) >= 3/4 and 0 < Im(s) <= T.

Key point: this is an upper bound on EXCEPTIONS to the critical line, not a proof that zeros lie on it.

## 2. Our finite-N results

For QW_lambda^N (the Weil quadratic form truncated to N primes):

- **Cartwright (PROVED):** eigenvalues of QW_lambda^N are SIMPLE for each finite N. (Steps 1-7 of the chain; ledger status: unconditional.)
- **CCM identification (NUMERICAL):** eigenvalues of D(lambda, N) match the first ~50 Riemann zeros to 10^{-55} accuracy with N = 6 primes.
- **Secular induction (PROVED at finite N):** rank-one perturbation from N to N+1 primes gives strict interlacing.

## 3. The proposed combination

Define:

- f(N) = number of zeros provably on the critical line via QW_lambda^N simplicity + CCM spectral identification with N primes.
- g(T) = T^{13/25}, the Guth-Maynard upper bound on zeros off the line below height T.
- pi(e^T) ~ e^T / T, roughly the total number of zeros below height T (by the Riemann-von Mangoldt formula, the zero count is (T/2pi) log(T/2pi) - T/2pi + O(log T)).

**Hypothetical argument:** if f(N) >= (T/2pi) log(T/2pi) - g(T) for some N = N(T), then ALL zeros below height T are on the critical line. Because: f(N) are provably on the line, and at most g(T) can be off the line. If f(N) + g(T) >= total zeros, the off-line allocation is exhausted.

For large T: g(T) = T^{13/25} grows as T^{0.52}, while the total zero count grows as T log T. So g(T) / (total zeros) -> 0. One needs f(N) to grow essentially like T log T, capturing almost all zeros.

## 4. Why this fails: the f(N) gap

The entire argument requires f(N) to be a PROVED lower bound, not a numerical observation. The current status:

**(a) f(6) >= 50 is NUMERICAL, not proved.** CCM demonstrate that 6 primes capture 50 zeros to extraordinary precision. But "capture numerically" is not "prove they are exactly on the critical line." The eigenvalues of D(lambda, 6) are computed to match gamma_1, ..., gamma_50 to 10^{-55}. This does not constitute a proof that the k-th eigenvalue of D(lambda, 6) EQUALS gamma_k. It is a floating-point computation.

**(b) Even if f(6) = 50 were proved, the growth rate is unknown.** We need f(N) ~ c * p_N (or faster) where p_N is the N-th prime. There is no theorem giving f(N) as a function of N. CCM do not prove: "with N primes, at least h(N) zeros are exactly captured." They prove spectral properties of D(lambda, N) and observe numerical agreement.

**(c) The Cartwright simplicity is about QW_lambda^N, not about zeta zeros.** Simplicity says: "the eigenvalues of QW_lambda^N are distinct." It does NOT say: "the eigenvalues of QW_lambda^N are Riemann zeros." The identification eigenvalue_k = gamma_k is the CCM spectral convergence, which is the SAME unproved step that is the wall (ledger: Step 10).

## 5. Adversarial verdict

**This lead is CIRCULAR.** The argument structure is:

1. Assume CCM spectral identification (eigenvalues = Riemann zeros) for finite N. [UNPROVED]
2. Count how many zeros this captures: f(N). [DEPENDS ON 1]
3. Combine with Guth-Maynard to bound the remainder. [VALID]
4. Conclude all zeros are on the line for large T. [DEPENDS ON 1 AND 2]

The Guth-Maynard bound is real and unconditional. But it only helps if f(N) is also unconditional. The CCM spectral identification IS the content of RH-for-finite-truncations: "the zeros of the partial Euler product lie on Re(s) = 1/2." If we could prove this, we would not need the Guth-Maynard combination at all -- finite-N results plus a standard density argument would suffice.

The Guth-Maynard improvement (from T^{3/5} to T^{13/25}) is quantitatively interesting but does not change the logical structure. Even with the BEST zero density estimate, the bottleneck remains: proving f(N) rigorously.

## 6. Is there a non-circular version?

One possibility: use Guth-Maynard NOT with CCM's f(N), but with Cartwright simplicity directly. Simplicity of QW_lambda^N is proved. If one could show that simplicity of the N-truncated operator IMPLIES at least one zero is on the critical line (without invoking CCM's numerical identification), the argument might have content. But simplicity alone says nothing about WHERE the eigenvalues are -- only that they are distinct.

**Score: 2/10.** The idea is well-motivated but logically dependent on the unproved CCM spectral convergence. Close this lead unless f(N) can be established independently of CCM's numerics.

**Ledger update:** add as CLOSED, reason: circular (f(N) requires CCM spectral identification = the wall).
