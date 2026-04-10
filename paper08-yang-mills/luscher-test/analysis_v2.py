#!/usr/bin/env python3
"""
Lüscher Test v2: CP^{N-1} Worldsheet vs Nambu-Goto
====================================================
Fixed: use direct numerical integration for the massive Casimir energy.
"""
import numpy as np
from scipy import integrate
import json

# Lattice data
M_AXION = 1.85  # worldsheet axion mass in units of √σ

def casimir_energy_massive(R, m):
    """
    Casimir energy of a single massive boson on an interval of length R.

    E(R,m) = ∫_0^∞ (dp/2π) ln(1 - exp(-2R√(p²+m²)))

    For m=0: E = -π/(24R).
    """
    def integrand(p):
        E_p = np.sqrt(p**2 + m**2)
        arg = 2 * R * E_p
        if arg > 500:
            return 0.0
        return np.log(1 - np.exp(-arg)) / (2 * np.pi)
    result, _ = integrate.quad(integrand, 0, 200/R if R > 0.01 else 20000,
                               limit=500, epsabs=1e-14)
    return result

def casimir_energy_massless(R):
    """E = -π/(24R) for one massless boson."""
    return -np.pi / (24 * R)

def c_eff_contribution(R, m):
    """
    Effective central charge contribution of one massive mode.
    Defined so that c = 1 for a massless mode.

    c_mode(R) = E_massive(R) / E_massless(R)

    Limits: c_mode → 1 as m → 0, c_mode → 0 as m → ∞.
    """
    E_m = casimir_energy_massive(R, m)
    E_0 = casimir_energy_massless(R)
    return E_m / E_0

def main():
    # Verify massless limit
    R_test = 1.0
    E0 = casimir_energy_massless(R_test)
    Em = casimir_energy_massive(R_test, 0.001)
    print(f"Massless check: E_0 = {E0:.6f}, E(m→0) = {Em:.6f}, ratio = {Em/E0:.6f}")
    print(f"(Should be ratio ≈ 1.0)")
    print()

    # R values in units of 1/√σ
    R_values = np.array([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0,
                         1.2, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0])

    print("=" * 85)
    print("EFFECTIVE CENTRAL CHARGE: THREE MODELS")
    print("(Using m_axion = 1.85 √σ from lattice data)")
    print("=" * 85)
    print()
    print(f"{'R√σ':>5s}  {'NG':>7s}  {'CP²(4mod)':>10s}  {'1 axion':>10s}  "
          f"{'δc(CP²)':>8s}  {'δc(1ax)':>8s}  {'CP²/NG':>7s}")
    print("-" * 72)

    results = {"R_sqrt_sigma": [], "c_NG": [], "c_CP2": [], "c_1axion": [],
               "delta_c_CP2": [], "delta_c_1axion": []}

    for R in R_values:
        c_ng = 2.0  # d - 2 for d = 4

        # CP² prediction: 4 massive modes at mass m_a
        c_per_mode = c_eff_contribution(R, M_AXION)
        c_cp2 = c_ng + 4 * c_per_mode  # 4 = 2(N-1) for N=3

        # Single axion (Dubovsky-Gorbenko)
        c_1ax = c_ng + 1 * c_per_mode

        dc_cp2 = c_cp2 - c_ng
        dc_1ax = c_1ax - c_ng

        print(f"{R:5.1f}  {c_ng:7.3f}  {c_cp2:10.4f}  {c_1ax:10.4f}  "
              f"{dc_cp2:8.4f}  {dc_1ax:8.4f}  {c_cp2/c_ng:7.3f}")

        results["R_sqrt_sigma"].append(float(R))
        results["c_NG"].append(c_ng)
        results["c_CP2"].append(float(c_cp2))
        results["c_1axion"].append(float(c_1ax))
        results["delta_c_CP2"].append(float(dc_cp2))
        results["delta_c_1axion"].append(float(dc_1ax))

    print()
    print("=" * 85)
    print("DETECTABILITY AT KEY DISTANCES")
    print("=" * 85)

    inv_sqrt_sigma_fm = 0.197 / 0.440  # ≈ 0.448 fm

    for R in [0.5, 0.7, 1.0, 1.5, 2.0]:
        c_mode = c_eff_contribution(R, M_AXION)
        dc_cp2 = 4 * c_mode
        dc_1ax = 1 * c_mode
        R_fm = R * inv_sqrt_sigma_fm

        print(f"\nR√σ = {R} (R = {R_fm:.2f} fm):")
        print(f"  Nambu-Goto:      c_eff = 2.000")
        print(f"  CP² (4 modes):   c_eff = {2+dc_cp2:.3f}  "
              f"(+{dc_cp2:.3f}, +{100*dc_cp2/2:.1f}%)")
        print(f"  1 axion:         c_eff = {2+dc_1ax:.3f}  "
              f"(+{dc_1ax:.3f}, +{100*dc_1ax/2:.1f}%)")
        print(f"  Lattice evidence: data consistent with ~1-2 modes")
        print(f"  3σ detection of CP² needs: σ(c) < {dc_cp2/3:.3f} "
              f"({100*dc_cp2/(3*2):.1f}% precision)")

    print()
    print("=" * 85)
    print("THE CRITICAL DISCRIMINATOR: 4 modes vs 1 mode")
    print("=" * 85)
    print()
    print("At R√σ = 1.0:")
    c1 = c_eff_contribution(1.0, M_AXION)
    print(f"  1 axion mode:  δc = {c1:.4f}")
    print(f"  4 CP² modes:   δc = {4*c1:.4f}")
    print(f"  Ratio: 4.0x (this is the distinguishing factor)")
    print()
    print("The lattice data (Dubovsky-Gorbenko) sees ~1 mode.")
    print("Our framework predicts 4 modes.")
    print()
    print("Three possibilities:")
    print("  (a) Only 1 mode is light enough → single axion wins")
    print("  (b) All 4 modes are at m ≈ 1.85√σ → CP² wins (δc 4× larger)")
    print("  (c) 1 mode at 1.85√σ, 3 heavier → intermediate δc")
    print()
    print("The excited string spectrum (Athenodorou-Teper) can distinguish")
    print("these: look for additional massive modes beyond the axion.")

    # Save
    results["parameters"] = {
        "m_axion": M_AXION,
        "sqrt_sigma_MeV": 440,
        "inv_sqrt_sigma_fm": inv_sqrt_sigma_fm,
        "N": 3,
        "n_internal_modes_CP2": 4,
    }
    with open("/Users/gsix/yang-mills/luscher-test/results_v2.json", "w") as f:
        json.dump(results, f, indent=2)
    print("\nResults saved to results_v2.json")


if __name__ == "__main__":
    main()
