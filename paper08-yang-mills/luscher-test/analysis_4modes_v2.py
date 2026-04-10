#!/usr/bin/env python3
"""
Four-mode analysis v2: uses the validated integral formula for massive Casimir.
"""
import numpy as np
from scipy import integrate
import json


def casimir_energy(R, m):
    """
    Casimir energy of ONE massive boson on an interval of length R.
    E(R,m) = ∫₀^∞ (dp/2π) ln(1 - exp(-2R√(p²+m²)))
    Massless limit: E(R,0) = -π/(24R).
    """
    def integrand(p):
        E_p = np.sqrt(p**2 + m**2)
        arg = 2 * R * E_p
        if arg > 500:
            return 0.0
        return np.log(1 - np.exp(-arg)) / (2 * np.pi)
    upper = max(200.0/R, 20*m) if R > 0.001 else 100000
    result, _ = integrate.quad(integrand, 0, upper, limit=500, epsabs=1e-14)
    return result


def c_eff(R, masses):
    """
    Effective central charge for d=4 with additional massive modes.
    c = (d-2) + Σ_i [E(R, m_i) / E(R, 0)]
    """
    E0 = -np.pi / (24 * R)  # massless Casimir (exact)
    c = 2.0  # d-2 translational modes
    for m in masses:
        Em = casimir_energy(R, m)
        c += Em / E0  # each massive mode contributes its fraction
    return c


def main():
    # Verify
    E0 = -np.pi / 24
    Em = casimir_energy(1.0, 0.001)
    print(f"Massless check: E(R=1,m≈0)/E₀ = {Em/E0:.4f} (should → 1.000)")
    Em_heavy = casimir_energy(1.0, 10.0)
    print(f"Heavy check:    E(R=1,m=10)/E₀ = {Em_heavy/E0:.6f} (should → 0)")
    print()

    scenarios = {
        "NG (no extra)":         [],
        "1 axion":               [1.85],
        "4 degenerate":          [1.85, 1.85, 1.85, 1.85],
        "4 hierarchy":           [1.85, 2.3, 2.3, 2.8],
        "1 light + 3 heavy":     [1.85, 4.0, 4.0, 5.0],
    }

    R_vals = [0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 1.0, 1.2, 1.5, 2.0, 3.0]

    print("=" * 90)
    print("c_eff(R) FOR FIVE SCENARIOS  (masses in units of √σ)")
    print("=" * 90)
    hdr = f"{'R√σ':>5s}"
    for s in scenarios:
        hdr += f"  {s:>14s}"
    print(hdr)
    print("-" * 85)

    all_results = {s: [] for s in scenarios}

    for R in R_vals:
        line = f"{R:5.1f}"
        for name, masses in scenarios.items():
            c = c_eff(R, masses)
            all_results[name].append(c)
            line += f"  {c:14.4f}"
        print(line)

    # Key comparison
    print()
    print("=" * 90)
    print("AT R√σ = 0.7 (R ≈ 0.31 fm)  —  THE SWEET SPOT")
    print("=" * 90)
    for name, masses in scenarios.items():
        c = c_eff(0.7, masses)
        dc = c - 2.0
        print(f"  {name:25s}: c = {c:.3f}, δc = {dc:.3f} ({100*dc/2:.1f}%)")

    # SU(N) scaling with degenerate modes
    print()
    print("=" * 90)
    print("SU(N) SCALING (all modes at m = 1.85√σ)")
    print("=" * 90)
    print(f"{'N':>3s}  {'modes':>5s}  {'c_eff(0.7)':>10s}  {'δc':>8s}")
    print("-" * 35)
    for N in [2, 3, 4, 5, 6]:
        n = 2*(N-1)
        masses = [1.85]*n
        c = c_eff(0.7, masses)
        print(f"{N:3d}  {n:5d}  {c:10.3f}  {c-2:.3f}")

    # Save
    with open("/Users/gsix/yang-mills/luscher-test/results_4modes_v2.json","w") as f:
        json.dump({"R": R_vals, "scenarios": all_results}, f, indent=2)
    print("\nSaved to results_4modes_v2.json")


if __name__ == "__main__":
    main()
