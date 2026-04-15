# ES4 — CF decay ρ ≥ 4.27, C ~ O(N), uniform in N

**Claim:** Uniform Carathéodory-Fejér decay in N.

**Pass criterion:** genuinely uniform in N; C ~ O(N) OK.

**Finding:** Paper 13 Proposition 8.1 / Appendix G tabulates
at λ = √14, N = 5, 10, 15, 20, 30:

| N  | ρ_N   | C_N |
|:---|:------|:----|
| 5  | 4.27  | 1.9 |
| 10 | 6.33  | 7.8 |
| 15 | 6.25  | 15.5 |
| 20 | 6.06  | 25.3 |
| 30 | 5.35  | 27.9 |

ρ_N ≥ 4.27 at every tested N. C_N is sub-linear.

**Concerns:**
- ρ_N is **non-monotone** (4.27 → 6.33 → 6.25 → 6.06 → 5.35),
  with a downward trend from N = 10. Paper attributes this to a
  "fit artefact" (Sec 8.1) but does not rigorously rule out ρ_N
  dipping below 4.27 at some N > 30 not tested.
- The "structural" argument ("ρ is determined by the
  singularity structure of the Weil distribution, independent of
  N") is plausible but not proved as a theorem in the paper.
- Uniform-in-N is therefore established **numerically at N ≤ 30**,
  not asymptotically.

**Status:** PASS at N ≤ 30; asymptotic uniformity in N is
structurally plausible but not rigorous.

**Confidence:** 7/10.
