# B2 — Eigenvector Approximation: Verdict

| Item | Status |
|:-----|:-------|
| Davis–Kahan structure | PASS |
| gap(T_0) ≥ C'' · λ | NOT PROVED (numerics only, research/24) |
| "ξ_0 converges to E(h)" | NOT PROVED (asserted) |
| PNT tail bound Σ (log p)/√p = O(1/λ) | **WRONG as stated** (series diverges) |
| L² → sup-norm on K via Paley–Wiener | PASS |
| Uniformity in N | NOT ESTABLISHED |
| λ vs N clarification | NOT DONE |

## Overall

**Weakened.** Theorem 6.4 is stated as λ → ∞ at fixed N, with
constants "depending on truncation geometry" (possibly on N). The
proof uses:

- a gap bound gap(T_0) ≥ C''·λ that is asserted but not proved,
- a PNT tail estimate that is wrong as literally written,
- a claim "ξ_0 converges to E(h)" that is not proved.

Structurally, the "ITPFI triangle" idea is sensible and the
Davis–Kahan + Meixner–Schäfke ingredients are standard. But the
as-written execution contains enough slips and unproved items
that a careful referee cannot close the argument from the
preprint alone.

The **downstream need** — joint uniformity in λ and N for the
Hurwitz identification in Section 10 — is also not established.
This is a real gap between Layer 3 and Layer 5.

**Confidence: 5/10** on the preprint as written. A corrected and
fully-supplied version could rise to 8/10 given the structural
soundness of the main idea.
