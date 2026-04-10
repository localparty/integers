# W8-17: Independent Computation Audit (Final Verification)

## Task
Re-run ALL numerical checks from the programme in a fresh environment, independently verifying every computational result. Also run additional checks not performed in earlier waves.

## Checks to perform (all at 50-digit mpmath precision)

### Reproducing Wave 2 results (from W2-07)
1. S₀ = 1 + 2ζ(0) = 0
2. E₂(-j; Q₀) = 0 for j=1..20 (extended from j=1..10)
3. Z₂ parity: f_even(n) + f_odd(n) = 0 for n=1..50 (extended from n=1..20)
4. Heat kernel factorization at 5 test points
5. Analyticity radius r_t for SU(2) and SU(3)
6. Poisson bridge to 10⁻²⁴
7. Eisenstein factorization by direct double sum
8. Weyl anomaly a_total = c_total = 0
9. Three-graviton vertex I_{+++} = πR/4 for 10 test pairs

### NEW checks not in earlier waves
10. **Seeley-DeWitt a₄ from scratch**: Compute a₄ for the Lichnerowicz operator on flat M⁴ × S¹/Z₂ using the Vassilevich formula directly (not citing Paper 10 — independent computation)
11. **Sunset Eisenstein zeta to j=20**: Verify E₂(-j; Q₀) = 6ζ(-j)L(-j,χ₋₃) = 0 for j=11..20
12. **Figure-eight topology**: Verify each one-loop factor gives 2ζ(-2j) = 0 for j=1..10
13. **Ghost contribution**: Verify ghost KK quadratic form Q = 2(n²+nm+m²) gives same Eisenstein zeta as graviton sector
14. **c₁(t) Wilson coefficient**: Compute the one-loop Wilson coefficient c₁(t,μ) from Luscher's formula and verify it matches the standard expression c₁ ~ t⁻²(log)⁻¹
15. **Convergence rate**: For the telescoping sum Σ_K g_K⁴(a_KΛ)^s with and without flow factor e^{-t/a_K²}, verify that the flowed sum converges triply exponentially

## What to read
- Wave 2 computation results for comparison:
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/numerical-verify/results.txt`
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/established-pack/results.txt`
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/heat-kernel-factor/results.txt`
  - `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/analyticity-in-t/results.txt`

## What to write
1. Code: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/final-audit/compute.py`
2. Results: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/final-audit/results.txt`
3. Summary: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W8-17-computation-audit.md`

## Output format
For each of the 15 checks: state what was computed, expected value, computed value, relative error, PASS/FAIL. Final summary: total PASS/FAIL count. Any FAIL must be analyzed. Overall verdict: ALL PASS / ISSUES FOUND.
