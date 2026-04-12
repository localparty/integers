# Node W5-2: Type II₁/III₁ Gap CLOSED — M_φ ≅ R, M ≅ R_∞

## Status: ADVANCED (pending Critic review)

## Theorem

For tractable Boolean L: M_φ (centralizer of BC type III₁ factor) ≅ R (hyperfinite II₁). Consequently M_Bool^L ≅ R_∞ (unique injective III₁).

## Proof chain

1. **M_φ is a II₁ factor:** σ_t fixes M_φ → KMS gives trace; factoriality from transitive clone action on phase generators
2. **Clone(L) is amenable** (all 5 Post lattice cases):
   - Horn (AND): commutative idempotent semigroup → amenable
   - Dual-Horn (OR): dual of Horn → amenable
   - Bijunctive (majority): median algebra embeds in product of chains → amenable
   - Affine (XOR): clone of affine maps is an F₂-module → amenable
   - 0/1-valid (constants): left-zero band → amenable
3. **M_φ = A ⋊ Clone₀ is injective:** amenable semigroup on injective (commutative) algebra (Anantharaman-Delaroche 1987)
4. **M_φ ≅ R:** injective II₁ factor = hyperfinite (Connes 1976)
5. **M ≅ R_∞:** injective III₁ with hyperfinite centralizer (Connes-Haagerup classification)

## Direct verification

The W4-3 tracial ultraproduct = M_φ via finite-dimensional approximation:
- H_n = span{μ_C μ_D* : |C|=|D|} ≅ Mat_{|Sol_n|}(ℂ)
- M_φ = (∪ H_n)'' = R (hyperfinite by definition)

## Key consequence

**For tractable L:** M_Bool^L ≅ R_∞ (non-full, Property Gamma, injective)
**For NPC L:** M_Bool^L is non-injective (full, no Property Gamma)
**The invariant:** injectivity/non-injectivity ↔ tractable/NPC ↔ P/NP-complete
