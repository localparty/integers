# YM Compliance Audit — Kills (run-02)

*Claims WEAKENED by this compliance audit, relative to run-01 x-ray status.*

*G Six and Claude Opus 4.6. 2026-04-14.*

---

## Scope

run-01 x-ray assigned face/projection/pattern/invariant per layer, not J-W compliance. run-02 is the first compliance audit against Jaffe-Witten's 7 requirements. This `kills.md` records cells where the compliance audit WEAKENS a prior assertion or clarifies a limitation.

A "kill" here means: a claim that appears stronger in x-ray / programme documentation but is tempered by the per-cell J-W audit. This does NOT invalidate the proof chain; it tightens the disclosure boundary.

---

## Kill 1 — L1 is not the uniform-in-V 4D mass gap

- **Prior suggestion** (x-ray L1): "spectral gap (load-bearing)" suggests L1 carries the 4D uniform gap.
- **Audit finding**: L1 proves μ₁ ≥ 2N/r₃² for the INTERNAL Laplacian on ℂP^{N-1}. This is the KK gap, volume-independent by virtue of the internal space being V-independent. The 4D Wilson-lattice mass gap Δ(a, L) ≥ δ₀ uniformly in L is established at L1b (cluster expansion + Feshbach), not at L1.
- **Effect**: L1 Req 3 verdict WEAKENED from author's P to **Pa** via arbiter. L1's role is the KK gap feeding L1b; the uniform-in-V 4D gap is downstream.
- **No impact** on chain validity — L1b closes the loop.

## Kill 2 — L15 Gradient-flow is not group-universal at layer level

- **Prior suggestion** (x-ray L15): "well-posedness, contractivity" implies group-universal Picard-Lindelöf argument.
- **Audit finding**: Lemma L.1.1 uses SU(N) structure explicitly — the orthonormal basis {T^a} of 𝔰𝔲(N), the compact manifold 𝓜 = SU(N)^|Λ|, the KK mass m₁ = 2√N/r₃ specific to ℂP^{N-1}. Extension to other compact simple G requires I4 group-specific Einstein constants (λ_G) and K group-general Balaban constants.
- **Effect**: L15 Req 1 verdict WEAKENED from author's P to **Pa** via arbiter.
- **No impact** on chain validity — I4 + K provide bootstrap for all compact simple G.

## Kill 3 — Intermediate L8/L9/L10 do not individually address AF match

- **Prior suggestion**: L8/L9/L10 dim-6 suppression bounds are "compatible with AF" and feed the AF-running structure.
- **Audit finding**: Compatibility with AF is not the same as discharging Req 5 (AF match at short distance). Req 5 per J-W §4 prose requires Schwinger-function agreement with perturbative RG; L8/L9/L10 are operator-suppression power-counting inputs. The full AF-match is the H4 statement at L18 (or its bypass).
- **Effect**: L8 Req 5, L9 Req 5, L10 Req 5 verdicts WEAKENED from author's Pa to **S** via arbiter. Bypass points to ADR-5 at L18.
- **No impact** on chain validity — L18 is where Req 5 is addressed (OPEN-BUT-ADDRESSED).

---

## No other kills

All other cells are consistent between run-01 x-ray and run-02 compliance audit. The chain's 17/18 unconditional + 1 OPEN-BUT-ADDRESSED structure holds intact.

## Confidence impact

- H4 aggregate confidence: unchanged at 0.65 (range 0.55–0.85).
- YM chain confidence (PROOF-CHAIN.md): 9.5/10 unchanged.
- §5d compliance: PASS (every J-W requirement addressed somewhere in chain).

---

*End of kills.md.*
