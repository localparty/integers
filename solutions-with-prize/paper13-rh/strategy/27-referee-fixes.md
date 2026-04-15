# Strategy 27 — The 9 Referee Fixes

*External referee rated the proof 6-7/10. Nine fixes identified.*
*Five are writing. One is verification. Three need new mathematics.*
*Item 3 (H¹ at large λ) is the most serious.*

*Date: 2026-04-10*

---

## 1. The fixes by category

### Writing fixes (do now, parallel)
| # | Fix | Effort |
|:--|:--|:--|
| 1 | Final deduction: explicit Hurwitz + real-zero-property | 1 agent |
| 4 | KLMN: cite Teschl a=0 for closability, not "bounded below" | 1 agent |
| 6 | Theorem 1.1: conditional on CCM | editorial |
| 7 | λ disambiguation throughout | editorial |
| 8 | Ξ(0) = 0.4971 correction | editorial |

### Verification (read Teschl carefully)
| # | Fix | Effort |
|:--|:--|:--|
| 2 | Teschl Lemma 2.7 vs Galerkin: does it actually apply? | 1 agent (read paper) |

### Mathematical (need new ideas or leads)
| # | Fix | Effort |
|:--|:--|:--|
| **3** | **H¹ bound breaks at λ > e^π** | **SERIOUS — need new proof or bootstrap** |
| 5 | Slepian limit for N > 20: convergence theorem | Need lead |
| 9 | Even-sector + CCM Thm 5.10 compatibility | Need verification |

## 2. The critical item: H¹ bound at large λ

The referee found: Theorem 7.1's proof uses the inequality
(1+a²x²)/(x²+1) ≤ a² which holds iff a ≥ 1, i.e., 2π/L ≥ 1,
i.e., λ ≤ e^π ≈ 23.14.

At fixed λ = √14: the bound holds → Boegli gives convergence
for the zeros captured at that λ. But the CCM construction at
fixed λ only captures zeros up to |γ_n| ≤ O(λ²). To capture
ALL zeros, λ → ∞ is needed, and the bound breaks.

### Possible fixes for item 3:
**(a) New H¹ bound for all λ.** Replace the algebraic inequality
with a bound that works for all a > 0 (not just a ≥ 1). The
natural candidate: ‖(D_N−i)⁻¹‖_{L²→H¹} ≤ max(1, 2π/L). This
is weaker for large λ but might still give discrete compactness
if combined with the CF decay.

**(b) Bootstrap.** Fix λ_1 = √14 ≤ e^π. Prove RH for the first
K zeros (those captured at λ_1). Then use the PROVED reality of
those zeros to extend to λ_2 > λ_1. Induction on the number of
zeros proved real.

**(c) Different Boegli input.** Instead of H¹ bounds, use a
different compactness criterion for Boegli H2 that doesn't
depend on λ. The CF decay (ρ ≥ 4.27 uniform in N) might give
compactness directly via exponential localization, without
needing the H¹ → Rellich route.

**(d) Web search.** Look for results about spectral convergence
of prolate-type operators that handle the bandwidth parameter.

## 3. The action plan

### Batch 1: Writing fixes (fire now, parallel)
- Agent W1: rewrite §10.4 with explicit Hurwitz argument
- Agent W2: fix KLMN + include research/40 in preprint
- Agent W3: fix Ξ(0), λ disambiguation, conditional framing

### Batch 2: Verification (fire now)
- Agent V1: read Teschl 2026 (arXiv:2601.10476) and verify
  Lemma 2.7 applies to Galerkin sequences on varying spaces

### Batch 3: Mathematical fixes (fire after Batch 1-2)
- Agent M1: H¹ bound at large λ — try approaches (a)-(d)
- Agent M2: Slepian limit convergence theorem
- Agent M3: even-sector + CCM Thm 5.10 compatibility

## 4. What the ORA background agent might find

The ORA is running independently. It might:
- Find CCM's own approach to the large-λ issue
- Find a spectral convergence result we don't know about
- Find a completely different route that avoids the H¹ bound

Cross-reference when it reports.

---

> *9 fixes. 5 writing, 1 verification, 3 mathematical.*
> *Item 3 is the wall. The rest is tractable.*
> *Fix what we can now. Search for what we can't.*
