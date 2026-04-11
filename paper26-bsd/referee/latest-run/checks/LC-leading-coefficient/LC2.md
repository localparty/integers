# Check LC2: BSD leading coefficient at rank 1

**Group:** LC
**Source:** Paper 26 §12.4, §13.1
**Pass criterion:** L'(E,1) = Ω · R · |Ш| · ∏ c_p / |E_tors|² with
all terms defined and computed.

**Verdict:** VACUOUS per Remark 12.6
**Rigor label:** [LEMMA] (vacuous statement)

**Justification:** Paper 26's own Remark 12.6 admits: "There are
no CM curves over ℚ with CM by a class-number-1 imaginary
quadratic field that have analytic rank ≥ 1 over ℚ." This
follows because GRH implies L(1, ψ) ≠ 0 (since Re(1) = 1 ≠ 1/2),
hence L(E, 1) = L(1, ψ) · L(1, ψ̄) ≠ 0 for all CM curves in
scope.

The rank-1 case of Theorem 13.1 is therefore vacuously true — it
is a conditional "if rank = 1, then ..." where the hypothesis is
never satisfied within the claimed scope.

**This is a valid logical statement.** Vacuous truths are truths.
But it means the substantive content of Paper 26's BSD theorem is
entirely at rank 0. The "rank 0 + rank 1" framing of Theorem 13.1
reduces to "rank 0" for CM curves with h_K = 1 over ℚ.

**Cross-references:**
- Per-Point: points/D3-gross-zagier-rank1/verdict.md (which
  expands on the vacuity)
