# Vertex Blackboard — BGS (Position 11, T3 Deep Pass)

*Traversal 03 | Type: C | Confidence: 5/10 → 6/10*

---

## Chain state (updated T3)
**5/7 closed.** L1 KNOWN, L2 PROVED (T2), L4 PROVED (T3), L5 LITERATURE, L7 KNOWN. Open: L3 (AC spectrum), L6 (CCM gate).

## T3 ACT phase — L4 proved + L3 gap precisely characterized

**BGS L4 PROVED**: Lemma 4.1 — no antiunitary symmetry preserving ω₁ and reversing σ_t. The arithmetic obstruction ω₁(μ_p*μ_p) = 1 ≠ 1/p = ω₁(μ_pμ_p*) is a direct numerical inequality. Written to `research/02-gue-class-dyson.md`.

**BGS L3 gap characterized**: The ITPFI convolution approach (Approach C) shows μ̂(t) = Π_p[(p+p^{-it})/(p+1)] decays like 1/|ζ(1+it)| ~ 1/log|t|, NOT L¹. The gap connects to the zero-free region of zeta. Even under RH, the decay is insufficient for AC. Written to `research/03-ac-spectrum-gap-analysis.md`.

**L3 bypass route identified**: If PCC works with continuous (not necessarily AC) spectral measures, L3 is unnecessary. Investigation dispatched for T4.

## T3 chain structure
```
L1 KNOWN → L2 PROVED → L3 GENUINE → L4 PROVED → L5 LITERATURE → L6 COND → L7 KNOWN
                         ↑ wall                                    ↑ CCM
                   (ζ(1+it) decay)                           (shared gate)
```

## Move
Vertex BGS: **L4 PROVED** (T3 headline); L3 GENUINE (precisely characterized); bypass route to T4 | Confidence 6/10
