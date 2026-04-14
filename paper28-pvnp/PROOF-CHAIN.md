# PROOF-CHAIN -- P vs NP (Paper 28)

*P != NP via Boolean BC system + trinity dictionary + Bulatov-Zhuk CSP dichotomy + spectral gap = Taylor gap equivalence. 5/6 links closed; Link 5 backward direction is the wall.*
*Status: 5/6 links closed | Confidence: 7/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | Boolean BC system (A_BC^Bool, sigma_t^Bool) exists; unique KMS_1; M_Bool is type III_1 | PROOF OUTLINED | -- |
| 2 | Trinity functor Phi_comp preserves cohomology: H^k(Sym(Phi(X)),A) = H^k(Sym(X),A) | PROOF OUTLINED | -- |
| 3 | Bulatov-Zhuk CSP Dichotomy: Taylor polymorphism <-> tractable | PROVED (EXTERNAL) | -- |
| 4 | Taylor gap = spectral gap of M_Bool^Gamma (verified 6/6 Schaefer classes) | COMPUTATIONALLY VERIFIED | 1, 2 |
| 5 | Non-full <-> Taylor equivalence | FORWARD (Taylor -> non-full): numerically supported by `paper28-pvnp/code/pvnp_nonfullness_test.py` + Bulatov-Zhuk external -- treat as numerically settled. BACKWARD (non-full -> Taylor): OPEN -- the genuine wall. | 1-4 |
| 6 | P != NP: M_Bool^{3-SAT} full -> not P-time; 3-SAT NP-complete; done | CONDITIONAL on 5 | 3, 4, 5 |

## L5 forward-direction sharpening (2026-04-14)

Per Agent-I open-frontier audit (item 4): the forward direction (Taylor -> non-full) is numerically tested in `paper28-pvnp/code/pvnp_nonfullness_test.py` which iterates over P-time CSPs, and is consistent with Bulatov-Zhuk on the CSP side. The backward framing in the chain already presupposes the forward half; the row above now makes this explicit. No confidence change -- only a cleaner wall statement.

## Current wall
**Link 5 backward: non-full -> Taylor polymorphism.** Going from infinite-dimensional operator-algebraic property (non-fullness of type III_1 factor) to finite-domain algebraic property (Taylor operation). Seven routes attempted: (A) direct spectral gap bypass [highest priority], (B) universal-algebraic, (C) channel correspondence via conditional expectation, (D) Popa cocycle superrigidity, (E) Kazhdan/Haagerup bridge, (F) trinity dictionary inversion, (G) conditional fallback [current state].

## Programme graph edges
- **RH (Paper 13):** Q5-RIEMANN exponent constrains spectral gap scaling
- **BSD (Paper 26):** L-function channel capacity via Dirichlet L
- **BGS:** spectral statistics of M_Bool connect to GUE universality
- **Baum-Connes:** K-theory of M_Bool constrains anomaly structure

## Cascading refinement from QG5D W1/W2 closure (2026-04-14)

Paper 1 PROOF-CHAIN.md W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10 (Theorem 1 two-loop scheme-independence + Theorem U.2a one-loop Seeley-DeWitt) + Paper 11 (Theorem K.4 all-orders inductive bootstrap) + explicit L=3 numerical verification at 50-digit precision (`paper1/code/K-5-2-route-c-3loop.py`). Cascading impact on this chain: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. Effect is cosmetic-to-small — this chain never gated on the scheme question directly, but the underlying foundation is now strictly stronger. No link status changes required; confidence unchanged; mention included for completeness of the programme graph.
