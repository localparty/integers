# PROOF-CHAIN -- Schanuel's Conjecture (Paper 35)

*If z_1,...,z_n are Q-linearly independent complex numbers, then*
*trdeg Q(z_1,...,z_n,e^{z_1},...,e^{z_n})/Q >= n.*
*Applied to z_k = gamma_k pi^2/2: algebraic independence of the*
*framework's eigenvalues exp(gamma_k pi^2/2) guarantees all 36*
*predictions are independent.*

*Status: 1/5 links closed | Confidence: 1/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | Framework uses exp(gamma_n pi^2/2) as eigenvalues of R-hat | KNOWN | -- | CBB axiom 1 |
| 2 | {gamma_n pi^2/2} are Q-linearly independent | CONJECTURED | -- | Related to simplicity of Riemann zeros |
| 3 | Schanuel: Q-lin indep -> trdeg >= n | OPEN | 2 | Schanuel 1960s (itself unproved) |
| 4 | Algebraic independence of exp(gamma_n pi^2/2) | CONDITIONAL | 2, 3 | Consequence of Schanuel applied to zeros |
| 5 | 36 predictions are algebraically independent | CONDITIONAL | 4 | No hidden relations reduce prediction count |

## Current wall

**Link 3 (Schanuel's conjecture is itself a major open problem).**

The conditional hierarchy is:

  RH (Paper 13) -> simplicity (open)
  -> Q-linear independence of {gamma_n pi^2/2} (open)
  -> Schanuel (open)
  -> algebraic independence of eigenvalues

Each arrow is a major open problem. Specific obstacles:

1. **Link 2:** Q-linear independence of Riemann zeros is not known for
   ANY pair of zeros. Even transcendence of gamma_1 = 14.134725... is open.
2. **Link 3:** Schanuel's conjecture subsumes both Lindemann-Weierstrass
   and the four exponentials conjecture. Only the n=1 case (Lindemann 1882)
   is proved.
3. The ITPFI factorization (Paper 13) or the BC algebraic structure might
   constrain algebraic properties of zeros, but no concrete route exists.

## Programme graph edges

- **RH (paper13-rh):** zero simplicity is prerequisite for Link 2; spectral realization connects
- **All predictions:** algebraic independence guarantees independence of 36 predictions
- **BSD (paper26-bsd):** algebraic independence of L-values at s=1
- **BGS (paper32-bgs-spectral-statistics):** GUE statistics assume generic (transcendental) zeros
- **Hodge (paper29-hodge):** period relations constrained by algebraic independence

## Cascading refinement from QG5D W1/W2 closure (2026-04-14)

Paper 1 PROOF-CHAIN.md W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10 (Theorem 1 two-loop scheme-independence + Theorem U.2a one-loop Seeley-DeWitt) + Paper 11 (Theorem K.4 all-orders inductive bootstrap) + explicit L=3 numerical verification at 50-digit precision (`integers/paper01-qg5d/code/K-5-2-route-c-3loop.py`). Cascading impact on this chain: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. Effect is cosmetic-to-small — this chain never gated on the scheme question directly, but the underlying foundation is now strictly stronger. No link status changes required; confidence unchanged; mention included for completeness of the programme graph.
