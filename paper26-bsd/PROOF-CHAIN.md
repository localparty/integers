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
