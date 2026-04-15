#!/usr/bin/env python3
"""
Lüscher Test: CP^{N-1} Worldsheet vs Nambu-Goto
================================================

Computes the effective central charge c_eff(R) predicted by the CP^{N-1}
worldsheet model and compares with the pure Nambu-Goto prediction.

Key data from lattice (Athenodorou-Teper, Dubovsky-Gorbenko-Mirbabayi):
- Worldsheet axion mass: m_a ≈ 1.85 ℓ_s^{-1} = 1.85 √σ
- Axionic coupling: Q ≈ 0.38 ± 0.04 (lattice) vs 0.37 (theory)

Our framework predicts: the worldsheet has 2(N-1) massive CP^{N-1} modes
with mass m_int ~ √σ. For SU(3) (N=3): 4 massive modes.
"""

import numpy as np
from scipy import integrate
import json

# =============================================================================
# Physical constants (in string units, ℓ_s = 1/√σ = 1)
# =============================================================================

# From lattice data (Athenodorou-Teper 2024, Dubovsky-Gorbenko 2016)
M_AXION = 1.85       # worldsheet axion mass in units of √σ
Q_AXION = 0.38       # axionic coupling (lattice)
Q_THEORY = 0.373     # axionic coupling (integrable theory)

# Framework prediction for CP^{N-1} internal mode mass
# The lightest CP^{N-1} mode should have mass ~ √σ
# The axion at 1.85 √σ is consistent with 2 × the CP¹ mass scale
M_CP_MODE = M_AXION  # Use the measured axion mass


# =============================================================================
# The massive Casimir function f(x)
# =============================================================================

def massive_casimir(x):
    """
    The Casimir energy contribution of a single massive boson on an
    interval of length R, with mass m. Argument x = mR.

    f(x) = (1/2π) ∫_0^∞ dp/p × exp(-R√(p²+m²)) / (1 - exp(-R√(p²+m²)))

    In terms of x = mR:
    f(x) = (1/2π) ∫_0^∞ dq/q × exp(-√(q²+x²)) / (1 - exp(-√(q²+x²)))

    Limits: f(0) = π/24 ≈ 0.1309 (massless)
            f(∞) → 0 (decoupled)
    """
    if x > 20:
        return 0.0  # exponentially small

    def integrand(q):
        if q < 1e-10:
            return 0.0
        E = np.sqrt(q**2 + x**2)
        exp_E = np.exp(-E)
        if exp_E > 1 - 1e-15:
            return 0.0
        return exp_E / (q * (1 - exp_E))

    result, _ = integrate.quad(integrand, 1e-10, 50, limit=200)
    return result / (2 * np.pi)


def massive_casimir_fast(x):
    """
    Fast approximation using the sum representation:
    f(x) = (1/2π) Σ_{n=1}^∞ K_0(nx) / n

    where K_0 is the modified Bessel function.
    """
    from scipy.special import kn
    if x > 20:
        return 0.0
    total = 0.0
    for n in range(1, 50):
        val = kn(0, n * x) / n
        total += val
        if abs(val) < 1e-15:
            break
    return total / (2 * np.pi)


# =============================================================================
# Effective central charge
# =============================================================================

def c_eff_nambu_goto(R_sigma, d=4):
    """
    Nambu-Goto effective central charge.
    c_eff = d - 2 for all R.
    """
    return (d - 2) * np.ones_like(np.atleast_1d(R_sigma))


def c_eff_cpn(R_sigma, N=3, m_int=M_CP_MODE, d=4):
    """
    CP^{N-1} worldsheet effective central charge.

    c_eff(R) = (d-2) + (12/π) × n_modes × f(m_int × R/√σ)

    where n_modes = 2(N-1) is the number of internal CP^{N-1} modes
    (real dimension of CP^{N-1}).

    For SU(3): N=3, n_modes = 4.
    """
    n_modes = 2 * (N - 1)
    R_arr = np.atleast_1d(R_sigma)
    result = np.zeros_like(R_arr, dtype=float)

    for i, R in enumerate(R_arr):
        x = m_int * R  # m_int is in units of √σ, R is in units of 1/√σ
        f_val = massive_casimir_fast(x)
        delta_c = (12.0 / np.pi) * n_modes * f_val
        result[i] = (d - 2) + delta_c

    return result


def c_eff_single_axion(R_sigma, m_a=M_AXION, d=4):
    """
    Single axionic mode (Dubovsky-Gorbenko model):
    c_eff = (d-2) + (12/π) × 1 × f(m_a R)
    """
    R_arr = np.atleast_1d(R_sigma)
    result = np.zeros_like(R_arr, dtype=float)

    for i, R in enumerate(R_arr):
        x = m_a * R
        f_val = massive_casimir_fast(x)
        delta_c = (12.0 / np.pi) * 1 * f_val
        result[i] = (d - 2) + delta_c

    return result


# =============================================================================
# Compute and output results
# =============================================================================

def main():
    # Verify the massless limit
    f0 = massive_casimir_fast(0.001)
    print(f"Massless Casimir f(0) = {f0:.6f}  (should be π/24 = {np.pi/24:.6f})")
    print()

    # R values in units of 1/√σ (i.e., R√σ values)
    R_values = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
                         1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0])

    c_ng = c_eff_nambu_goto(R_values)
    c_cp3 = c_eff_cpn(R_values, N=3)
    c_cp2 = c_eff_cpn(R_values, N=2)
    c_axion = c_eff_single_axion(R_values)

    print("=" * 80)
    print("EFFECTIVE CENTRAL CHARGE: PREDICTIONS")
    print("=" * 80)
    print()
    print(f"{'R√σ':>6s}  {'NG (d=4)':>10s}  {'CP² (N=3)':>10s}  "
          f"{'CP¹ (N=2)':>10s}  {'1 axion':>10s}  {'δc (CP²)':>10s}")
    print("-" * 72)

    for i, R in enumerate(R_values):
        delta = c_cp3[i] - c_ng[i]
        print(f"{R:6.1f}  {c_ng[i]:10.4f}  {c_cp3[i]:10.4f}  "
              f"{c_cp2[i]:10.4f}  {c_axion[i]:10.4f}  {delta:10.4f}")

    print()
    print("=" * 80)
    print("KEY COMPARISON POINTS")
    print("=" * 80)

    for R in [0.5, 0.7, 1.0, 1.5]:
        c_n = c_eff_nambu_goto(np.array([R]))[0]
        c_c = c_eff_cpn(np.array([R]), N=3)[0]
        c_a = c_eff_single_axion(np.array([R]))[0]
        delta = c_c - c_n
        pct = 100 * delta / c_n
        print(f"\nR√σ = {R}:")
        print(f"  Nambu-Goto:   c = {c_n:.4f}")
        print(f"  CP² (N=3):    c = {c_c:.4f}  (+{delta:.4f}, +{pct:.1f}%)")
        print(f"  Single axion: c = {c_a:.4f}")
        print(f"  Precision needed for 3σ detection of δc = {delta:.3f}: "
              f"σ(c) < {delta/3:.3f} ({100*delta/(3*c_n):.1f}%)")

    # R in fm (using √σ ≈ 440 MeV, so 1/√σ ≈ 0.45 fm)
    print()
    print("=" * 80)
    print("IN PHYSICAL UNITS (√σ = 440 MeV, 1/√σ ≈ 0.45 fm)")
    print("=" * 80)
    print()
    inv_sqrt_sigma_fm = 0.197 / 0.440  # ≈ 0.448 fm
    print(f"{'R (fm)':>8s}  {'R√σ':>6s}  {'c_NG':>8s}  {'c_CP²':>8s}  "
          f"{'δc':>8s}  {'% effect':>8s}")
    print("-" * 56)
    for R in R_values:
        R_fm = R * inv_sqrt_sigma_fm
        c_n = c_eff_nambu_goto(np.array([R]))[0]
        c_c = c_eff_cpn(np.array([R]), N=3)[0]
        delta = c_c - c_n
        pct = 100 * delta / c_n
        if R_fm < 2.5:
            print(f"{R_fm:8.3f}  {R:6.2f}  {c_n:8.4f}  {c_c:8.4f}  "
                  f"{delta:8.4f}  {pct:7.1f}%")

    # The critical comparison with the axionic string data
    print()
    print("=" * 80)
    print("COMPARISON WITH LATTICE DATA")
    print("=" * 80)
    print()
    print("Dubovsky-Gorbenko-Mirbabayi / Athenodorou-Teper data:")
    print(f"  Worldsheet axion mass: m_a = {M_AXION} √σ")
    print(f"  Axionic coupling: Q = {Q_AXION} ± 0.04 (lattice)")
    print(f"  Q = {Q_THEORY} (integrable theory prediction)")
    print()
    print("Our CP^{N-1} framework interpretation:")
    print(f"  The axion IS one of the {2*(3-1)} CP² worldsheet modes")
    print(f"  Mass m ≈ {M_AXION} √σ ≈ {M_AXION * 440:.0f} MeV")
    print(f"  This is close to 2Λ_QCD ≈ 2 × 213 ≈ 426 MeV")
    print(f"  and close to 2√σ ≈ {2*440:.0f} MeV")
    print()
    print("Prediction: there should be {0} modes total, not just 1 axion.".format(
        2*(3-1)))
    print("The single-axion model (Dubovsky-Gorbenko) has 1 mode.")
    print("Our model has 4 modes (real dim of CP²).")
    print("The difference is testable in the excited string spectrum.")

    # Save numerical results for the paper
    results = {
        "R_sqrt_sigma": R_values.tolist(),
        "c_eff_NG": c_ng.tolist(),
        "c_eff_CP2_N3": c_cp3.tolist(),
        "c_eff_CP1_N2": c_cp2.tolist(),
        "c_eff_single_axion": c_axion.tolist(),
        "parameters": {
            "m_axion_lattice": M_AXION,
            "Q_lattice": Q_AXION,
            "Q_theory": Q_THEORY,
            "N": 3,
            "n_internal_modes": 4,
            "sqrt_sigma_MeV": 440
        }
    }

    with open("/Users/gsix/yang-mills/luscher-test/results.json", "w") as f:
        json.dump(results, f, indent=2)
    print()
    print("Results saved to results.json")


if __name__ == "__main__":
    main()
