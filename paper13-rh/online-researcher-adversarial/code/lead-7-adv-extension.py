"""LEAD 7 — ADVERSARIAL EXTENSION TEST (Cycle 2 Phase 3).

Purpose: extend the L7 executor's grid and test the factor-separation claim
at new (λ, N, T) points outside the tested envelope.

Tests run:
  (A) New (λ, N) pairs:
        (λ=8,   N=40)
        (λ=32,  N=100)  [heavy — optional if runtime OK]
        (λ=5.5, N=30)   [non-integer λ]
        (λ=π,   N=20)   [transcendental λ]
  (B) Boundary T test: at (λ=16, N=60), evaluate ladder/useful at
        T ∈ {T_N − 0.01, T_N, T_N + 0.01, T_N + 0.5, T_N + 1.0}
        to check the transition is clean, not smeared.
  (C) Large T test: at (λ=16, N=60), sweep T ∈ {100, 150, 200} and
        verify integer-sharp ladder-tail prediction Δ(T) = #{j: N+1 ≤ j ≤
        ⌊T·L/(2π)⌋} against the useful+ladder factorization.
  (D) Finite-N convergence lag re-check at (λ=16, N=70): count useful-
        factor zeros in [0, 30] and confirm / deny L7 executor's Δ=+2 claim.

Precision: mp.dps = 150 (matches executor) — the Ladder and useful
polynomial evaluations cancel at roughly 10^(-50) relative near zeros,
which is well above the dps floor for N ≤ 80.
"""

import os
import sys
import time
import json

import mpmath as mp

mp.mp.dps = 150

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
P13_CODE_DIR = os.path.normpath(os.path.join(CODE_DIR, "..", "..", "code"))
sys.path.insert(0, P13_CODE_DIR)

from r49_fourier_circle import build_QW, eigh_mp  # noqa
from r51b_evenblock import project_to_even, even_eigvec_to_full  # noqa


def poly_EN(z, L, N):
    twopi = 2 * mp.pi
    p = mp.mpf(1)
    for j in range(-N, N + 1):
        p *= (twopi * j / L - z)
    return p


def det_full_free(z, L):
    return 1 - mp.exp(mp.mpc(0, -1) * z * L)


def det_ladder_factor(z, L, N):
    return det_full_free(z, L) / poly_EN(z, L, N)


def det_useful_factor(z, L, N, xi_full):
    twopi = 2 * mp.pi
    prod = poly_EN(z, L, N)
    s = mp.mpf(0)
    for j in range(-N, N + 1):
        s += xi_full[j + N] / (twopi * j / L - z)
    return mp.power(L, mp.mpf(-1) / 2) * prod * s


def xi_hat(z, xi_full, L, N):
    twopi = 2 * mp.pi
    pre_sin = mp.sin(z * L / 2)
    s = mp.mpf(0)
    for j in range(-N, N + 1):
        s += xi_full[j + N] / (z - twopi * j / L)
    return 2 * mp.power(L, mp.mpf(-1) / 2) * pre_sin * s


def det_reg_full(z, lam, xi_full, L, N):
    lam_mp = mp.mpf(lam)
    return mp.mpc(0, -1) * mp.power(lam_mp, mp.mpc(0, -1) * z) * xi_hat(
        z, xi_full, L, N)


def det_full_factorized(z, lam, L, N, xi_full):
    lam_mp = mp.mpf(lam)
    u = det_useful_factor(z, L, N, xi_full)
    l = det_ladder_factor(z, L, N)
    return mp.mpc(0, -1) * mp.power(lam_mp, mp.mpc(0, -1) * z) * u * l


def build_lam_N(lam, N):
    """Build QW and smallest-even eigenvector for (lam, N)."""
    lam_mp = mp.mpf(str(lam)) if not isinstance(lam, mp.mpf) else lam
    L = 2 * mp.log(lam_mp)
    t0 = time.time()
    A, _ = build_QW(lam_mp, N, dps=mp.mp.dps, verbose=False)
    t_build = time.time() - t0
    Aev = project_to_even(A, N)
    vals_ev, Q_ev = eigh_mp(Aev)
    mu1 = vals_ev[0]
    xi_ev = [Q_ev[i, 0] for i in range(N + 1)]
    xi_full = even_eigvec_to_full(xi_ev, N)
    T_N = 2 * mp.pi * (N + 1) / L
    return {
        "lam": float(lam_mp),
        "N": N,
        "L": float(L),
        "L_mp": L,
        "T_N": float(T_N),
        "T_N_mp": T_N,
        "mu1": mp.nstr(mu1, 8),
        "xi_full": xi_full,
        "t_build": t_build,
    }


def count_zeros_useful(ctx, T, n_grid=6000):
    """Count sign changes of the real useful factor on [a, T], a = 0.5."""
    L = ctx["L_mp"]
    N = ctx["N"]
    xi_full = ctx["xi_full"]
    a_f = 0.5
    T_f = float(T)
    sc = 0
    prev = None
    for i in range(n_grid + 1):
        zf = a_f + (T_f - a_f) * i / n_grid
        zm = mp.mpf(zf)
        val = det_useful_factor(zm, L, N, xi_full)
        # Useful factor is real on real axis. Take real part.
        vr = float(mp.re(val))
        if prev is not None:
            if (prev > 0 and vr < 0) or (prev < 0 and vr > 0):
                sc += 1
        prev = vr
    return sc


def riemann_N(T):
    return int(mp.nzeros(mp.mpf(T)))


def check_factorization_at(ctx, z_list):
    lam = ctx["lam"]
    L = ctx["L_mp"]
    N = ctx["N"]
    xi_full = ctx["xi_full"]
    out = []
    for zv in z_list:
        zm = mp.mpf(str(zv))
        lhs = det_reg_full(zm, lam, xi_full, L, N)
        rhs = det_full_factorized(zm, lam, L, N, xi_full)
        diff = abs(lhs - rhs)
        scale = max(abs(lhs), abs(rhs), mp.mpf(1))
        rel = diff / scale
        out.append((float(zv), mp.nstr(diff, 5), mp.nstr(rel, 5)))
    return out


def ladder_zeros(ctx, j_range):
    L = ctx["L_mp"]
    N = ctx["N"]
    out = []
    eps = mp.mpf("1e-30")
    for j in j_range:
        zj = 2 * mp.pi * j / L
        val = det_ladder_factor(zj + eps, L, N)
        exp = "ZERO" if abs(j) > N else "REGULAR"
        out.append((j, float(zj), mp.nstr(abs(val), 5), exp))
    return out


def run_one(lam, N, big=False):
    print()
    print("=" * 78)
    print(f"  EXTENSION   λ = {lam}   N = {N}   dps = {mp.mp.dps}")
    print("=" * 78)
    ctx = build_lam_N(lam, N)
    print(f"  L = {ctx['L']:.6f}    T_N = {ctx['T_N']:.4f}    "
          f"mu1 = {ctx['mu1']}    build = {ctx['t_build']:.1f}s")

    # Factorization check at a few points incl. near T_N.
    test_z = [
        mp.mpf("14.134725"),
        mp.mpf("25.010858"),
        mp.mpf("42.0"),
        ctx["T_N_mp"] - mp.mpf("0.5"),
        ctx["T_N_mp"] + mp.mpf("0.5"),
    ]
    print("  Factorization |lhs - rhs| (abs)  /  rel:")
    for (z, d, r) in check_factorization_at(ctx, test_z):
        print(f"    z = {z:<14.6f}   |diff|={d}   rel={r}")

    # Ladder zeros around N.
    print("  Ladder zeros (N-2..N+5):")
    for (j, zj, v, e) in ladder_zeros(ctx, range(max(1, N - 2), N + 6)):
        print(f"    j={j:>5}  2pij/L={zj:>10.4f}  |ladder|={v}  [{e}]")

    # Useful-factor zero count at key T's.
    T_list = [10, 30, 50, 65, min(float(ctx["T_N"]) - 0.5, 100), 80, 100]
    T_list = sorted(set(round(t, 3) for t in T_list if t > 5))
    print("  Useful-factor zero count:")
    for T in T_list:
        try:
            nT = riemann_N(T)
        except Exception:
            nT = -1
        nu = count_zeros_useful(ctx, T, n_grid=4000)
        status = "OK" if nu == nT else f"Δ={nu - nT:+d}"
        lab = "(< T_N)" if T < ctx["T_N"] else "(> T_N)"
        print(f"    T={T:>6}  N(T)={nT:>4}  N_useful={nu:>4}  {status:>7} {lab}")

    return ctx


def run_boundary(lam, N):
    print()
    print("=" * 78)
    print(f"  BOUNDARY T TEST   λ = {lam}   N = {N}")
    print("=" * 78)
    ctx = build_lam_N(lam, N)
    TN = ctx["T_N_mp"]
    print(f"  T_N = {float(TN):.8f}")
    delta_list = [mp.mpf("-0.1"), mp.mpf("-0.01"), mp.mpf("-0.001"),
                  mp.mpf("0"), mp.mpf("0.001"), mp.mpf("0.01"),
                  mp.mpf("0.1"), mp.mpf("0.5"), mp.mpf("1.0")]
    print("  ladder factor & useful factor at T_N + delta:")
    print(f"  {'delta':>10} {'|ladder|':>16} {'|useful|':>16} {'|full|':>16}")
    for d in delta_list:
        z = TN + d
        lf = det_ladder_factor(z, ctx["L_mp"], N)
        uf = det_useful_factor(z, ctx["L_mp"], N, ctx["xi_full"])
        full = det_reg_full(z, lam, ctx["xi_full"], ctx["L_mp"], N)
        print(f"  {float(d):>10.4f} {mp.nstr(abs(lf), 6):>16} "
              f"{mp.nstr(abs(uf), 6):>16} {mp.nstr(abs(full), 6):>16}")


def run_large_T(lam, N):
    print()
    print("=" * 78)
    print(f"  LARGE-T (T=200) TEST   λ = {lam}   N = {N}")
    print("=" * 78)
    ctx = build_lam_N(lam, N)
    L = ctx["L_mp"]
    TN = float(ctx["T_N"])
    print(f"  T_N = {TN:.4f}")
    # Useful-factor zero count up to T=200
    # (useful factor has degree 2N so cannot exceed 2N zeros on reals)
    T_list = [80, 100, 150, 200]
    print("  Useful-factor zero count:")
    for T in T_list:
        nT = riemann_N(T)
        nu = count_zeros_useful(ctx, T, n_grid=8000)
        lab = "(< T_N)" if T < TN else "(> T_N)"
        print(f"    T={T:>5}  N(T)={nT:>4}  N_useful={nu:>4}   {lab}")

    # Integer-sharp ladder prediction:
    # ladder zeros on (0, T] are {2π j/L : N+1 ≤ j ≤ floor(T*L/(2π))}
    print("  Integer-sharp ladder-tail prediction:")
    for T in T_list:
        j_max = int(mp.floor(mp.mpf(T) * L / (2 * mp.pi)))
        n_ladder = max(0, j_max - N)
        print(f"    T={T:>5}  j_max={j_max:>5}  #ladder zeros in (0,T] "
              f"= max(0,j_max-N) = {n_ladder}")


def run_finite_N_lag(lam, N):
    print()
    print("=" * 78)
    print(f"  FINITE-N LAG CHECK   λ = {lam}   N = {N}")
    print("=" * 78)
    ctx = build_lam_N(lam, N)
    for T in [20, 25, 30, 40, 50]:
        nT = riemann_N(T)
        nu = count_zeros_useful(ctx, T, n_grid=6000)
        d = nu - nT
        print(f"    T={T:>3}  N(T)={nT:>3}  N_useful={nu:>3}   Δ={d:+d}")


def main():
    t0 = time.time()
    print(f"dps = {mp.mp.dps}")
    # (A) Boundary behavior at (16, 60)
    run_boundary(16, 60)

    # (B) Large T test at (16, 60)
    run_large_T(16, 60)

    # (C) Finite-N lag at (16, 70)
    run_finite_N_lag(16, 70)

    # (D) New (λ, N) pairs
    run_one(8, 40)

    # (E) Non-integer λ tests
    run_one(mp.mpf("5.5"), 30)
    run_one(mp.pi, 20)

    print()
    print(f"Total: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
