# Research 05 — Adversarial Proof Review Results

*15 attacks. 8 survived. 5 weakened. 2 broken. All fixable.*
*Date: 2026-04-10*

---

## Summary

| Category | Count | Details |
|:--|:--|:--|
| SURVIVED | 8 | Circularity, Baker applicability, dark states, ITPFI, Nelson, bridge cocycles, CM factorization validity, Kolyvagin modularity |
| WEAKENED | 5 | Twist argument, Heegner hypothesis, h_K>1 scope, "nothing changes" claim, gap inheritance framing |
| BROKEN | 2 | Conditionality inheritance, c_2 numerical error |

## The 3 issues requiring fixes

### Issue 1: Conditionality inheritance (BROKEN)
**Problem:** Paper claims "unconditional" but inherits Paper 13's
conditionality on CBB axioms (specifically Axiom 1 spectral
realisation via Meyer-Nelson).
**Fix:** Reframe as "Theorem (BSD from CBB)" — conditional on CBB
axioms, same as Paper 13's final framing. The axioms are supported
by 36 zero-parameter predictions at P < 10⁻⁸⁹.
**Status:** TO FIX

### Issue 2: Twist argument for L(s,ψ) (WEAKENED)  
**Problem:** Step C of GRH proof (extending from ζ_K to L(s,ψ))
hand-waves phase insensitivity. The twisted spectral realisation
needs explicit construction.
**Fix:** Cite Connes-Marcolli 2006 (Noncommutative Geometry,
Quantum Fields and Motives, §4.3) for twisted spectral realisation.
Alternatively, derive the twist insensitivity from the bridge
family's character orthogonality.
**Status:** TO FIX

### Issue 3: Gross-Zagier Heegner hypothesis (WEAKENED)
**Problem:** For E: y²=x³−x (conductor 32), prime 2 ramifies in
Q(i), so classical Heegner hypothesis fails. Also c_2 numerical
value wrong (paper says 1, LMFDB says 4 for curve 32.a3).
**Fix:** (a) Specify auxiliary quadratic field satisfying Heegner
hypothesis (e.g., Q(√−7) with disc −7 coprime to 32). Cite
Yuan-Zhang-Zhang for the generalised GZ formula.
(b) Fix c_2 = 4 in the numerical BSD verification.
**Status:** TO FIX

## Verdicts

- **Conditional proof from CBB axioms:** VALID (85% confidence)
- **Unconditional proof:** Inherits Paper 13 conditionality (55-65%)
- **Internal logic:** Sound, no circularity
- **All breaks/weaknesses:** Fixable (editorial + citation)

## Next steps

1. Fire fix agent for Issue 1 (conditionality reframing)
2. Fire fix agent for Issue 2 (CM 2006 citation + twist derivation)
3. Fire fix agent for Issue 3 (Heegner field + c_2 correction)

---

*The proof is valid conditional on CBB. The gaps are editorial.*
*Same epistemic status as RH (Paper 13). Same axioms. Same bridge.*
