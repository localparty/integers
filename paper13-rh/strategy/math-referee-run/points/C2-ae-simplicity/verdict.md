# C2 — AE Simplicity: Verdict

| Item | Status |
|:-----|:-------|
| AE meaning (discrete exceptional set) | PASS |
| Finite certification at N ≤ 20, λ = √14 | PASS (120-digit) |
| Slepian-limit extension to N > 20 | **HEURISTIC, not theorem** |
| Sufficiency for the chain | CONDITIONAL |
| Gap erosion (gap → 0 as N → ∞) | NOT DISCUSSED |
| Per-N simplicity for all N (at λ = √14) | NOT RIGOROUSLY ESTABLISHED |
| Identity-theorem + real-analyticity | PASS at each fixed N |
| N = 1 codimension argument | PASS |
| Even-sector restriction validity | INHERITED FROM A1 |

## Overall

**Split verdict.** The **finite certification** at N ≤ 20 is
rigorous and uses 120-digit arithmetic carefully. The identity
theorem then extends it to AE simplicity at each N ≤ 20. This
is a genuine contribution.

**But** the extension to N > 20 is the paper's weakest point in
Layer 3. The Slepian-limit argument is a **plausibility
argument**, not a proof. It relies on:

- Operator convergence A^{ev}(λ, N) → P^{(λ)} (not stated as a
  theorem),
- Continuity of the ground-state overlap under this convergence
  (not stated),
- Monotonicity of the overlap in N inferred from 5 data points
  (not monotonic in general).

The erosion of the spectral gap (exponentially in N) is also not
discussed as a concern. At high enough N, the numerical
certification method fails at any fixed precision.

**Confidence: 6/10** on AE simplicity as presented. The
certification for N ≤ 20 is excellent; the extension is a
weak link.

For a Clay-millennium-grade proof, this needs to be upgraded to a
genuine theorem. Either:

(a) A Slepian-convergence theorem proving operator convergence
and eigenvector continuity, or

(b) A precision-scalable certification at all N up to some
N_max determined by the downstream argument, or

(c) A fundamentally different approach (e.g., analytic
continuation in N) that does not rely on per-N simplicity.

As currently written, this is a concrete gap.
