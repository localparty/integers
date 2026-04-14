# Vertex Blackboard — BGS (Position 11, T2)

*Traversal 02 | Type: C (construction-primary) | Confidence: 5/10*

---

## Chain state (updated T2)
4/7 closed. Links 1, 2, 5, 7 closed. Links 3, 4, 6 open.

## T2 ACT phase — Links 3 and 4 assessed

**Link 2 closure (T2 deliverable)**: Modular flow ergodicity proved via Path B (factoriality + Tomita-Takesaki). Written to `paper32-bgs-spectral-statistics/research/01-modular-flow-ergodicity.md`. PROOF-CHAIN.md updated.

**Link 3 assessment (AC spectrum)**: **GENUINE gap**, but targeted.

The gap: Corollary 2.2 gives purely continuous spectrum (no atoms). But "continuous" ≠ "absolutely continuous" — singular continuous (Cantor-type) is logically possible.

In favor of AC:
- Sd(M) = R forces full-line support, consistent with AC
- For Araki-Woods/Powers hyperfinite type III₁ factors, modular spectrum tends to be Lebesgue AC
- Singular continuous on a dense Cantor subset of R would be exotic coincidence

What's needed:
- Show modular Hamiltonian has dense set of analytic vectors, OR
- Apply Haagerup standard-form smoothness to bootstrap to AC
- Likely a half-page argument if the right functional-analytic handle exists

**Link 4 assessment (GUE class)**: **CLOSABLE**.

Argument: KMS condition at β = 1 defines preferred time direction. Any antiunitary T commuting with σ_t must fix ω₁. For type III₁ factor with trivial center, T is forced to be modular conjugation J (already in Tomita-Takesaki). No residual antiunitary → Dyson threefold way → GUE class.

One lemma needed: "centralizer of σ_t acting on ω₁ contains no antiunitary" — follows from faithfulness + type III₁.

**Link 6 (GUE for BC = GUE for Riemann zeros)**: CONDITIONAL on Paper 13 spectral realization. Same CCM gate.

## T2 chain structure summary
```
L1 KNOWN → L2 PROVED → L3 GENUINE (AC spectrum) → L4 CLOSABLE (GUE class)
                                                           ↓
                         L5 LITERATURE → L6 CONDITIONAL (CCM) → L7 KNOWN
```

**The critical path is L3.** If AC spectrum closes, L4 is immediately CLOSABLE, and L5 is already LITERATURE. Only L6 (CCM gate, shared with RH/GRH) remains.

## Move
Vertex BGS: L2 PROVED, L3 GENUINE (AC spectrum — targeted), L4 CLOSABLE | Confidence 5/10
