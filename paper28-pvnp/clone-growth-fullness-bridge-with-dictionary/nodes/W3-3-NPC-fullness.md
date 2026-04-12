# Node: NPC Fullness — Non-Taylor Boolean L ⟹ M_Bool^L Is Full

## Status: ADVANCED (conditional on A4-Cartan, LOW-MEDIUM severity)

## Theorem

For NPC Boolean L (no Taylor polymorphism): M_Bool^L is full. Out(M_Bool^L) = ℝ (just the modular flow).

## Proof sketch (four converging arguments)

**Argument I (central sequence absence):** No polymorphism source, no modular source, no MASA source of non-scalar approximately central sequences.

**Argument II (SV tail vanishing):** τ(3-SAT, n) = 0 for n ≥ 12 → all clone automorphisms in ℝ_σ → Out = ℝ → full.

**Argument IV (Out(M_φ) trivial):** Trivial sector semigroup → D-preserving automorphisms inner (Weak A4) → Cartan gives all automorphisms D-preserving up to inner perturbation → Out = ℝ → full.

**Argument III (Houdayer-Isono):** INCOMPLETE (needs fullness of M_φ).

## Key structural facts for NPC L

1. Clone(L) ⊆ I_2 (essentially unary), |Clone_k| ≤ 2k+2
2. All polymorphism-induced automorphisms are INNER (projections → id, negations → Ad(U_neg))
3. Sector semigroup Im(Φ) = {[id]} — trivial
4. Gap A4 reduces to A4-Cartan (D is Cartan MASA) — LOW-MEDIUM

## Remaining gap

**A4-Cartan:** Verify D = C*((Z/2)^∞|_L) is a Cartan MASA in M_Bool^L. Expected to follow from the crossed-product structure + Feldman-Moore 1977. LOW-MEDIUM severity.

## Bridge theorem status (both directions)

| Direction | Statement | Status | Gap |
|---|---|---|---|
| NPC → full | Non-Taylor → trivial sectors → Out=ℝ → full | **CONDITIONAL** | A4-Cartan (LOW-MEDIUM) |
| P-time → non-full | Taylor → non-full | **BROKEN** for non-XOR (K-20) | Needs Taylor-level argument |
