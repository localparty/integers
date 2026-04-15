# A1 — CCM Construction: Verdict

## Summary

Layer 1 is an **external dependency on an unrefereed 2025 preprint
(arXiv:2511.22755)** plus a **non-trivial even-sector modification**
introduced by Paper 13 whose compatibility with CCM's Theorem 5.10
is asserted but not proved.

## Scored items

| Item | Status |
|:-----|:-------|
| Operators D_N correctly referenced | PASS |
| Self-adjointness in T-inner product | PASS (on CCM's authority) |
| Theorem 5.10(i) reality+simplicity | PASS (on CCM's authority) |
| Theorem 5.10(ii) O(ρ^{-N}) rate | PASS (on CCM's authority, assumed a priori not a posteriori) |
| Theorem 5.10(iii) zero/spectrum identification | PASS (on CCM's authority) |
| Even-sector restriction compatibility | **WEAKENED** — asserted but not proved |
| Real-zero property of ξ̂_N (needed for Hurwitz) | **NOT STATED** — required for the real argument |
| δ_N(ξ) ≠ 0 | UNPROVEN (flagged LOW in research/43) |
| 10^{−55} at N = 6 independently verified | NO |
| No hidden RH assumption | PASS |

## Overall verdict

**Layer 1 is conditional on CCM being correct, and Paper 13's
even-sector modification of CCM being compatible.** The latter is
a new assumption that Paper 13 introduces and does not
substantiate rigorously.

The proof is appropriately labelled 8/10 by the authors, with the
2-point gap attributed to CCM preprint status. That accounting is
honest. However, even a fully refereed CCM would not automatically
cover the even-sector restriction — that is a separate burden on
Paper 13 that remains unmet.

**What would close this point:**

1. Either cite or prove that CCM's Theorem 5.10 (all three
   conclusions) restricts cleanly to the even sector. Specifically:
   parity commutation with QW_λ^N, the structure of the rank-one
   perturbation vector η in the even sector, and the even-sector
   analogue of the identification theorem.

2. Explicitly state and prove the real-zero property of ξ̂_N
   (every zero in the complex plane is real). This is what the
   Hurwitz argument in Section 10 actually needs but does not
   explicitly invoke.

3. Settle δ_N(ξ) ≠ 0 — this is a concrete finite-dim computation.

Until these three items are closed, Layer 1 carries a compound
risk of (CCM preprint errors) × (even-sector modification not
fully justified).
