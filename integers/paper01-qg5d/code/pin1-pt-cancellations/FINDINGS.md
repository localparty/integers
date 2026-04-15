# Agent O — Pin #1 3rd/4th-order PT cancellations (2026-04-14)

## TL;DR

**The "all-orders PT cancellation" hypothesis is FALSIFIED.** 3rd and 4th-order Rayleigh-Schrödinger corrections move the c_m coefficients by only ~10% of 2nd-order — nowhere near the ~500% correction needed to match empirical.

**Bug found in Agent H**: `V_{nm}` was non-Hermitian (V_{11} had a spurious 0.23i imaginary part). Corrected definition restores V = V*; recalibration gives enhance = 0.5224 (vs Agent H's 0.6454).

## Methodological finding

Agent H's V_{nm} = `Σ c_p/√p · [K_{nm}(log p) + K_{mn}(log p)]`. This makes V non-Hermitian (V_{11} = 0.190 + 0.23i).

Physically correct: `V_{nm} = Σ c_p/√p · [K_{nm}(log p) + conj(K_{mn}(log p))]`. Gives V_{11} = 0.190 (real), V = V*. Refit on 25-prime set preserving |V_{12}|² = 0.2425: **enhance = 0.5224** (Agent H: 0.6454). All numbers below use the corrected V.

## 3rd/4th-order corrections (outer-channel decomposition, basis cutoff M=20)

| m | c_m^(2) | c_m^(2+3) | c_m^(2+3+4A) | empirical c_m |
|---|---|---|---|---|
| 2 | 0.150 | 0.135 | 0.137 | +0.15 |
| 3 | 0.177 | 0.160 | 0.162 | **−0.03** |
| 4 | 0.150 | 0.134 | 0.136 | 0 |
| 5 | 0.099 | 0.089 | 0.090 | 0 |

3rd order ≈ −9% of 2nd; 4th order ≈ +1% of 3rd. **Sign and magnitude of each c_m barely moves across PT orders.** No cancellation mechanism visible.

## Hypothesis falsified

Σ E_1^{(k)} at M=20 = **−0.0347** vs empirical target **−0.00991** — a **3.5× overshoot**, essentially the same as 2nd-order alone (−0.0383, 3.9× overshoot). 3rd + 4th give ~10% net relief, nowhere near the 500% correction needed to flip c_3's sign or zero the m≥4 tail.

Geometric ratios `|E_{k+1}/E_k| ≈ 0.10`. All-orders resummation adds at most another ~11% on top. Even infinite-order PT at this calibration gives Δ ≈ −0.031, still 3× the empirical. **Summation order is not the bottleneck.**

PV scheme is fine; Borel is irrelevant (series converges geometrically at fixed cutoff). What grows is M-dependence: `E2(M=5) = −0.022 → E2(M=20) = −0.038`, because `|V_{1m}|² stays O(1)` while `(γ_m − γ_1)^{−1} ~ 1/(γ_m log γ_m)`, giving `Σ 1/(m (log m)²)` — converges as `log log γ`, slowly.

## Three surviving possibilities (hypothesis space)

1. **Empirical pattern is a FITTED SUMMARY, not channel-by-channel RS.** The `−0.15/γ_2 + 0.03/γ_3 − 0.01·log(γ_2/γ_1)` expression is a post-hoc parametrization of the total residual Δ, NOT individual RS channel readouts. **Most likely** — the m≥4 tail overshoots the log term 6:1, consistent with the tail being summarized into the logarithm.
2. SM `c_p ~ log p / p` profile falls off too slowly; needs a harder KK cutoff at p = `M_KK / (2π R)`.
3. Missing counterterm needed — subtracted V_{11}, holomorphic CT.

Research/05 §4.3's "3rd-order interference" story for the +0.03/γ_3 term is **numerically inconsistent with straight RS channel decomposition**.

## Implication for Pin #1 status

The Cycle-2 claim "the 5 ppb mechanism is all-orders PT cancellation" — based on Agent H — is incorrect. The mechanism is most likely:

**The empirical `−0.15/γ_2 + 0.03/γ_3 − 0.01·log` pattern is a compact functional parametrization of the aggregate Δ ≈ −0.0099, NOT a channel-resolved readout.** In which case:

- The leading term γ_1 · π²/2 is rigorously ab initio (theorem).
- The radiative correction sector is identically zero (K.1/K.3/K.4, Agent C).
- The Δ ≈ −0.0099 residual IS the BC perturbation-theory sum but it is the TOTAL Σ, not a sum of individual sign-flipped channels.
- The specific functional form (−0.15/γ_2 + ...) is a FIT to that total. Pin #1's **quantitative** theorem status requires computing the aggregate Δ ab initio — which combined with Agent N's enhance = 0.829 + F_φ KK-overlap gets it to 624 ppm, not 5 ppb.

Pin #1 "theorem at structural level" is accurate. "Zero free parameters + 1 unevaluated geometric integral" (Agent N's framing) is accurate. Closing the gap between 624 ppm (ab initio) and 5 ppb (empirical) likely requires the F_φ integral AND perhaps missing counterterm/cutoff physics — not a hidden PT-cancellation structure.

## Deliverables

- `compute_pt_orders.py`
- `pt_results.json`
- this FINDINGS.md
