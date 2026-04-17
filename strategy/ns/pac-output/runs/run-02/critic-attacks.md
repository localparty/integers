# NS run-02 critic attacks

*Per-cell critic attack record. Paired with arbiter-decisions.md and kills.md.*
*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## Attack sweep scope

Critic agent swept all 70 cells of the 10-link × 7-requirement matrix. Non-trivial dissents recorded here (triviality: critic agrees with author → recorded silently).

## Non-trivial attacks (8 total)

### Attack A1 — L1 Req 4 (periodic T³)

- **Author verdict**: Pa — "S¹/Z₂ compact factor naturally provides periodic base" (p1§KK)
- **Critic attack**: SILENT. Argument: KK reduction produces a 4D theory where the periodic structure is in the *compactified* fifth dimension, not in the *base* T³ that variant (B) requires. L1 does not directly address T³ periodicity of u, p.
- **Author rebuttal**: The M⁴ base of KK reduction, when further compactified to M⁴ × S¹/Z₂ and sliced, gives the T³ base required by (B). The S¹/Z₂ factor is ALSO periodic-compatible. L1 materially feeds Req 4 even if it doesn't directly discharge it.
- **Resolution**: see arbiter-decisions.md A1.

### Attack A2 — L2 Req 2 (bounded energy)

- **Author verdict**: Pa — BHMR Landau-frame stress-energy → NS energy form at leading order
- **Critic attack**: SILENT. Argument: BHMR 2008 is a formal gradient expansion; convergence unknown; cannot count toward bounded-energy without rigorous convergence proof.
- **Author rebuttal**: The leading-order form ∫_{T³}|u|²dx is EXPLICITLY present in BHMR Landau-frame expansion at zeroth order. PARTIAL is honest — it's not PROVED (convergence open), but it's not SILENT (leading term is contentful).
- **Resolution**: see arbiter-decisions.md A2.

### Attack A3 — L2 Req 3 (div u = 0)

- **Author verdict**: Pa — incompressibility emerges at leading order of gradient expansion
- **Critic attack**: SILENT. Argument: "incompressibility at leading order" is an ASSUMPTION of BHMR, not a derivation.
- **Author rebuttal**: BHMR 2008 §4 shows that the near-equilibrium Landau-frame reduction *yields* the incompressibility constraint as a leading-order *consequence* of the conservation laws, not an assumption. PARTIAL is correct.
- **Resolution**: see arbiter-decisions.md A3.

### Attack A4 — L3 Req 3 (div u = 0)

- **Author verdict**: Pa — "structural parallel to YM gauge constraint"
- **Critic attack**: OPEN-BUT-ADDRESSED. Argument: the gauge-constraint → div-free functor is SPECIFICALLY unconstructed per p30§00 §3 "third wall" discussion. Naming this as W2 is more honest than PARTIAL, which would suggest progress where there is none beyond structural parallel.
- **Author rebuttal**: structural parallel is material progress. But critic is right that the functor itself is the named gap.
- **Resolution**: see arbiter-decisions.md A4 — critic wins, upgrade to O + name W2.

### Attack A5 — L4 Req 1 (C^∞)

- **Author verdict**: P — Δ₀^KK > 0 is PROVED (p8T4 + p11K.4 + p10 UNCONDITIONAL ALL-LOOP)
- **Critic attack**: PARTIAL. Argument: L4 is PROVED as a statement about the *spectral gap*, but that does NOT directly give C^∞ smoothness of u, p — the gap *feeds* L5 (BKM), which is the actual C^∞ addresser. L4 is an INPUT to Req 1, not an ADDRESSER.
- **Author rebuttal**: L4 is PROVED and L4 appears in the Req-1 discharge chain; labeling it P is accurate.
- **Resolution**: see arbiter-decisions.md A5 — critic wins; author's confusion between "this link is proved" and "this link addresses this sub-requirement" corrected.

### Attack A6 — L5 composite Req 5 (Leray→smooth)

- **Author verdict**: Pa — "composition handles the passage"
- **Critic attack**: OPEN-BUT-ADDRESSED. Argument: the passage Leray weak → strong smooth at L5 is CONDITIONAL on W1 resolution. Pa obscures the conditionality; O with explicit bypass citation is the §5d-honest verdict.
- **Author rebuttal**: Pa captures the conditionality via the "conditional on L5 closure" qualifier.
- **Resolution**: see arbiter-decisions.md A6 — critic wins; O is cleaner.

### Attack A7 — L5b Req 8 (CKN)

- **Author verdict**: P — cosphere-bundle WF-set triviality ⇒ E = ∅ ⇒ P₁(E) = 0 trivially
- **Critic attack**: PARTIAL. Argument: the claim "WF-triviality ⇒ singular set empty" requires an explicit Hörmander-calculus theorem equating wave-front-set triviality with pointwise smoothness. Standard in microlocal analysis BUT requires citation-level rigor not yet in p30§CKN-compat.
- **Author rebuttal**: the equivalence is textbook (Hörmander IV §8). P is defensible.
- **Resolution**: see arbiter-decisions.md A7 — critic wins; pending explicit citation chain in B_bare §14. Upgrade to P after WF→CKN cross-reference audit.

### Attack A8 — L6 Req 2 (bounded energy)

- **Author verdict**: Pa — "KK Killing → 4D viscous dissipation"
- **Critic attack**: OPEN-BUT-ADDRESSED. Argument: L6 is CONJECTURED per PROOF-CHAIN v2.1. That is a NAMED GAP, not a partial success. Labeling as Pa is insufficient disclosure; O with W3 name + bypass is §5d-mandatory.
- **Author rebuttal**: CONJECTURED ≠ SILENT — Pa was a compromise.
- **Resolution**: see arbiter-decisions.md A8 — critic wins; upgrade to O + name W3.

---

## Attack summary

| Cell | Author | Critic | Arbiter final | Winner |
|------|--------|--------|---------------|--------|
| A1  L1 Req 4   | Pa | S  | **Pa** | Author |
| A2  L2 Req 2   | Pa | S  | **Pa** | Author |
| A3  L2 Req 3   | Pa | S  | **Pa** | Author |
| A4  L3 Req 3   | Pa | O  | **O**  | Critic |
| A5  L4 Req 1   | P  | Pa | **Pa** | Critic |
| A6  L5 Req 5   | Pa | O  | **O**  | Critic |
| A7  L5b Req 8  | P  | Pa | **Pa** | Critic |
| A8  L6 Req 2   | Pa | O  | **O**  | Critic |

Critic-wins: 5. Author-wins: 3. Net: matrix tightened toward HONESTY (5 upgrades to OPEN-BUT-ADDRESSED or PARTIAL-downgrade from over-claimed P/Pa).

No SILENTs introduced; no new named walls introduced beyond W1/W2/W3/W4 already identified in strategy §6 / §11 / brief DELTA 10.

---

## Attacks considered and dropped (trivial / sweep-rejected)

- 62 cells where critic agrees with author's verdict at first pass (most SILENT cells with clean bypass pointers; most P/Pa cells at L7/L8 where composition semantics are clear).

---

*End of critic-attacks.md. 2026-04-14.*
