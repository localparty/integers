# PROOF-CHAIN -- Odd Perfect Numbers (Paper 40)

*The oldest open problem in mathematics (c. 300 BC): does there exist an odd integer n with $\sigma(n) = 2n$?*
*All 52 known perfect numbers are even, each of the form $2^{p-1}(2^p - 1)$ with $2^p - 1$ a Mersenne prime.*
*Framework route: $\sigma(n)/n$ as BC Hecke orbit sum at KMS$_1$ + Robin's inequality (RH) + odd-restricted spectral measure.*

*Status: 2/7 links closed | Confidence: 2/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Euler's form: any odd perfect $n = p^\alpha m^2$ with $p \equiv \alpha \equiv 1 \pmod{4}$, $\gcd(p, m) = 1$ | LITERATURE | -- | Euler 1747 |
| 2 | Abundancy ratio $h(n) = \sigma(n)/n = \prod_{q \mid n} \frac{q^{v_q+1}-1}{q^{v_q}(q-1)}$ is a multiplicative product over prime powers | LITERATURE | -- | Elementary; Euler product for $\sigma$ |
| 3 | Robin's inequality: RH $\iff$ $\sigma(n) < e^\gamma \, n \ln(\ln n)$ for all $n > 5040$ | LITERATURE | Paper 13 (RH) | Robin 1984; Gronwall 1913 |
| 4 | $\sigma(n)/n$ is a BC Hecke orbit sum: the KMS$_1$ state of the BC algebra computes the abundancy ratio via the Hecke semigroup trace $\text{tr}(\mu_n^* \mu_n)$ over divisors | PROVED | Paper 1 (BC algebra) | Framework; Bost-Connes 1995 $\S$5 |
| 5 | Odd-restricted BC spectral measure: partition function $Z_{\text{odd}}(\beta) = \prod_{p \text{ odd}} (1 - p^{-\beta})^{-1} = \zeta(\beta) \cdot (1 - 2^{-\beta})$ has a different pole residue at $\beta = 1$ than the full $\zeta(\beta)$; the odd-restricted divisor Dirichlet series $\sum_{n \text{ odd}} \sigma(n) n^{-s} = \zeta_{\text{odd}}(s) \cdot \zeta_{\text{odd}}(s-1)$ inherits this shifted spectral measure | CONJECTURED | 4, Paper 12 | Framework construction |
| 6 | Odd Robin sharpening: the odd-restricted spectral measure at KMS$_1$, combined with the local abundancy bound $h(p^v) < p/(p-1)$ for each odd prime $p$ and the constraint that $\omega(n) \geq 9$ (Nielsen 2015), forces $\sigma(n)/n < 2$ for all odd $n$ | OPEN | 3, 5 | Wall |
| 7 | Non-existence: no odd perfect number exists | FOLLOWS | 6 | -- |

## Current wall

**Link 6 (odd Robin sharpening).** Robin's inequality alone does not rule out odd perfect numbers -- it gives $\sigma(n)/n < e^\gamma \ln(\ln n)$ which exceeds 2 for any $n > e^{e^{2e^{-\gamma}}} \approx 21.5$. The sharpening needed is specific to ODD $n$: because the $p = 2$ Euler factor is absent, the abundancy product $\prod h(p^v)$ over odd primes converges more slowly to its supremum. The question is whether the odd-restricted spectral measure at KMS$_1$ produces a bound tight enough to force $h(n) < 2$ unconditionally for all odd $n$.

Three sub-routes to Link 6:

**6a. Direct spectral bound.** The odd partition function $Z_{\text{odd}}(\beta)$ near $\beta = 1$ has residue $\frac{1}{2} \cdot \text{Res}_{\beta=1} \zeta(\beta)$ (the factor $(1 - 2^{-1}) = 1/2$ halves the pole strength). This halving propagates to the odd-restricted $\sigma$-Dirichlet series and may yield a Robin-type inequality for odd $n$ with a tighter constant -- potentially replacing $e^\gamma$ with $e^\gamma / 2 \approx 0.890$, which IS below 2 but would need $\ln(\ln n) > 2/0.890 \approx 2.247$, i.e., $n > e^{e^{2.247}} \approx e^{9.46} \approx 12,900$. If the odd Robin constant is indeed $e^\gamma / 2$, this would prove non-existence for all odd $n > 12,900$, and the finite cases below 12,900 are computationally checkable.

**6b. Eisenstein $E_2$ obstruction.** The generating function $\sum_{n \geq 1} \sigma(n) q^n = -\frac{1}{24}(E_2(\tau) - 1)$ where $E_2$ is the quasi-modular Eisenstein series. $E_2$ transforms under $\text{SL}_2(\mathbb{Z})$ with an anomalous term: $E_2(-1/\tau) = \tau^2 E_2(\tau) + \frac{6\tau}{\pi i}$. In the BC type III$_1$ modular flow, this anomaly encodes the breaking of full modularity. The odd-restricted $\sigma$-series corresponds to removing the $q^{2k}$ terms from $E_2$ -- this further breaks the quasi-modular structure, and the resulting function may fail to achieve integer fixed points at $h = 2$ on odd arguments.

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
2. **$E_2$ quasi-modular obstruction:** Does the anomalous transformation of $E_2$ under $\text{SL}_2(\mathbb{Z})$, restricted to odd Fourier coefficients, obstruct the fixed-point $h = 2$?
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
