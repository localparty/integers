# W2-07: Independent Numerical Verification (Wave 2 Computation Agent)

## Task
Independently reproduce and extend all numerical results from Wave 1 agents. Create fresh computation scripts that do NOT copy Wave 1 code — implement from scratch as an independent verification. Also compute additional quantities needed for later waves.

## Checks to perform (all at 50-digit mpmath precision)

### Reproducing Wave 1 results
1. **S₀ = 1 + 2ζ(0) = 0** — compute ζ(0) independently
2. **E₂(-j; Q₀) = 0 for j=1..10** — compute via 6ζ(s)L(s,χ₋₃), verify complementary zeros
3. **Z₂ parity cancellation** — for each n=1..20, compute f_even(n) and f_odd(n) from the y-integrals ∫cos³(ny/R)dy and ∫sin²(ny/R)cos(ny/R)dy, verify f_even(n) + f_odd(n) = 0
4. **Heat kernel factorization** — verify K_{M⁴×S¹}(t) = K_{M⁴}(t)·K_{S¹}(t) for t = 0.01, 0.1, 1.0 at several (x,y,φ,φ') points
5. **Analyticity radius** — reproduce r_t ≈ 3.16 × 10⁻⁴ for SU(2) and SU(3) from the formula r_t = min(r_ODE, ρ/L_F)

### New computations for later waves
6. **Poisson bridge** — verify the Poisson resummation identity between KK sum and winding sum to 10⁻²⁴ precision (reproducing Paper 10 Route 04 result)
7. **Sunset Eisenstein zeta** — compute E₂(s; n²+nm+m²) = 6ζ(s)L(s,χ₋₃) and verify factorization by direct double sum (N_max = 1000) for s = 2, 3, 4
8. **Weyl anomaly sum** — verify a_total = (43/360) × [1 + 2ζ(0)] = 0 and c_total = (87/20) × [1 + 2ζ(0)] = 0
9. **Three-graviton vertex** — verify I_{+++}(n₁,n₂,n₁+n₂) = πR/4 for (n₁,n₂) ∈ {(1,1), (1,10), (5,5), (3,7), (100,200)} by numerical integration

## What to read
- Wave 1 results files (for comparison, NOT for copying code):
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/established-pack/results.txt`
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/heat-kernel-factor/results.txt`
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/analyticity-in-t/results.txt`
- Paper 10 research memos for the Poisson bridge and vertex computation:
  - `/Users/gsix/quantum-geometry-in-5d-latex/paper10/research/` (if accessible)
  - `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md` — Poisson identity, Section 4.2

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W2-07-numerical-verification.md` — summary of all checks
2. Code: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/numerical-verify/compute.py` — single script, all checks
3. Results: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/numerical-verify/results.txt`

## Output format
For each check: state what was computed, the expected value, the computed value, the relative error, and PASS/FAIL. Final summary table with all 9 checks. Any FAIL must be flagged with detailed analysis.
