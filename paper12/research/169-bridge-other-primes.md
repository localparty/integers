# Research 169: Bridge at Other Primes and Cyclotomic Levels

*Cycle 5 — creative. Authors: G Six with Claude Opus 4.6. Date: 2026-04-09.*

> **Goal.** Extend the bridge theorem of research/158, 162 —
> Frobenius-Z/3Z (p=5, N=13) = Jones-Z/3Z (index 3) — to other
> (p, N) pairs. For each k = [(Z/NZ)*:⟨p⟩] ∈ {2, 4, 5, 6} find
> the minimal candidate and ask: does it encode framework content?

## 1. Setup

Given prime p and level N with gcd(p,N) = 1, let f = ord_N(p)
(residue degree of Frob_p on Q(ζ_N)/Q) and

  k := φ(N) / f = |(Z/NZ)*/⟨p⟩|.

When (Z/NZ)*/⟨p⟩ is cyclic of order k, the cyclic algebra
(Q(ζ_N)/Q, Frob_p, ζ_k) carries a Brauer class in
Br(Q)[k] with local Hasse invariant 1/k at p, and pairs (by the
research/158 construction) with a Jones subfactor of index k.

The reference case k = 3 is (p, N, f) = (5, 13, 4).

## 2. Table of minimal candidates

| k | p | N  | f = ord_N(p) | φ(N) | (Z/NZ)*/⟨p⟩ cyclic? |
|---|---|----|--------------|------|---------------------|
| 2 | 2 | 7  | 3            | 6    | yes (≅ Z/2Z)        |
| 3 | 5 | 13 | 4            | 12   | yes (≅ Z/3Z) [ref]  |
| 4 | 3 | 13 | 3            | 12   | yes (≅ Z/4Z)        |
| 5 | 7 | 25 | 4            | 20   | yes (≅ Z/5Z)        |
| 6 | 7 | 19 | 3            | 18   | yes (≅ Z/6Z)        |

(k = 2 chosen with nontrivial f > 1 for arithmetic content; the
degenerate (p, N) = (5, 4) with f = 1 also gives k = 2 but is
trivial. k = 4 uses the **same** level N = 13 as the reference,
now with Frob_3 instead of Frob_5. k = 5 requires N = 25 = 5²
because φ(N) must be divisible by 5, forcing N ∈ {11, 25, …};
(7, 25) has (Z/25Z)*/⟨7⟩ ≅ Z/5Z. k = 6 uses N = 19 with
Frob_7 of order 3, quotient ≅ Z/6Z.)

## 3. Proposed physical identifications

**k = 2, (p, N) = (2, 7): CP and the Z/2Z of matter/antimatter.**
H²(Z/2Z, U(1)) = 0, so the cocycle class is trivial — there is
no Brauer obstruction. This matches the fact that CP is a
**discrete symmetry**, not a sub-factor index. The k = 2 bridge
says: CP is Frobenius-trivial, consistent with CP being realised
by complex conjugation on Q(ζ_7) (the unique Z/2Z quotient of
(Z/7Z)* modulo ⟨2⟩). **Verdict: structural, but expected-trivial.**

**k = 4, (p, N) = (3, 13): four forces? No — SU(4) flavour.**
N = 13 is the same level as the generation bridge; switching
p = 5 → p = 3 turns the Z/3Z quotient into Z/4Z. The natural
interpretation is **not** "4 forces" (forces are gauge, not
flavour) but rather the **Pati–Salam SU(4)_c ⊃ SU(3)_c × U(1)_{B−L}**
lepton-as-fourth-colour structure, or equivalently the four
weak-isospin components of one generation (u_L, d_L, u_R, d_R).
H²(Z/4Z, U(1)) ≅ Z/4Z, so the class is **nontrivial** and the
Jones subfactor has index 4 — exactly Jones' first non-integer
index above 3 is 4. **Verdict: strong candidate; deserves a
full Step-1–6 replay at (p, N) = (3, 13).**

**k = 5, (p, N) = (7, 25): no obvious framework slot.**
Five generations are excluded by Z-pole width. Five dimensions
(M⁴ × S¹) is a geometric, not cocycle, feature. H²(Z/5Z, U(1))
≅ Z/5Z is nontrivial but the index-5 Jones subfactor lies
beyond the physically realised index set {1, 2, 3, 4, 4cos²(π/n)}
for discrete series. **Verdict: mathematically real, physically
unassigned. Park.**

**k = 6, (p, N) = (7, 19): six quarks? Yes — the flavour Z/6Z.**
The Standard Model has exactly **six quark flavours** (u, d, c,
s, t, b), and the natural Z/6Z = Z/2Z × Z/3Z factorises as
**(up/down) × (generation)**. The k = 6 bridge at (p, N) = (7, 19)
therefore sits directly above the k = 3 bridge at (5, 13), with
the Z/2Z factor supplying weak isospin. H²(Z/6Z, U(1)) ≅ Z/6Z
is nontrivial, and index 6 is a legal Jones index (integer > 4).
Even better: the factorisation Z/6Z ≅ Z/2Z × Z/3Z mirrors the
arithmetic factorisation 19 − 1 = 18 = 2 · 3², so Frob_7 of
order 3 leaves the Z/2Z ⊕ Z/3Z quotient. **Verdict: strongest
creative candidate. Promote to research/170.**

## 4. Summary verdict

| k | candidate      | physical slot                        | strength |
|---|----------------|--------------------------------------|----------|
| 2 | (2, 7)         | CP (trivially, H² = 0)               | expected |
| 3 | (5, 13) [ref]  | 3 generations + Koide                | proven   |
| 4 | (3, 13)        | Pati–Salam SU(4) / weak-isospin quad | strong   |
| 5 | (7, 25)        | none                                 | park     |
| 6 | (7, 19)        | 6 quark flavours = isospin × gen     | strong   |

The k = 3 bridge is not isolated: it sits inside a lattice of
Frobenius-Jones dualities indexed by (p, N), and at least two
other entries (k = 4 and k = 6) land squarely on **already-known**
Standard-Model multiplicities. The k = 6 case is especially
striking because its arithmetic factorisation Z/6Z = Z/2Z × Z/3Z
exactly matches the physical factorisation (isospin) × (generation).

**Next step (research/170):** replay research/158 Steps 1–6 at
(p, N) = (7, 19) with target G = Z/6Z and index-6 Jones subfactor,
and check whether the resulting cocycle encodes the CKM structure.
