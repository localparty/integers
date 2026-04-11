"""LEAD 3 — Weyl count completeness for D^(λ,N)_log on L²([λ⁻¹,λ]).

Question: does the eigenvalue count of D^(λ,N)_log on [0, T] match the
Riemann–von Mangoldt count N(T) up to the Weyl error, so that no zero
is "missed" in the limit (λ, N) → ∞?

Construction (CCM-2025 §5):
  1. Build the (2N+1)×(2N+1) Galerkin matrix QW^N_λ in the V_n basis.
  2. Diagonalise; smallest eigenvalue ε_N has eigenvector ξ (assume even,
     simple — verified separately by Lead 2).
  3. By Theorem 5.10, the spectrum of D^(λ,N)_log equals the real zeros
     of the entire function
        ξ̂(z) = 2 L^{-1/2} sin(zL/2) Σ_{|j|≤N} ξ_j / (z − 2πj/L)
     where L = 2 log λ.

Counting protocol:
  • Riemann–von Mangoldt:
        N(T) = (T/2π) log(T/2π) − T/2π + 7/8 + S(T) + O(1/T),
    where S(T) = (1/π) arg ζ(1/2 + iT) and S(T) = O(log T).
    Weyl error envelope: |Δ_W(T)| ≤ 0.137 log T + 0.443 log log T + 1.588
    (Trudgian 2014, sharp explicit bound). For our T ≤ 50, use the
    looser one-sided bound  |N_count − N(T)| ≤ C log T  with C = 1.0.

  • Eigenvalue count for D^(λ,N)_log:
        N_op(T; λ, N) := #{ z ∈ R : ξ̂(z) = 0, 0 < z ≤ T }.
    Computed by sign-change scan of ξ̂ on a fine grid avoiding pole
    locations p_j = 2πj/L (which are removable but numerically annoying).

  • Compare N_op(T; λ, N) vs N(T). Tabulate for T ∈ {10, 20, 30, 40, 50}
    and λ ∈ {8, 16, 32}, N chosen so that the pure-Fourier ladder
    {2π|k|/L : |k| ≤ N} reaches well past T.

KILL/ADVANCE:
  • If for ANY (λ, T) tested at sufficient N we get
    N_op(T) < N(T) − C_kill log T  with C_kill ≥ 5  → KILLED (Numeric)
  • If N_op(T) > N(T) + C_kill log T (spurious) → KILLED (Wrong-space)
  • If |N_op(T) − N(T)| ≤ C log T uniformly → ADVANCED as EVIDENCE

mp.dps ≥ 50.
"""

import json
import os
import sys
import time

import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
P13_CODE_DIR = os.path.normpath(
    os.path.join(CODE_DIR, "..", "..", "code"))
sys.path.insert(0, P13_CODE_DIR)

from r49_fourier_circle import build_QW, eigh_mp, parity_projector_indices, parity_score
from r51b_evenblock import project_to_even, even_eigvec_to_full


# ---------------------------------------------------------------------------
# Riemann–von Mangoldt main term and known zero counts.
# ---------------------------------------------------------------------------

def NT_main(T):
    """Riemann–von Mangoldt smooth main term:
       N̄(T) = (T/(2π)) log(T/(2πe)) + 7/8.
    """
    T = mp.mpf(T)
    twopi = 2 * mp.pi
    return (T / twopi) * mp.log(T / twopi) - T / twopi + mp.mpf(7) / 8


def NT_exact(T):
    """Exact Riemann zero count up to T using mpmath nzeros (Odlyzko/Riemann–
    Siegel-based).  Returns the integer count of nontrivial zeros 0 < γ ≤ T.
    """
    return int(mp.nzeros(T))


def weyl_envelope(T, C=1.0):
    """One-sided envelope C log T (extra +1 for the constant offset).
    Loose, asymptotically correct."""
    return C * mp.log(T) + 1


# ---------------------------------------------------------------------------
# ξ̂(z) evaluator with safe handling near removable poles.
# ---------------------------------------------------------------------------

def xi_hat_safe(z, xi_full, L, N, eps=mp.mpf("1e-30")):
    """Evaluate ξ̂(z) = 2 L^{-1/2} sin(zL/2) Σ_j ξ_j /(z − 2πj/L).

    The poles at z = 2πj/L (|j| ≤ N) are cancelled by the sin factor; the
    function is entire. Near such a point we expand the offending term:
        sin(zL/2) / (z - 2π j/L)  ≈  (-1)^j (L/2)
    which is finite. This routine returns the exact analytic limit when
    z is within eps of a pole, otherwise the straightforward sum.
    """
    twopi = 2 * mp.pi
    pre_sin = mp.sin(z * L / 2)
    s = mp.mpf(0)
    used_limit = False
    for j in range(-N, N + 1):
        pj = twopi * j / L
        denom = z - pj
        if abs(denom) < eps:
            # sin(zL/2) ≈ (-1)^j (L/2) (z - pj) → contribution ξ_j (-1)^j (L/2).
            sign = mp.mpf(1) if (j % 2 == 0) else mp.mpf(-1)
            limit_val = xi_full[j + N] * sign * (L / 2)
            # All other terms get the regular pre_sin · ξ_k/(z - pk) treatment.
            s_other = mp.mpf(0)
            for k in range(-N, N + 1):
                if k == j:
                    continue
                pk = twopi * k / L
                s_other += xi_full[k + N] / (z - pk)
            return 2 * L ** (mp.mpf(-1) / 2) * (pre_sin * s_other + 2 * limit_val / 1)
        s += xi_full[j + N] / denom
    return 2 * L ** (mp.mpf(-1) / 2) * pre_sin * s


def xi_hat_simple(z, xi_full, L, N):
    """Plain ξ̂(z) — assumes z stays away from pole locations."""
    twopi = 2 * mp.pi
    pre_sin = mp.sin(z * L / 2)
    s = mp.mpf(0)
    for j in range(-N, N + 1):
        s += xi_full[j + N] / (z - twopi * j / L)
    return 2 * L ** (mp.mpf(-1) / 2) * pre_sin * s


# ---------------------------------------------------------------------------
# Sign-change zero counter on [a, b] avoiding pole locations.
# ---------------------------------------------------------------------------

def count_zeros_in_interval(a, b, xi_full, L, N, n_grid=2000):
    """Count real zeros of ξ̂(z) on (a, b] by adaptive sign-change scan.

    The grid is uniform on [a, b] but pushed off any pole locations
    p_j = 2πj/L for |j| ≤ N (these are removable so the function is
    entire, but numerically the plain evaluator is unstable nearby).
    Returns (count, list of approximate zero locations).
    """
    twopi = 2 * mp.pi
    pole_set = set()
    for j in range(-N, N + 1):
        pj = float(twopi * j / L)
        if a - 0.01 <= pj <= b + 0.01:
            pole_set.add(round(pj, 8))
    a_f = float(a); b_f = float(b)
    grid = [a_f + (b_f - a_f) * i / n_grid for i in range(n_grid + 1)]

    # Push grid points off any pole; minimum 1e-3 separation in z-units.
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
            # Skip sign changes that straddle a pole point — these are
            # spurious because the sign of the residue flips.
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
                # Fall back to bisection midpoint as best guess.
                zeros.append((z0 + z1) / 2)
    # Deduplicate by proximity
    zeros.sort()
    dedup = []
    for r in zeros:
        if not dedup or abs(r - dedup[-1]) > mp.mpf("1e-6"):
            dedup.append(r)
    return len(dedup), dedup


# ---------------------------------------------------------------------------
# Main driver.
# ---------------------------------------------------------------------------

def run_one(lam, N, dps, T_grid):
    print()
    print("=" * 78)
    print(f"  λ = {lam}    N = {N}    dps = {dps}")
    print("=" * 78)
    mp.mp.dps = dps
    lam = mp.mpf(lam)
    L = 2 * mp.log(lam)
    print(f"  L = 2 log λ = {float(L):.6f}")
    K_max = int(mp.floor(lam * lam))
    print(f"  K_max (prime cutoff = ⌊λ²⌋) = {K_max}")

    t0 = time.time()
    A, L = build_QW(lam, N, dps=dps, verbose=False)
    t_build = time.time() - t0
    print(f"  build_QW done [{t_build:.1f}s]")

    # Use even-block projection (faster, well tested in r51b).
    t1 = time.time()
    Aev = project_to_even(A, N)
    vals_ev, Q_ev = eigh_mp(Aev)
    t_eig = time.time() - t1
    print(f"  even-block eigh done [{t_eig:.1f}s]")

    mu1 = vals_ev[0]
    mu2 = vals_ev[1]
    delta = mu2 - mu1
    print(f"  μ_1^ev = {mp.nstr(mu1, 12)}")
    print(f"  δ^ev   = {mp.nstr(delta, 12)} (positive ⇒ even-simple)")

    xi_ev = [Q_ev[i, 0] for i in range(N + 1)]
    xi_full = even_eigvec_to_full(xi_ev, N)

    # Pure-Fourier ladder maximum: 2π N / L
    z_max_ladder = float(2 * mp.pi * N / L)
    print(f"  pure-Fourier ladder max  2πN/L = {z_max_ladder:.2f}")
    if z_max_ladder < float(max(T_grid)):
        print(f"  WARN: ladder max < T_max — truncation may bias counts")

    # Counting on [0, T] for each T in T_grid.
    rows = []
    print(f"\n  {'T':>6} {'N(T) main':>12} {'N(T) exact':>11} "
          f"{'N_op(T)':>9} {'Δ = N_op−N':>12} {'Weyl env C log T':>17}")
    for T in T_grid:
        Tm = mp.mpf(T)
        Nbar = NT_main(Tm)
        try:
            Nex = NT_exact(Tm)
        except Exception:
            Nex = -1
        n_op, zeros = count_zeros_in_interval(
            mp.mpf("0.5"), Tm, xi_full, L, N, n_grid=4000)
        env = float(weyl_envelope(Tm, C=1.0))
        diff = n_op - Nex if Nex >= 0 else None
        rows.append({
            "T": float(T),
            "NT_main": float(Nbar),
            "NT_exact": int(Nex),
            "N_op": int(n_op),
            "diff_op_minus_exact": diff,
            "weyl_env_C1": env,
            "first_few_op_zeros": [float(z) for z in zeros[:8]],
        })
        diff_s = f"{diff:+d}" if diff is not None else "?"
        print(f"  {T:>6.1f} {float(Nbar):>12.3f} {Nex:>11d} "
              f"{n_op:>9d} {diff_s:>12} {env:>17.3f}")

    return {
        "lam": str(lam),
        "L": float(L),
        "N": N,
        "dps": dps,
        "K_max": K_max,
        "mu1_ev": str(mu1),
        "delta_ev": str(delta),
        "ladder_max": z_max_ladder,
        "build_time_s": t_build,
        "eigh_time_s": t_eig,
        "counts": rows,
    }


def main():
    # Parameter grid: lead specifies λ ∈ {8, 16, 32}; choose N so that the
    # pure-Fourier ladder 2πN/L extends past T_max = 50.
    #   λ=8  : L=4.158  →  N ≥ 50·L/(2π) ≈ 33,  use N = 80
    #   λ=16 : L=5.545  →  N ≥ 44,             use N = 60
    #   λ=32 : L=6.931  →  N ≥ 56,             use N = 70
    #
    # CRITICAL: ε_N (smallest eigenvalue of QW^N_λ) decays as exp(−ρN) with
    # CF rate ρ ≥ 4.27 (toolkit row CF-ρ≥4.27). At dps ≪ 4.27·N/log(10),
    # ε_N drops below the precision floor and the eigenvector ξ becomes
    # noise — producing spurious "low" eigenvalues in ξ̂. To avoid this we
    # use dps high enough that ε_N stays computable (verified empirically:
    # the spurious extras vanish at dps ≥ 200 for λ ≤ 32, N ≤ 90).
    schedule = [
        (mp.mpf(8),  50, 220),
        (mp.mpf(16), 50, 220),
        (mp.mpf(32), 55, 250),
    ]
    T_grid = [10, 20, 30, 40, 50]

    results = []
    t0 = time.time()
    out_path = os.path.join(CODE_DIR, "lead-3-verify-weyl-count.json")
    for (lam, N, dps) in schedule:
        try:
            r = run_one(lam, N, dps, T_grid)
        except Exception as e:
            r = {"lam": str(lam), "N": N, "dps": dps, "error": str(e)}
            print(f"  FAILED: {e}")
            import traceback; traceback.print_exc()
        results.append(r)
        # Write incremental JSON after each λ completes.
        partial = {
            "schedule": [(str(l), N, d) for (l, N, d) in schedule],
            "T_grid": T_grid,
            "results": results,
            "elapsed_s": time.time() - t0,
            "complete": False,
        }
        with open(out_path, "w") as f:
            json.dump(partial, f, indent=2, default=str)
        print(f"  [partial JSON written, elapsed {time.time() - t0:.1f}s]")

    summary = {
        "schedule": [(str(l), N, d) for (l, N, d) in schedule],
        "T_grid": T_grid,
        "results": results,
        "total_time_s": time.time() - t0,
    }

    print()
    print("=" * 78)
    print("SUMMARY — Weyl count vs Riemann–von Mangoldt")
    print("=" * 78)
    for r in results:
        if "error" in r:
            print(f"λ={r['lam']}: ERROR {r['error']}")
            continue
        print(f"\nλ = {r['lam']}    N = {r['N']}    dps = {r['dps']}    "
              f"L = {r['L']:.4f}    ladder_max ≈ {r['ladder_max']:.2f}")
        for c in r["counts"]:
            print(f"   T={c['T']:5.1f}  N(T)_exact={c['NT_exact']:3d}  "
                  f"N_op={c['N_op']:3d}  Δ={c['diff_op_minus_exact']:+d}  "
                  f"|Δ| vs C log T = {c['weyl_env_C1']:5.2f}")

    out_path = os.path.join(CODE_DIR, "lead-3-verify-weyl-count.json")
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")
    print(f"Total time {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
