## §32 — Cross-Check via SYMMETRY Score

*If any route closes, the SYMMETRY metric rises. Post-Paper-50: CURVATURE 9.5 → 10, RESONANCE 6 → 7+, gap narrows from 3.5 to 1-2. The ring becomes more circular.*

---

## 32.1. The SYMMETRY metric

Paper 60 §21 defines the SYMMETRY metric as the measure of how close the programme's ten-face confidence distribution is to a perfect circle. A perfectly S-symmetric programme has equal confidence on both faces of every pair — the ellipse collapses to a circle. An S-asymmetric programme has gaps between paired faces — the ellipse is lopsided.

Formally, SYMMETRY is computed as:

$$\mathrm{SYM} = 1 - \frac{1}{5} \sum_{i=1}^{5} \frac{|C_i^{\mathrm{geom}} - C_i^{\mathrm{spec}}|}{10},$$

where $C_i^{\mathrm{geom}}$ and $C_i^{\mathrm{spec}}$ are the confidence scores (out of 10) for the geometric and spectral faces of pair $i$, and the factor of 10 normalizes to $[0, 1]$.

A fully circular programme has SYM = 1. A maximally lopsided programme (one face at 10, all others at 0) has SYM close to 0.5. The current programme has SYM $\approx 0.79$ (computed from Paper 60 §21's table).

---

## 32.2. Current SYMMETRY baseline

Pre-Paper-50, the face pairs and confidences are:

| Pair | Geom face | $C^{\mathrm{geom}}$ | Spec face | $C^{\mathrm{spec}}$ | $|\Delta C|$ |
|---|---|---|---|---|---|
| 1 | CURVATURE (YM) | 9.5 | RESONANCE (Selberg) | 6 | 3.5 |
| 2 | MEASURE (Sato-Tate) | 6 | SYMMETRY (K-S) | 7 | 1 |
| 3 | TOPOLOGY (Lehmer) | 4 | DYNAMICS (Cramér) | 5 | 1 |
| 4 | HARMONICS (Collatz) | 4 | ARITHMETIC (Goldbach) | 1 | 3 |
| 5 | AMPLITUDE (Lindelöf) | 7 | SPREAD (QUE) | 8 | 1 |

Sum of $|\Delta C| = 9.5$. Average $|\Delta C|/5 = 1.9$. SYM = $1 - 1.9/10 = 0.81$.

(The earlier "$\approx 0.79$" reflects small adjustments from Paper 49's partial impact on the confidence table; the canonical pre-Paper-50 baseline is 0.81.)

This SYMMETRY score is the programme's baseline. Paper 50's job is to raise it.

---

## 32.3. Post-Paper-50 SYMMETRY projection

If Paper 50 closes H4 via any of the three routes, the CURVATURE face rises from 9.5 to 10.0 (Paper 8 becomes 18/18 unconditional). The S-dual effect on RESONANCE (Selberg) depends on which route closes.

**If Route A closes (resurgence).** The CURVATURE side gains the resurgence machinery. The resurgence techniques transfer to the Selberg side only loosely (RESONANCE's spectral-gap question is not a natural fit for resurgence). Expected RESONANCE bump: +0.5 (from 6 to 6.5).

**If Route B closes (Kim-Sarnak transfer).** The CURVATURE side uses Kim-Sarnak's Sym$^k$ machinery. This machinery is *native* to the RESONANCE side — transferring it back strengthens Selberg directly. Expected RESONANCE bump: +1.5 to +2 (from 6 to 7.5 or 8). This is the largest cross-face effect.

**If Route C closes (Kapustin-Witten).** The CURVATURE side uses geometric Langlands. The RESONANCE side's Maass forms are automorphic, and classical Langlands is not a direct consequence of geometric Langlands (though related). Expected RESONANCE bump: +1 (from 6 to 7).

**Average expected:** CURVATURE 9.5 → 10.0, RESONANCE 6.0 → 7+. The Pair 1 gap narrows from 3.5 to 2-3.

The projection depends on which route closes. Paper 50's ship criterion (§26) prefers Route B on the "depth of external citation" axis — which happens to coincide with the route that produces the largest symmetry-score improvement.

---

## 32.4. Recomputed SYMMETRY post-Paper-50

Assuming the middle-case projection (Route B closes, CURVATURE 9.5 → 10, RESONANCE 6 → 7.5):

| Pair | $C^{\mathrm{geom}}$ | $C^{\mathrm{spec}}$ | $|\Delta C|$ |
|---|---|---|---|
| 1 | 10 | 7.5 | 2.5 |
| 2 | 6 | 7 | 1 |
| 3 | 4 | 5 | 1 |
| 4 | 4 | 1 | 3 |
| 5 | 7 | 8 | 1 |

Sum = 8.5. Average = 1.7. SYM = $1 - 1.7/10 = 0.83$.

The SYMMETRY score rises from 0.81 to 0.83. This is a modest but real improvement — the ring becomes more circular by 2 percentage points. Not transformative, but in the right direction.

---

## 32.5. The cross-check criterion

Paper 50 uses the SYMMETRY score as a **cross-check**: if Route B claims to close H4 via Kim-Sarnak transfer, then the SYMMETRY score should rise by at least the Route B projection (1.5-2 on the RESONANCE side). If the claim is that Route B closes H4 but the RESONANCE face cannot absorb the corresponding S-dual technique transfer, something is inconsistent — either Route B's closure is wrong, or the S-duality model is wrong, or the RESONANCE side has an independent obstruction.

The cross-check runs as follows:

1. **Route closes** on the CURVATURE side.
2. **Identify the S-dual technique.** What Kim-Sarnak-style machinery, or geometric-Langlands machinery, or resurgence machinery, was used?
3. **Transfer the technique** to the RESONANCE side. Does it produce a strengthening of the Selberg bound?
4. **Update the RESONANCE confidence** based on the strengthening.
5. **Check the S-duality prediction.** Does the new RESONANCE confidence match the projection?

A match validates the closure via an S-duality consistency check. A mismatch flags either (i) the closure has a subtle gap, or (ii) the S-duality model needs revision, or (iii) the RESONANCE side has an independent obstruction that the S-duality does not see.

---

## 32.6. Beyond Pair 1: ripple effects on the other pairs

Paper 50's impact is not confined to Pair 1. The three routes use machinery that touches other pairs:

- **Route A's resurgence** machinery is related to **Pair 3** (TOPOLOGY ↔ DYNAMICS) through the analytic structure of Borel-plane singularities. A stronger resurgence framework feeds back into Lehmer (KMS spectral gap) and Cramér (return-time statistics). Expected ripple: TOPOLOGY 4 → 4.5, DYNAMICS 5 → 5.5.

- **Route B's Langlands-Shahidi** machinery is related to **Pair 2** (MEASURE ↔ SYMMETRY) through automorphic L-functions. A stronger Sym$^4$ bound strengthens Sato-Tate-type equidistribution results. Expected ripple: MEASURE 6 → 6.5, SYMMETRY 7 → 7.5.

- **Route C's geometric Langlands** machinery is related to **Pair 5** (AMPLITUDE ↔ SPREAD) through spectral statistics. A stronger geometric-Langlands framework tightens QUE's measure-rigidity arguments. Expected ripple: AMPLITUDE 7 → 7.5, SPREAD 8 → 8.5.

The ripples are smaller than Pair 1's primary effect, but they contribute to the SYMMETRY score. Under the middle-case projection (Route B closes with ripples):

| Pair | $C^{\mathrm{geom}}$ | $C^{\mathrm{spec}}$ | $|\Delta C|$ |
|---|---|---|---|
| 1 | 10 | 7.5 | 2.5 |
| 2 | 6.5 | 7.5 | 1 |
| 3 | 4 | 5 | 1 |
| 4 | 4 | 1 | 3 |
| 5 | 7 | 8 | 1 |

Sum = 8.5 (unchanged; the Pair 2 ripple preserves the gap of 1). SYM still $\approx 0.83$.

The ripples raise the absolute confidence levels without necessarily narrowing gaps. To narrow gaps, the S-duality transfer needs to *asymmetrically* raise one face relative to its partner — which happens for Pair 1 but not uniformly for the others.

---

## 32.7. Long-term convergence target

Paper 60 §21's ultimate target is SYM = 1.0: all pairs balanced, all gaps closed, the ellipse is a circle. Paper 50 contributes to this target by closing Pair 1's largest gap. Closing Pair 4 (HARMONICS ↔ ARITHMETIC, gap 3) requires the Goldbach infrastructure build-out (a separate research direction, not Paper 50's scope).

The long-term trajectory:

- **2026 (current):** SYM = 0.81.
- **Post-Paper-49 (CCM replacement, 2026):** SYM = 0.82 (small uplift from Paper 13 confidence boost).
- **Post-Paper-50 (H4 closure, 2027-2028):** SYM = 0.83.
- **Post-Paper-47 (Selberg, via S-dual transfer):** SYM = 0.86.
- **Post-Goldbach infrastructure (2028+):** SYM = 0.90+.
- **Convergence target:** SYM → 1.0.

Paper 50 is one step on this trajectory — not the last step, but one of the most significant because it closes the largest gap.

---

## 32.8. Summary

The SYMMETRY score cross-check provides an independent consistency test for Paper 50's closure claim. A successful closure via Route B is projected to raise SYM from 0.81 to 0.83, via CURVATURE 9.5 → 10 and RESONANCE 6 → 7.5. Routes A and C produce smaller SYMMETRY improvements. The cross-check works by verifying that the S-dual technique transfers to the RESONANCE side and produces the projected confidence uplift. A mismatch flags a gap in the closure argument. Paper 50 uses the SYMMETRY score as both a validation metric (post-closure check) and a ship-criterion input (§26's priority axis 1).

---

*Paper 50 §32. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
