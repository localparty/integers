# Node: XOR Exception — M_Bool^{XOR} Non-fullness via Parity Decomposition

## Status: ADVANCED

## Result

M_Bool^{XOR} is non-full. The mechanism is fundamentally different from the local-polymorphism cases:

- **XOR-SAT solution space** = affine subspace V = x₀ + ker(A) of GF(2)^n
- **Parity checks** (rows of A) define conserved GF(2)-linear quantities
- These conserved quantities generate a **non-trivial center** in π_ω(A)''
- M_Bool^{XOR} decomposes as a **direct integral of type I factors**
- A direct integral of type I factors is non-full (it's not even a single factor)

## Bridge theorem survival

| CSP | Mechanism | Factor | Non-full? |
|---|---|---|---|
| 2-SAT | Mixing (local polymorphisms) | II₁ or III₁, non-Gamma | YES |
| Horn | Mixing | same | YES |
| dual-Horn | Mixing | same | YES |
| XOR-SAT | Parity decomposition (algebraic) | Direct integral of type I | YES |
| NPC (3-SAT etc.) | — | Full (conjectured) | NO |

All 5 tractable classes give non-full factors. The bridge holds: Taylor ↔ non-full.

## Self-Suspicion

1. The identification of M_Bool^{XOR} as direct integral of type I needs verification in the thermodynamic limit (d → ∞). Parity checks must remain central as n → ∞ with bounded check density.
2. PATD-CONDEXP should be corrected from 4/5 to 5/5 (XOR uses Route B, not Route A).
3. The "disconnected walk" framing is misleading — it's not a walk failure but a wrong-tool-for-the-job situation. The correct tool is linear algebra over GF(2).
