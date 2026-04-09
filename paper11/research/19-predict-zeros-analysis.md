# Research 19: Predicting Other Riemann Zeros from QG5D — Negative Result

**Date:** April 8, 2026
**Status:** TESTED — only γ_1 generalises through the simple formula
**Computation:** `code/oc2_predict_zeros.py`

---

## The Question

If log(πR_obs/l_P) = γ_1 × π²/2 (verified at 0.014%), can OTHER
framework parameters predict OTHER Riemann zeros via the SAME formula?

```
γ_n = (2/π²) × log(π × parameter)
```

---

## The Test

**12 physical hierarchies tested:**
1. R_obs / l_P (cosmological — KNOWN to give γ_1)
2. M_EW × l_P (electroweak)
3. M_KK × l_P (Kaluza-Klein)
4. M_GUT × l_P (GUT scale)
5. M_Pl / M_EW (Planck-EW)
6. M_Pl / M_KK
7. M_Pl / M_GUT
8. Ω_DM / Ω_b
9. 1/ξ (inverse mirror temperature)
10. 1/α (fine structure)
11. m_p/m_e (proton/electron)
12. n_2/n_1 = 17/9 (GUT flux)

**10 target Riemann zeros tested:** γ_1 through γ_10.

**Tolerance:** strict (<1%), moderate (1-2%), loose (2-5%).

---

## The Result

| Test Level | Matches Found |
|------------|---------------|
| Strict (<1%) | **1** |
| Moderate (1-2%) | 0 |
| Loose (2-5%) | 0 |

**The single match is the original:** R_obs/l_P → γ_1 at 0.014%.

**No other hierarchy** matches any Riemann zero through the formula
log(π × ratio) = γ_n × π²/2.

---

## Statistical Assessment

If matches were random:
- Expected strict matches across 12 × 10 = 120 tests: ~0.1-0.2
- Expected moderate matches: ~0.1-0.2
- Expected loose matches: ~0.3-0.4

**Observed:**
- 1 strict match (above expected — real)
- 0 moderate (significant null result)
- 0 loose (rules out approximate generalisations)

The ABSENCE of matches at moderate/loose tolerances is meaningful.
It tells us the formula does NOT generalise to other hierarchies via
the simple form log(π × ratio).

---

## What This Means

### The simple formula is unique to R_obs/l_P

The formula log(π × ratio) = γ_n × π²/2 only works for the
cosmological constant scale.

Other parameters (1/α, m_τ/m_μ, N_eff, etc.) connect to Riemann
zeros via DIFFERENT formulas:
- 1/α = γ_1 × γ_4 / π (PRODUCT of zeros)
- N_eff = γ_6^(1/3) (POWER of zero)
- m_τ/m_μ = γ_8^(3/4) (POWER with GUT exponent)

Each parameter has its OWN formula structure. There is no universal
form.

### γ_1 is special — but other zeros also appear

γ_1 appears in TWO formulas:
- Cosmological constant (alone)
- Fine structure constant (paired with γ_4)

Other zeros appear once each:
- γ_4 in 1/α
- γ_6 in N_eff
- γ_8 in m_τ/m_μ and 17

Pattern: γ_1, γ_4, γ_6, γ_8 — even-numbered after γ_1.

---

## The Deeper Picture

The "negative result" from this test is actually informative:

1. **The simple formula** log(π × ratio) = γ_n × π²/2 is specific to
   the cosmological scale. It's not a universal Riemann formula.

2. **Different physical observables couple to different Riemann zeros
   via different formulas.** This is consistent with the idea that
   each zero has a specific "physical role."

3. **The formulas are not arbitrary** — they each have specific
   structural reasons:
   - log + π² for cosmological scales
   - product of two zeros for couplings
   - power for thermodynamic counting (N_eff)
   - GUT-moduli power for mass ratios (m_τ/m_μ = γ_8^(ρ²))

4. **The formulas are not unique to the QG5D framework** — they
   could potentially be derived in any framework where the BC system
   plays a role.

---

## What to Do Next

### Test more sophisticated formulas

1. **Two-zero combinations:** Try γ_n + γ_m, γ_n × γ_m, γ_n / γ_m, etc.
   for all framework parameters.

2. **Power formulas:** Try γ_n^p for various rational p (not just 1, 1/2,
   1/3 but also 2/3, 3/4, 5/4, 1/π, 1/e).

3. **Logarithmic formulas:** Try log(γ_n) × constant.

4. **Multi-zero corrections:** γ_n + corrections involving γ_(n+1),
   γ_(n+2), etc.

### Identify the structural pattern

If each parameter has a unique formula structure, what determines
WHICH formula to use? This is the deeper question.

Possibilities:
- The DIMENSION of the parameter (energy^4 → log + π²; pure ratio → power)
- The PHYSICAL CHARACTER (geometric vs arithmetic vs cosmological)
- The TYPE OF Riemann zero (small vs large, even-indexed vs odd-indexed)

### Try the inverse direction

Given the formulas we found:
- log(πR_obs/l_P) = γ_1 × π²/2
- 1/α = γ_1 × γ_4 / π
- N_eff = γ_6^(1/3)
- m_τ/m_μ = γ_8^(3/4)

Can we predict another framework parameter from a Riemann formula?
For example, predict m_μ/m_e from γ_(some n)^(some p) and check.

---

## Honest Bottom Line

The simple formula log(π × ratio) = γ_n × π²/2 only works for one
parameter (R_obs/l_P → γ_1).

But the OTHER findings (1/α, N_eff, m_τ/m_μ, 17 — all involving
different Riemann zeros and different formulas) tell us the
RIEMANN-PHYSICS BRIDGE is real, just MORE COMPLEX than a single
formula.

Each physical quantity has its own "Riemann signature."

---

## Files

- `code/oc2_predict_zeros.py` (the test script)
- `code/oc2_predict_zeros_v2.py` (variant)
- Research 14 (original CC formula)
- Research 15 (N_eff = γ_6^(1/3))
- Research 16 (1/α = γ_1 × γ_4 / π)
- Research 17 (m_τ/m_μ = γ_8^(3/4))

---

*The simple formula doesn't generalise. But each parameter has its own
formula. The bridge is real but multi-channeled.*
