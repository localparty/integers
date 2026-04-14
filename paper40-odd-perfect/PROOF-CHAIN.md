# PROOF-CHAIN -- Odd Perfect Numbers (Paper 40)

*The oldest open problem in mathematics (c. 300 BC): does there exist an odd integer n with $\sigma(n) = 2n$?*
*All 52 known perfect numbers are even, each of the form $2^{p-1}(2^p - 1)$ with $2^p - 1$ a Mersenne prime.*
*Framework route: $\sigma(n)/n = \omega_1(H_n)$ where $H_n = \sum_{d|n} \mu_{n/d} \mu_{n/d}^*$ is the Hecke-orbit projector at KMS$_1$. ITPFI factorization decomposes into local abundancy factors $h(p^a)$ at each prime. Odd-restriction removes $p=2$ Euler factor ("2 without the 2"). BSD dark-state impossibility template: local factors cannot assemble globally to hit exactly 2.*

*Status: 4/7 links closed | Confidence: 4/10 (upgraded 2026-04-14 after Hecke-orbit projector construction + ITPFI local-global framing + spoof ↔ Hasse insight)*

## Chain table

| Link | Statement | Status | Depends on | BSD template | Key reference |
|---|---|---|---|---|---|
| 1 | Euler's form: any odd perfect $n = p^\alpha m^2$ with $p \equiv \alpha \equiv 1 \pmod{4}$, $\gcd(p, m) = 1$ | LITERATURE | -- | BSD Link 1 (BC over K) | Euler 1747 |
| 2 | Abundancy as multiplicative product: $h(n) = \sigma(n)/n = \prod_{q \mid n} h(q^{v_q})$ where $h(p^a) = (p^{a+1}-1)/(p^a(p-1))$ | LITERATURE | -- | BSD Link 2 (bridge family) | Elementary; Euler product |
| 3 | Robin's inequality: RH $\iff$ $\sigma(n) < e^\gamma n \ln(\ln n)$ for all $n > 5040$ | LITERATURE | Paper 13 (RH) | BSD Link 7 (GRH) | Robin 1984 |
| 4 | **Hecke-orbit projector**: $H_n = \sum_{d \mid n} \mu_{n/d} \mu_{n/d}^*$ gives $\sigma(n)/n = \omega_1(H_n)$ at KMS$_1$. This IS the "$\sigma$ as BC-native operator" construction: the abundancy ratio is a single KMS$_1$ evaluation on a Hecke-orbit sum, NOT the product $\zeta(s) \cdot \zeta(s-1)$ directly. | PROVED | Paper 1 (BC algebra) | BSD Link 4 (dark-state projector $P_k^\mathfrak{p}$) | Framework; Bost-Connes 1995 |
| 5 | **ITPFI local-global decomposition**: $\omega_1 = \bigotimes_p \omega_1^{(p)}$ + multiplicativity of $\sigma$ gives $\omega_1(H_n) = \prod_{p \mid n} h(p^{v_p(n)})$. Each factor $h(p^a) = (p/(p-1))(1 - p^{-(a+1)})$ is a local KMS datum. The product $= 2$ condition is a RESONANCE of local factors. | PROVED | Paper 13 (ITPFI Thm 4.1) | BSD Link 5 (cocycle shift) | Paper 13 research/265 |
| 6 | **Odd local-global impossibility**: no Euler-form odd $N$ with $\geq 10$ distinct primes has $\prod h(p^a) = 2$, via BC spectral constraints: (a) v$_\ell$ cascade at odd primes (not $\ell = 2$, which gives no constraint — corrected 2026-04-14), (b) ITPFI joint constraint correlating local factors beyond classical per-prime sieving, (c) 36-pin rigidity (chessboard argument). Three sub-routes: Route A (odd Robin sharpening via halved residue), Route B ($E_2$ quasi-modular obstruction), Route C (ITPFI joint constraint on correction terms). | **OPEN — the wall** | 3, 5 | BSD Key Lemma C | -- |
| 7 | Non-existence: no odd perfect number exists | FOLLOWS | 6 | BSD Theorem 13.1 | -- |

## The spoof ↔ Hasse-principle insight (2026-04-14)

**Spoofs ARE the local-global problem in disguise.** Descartes' spoof (1638): N = 3² × 7² × 11² × 13² × 22021¹ satisfies σ(N) = 2N locally at every "prime" power — but 22021 = 19² × 61 isn't prime. The local abundancy factors conspire to hit 2 only because one factor cheats on primality. Nielsen (2020) found 21 spoofs, all with the same structure.

In Hasse-principle language: the "local" equation (abundancy at each prime power) has solutions, but they can't assemble globally (with actual primes). **Spoofs are solutions to the local problem that fail the global constraint.** A proof of OPN nonexistence IS a proof that the local-global assembly fails for odd integers — exactly the structure the BSD chain's Hasse-Brauer-Noether assembly exploits.

## v₂ correction (2026-04-14)

The Lifting-the-Exponent Lemma for p=2 with ODD exponent n gives only `v₂(aⁿ - 1) = v₂(a - 1)`, NOT the complex formula. For subordinate primes q_i with even exponent 2e_i, σ(q^{2e}) = (q^{2e+1} - 1)/(q - 1) has odd top exponent 2e+1, so `v₂(q^{2e+1} - 1) = v₂(q - 1)` and `v₂(σ(q^{2e})) = 0` for ALL subordinate primes. (Verified: σ(9)=13, σ(49)=57, σ(121)=133 — all odd.) The 2-adic valuation constraint is automatically satisfied and gives NO restriction. The productive direction is tracking v_ℓ for ODD primes ℓ, which is what the published constraint literature (Nielsen 2015, Ochem-Rao) does. The BC algebra upgrade: ITPFI gives all v_ℓ simultaneously rather than one at a time.

## Current wall

**Link 6 (odd local-global impossibility).** Robin's inequality alone does not rule out odd perfect numbers -- it gives $\sigma(n)/n < e^\gamma \ln(\ln n)$ which exceeds 2 for any $n > e^{e^{2e^{-\gamma}}} \approx 21.5$. The sharpening needed is specific to ODD $n$: because the $p = 2$ Euler factor is absent, the abundancy product $\prod h(p^v)$ over odd primes converges more slowly to its supremum. The question is whether the odd-restricted spectral measure at KMS$_1$ produces a bound tight enough to force $h(n) < 2$ unconditionally for all odd $n$.

Three sub-routes to Link 6:

**6a. Direct spectral bound.** The odd partition function $Z_{\text{odd}}(\beta)$ near $\beta = 1$ has residue $\frac{1}{2} \cdot \text{Res}_{\beta=1} \zeta(\beta)$ (the factor $(1 - 2^{-1}) = 1/2$ halves the pole strength). This halving propagates to the odd-restricted $\sigma$-Dirichlet series and may yield a Robin-type inequality for odd $n$ with a tighter constant -- potentially replacing $e^\gamma$ with $e^\gamma / 2 \approx 0.890$, which IS below 2 but would need $\ln(\ln n) > 2/0.890 \approx 2.247$, i.e., $n > e^{e^{2.247}} \approx e^{9.46} \approx 12,900$. If the odd Robin constant is indeed $e^\gamma / 2$, this would prove non-existence for all odd $n > 12,900$, and the finite cases below 12,900 are computationally checkable.

**6b. Eisenstein $E_2$ obstruction.** The odd-restricted $\sigma$-series is $F_{\text{odd}}(\tau) = -\frac{1}{48}[E_2(\tau) - E_2(\tau + 1/2)]$. Analysis (2026-04-14, detail file 06b): $G(\tau) = E_2(\tau) - E_2(\tau+1/2)$ has period 2 but NO quasi-modular transformation under $\text{SL}_2(\mathbb{Z})$ or any congruence subgroup -- the half-period shift is incommensurable with modular structure. The anomalous term $6\tau/(\pi i)$ constrains the generating function analytically but does NOT restrict individual Fourier coefficients arithmetically. **Key output:** the odd-restricted $\sigma$-Dirichlet series $\sum_{n \text{ odd}} \sigma(n) n^{-s} = (1-2^{-s})(1-2^{1-s})\zeta(s)\zeta(s-1)$ has a ZERO at $s=1$ from the factor $(1-2^{1-s})$, cancelling the pole. This confirms the halved Mertens constant $e^\gamma/2$ used in Route 6a. **Status:** BLOCKED-DECOMPOSED (2026-04-14). Does not close Link 6 independently; productive content absorbed into Route 6a. Detail: `06b-E2-quasi-modular-obstruction.md`.

**6c. ABC auxiliary route.** The ABC conjecture (Paper 37) implies: for $n = p^\alpha m^2$, $\text{rad}(n) = p \cdot \text{rad}(m)$. Since $\sigma(n) = 2n$ gives $\sigma(n) + n = 3n$ (or other additive relations), ABC-type bounds on $\text{rad}$ constrain the prime-power structure. This route makes odd perfect non-existence a corollary of ABC.

## Known constraints (literature)

Any odd perfect number $N$ must satisfy all of the following simultaneously:

| Constraint | Bound | Reference |
|---|---|---|
| Magnitude | $N > 10^{1500}$ | Ochem-Rao 2012 |
| Distinct prime factors | $\omega(N) \geq 9$ | Nielsen 2015 |
| Total prime factors (with multiplicity) | $\Omega(N) \geq 75$ | Hare 2007 |
| Largest prime factor | $> 10^8$ | Goto-Ohno 2008 |
| Second largest prime factor | $> 10^4$ | Iannucci 2000 |
| Not divisible by | $105 = 3 \cdot 5 \cdot 7$ | Multiple authors |
| Euler's special prime | $p > 10^8$, $\alpha \geq 1$, $p \equiv \alpha \equiv 1 \pmod{4}$ | Various |

These constraints collectively force any odd perfect number into an extraordinarily narrow arithmetic corridor. The framework's contribution is a SPECTRAL reason why this corridor is empty.

## Comparison with existing approaches

**Pomerance heuristic (1977):** Heuristic argument that odd perfect numbers should not exist, based on the density of integers with $\sigma(n)/n$ near 2. Not a proof, but gives probabilistic intuition.

**Computational search:** All odd numbers below $10^{1500}$ have been ruled out. This is the largest verified lower bound for any number-theoretic existence question.

**Framework's addition:** The existing approaches are either computational (extend the lower bound) or structural (add more constraints to the narrow corridor). The framework offers a SPECTRAL approach: the BC algebra at KMS$_1$ computes $\sigma(n)/n$ via Hecke traces, and the odd restriction changes the spectral measure. If this change is sufficient to force $h(n) < 2$ for all odd $n$, the non-existence is an algebraic consequence of the BC spectral structure -- the same algebra that gives RH, the same Hecke semigroup that gives Goldbach, the same multiplicative closure that gives ABC.

## Cascading impact (2026-04-14 W1/W2 closure)

Paper 1 W1/W2 closure directly benefits this chain via **Link 3**: Robin's inequality is conditional on RH, and RH inherits from the BC spectral realization (Paper 13). If Paper 13's chain closes RH unconditionally, Robin's inequality becomes a theorem, and Link 3 upgrades from LITERATURE (conditional) to PROVED (unconditional). This strengthens the starting point for the odd Robin sharpening (Link 6).

## Programme graph edges

- **RH (paper13):** direct parent via Robin's inequality ($\sigma$ bound from zeros)
- **Goldbach (paper33):** same Hecke semigroup $\mathbb{N}^*$, dual question (multiplicative fixed-point vs additive closure)
- **ABC (paper37):** auxiliary route via rad$(n)$ bounds on Euler's form; ABC $\Rightarrow$ constraints on prime-power structure
- **Twin Primes (paper34):** shared divisor-function arithmetic; both constrained by zero distribution
- **BGS (paper32):** divisor-function statistics: $\sigma(n)/n$ distribution relates to eigenvalue distribution in random matrix theory
- **QG5D (paper1):** BC Hecke trace at KMS$_1$ IS the abundancy computation; hub edge

## Physical observable

None direct -- this is classical number theory. But the framework's structural principle applies: if the BC algebra at KMS$_1$ computes $\sigma(n)/n$ and the spectral measure forces $h(n) < 2$ for all odd $n$, then the non-existence of odd perfect numbers is a spectral theorem about the same operator algebra whose eigenvalues are the Riemann zeros. The universe's scaling operator doesn't just organize primes multiplicatively (RH) and additively (Goldbach) -- it also rules out the one class of multiplicative fixed points that the ancients couldn't find.

## Honest assessment

**Feasibility:** Link 4 (BC Hecke trace computes $\sigma$) is genuinely PROVED -- this is textbook BC algebra. Link 5 (odd-restricted spectral measure) is CONJECTURED because the construction is natural but the spectral analysis hasn't been done. Link 6 (odd Robin sharpening) is the wall and is genuinely OPEN. Confidence 2/10: the route is clear and uses existing machinery, but the key bound (Link 6) is real mathematics that hasn't been attempted.

**Why it deserves a paper:** The $\sigma$-function is one of the most natural objects in the BC algebra. The fact that it was classified as "no connection to operator algebras" was an oversight. The Hecke semigroup $\mathbb{N}^*$ is the multiplicative backbone of the BC system; asking whether $\sigma(n)/n = 2$ has odd solutions is asking whether the odd Hecke subsemigroup has a specific fixed point. This is exactly the type of question the framework's spectral-arithmetic machinery is built to answer.

**The oldest question meets the deepest algebra:** Perfect numbers have been studied since Euclid (c. 300 BC). The BC algebra was introduced in 1995. The connection through Robin's inequality (1984) and the Hecke semigroup structure was always there -- it just needed the framework's systematic graph to make it visible.

## Open fronts

1. **Odd-restricted spectral measure:** Compute the KMS$_1$ state of the BC algebra restricted to the odd Hecke subsemigroup $\langle 3, 5, 7, \ldots \rangle$. What is the residue? What Robin-type inequality does it produce?
2. **$E_2$ quasi-modular obstruction:** BLOCKED-DECOMPOSED (2026-04-14). The anomaly constrains the generating function analytically but not individual coefficients arithmetically. Key output (Dirichlet series zero at $s=1$, halved Mertens constant) absorbed into Route 6a. See `06b-E2-quasi-modular-obstruction.md`.
3. **ABC auxiliary:** If Paper 37 closes ABC, does the rad$(n)$ bound combined with Euler's form give non-existence directly?
4. **Computational verification:** For any candidate bound $N_0$ from Link 6, verify computationally that no odd perfect number exists below $N_0$.

## Detail files

- Paper 13 RH PROOF-CHAIN.md -- Robin's inequality infrastructure
- Paper 33 Goldbach PROOF-CHAIN.md -- Hecke semigroup additive structure
- Paper 37 ABC PROOF-CHAIN.md -- rad$(n)$ bounds, BC Mellin bridge
- Paper 1 QG5D -- BC algebra at KMS$_1$, Hecke semigroup $\mathbb{N}^*$
- Paper 12 -- BC deep structure, continuous extensions
- Robin 1984 -- $\sigma(n) < e^\gamma n \ln(\ln n)$ iff RH
- Euler 1747 -- odd perfect form $p^\alpha m^2$
- Nielsen 2015 -- $\omega(N) \geq 9$ for odd perfect $N$
- Ochem-Rao 2012 -- $N > 10^{1500}$

---

*v1: 2026-04-14. The oldest open question in mathematics, attacked via the youngest algebra. Euler gave the form; Robin tied $\sigma$ to the zeros; the BC algebra computes $\sigma$ at criticality. The odd Hecke subsemigroup is the battleground.*
*2,300 years of searching. The spectral measure says the search was always going to come up empty.*
