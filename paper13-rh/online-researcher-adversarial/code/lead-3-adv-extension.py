"""ADVERSARIAL EXTENSION TEST for Lead 3.

Re-runs the Weyl count on an extended grid the executor didn't test:

  1. Higher T: T ∈ {60, 80, 100} to check the claim of completeness
     beyond T=50. At T=100, N(T) ≈ 29.
  2. Higher λ: λ = 64 with a correspondingly larger N (needs
     dps ≥ 1.86·N + 30 per the executor's empirical rule).
  3. Interpolating T values between γ_n to verify N_op is a proper
     step function: T ∈ {14.1, 14.14, 14.2, 21.0, 21.03, 21.1, ...}.
  4. Below the lowest zero: T = 10.0, 13.0, 14.1, 14.13 → should
     be 0; T = 14.14 → should be 1.
  5. Precision-floor artifact test: run (λ=8, N=50) at dps=80 (well
     BELOW the 1.86·50 + 30 = 123 threshold) to see whether spurious
     eigenvalues ACTUALLY emerge near the Fourier ladder 2π k / L
     as the executor claimed.
"""

import json
import os
import sys
import time

import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
P13_CODE_DIR = os.path.normpath(os.path.join(CODE_DIR, "..", "..", "code"))
sys.path.insert(0, P13_CODE_DIR)

from r49_fourier_circle import build_QW, eigh_mp
from r51b_evenblock import project_to_even, even_eigvec_to_full


def NT_main(T):
    T = mp.mpf(T)
    twopi = 2 * mp.pi
    return (T / twopi) * mp.log(T / twopi) - T / twopi + mp.mpf(7) / 8


def NT_exact(T):
    return int(mp.nzeros(T))


def xi_hat_simple(z, xi_full, L, N):
    twopi = 2 * mp.pi
    pre_sin = mp.sin(z * L / 2)
    s = mp.mpf(0)
    for j in range(-N, N + 1):
        s += xi_full[j + N] / (z - twopi * j / L)
    return 2 * L ** (mp.mpf(-1) / 2) * pre_sin * s


def count_zeros_in_interval(a, b, xi_full, L, N, n_grid=2000):
    twopi = 2 * mp.pi
    pole_set = set()
    for j in range(-N, N + 1):
        pj = float(twopi * j / L)
        if float(a) - 0.01 <= pj <= float(b) + 0.01:
            pole_set.add(round(pj, 8))
    a_f = float(a); b_f = float(b)
    grid = [a_f + (b_f - a_f) * i / n_grid for i in range(n_grid + 1)]
    safe_grid = []
    min_sep = max((b_f - a_f) / n_grid * 0.1, 1e-3)
    for z in grid:
        zz = z
        for p in pole_set:
            if abs(zz - p) < min_sep:
                zz = p + (min_sep if (zz >= p) else -min_sep)
        safe_grid.append(zz)
    safe_grid.sort()
    vals = []
    for z in safe_grid:
        zm = mp.mpf(z)
        v = xi_hat_simple(zm, xi_full, L, N)
        vals.append((zm, v))
    zeros = []
    for k in range(len(vals) - 1):
        z0, v0 = vals[k]
        z1, v1 = vals[k + 1]
        if v0 == 0:
            zeros.append(z0)
            continue
        if (v0 > 0 and v1 < 0) or (v0 < 0 and v1 > 0):
            straddles_pole = False
            for p in pole_set:
                if (z0 < p < z1) or (z1 < p < z0):
                    straddles_pole = True
                    break
            if straddles_pole:
                continue
            try:
                root = mp.findroot(
                    lambda z: xi_hat_simple(z, xi_full, L, N),
                    (z0 + z1) / 2,
                    solver="anderson",
                    tol=mp.mpf("1e-20"),
                )
                if a <= root <= b:
                    zeros.append(root)
            except Exception:
                zeros.append((z0 + z1) / 2)
    zeros.sort()
    dedup = []
    for r in zeros:
        if not dedup or abs(r - dedup[-1]) > mp.mpf("1e-6"):
            dedup.append(r)
    return len(dedup), dedup


def build_xi(lam, N, dps):
    mp.mp.dps = dps
    lam_m = mp.mpf(lam)
    L = 2 * mp.log(lam_m)
    t0 = time.time()
    A, L = build_QW(lam_m, N, dps=dps, verbose=False)
    Aev = project_to_even(A, N)
    vals_ev, Q_ev = eigh_mp(Aev)
    mu1 = vals_ev[0]
    delta = vals_ev[1] - vals_ev[0]
    xi_ev = [Q_ev[i, 0] for i in range(N + 1)]
    xi_full = even_eigvec_to_full(xi_ev, N)
    t_tot = time.time() - t0
    print(f"  λ={lam} N={N} dps={dps}  mu1={mp.nstr(mu1,6)}  "
          f"δ={mp.nstr(delta,6)}  build+eig {t_tot:.1f}s")
    return xi_full, L, mu1, delta, t_tot


# -------------------- Experiments --------------------

def exp1_higher_T():
    """Extend T beyond 50 to test completeness claim."""
    print("\n" + "=" * 78)
    print("  EXP1: Higher T (T ∈ {60, 80, 100}) at λ=16, N=60, dps=250")
    print("  N(60)≈14, N(80)≈22, N(100)≈29")
    print("=" * 78)
    xi_full, L, mu1, delta, _ = build_xi(16, 60, 250)
    ladder_max = float(2 * mp.pi * 60 / L)
    print(f"  ladder_max 2πN/L = {ladder_max:.2f}")
    out = []
    for T in [60, 80, 100]:
        Tm = mp.mpf(T)
        Nex = NT_exact(Tm)
        n_op, zeros = count_zeros_in_interval(
            mp.mpf("0.5"), Tm, xi_full, L, 60, n_grid=6000)
        print(f"  T={T:5.1f}  N(T)={Nex:3d}  N_op={n_op:3d}  "
              f"Δ={n_op-Nex:+d}")
        out.append({"T": float(T), "NT_exact": Nex, "N_op": n_op,
                    "diff": n_op - Nex,
                    "first_zeros": [float(z) for z in zeros[:4]]})
    return out


def exp1b_higher_T_lambda32():
    """At λ=32, N=70, higher dps, extend T to 100."""
    print("\n" + "=" * 78)
    print("  EXP1b: Higher T at λ=32, N=70, dps=250")
    print("=" * 78)
    xi_full, L, mu1, delta, _ = build_xi(32, 70, 250)
    ladder_max = float(2 * mp.pi * 70 / L)
    print(f"  ladder_max 2πN/L = {ladder_max:.2f}")
    out = []
    for T in [50, 60, 63, 80, 100]:
        Tm = mp.mpf(T)
        Nex = NT_exact(Tm)
        n_op, zeros = count_zeros_in_interval(
            mp.mpf("0.5"), Tm, xi_full, L, 70, n_grid=6000)
        print(f"  T={T:5.1f}  N(T)={Nex:3d}  N_op={n_op:3d}  "
              f"Δ={n_op-Nex:+d}")
        out.append({"T": float(T), "NT_exact": Nex, "N_op": n_op,
                    "diff": n_op - Nex,
                    "first_zeros": [float(z) for z in zeros[:6]]})
    return out


def exp2_interp_T():
    """Interpolating T: N_op should be a proper step function."""
    print("\n" + "=" * 78)
    print("  EXP2: Interpolating T around γ_1=14.1347, γ_2=21.0220, γ_3=25.0109")
    print("  Uses executor's λ=8, N=50, dps=220 rig.")
    print("=" * 78)
    xi_full, L, mu1, delta, _ = build_xi(8, 50, 220)
    T_list = [10.0, 13.0, 14.0, 14.1, 14.13, 14.14, 14.2, 15.0,
              20.0, 21.0, 21.02, 21.03, 21.5, 25.0, 25.01, 25.02]
    out = []
    for T in T_list:
        Tm = mp.mpf(T)
        try:
            Nex = NT_exact(Tm)
        except Exception:
            Nex = -1
        n_op, zeros = count_zeros_in_interval(
            mp.mpf("0.5"), Tm, xi_full, L, 50, n_grid=3000)
        flag = "" if n_op == Nex else "  ← MISMATCH"
        print(f"  T={T:7.3f}  N(T)={Nex:3d}  N_op={n_op:3d}  {flag}")
        out.append({"T": float(T), "NT_exact": Nex, "N_op": n_op,
                    "diff": n_op - Nex})
    return out


def exp3_below_first_zero():
    """Below γ_1 the count MUST be 0; just above, 1."""
    print("\n" + "=" * 78)
    print("  EXP3: Below first zero γ_1=14.13472514")
    print("=" * 78)
    xi_full, L, mu1, delta, _ = build_xi(8, 50, 220)
    T_list = [1.0, 5.0, 10.0, 13.0, 14.0, 14.13, 14.14, 14.15, 14.2]
    out = []
    for T in T_list:
        Tm = mp.mpf(T)
        try:
            Nex = NT_exact(Tm)
        except Exception:
            Nex = -1
        n_op, _ = count_zeros_in_interval(
            mp.mpf("0.5"), Tm, xi_full, L, 50, n_grid=3000)
        flag = "" if n_op == Nex else "  ← MISMATCH"
        print(f"  T={T:7.3f}  N(T)={Nex:3d}  N_op={n_op:3d}  {flag}")
        out.append({"T": float(T), "NT_exact": Nex, "N_op": n_op,
                    "diff": n_op - Nex})
    return out


def exp4_precision_floor():
    """Test the claim: dps < 1.86·N + 30 produces spurious eigenvalues
    near the Fourier ladder 2π k / L. For (λ=8, N=50), threshold is 123.
    We test dps = 80 (well below)."""
    print("\n" + "=" * 78)
    print("  EXP4: Precision floor — (λ=8, N=50, dps=80) vs threshold 123")
    print("  Expectation: spurious eigenvalues near 2π k / L (k=1,2,...)")
    print("=" * 78)
    try:
        xi_full, L, mu1, delta, _ = build_xi(8, 50, 80)
    except Exception as e:
        print(f"  build_xi failed: {e}")
        return {"error": str(e)}
    ladder = [float(2 * mp.pi * k / L) for k in range(-10, 11)]
    print(f"  ladder z = 2πk/L for |k|≤10:")
    for k in range(1, 11):
        print(f"    k={k}: z = {ladder[k + 10]:.4f}")
    # Test T=50
    n_op, zeros = count_zeros_in_interval(
        mp.mpf("0.5"), mp.mpf("50"), xi_full, L, 50, n_grid=5000)
    print(f"  N_op(50) at dps=80 = {n_op}  (executor claims spurious at "
          f"dps<123)")
    print(f"  Zeros found: {[float(z) for z in zeros]}")
    return {"dps": 80, "N_op_at_50": n_op,
            "zeros": [float(z) for z in zeros], "mu1": str(mu1),
            "delta": str(delta), "ladder_first_10": ladder[10:21]}


def exp5_lambda64():
    """Higher λ: λ=64 with N chosen for ladder_max > 50 and dps per rule."""
    print("\n" + "=" * 78)
    print("  EXP5: Higher λ — λ=64, N=65, dps=250")
    print("  (N=65, L=2 log 64 ≈ 8.318 → ladder_max ≈ 49.08 < 50 — boundary")
    print("   N=75 → ladder_max ≈ 56.66 > 50, use N=75)")
    print("=" * 78)
    xi_full, L, mu1, delta, _ = build_xi(64, 75, 250)
    ladder_max = float(2 * mp.pi * 75 / L)
    print(f"  ladder_max 2πN/L = {ladder_max:.2f}")
    out = []
    for T in [10, 20, 30, 40, 50]:
        Tm = mp.mpf(T)
        Nex = NT_exact(Tm)
        n_op, zeros = count_zeros_in_interval(
            mp.mpf("0.5"), Tm, xi_full, L, 75, n_grid=4000)
        print(f"  T={T:5.1f}  N(T)={Nex:3d}  N_op={n_op:3d}  "
              f"Δ={n_op-Nex:+d}")
        out.append({"T": float(T), "NT_exact": Nex, "N_op": n_op,
                    "diff": n_op - Nex})
    return out


def main():
    results = {}
    t0 = time.time()
    try:
        results["exp3_below_first"] = exp3_below_first_zero()
    except Exception as e:
        results["exp3_below_first"] = {"error": str(e)}
        import traceback; traceback.print_exc()

    try:
        results["exp2_interp"] = exp2_interp_T()
    except Exception as e:
        results["exp2_interp"] = {"error": str(e)}
        import traceback; traceback.print_exc()

    try:
        results["exp4_prec_floor"] = exp4_precision_floor()
    except Exception as e:
        results["exp4_prec_floor"] = {"error": str(e)}
        import traceback; traceback.print_exc()

    try:
        results["exp1_higher_T"] = exp1_higher_T()
    except Exception as e:
        results["exp1_higher_T"] = {"error": str(e)}
        import traceback; traceback.print_exc()

    try:
        results["exp1b_lambda32"] = exp1b_higher_T_lambda32()
    except Exception as e:
        results["exp1b_lambda32"] = {"error": str(e)}
        import traceback; traceback.print_exc()

    try:
        results["exp5_lambda64"] = exp5_lambda64()
    except Exception as e:
        results["exp5_lambda64"] = {"error": str(e)}
        import traceback; traceback.print_exc()

    print(f"\nTotal elapsed {time.time() - t0:.1f}s")
    out_path = os.path.join(CODE_DIR, "lead-3-adv-extension.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"JSON → {out_path}")


if __name__ == "__main__":
    main()
