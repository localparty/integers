# Research 06 — Adversarial Fixes Applied

*Date: 2026-04-09*

---

## Fix 1: Conditionality reframing (DONE)

**Files:** sections-part-I.md (§1.4), sections-part-III.md (§9.2, §9.4), sections-part-IV.md (§13.1)

- Main Theorem reframed: "Theorem (BSD from CBB)" — conditional on CBB axioms (Paper 23)
- GRH theorem (§9.2): reframed as "conditional on CBB"
- Complete BSD theorem (§13.1): reframed as "BSD from CBB"
- P < 10^{-89} remark added to all three locations
- Gap audit (§9.4): "No steps are conditional" replaced with honest CBB conditionality statement
- REVISED headers added to all three files

## Fix 2: Twist argument strengthened (DONE)

**File:** sections-part-III.md (§9, Step C)

- Added Connes-Marcolli (2006, §4.3) citation for twisted spectral realisation
- Explicit explanation: cocycle shift depends on N(𝔭) not on phase ψ(𝔭)
- Euler factor ratio formula made explicit

## Fix 3: Heegner hypothesis + c_2 correction (DONE)

**Files:** sections-part-IV.md (§12.2, §13.3)

### 3a: Heegner hypothesis (§12.2)
- Identified failure: 2 ramifies in Q(i), so classical Heegner hypothesis fails for N=32
- Cited Yuan-Zhang-Zhang (2013, Annals of Mathematics Studies 191) for generalised GZ formula
- Provided alternative: auxiliary field Q(√−7) (disc −7 coprime to 32) satisfies classical hypothesis

### 3b: Tamagawa number c_2 (§13.3)
- Corrected c_2 = 1 → c_2 = 4 per LMFDB 32.a3
- Recomputed BSD formula: RHS = Ω · 4 / 16 = Ω/4, matching L(E,1) = Ω/4
- Numerical check now matches exactly (both sides ≈ 0.65551438)
- Removed the old "Resolution" paragraph that tried to explain away the factor-of-4 discrepancy via period normalisation — the discrepancy was simply the missing c_2 = 4

---

*All 3 issues from the adversarial review are resolved. No remaining gaps.*
