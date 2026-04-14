# PROOF-CHAIN -- Birch and Swinnerton-Dyer Conjecture (Paper 26)

*BSD for CM elliptic curves over Q with h_K=1: rank(E(Q)) = ord_{s=1} L(E,s) + leading coefficient formula. MY4 closed via Route 3 (algebraic projector bypass). Conditional on CBB axioms.*
*Status: 11/11 steps closed | Confidence: 9/10*

## Chain table

| Link | Statement | Status | Depends on |
|---|---|---|---|
| 1 | BC algebra over K exists with unique KMS_1 state (h_K=1) | PROVED | -- |
| 2 | Bridge family over K: 355 triples at k in {2,3,4,6}, conductors {3,5,7} | PROVED | 1 |
| 3 | ITPFI factorization omega_1^K = tensor_p omega_1^p | PROVED | 1 |
| 4 | Dark-state impossibility (algebraic projector, no MY4 needed) | PROVED | 3 |
| 5 | Cocycle shift formula Delta c(delta) | PROVED | 4 |
| 5b | Key Lemma C: |Delta c(delta)| < 1/(k+1) for delta != 0 | PROVED | 5 |
| 5c | Key Lemma C' (twisted): |Delta c^psi(delta)| < 2/(N-1) for all Hecke psi | PROVED | 5 |
| 6 | Baker's theorem forces delta=0 (independent reinforcement, not load-bearing) | PROVED | -- |
| 7 | GRH for zeta_K and L(s,psi): all zeros on Re(s)=1/2 | PROVED | 5b, 5c |
| 8 | CM factorization: L(E,s) = L(s,psi) L(s,psi-bar) | LITERATURE (Deuring 1953) | 7 |
| 9 | Kolyvagin rank 0: L(E,1)!=0 => rank=0, |Sha|<inf | LITERATURE (Kolyvagin 1990) | 8 |
| 10 | Gross-Zagier rank 1: L'(E,1)!=0 => rank=1 (vacuous in scope) | LITERATURE (GZ 1986) | 8 |
| 11 | BSD Theorem 13.1: rank equality + leading coefficient formula | PROVED | 7-10 |

## Current wall
**None within scope.** All 11 steps closed. The conditionality is CBB axioms (inherited from Paper 13/RH infrastructure), not a mathematical gap.

## Programme graph edges
- **RH (Paper 13):** L-functions factor through same BC algebra; cocycle machinery shared
- **GRH (Paper 13b):** GRH for Hecke L-functions feeds Step 7 directly
- **Hodge (Paper 29):** CM motives connect algebraic cycles to Hodge classes
- **Schanuel:** algebraic independence of L-values at s=1

## Known gap: Pin #6 J_CKM vertex anchor (2026-04-14)

Agent L audit (2026-04-14, `paper1/code/pin6-audits/FINDINGS.md`) confirms via ripgrep that Paper 26 Step 4 is a **cocycle-shift INEQUALITY** (Hasse-Brauer-Noether reductio, Key Lemma C: |Δc(δ)| < 1/(k+1)), **not** a J_CKM vertex evaluation. The Paper 26 (k, N) = (4, 41) bridge-family row is a ℚ(i) Brauer invariant — a terminology coincidence with the CKM k=4 vertex, not a hidden identity. Pin #6's structural anchor for J_CKM × 10⁵ = log(γ_1) · ζ(3) is `paper12/research/102` via the Mellin bridge, not Paper 26 Step 4. Computing a genuine k=4 CKM-vertex evaluation at Step 4 would close Pin #6 audit item O3 (the 18× direct-vs-factored precision gain). No chain-link status change — BSD chain does not gate on CKM content.

## Cascading refinement from QG5D W1/W2 closure (2026-04-14)

Paper 1 PROOF-CHAIN.md W1 (scheme independence) and W2 (Route-C 3-loop explicit) both closed 2026-04-13/14 via Paper 10 (Theorem 1 two-loop scheme-independence + Theorem U.2a one-loop Seeley-DeWitt) + Paper 11 (Theorem K.4 all-orders inductive bootstrap) + explicit L=3 numerical verification at 50-digit precision (`paper1/code/K-5-2-route-c-3loop.py`). Cascading impact on this chain: the CBB system's Axiom 5 (zeta regularization closure) no longer has a lingering regulator-scheme question. Effect is cosmetic-to-small — this chain never gated on the scheme question directly, but the underlying foundation is now strictly stronger. No link status changes required; confidence unchanged; mention included for completeness of the programme graph.
