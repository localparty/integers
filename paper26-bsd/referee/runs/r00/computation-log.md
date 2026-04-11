# Computation Log

**Run:** r01
**Date:** 2026-04-09
**Referee:** Claude Opus 4.6 (1M context)

---

## Computational Verification Environment

The computational verification environment (Python venv) was NOT set up for this run, per instructions. All computational checks below are analytical/manual verifications rather than machine-verified.

## Analytical Verifications Performed

### 1. Cocycle shift formula at delta = 0
Delta c(0) = (1 - N(p)^0) / (N(p) - N(p)^0) = 0/( N(p) - 1) = 0.
Verified algebraically. Correct.

### 2. Dark-state bound
For N(p) = 2 (ramified prime (1+i)):
|w^2| = 2^{-1} = 0.5 < 1. Correct.
|w^6| = 2^{-3} = 0.125 < 1. Correct.

For N(p) = 5 (split prime (2+i)):
|w^2| = 5^{-1} = 0.2 < 1. Correct.

### 3. Frobenius order check at ((1+i), (3))
N(1+i) = 2. In (Z/3Z)*, ord(2) = 2 (since 2^1 = 2, 2^2 = 4 = 1 mod 3).
k = phi(3)/ord(2) = 2/2 = 1.
Preprint table states k = 2 with ord = 1. DISCREPANCY NOTED.
The stated order "ord(2) = 1 in (Z/3Z)*" is incorrect; ord(2 mod 3) = 2.

### 4. BSD formula for E: y^2 = x^3 - x
L(E, 1) = Omega/4 with c_2 = 4, |Sha| = 1, |E_tors|^2 = 16.
RHS = (1 * Omega * 1 * 4) / 16 = Omega/4. Matches. Correct.

### 5. Multiplicative independence of norms
log(2)/log(5): if 2^a = 5^b, unique factorization gives contradiction. Transcendental by Baker.
log(5)/log(13): same argument. Transcendental by Baker.

### 6. Residue of zeta_K at s = 1 for K = Q(i)
Res_{s=1} zeta_K(s) = 2pi/(w_K * sqrt(|d_K|)) * h_K = 2pi/(4*2) * 1 = pi/4.
Correct per class number formula.

### 7. L(E, 1) = L(1, chi_{-4}) * L(1, psi) nonvanishing
L(1, chi_{-4}) = pi/4 (Leibniz formula). Nonzero.
L(1, psi) nonzero by Hecke theory (Grossencharacters of imaginary quadratic fields with infinity type (1,0) have nonvanishing L-values at s = 1).
Therefore L(E, 1) = L(1, chi_{-4}) * L(1, psi) != 0 for the canonical curve.

---

## Tools Added During This Run

None. No computational environment was set up.

---

## Items Requiring Machine Verification in Future Run

1. All 355 bridge triples and their Frobenius orders (especially the ((1+i), (3)) entry).
2. Cocycle shift values at delta = 0.01 for all Gaussian bridge primes to 100 digits.
3. BSD formula for y^2 = x^3 - 1 (CM by Q(sqrt{-3})) with all terms.
4. Explicit rank-1 CM curve verification (if such curves exist for h_K = 1 CM fields).
5. Cross-file constant consistency check.
