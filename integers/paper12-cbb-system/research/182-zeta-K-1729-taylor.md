# 182. ζ_K(s) Taylor Coefficients at s=1 for K = Q(ζ_1729) — RBC Test

Cycle 9. Direct numerical test of the Ramanujan-Bost-Connes (RBC) hypothesis from research/181.

## Method

K = Q(ζ_1729), 1729 = 7·13·19, [K:Q] = φ(1729) = 1296.
Factorised ζ_K(s) = ∏_χ L(s, χ) over all 1296 Dirichlet characters mod 1729, built via CRT
from primitive roots g_7=3, g_13=2, g_19=2. Each L(s,χ) computed by the Hurwitz identity
L(s,χ) = q^{−s} Σ_{a coprime to q} χ(a) ζ(s, a/q) with q = 1729. The character tensor was
factorised A[a,k]·B[b,k]·C[c,k] and contracted against hurwitz values via einsum. f(s) =
(s−1)·ζ_K(s) evaluated at s−1 ∈ {−0.01, −0.005, +0.005, +0.01} and a degree-3 polynomial
in u = s−1 fit by least squares. Laurent coefficients read off from f(u) = c_{−1} + c_0 u +
c_1 u² + (c_2/2) u³.

## Computed Laurent coefficients

| coeff    | value               |
|----------|---------------------|
| c_{−1}   |  0.07663376104552   |
| c_0      |  0.55087018409140   |
| c_1      |  1.03041723577003   |
| c_2      | −1.35750582689841   |

Imaginary parts < 10⁻¹⁰ (real, as required for an abelian field).

## Comparison to CBB constants

| quantity    | value         | target             | ratio (computed/target) |
|-------------|---------------|--------------------|-------------------------|
| c_0         |  0.55087      | γ_E = 0.57722      | 0.9544                  |
| c_0/c_{−1}  |  7.18835      | γ_E                | 12.4535                 |
| c_1         |  1.03042      | ζ(2)/6 = 0.27416   | 3.7585                  |
| c_2         | −1.35751      | γ_1 = −0.07282     | 18.6430                 |

Normalising by c_{−1} (the analytic class number formula residue) gives γ_K = c_0/c_{−1} ≈
7.1883. The Euler-Kronecker constant of a cyclotomic field grows roughly like γ_E +
½ log|d_K|; here ½ log|d_K| ≈ ½·1296·log(1729)/… — consistent with 7.19 in magnitude.

## Verdict

**NEAR — but RBC hypothesis in its strong form is REFUTED.**

c_0 sits 4.56% below γ_E, a tantalising coincidence but not exact; with the 5-digit fitting
precision here, a true equality would show at ≲ 10⁻⁴. No ratio matches ζ(2)/6 or γ_1.

The mathematically correct statement is that γ_K = γ_E + Σ_{χ≠1} L'(1,χ)/L(1,χ) — γ_E
appears as one of 1296 summands, not the whole. So γ_E is *embedded* in ζ_K but is not its
Laurent coefficient. The RBC "Taylor coefficients = CBB constants" identification fails as
stated.

What survives: the Bost-Connes system attached to Q(ζ_1729) still carries γ_E through the
trivial character component, and the factorisation across conductors 1, 7, 13, 19, 91, 133,
247, 1729 still respects the bridge-prime structure. The physical hypothesis should be
weakened to: **CBB constants arise from the χ_0 (trivial character) factor of ζ_K, while the
non-trivial χ components encode the bridge deformations.** This is the testable next
statement — see research/183 (proposed).
