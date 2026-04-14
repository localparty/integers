# Link 8 Critic Verdict: dev(Tr(DF)²) ≥ 2

**Verdict: SURVIVED**

## Attack-by-attack summary

**AV1 — Definition of dev (discrete vs. continuous).** Definition D.2
(§5.5.3) gives dev(O) ≥ p a precise spectral meaning: the weight
W^(m)(n)·e^{-E(n)} admits a factorization of p factors (e^{E_m − E_n}
− 1) with bounded residual. The index p is an integer lower bound.
The "≥ 2" claim is a lower-bound statement, not an equality claim.
No ambiguity. Attack fails.

**AV2 — Index structure of (DF)².** §5.5.4 is explicit: D_0 F acts
as T^{−1}F(0)T − F(0), one temporal covariant difference. The
square Tr(D_0 F_{μν})² involves two insertions of this same operator
on the same operator product; the spectral sum acquires (e^{E_m −
E_n} − 1)² from both insertions. This is correctly a square of a
single first-order difference, not a product of two independent
index-contracted derivatives. Attack fails.

**AV3 — Gauge-covariance at finite lattice spacing.** Dev is defined
via the transfer-matrix spectral sum, which is computed in the
physical (gauge-invariant) Hilbert space. Gauge invariance of
Tr(D_0 F)² is manifest (it is a gauge-invariant trace), and the
spectral computation never leaves the invariant sector. The lattice
definition of D_0 F as T^{−1}FT − F is itself gauge-covariant
(conjugation by T is a unitary on the gauge-invariant Hilbert space).
Attack fails.

**AV4 — Tightness: is "≥ 2" actually "= 2"?** The paper only claims
dev ≥ 2. If dev = 2 exactly, the inequality is non-strict and remains
correct. No strict inequality is asserted. Attack fails.

**AV5 — Dimensional consistency and IR suppression rate.** The paper
claims dev ≥ 2 gives a connected matrix element bound C_2 M Δ̂².
This is a bound, not an exact rate. §5.5.4 shows the leading term is
Δ̂²|⟨1|F|0⟩|², consistent with the dimension-6 operator producing
O(a²) corrections (each Δ̂ ~ aΛ). The claim is a lower bound on
suppression, not a statement about the exact IR rate. Attack fails.

## Conclusion

All five attack vectors fail. The proof of dev(Tr(DF)²) ≥ 2 in
§5.5.4 is structurally sound: the definition is precise, the
spectral computation is explicit and gauge-invariant, and the
inequality is correctly stated as a lower bound.

**SURVIVED** (≤150 words: verdict body above is ~140 words)
