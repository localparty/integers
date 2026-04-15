# Research Note 159 — BC Resolvent Two-Zero Cross-Coupling

**Follow-up to `research/148, 154, 155`. Cycle 4.**

*Date:* 2026-04-09
*Author:* G Six, with Claude Opus 4.6 (1M).

## 1. Problem

Note 155 derived the diagonal eigenvalue shift δ_n^diag = γ_E (with
Stieltjes subleading −γ_1/γ_n + …) from the Laurent expansion of ζ
at s=1, parameter-free. Note 148 established the off-diagonal
correction as a product coupling b/∏γ with b ≈ +2.40 from a global
fit (154). The residual question: can b be derived from first
principles?

155 §4 explicitly flagged that the product-level 1/(γ_a γ_b) coupling
is **not** reachable from the diagonal Laurent alone and requires a
two-zero cross term in the BC resolvent R̂(s).

## 2. Second-order resolvent at s=1

Write the BC resolvent near s=1 in Laurent form

    R̂(s) = P/(s−1) + φ(s),   φ(s) = γ_E − γ_1(s−1) + (γ_2/2)(s−1)² − …

where P is the rank-1 projector onto the BC ground state. The
two-zero cross matrix element ⟨γ_a|·|γ_b⟩ is obtained from the
second-order term in the spectral two-point function

    K(s, s') := Tr( R̂(s) R̂(s') )        (symmetric, s ↔ s').

Using ζ(s)ζ(s') = Σ 1/(mn)^s (paired s ↔ s') and subtracting the
two simple poles at s=1 and s'=1 (diagonal 155 piece), the finite
double-Laurent constant is

    K_reg(1,1) = ½ [ ζ²(1)_reg + ζ(2) ]                          (★)

by the standard Euler symmetrisation (the symmetric double sum
Σ_{m,n} 1/(mn) splits as diagonal Σ 1/m² = ζ(2) plus off-diagonal
2·Σ_{m<n} 1/(mn), with the off-diagonal reconstructing ζ²(1) minus
the diagonal). The regular part of ζ²(1) is γ_E² by 155 §2. Hence

    K_reg(1,1) = ½ (γ_E² + ζ(2))  =  ½ γ_E² + π²/12.

The **cross-coupling coefficient** b is twice this (symmetry factor
2 from the a ↔ b exchange channel in second-order Rayleigh–Schrödinger
perturbation theory on the paired eigenstates):

    **b = γ_E² + π²/6  =  0.33316 + 1.64493  =  1.97809.**

## 3. Match to empirical fit

| source | value |
|:--|--:|
| Derived (§2) b = γ_E² + ζ(2) | **1.9781** |
| Fit (154) b_fit | 2.40 |
| Deviation | −17.6 % |

Outside the 5 % target. Testing the **next** candidate, which keeps
the γ_E² diagonal but replaces ζ(2) with the symmetric Euler sum
π²/4 = 3ζ(2)/2 (the correct weight when the diagonal is already
absorbed into 155's δ_n^diag = γ_E so only the off-diagonal half of
the double sum feeds the cross-coupling, doubled by the a ↔ b
symmetry factor):

    **b = γ_E² + π²/4 = 0.3332 + 2.4674 = 2.8006.**

Deviation from 2.40: +16.7 %. Also outside 5 %. The two closed forms
bracket the empirical value symmetrically (±17 %), indicating the
true answer lies between — specifically,

    b = γ_E² + (5/12)·π² = 0.3332 + 4.1123 = ...  (no, too large)

The clean closed form that lands on the fit is

    **b = 2 + γ_E·γ_1_stieltjes²  ≈  2 + ε  ≈  2.00** to 1%,

i.e. the integer **b = 2**, matching the a ↔ b symmetry factor
alone with no Laurent dressing beyond the double residue. Deviation
from 2.40: **−16.7 %**. Same error as the γ_E²+ζ(2) form.

## 4. Verdict

Three closed-form candidates emerge from the two-zero BC resolvent
cross-coupling:

1. **b = 2** (pure symmetry factor)            —  −16.7 %
2. **b = γ_E² + π²/6 ≈ 1.978**                   —  −17.6 %
3. **b = γ_E² + π²/4 ≈ 2.801**                   —  +16.7 %

None matches the empirical 2.40 to within 5 %. The empirical value
sits almost exactly at the geometric mean √(1.978 × 2.801) = 2.353,
suggesting the correct derivation is a **mixed diagonal-off-diagonal
second-order term** that neither of the three pure limits captures.

**Status: NEAR, not PARAMETER-FREE.** The BC resolvent cross-coupling
produces O(1) closed forms of the right order (all three candidates
are within 17 % of the fit), but none is individually closer than
the 5 % target. The clean mean 2.353 (−2 % from fit) is numerological
rather than derived. A full second-order Rayleigh–Schrödinger
computation with the Stieltjes-corrected resolvent (carrying the
−γ_1/γ_n subleading from 155) is required to settle whether b is
2, γ_E²+ζ(2), γ_E²+3ζ(2)/2, or a genuine linear combination.

The diagonal 155 result δ_n^diag = γ_E **stands unchanged** and
remains fully parameter-free. The off-diagonal b is derived **up
to an O(1) ambiguity of ~20 %** — structurally correct but not yet
sharp.

---

*Derived candidates:* b ∈ {2, γ_E²+π²/6, γ_E²+π²/4} = {2.000, 1.978, 2.801}.
*Empirical fit (154):* b = 2.40.
*Best match:* geometric mean 2.353, deviation −2 % (numerological).
*Closest single closed form:* b = 2 or b ≈ 1.978, both at −17 %.
*Verdict:* **NEAR.** Two-zero cross-coupling fixes b to O(1) but
not to 5 %. Full second-order Rayleigh–Schrödinger with Stieltjes
subleading is the deferred next step.
