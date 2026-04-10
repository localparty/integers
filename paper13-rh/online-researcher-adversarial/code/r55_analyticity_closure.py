"""R55 — Analyticity closure investigation.

Part 1: Reproduce the R53-2 exponential decay of epsilon(lambda,N) as N grows.
Part 2: Analyze kernel analyticity (W02, WR matrix element decay).
Part 3: Ground state Fourier coefficient decay (analyticity strip).
Part 4: Apply Galerkin convergence theorem to predict the rate.

Uses the existing r49_fourier_circle.py builder and r51b_evenblock.py projector.
"""

import json
import math
import os
import sys
import time

import mpmath as mp

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import (
    GAMMAS_50DIG,
    build_QW,
    eigh_mp,
    build_W02,
    build_WR,
    build_Wprimes,
    precompute_abc,
    von_mangoldt_terms,
    q_UnUm,
)
from r51b_evenblock import project_to_even


def compute_epsilon_even(lam, N, dps=80, verbose=False):
    """Build Q_W, project to even block, return smallest eigenvalue."""
    A, L = build_QW(lam, N, dps=dps, verbose=verbose)
    Aev = project_to_even(A, N)
    vals, Q = eigh_mp(Aev)
    return vals[0], vals, Q, L


# ============================================================================
# PART 1 — Reproduce exponential decay of epsilon(lambda, N)
# ============================================================================

def part1_exponential_decay():
    """Compute epsilon(N) at lambda=sqrt(13) and lambda=10 for various N."""
    print("=" * 72)
    print("PART 1 — Exponential decay of epsilon(lambda, N) as N -> infinity")
    print("=" * 72)

    results = {}

    for lam_label, lam_val, dps in [("sqrt13", None, 150), ("10", 10, 150)]:
        print(f"\n--- lambda = {lam_label}, dps = {dps} ---")
        mp.mp.dps = dps
        if lam_val is None:
            lam = mp.sqrt(13)
        else:
            lam = mp.mpf(lam_val)

        # N values — go up to 100 at dps=150 (higher N is very slow)
        N_list = [10, 20, 30, 40, 50, 60, 80]
        if lam_label == "sqrt13":
            N_list = [10, 20, 30, 40, 50, 60, 80, 100]

        rows = []
        for N in N_list:
            t0 = time.time()
            try:
                eps, vals, Q, L = compute_epsilon_even(lam, N, dps=dps, verbose=False)
                log10_eps = float(mp.log10(abs(eps))) if abs(eps) > 0 else -dps
                elapsed = time.time() - t0
                print(f"  N={N:4d}  eps={mp.nstr(eps, 8):>20s}  "
                      f"log10|eps|={log10_eps:+8.1f}  [{elapsed:.1f}s]")
                rows.append({
                    "N": N, "eps": str(eps),
                    "log10_abs_eps": log10_eps,
                    "elapsed": elapsed
                })
            except Exception as e:
                print(f"  N={N:4d}  FAILED: {e}")
                rows.append({"N": N, "error": str(e)})

        results[lam_label] = rows

        # Fit: log10|eps| = a + b*N (pure exponential)
        # and log10|eps| = a + b*N + c*N^2
        valid = [(r["N"], r["log10_abs_eps"]) for r in rows
                 if "error" not in r and r["log10_abs_eps"] > -dps + 5]
        if len(valid) >= 3:
            Ns = [v[0] for v in valid]
            ys = [v[1] for v in valid]
            # Linear fit: y = a + b*N
            n = len(Ns)
            sx = sum(Ns)
            sy = sum(ys)
            sxx = sum(x*x for x in Ns)
            sxy = sum(x*y for x,y in zip(Ns, ys))
            b = (n*sxy - sx*sy) / (n*sxx - sx*sx)
            a = (sy - b*sx) / n
            # Residuals
            resid = [y - (a + b*x) for x,y in zip(Ns, ys)]
            rms = math.sqrt(sum(r*r for r in resid)/n)
            print(f"\n  Linear fit: log10|eps| = {a:.2f} + {b:.4f}*N  (rms={rms:.2f})")
            print(f"  => |eps| ~ 10^{a:.1f} * exp(-{-b*math.log(10):.4f} * N)")
            alpha = -b * math.log(10)  # decay rate in natural log
            print(f"  => exponential rate alpha = {alpha:.4f}")
            results[lam_label + "_fit"] = {
                "model": "linear_in_N",
                "a": a, "b": b, "rms": rms,
                "alpha_natural": alpha
            }

    return results


# ============================================================================
# PART 2 — Kernel analyticity: matrix element decay
# ============================================================================

def part2_kernel_analyticity():
    """Examine decay of W02, WR, Wp matrix elements in |m|+|n|."""
    print("\n" + "=" * 72)
    print("PART 2 — Kernel analyticity: matrix element decay")
    print("=" * 72)

    dps = 50
    mp.mp.dps = dps
    lam = mp.sqrt(13)
    L = 2 * mp.log(lam)
    N = 60
    K_max = int(mp.floor(lam * lam + mp.mpf("1e-30")))

    results = {}

    # 2a: W02 matrix elements — should decay exponentially
    print("\n--- W02 matrix elements (archimedean pole, rank-2) ---")
    W02 = build_W02(N, L)
    # Check diagonal decay
    diag_w02 = []
    for n in range(0, N+1):
        idx = n + N
        val = float(abs(W02[idx, idx]))
        diag_w02.append((n, val))
    print("  W02 diagonal |W02[n,n]| for selected n:")
    for n, v in diag_w02:
        if n <= 10 or n % 10 == 0:
            log_v = math.log10(max(v, 1e-300))
            print(f"    n={n:3d}  |W02[n,n]| = {v:.6e}  log10 = {log_v:.1f}")

    # W02 is rank-2, so off-diagonal decays as 1/(n^2 * m^2) type
    # Check row n=0
    print("\n  W02 row 0: |W02[0,m]| for selected m:")
    row0_w02 = []
    for m in range(0, N+1):
        idx_m = m + N
        val = float(abs(W02[N, idx_m]))
        row0_w02.append((m, val))
        if m <= 5 or m % 10 == 0:
            log_v = math.log10(max(val, 1e-300))
            print(f"    m={m:3d}  |W02[0,m]| = {val:.6e}  log10 = {log_v:.1f}")

    results["W02_rank2"] = True
    results["W02_diagonal_sample"] = [(n, v) for n, v in diag_w02 if n <= 20 or n % 10 == 0]

    # 2b: WR matrix elements — the critical one
    print("\n--- WR matrix elements (archimedean remainder) ---")
    alpha, diag = precompute_abc(N, L, verbose=False)
    WR = build_WR(N, L, alpha, diag)

    diag_wr = []
    for n in range(0, N+1):
        idx = n + N
        val = float(abs(WR[idx, idx]))
        diag_wr.append((n, val))
    print("  WR diagonal |WR[n,n]| for selected n:")
    for n, v in diag_wr:
        if n <= 10 or n % 10 == 0:
            log_v = math.log10(max(v, 1e-300))
            print(f"    n={n:3d}  |WR[n,n]| = {v:.6e}  log10 = {log_v:.1f}")

    # Check if WR diagonal grows (this would be problematic for analyticity)
    print("\n  WR diagonal GROWTH check:")
    for n in [1, 5, 10, 20, 30, 40, 50, 60]:
        if n <= N:
            v = float(abs(WR[n+N, n+N]))
            print(f"    n={n:3d}  WR[n,n] = {float(WR[n+N,n+N]):+.6e}")

    # Off-diagonal WR decay
    print("\n  WR off-diagonal |WR[0,m]| for selected m:")
    for m in [1, 2, 5, 10, 20, 30, 40, 50]:
        if m <= N:
            val = float(abs(WR[N, m+N]))
            log_v = math.log10(max(val, 1e-300))
            print(f"    m={m:3d}  |WR[0,m]| = {val:.6e}  log10 = {log_v:.1f}")

    results["WR_diagonal_sample"] = [(n, v) for n, v in diag_wr if n <= 20 or n % 10 == 0]

    # 2c: Wp matrix elements — translation operator in Fourier basis
    print("\n--- Wp matrix elements (prime perturbation) ---")
    Wp = build_Wprimes(N, L, K_max, verbose=False)

    print("  Wp diagonal |Wp[n,n]| for selected n:")
    for n in [0, 1, 2, 5, 10, 20, 30, 40, 50, 60]:
        if n <= N:
            val = float(abs(Wp[n+N, n+N]))
            log_v = math.log10(max(val, 1e-300))
            print(f"    n={n:3d}  |Wp[n,n]| = {val:.6e}  log10 = {log_v:.1f}")

    # 2d: Full QW diagonal — does it grow?
    print("\n--- Full QW = W02 - WR - Wp diagonal ---")
    for n in [0, 1, 2, 5, 10, 20, 30, 40, 50, 60]:
        if n <= N:
            idx = n + N
            qw = float(W02[idx,idx] - WR[idx,idx] - Wp[idx,idx])
            print(f"    n={n:3d}  QW[n,n] = {qw:+.6e}")

    return results


# ============================================================================
# PART 3 — Ground state Fourier coefficient decay
# ============================================================================

def part3_ground_state_decay():
    """Compute the even ground state and examine its Fourier coefficient decay."""
    print("\n" + "=" * 72)
    print("PART 3 — Ground state Fourier coefficient decay (analyticity strip)")
    print("=" * 72)

    results = {}

    for lam_label, lam_val, dps, N in [("sqrt13", None, 80, 60), ("10", 10, 80, 60)]:
        print(f"\n--- lambda = {lam_label}, N = {N}, dps = {dps} ---")
        mp.mp.dps = dps
        if lam_val is None:
            lam = mp.sqrt(13)
        else:
            lam = mp.mpf(lam_val)

        A, L = build_QW(lam, N, dps=dps, verbose=False)
        Aev = project_to_even(A, N)
        vals, Q = eigh_mp(Aev)

        # Ground state in the cosine basis: C_0 = V_0, C_n = (V_n + V_{-n})/sqrt(2)
        # Coefficients: xi_0^ev = Q[0,0], xi_n^ev = Q[n,0] for n=1..N
        # In the Fourier basis: xi_0 = xi_0^ev, xi_n = xi_{-n} = xi_n^ev / sqrt(2)

        print(f"  eps_even = {mp.nstr(vals[0], 8)}")
        print(f"  Fourier coefficients of even ground state |xi_n^ev|:")

        coeffs = []
        for n in range(N+1):
            c = float(abs(Q[n, 0]))
            coeffs.append((n, c))

        # Print and check decay
        for n, c in coeffs:
            if n <= 10 or n % 5 == 0:
                log_c = math.log10(max(c, 1e-300))
                print(f"    n={n:3d}  |xi_n^ev| = {c:.6e}  log10 = {log_c:.2f}")

        # Fit exponential decay: log10|xi_n| = a + b*n for n >= 2
        valid = [(n, math.log10(max(c, 1e-300))) for n, c in coeffs
                 if n >= 2 and c > 1e-70]
        if len(valid) >= 5:
            Ns_fit = [v[0] for v in valid]
            ys_fit = [v[1] for v in valid]
            nf = len(Ns_fit)
            sx = sum(Ns_fit)
            sy = sum(ys_fit)
            sxx = sum(x*x for x in Ns_fit)
            sxy = sum(x*y for x,y in zip(Ns_fit, ys_fit))
            b = (nf*sxy - sx*sy) / (nf*sxx - sx*sx)
            a = (sy - b*sx) / nf
            resid = [y - (a + b*x) for x,y in zip(Ns_fit, ys_fit)]
            rms = math.sqrt(sum(r*r for r in resid)/nf)
            alpha = -b * math.log(10)
            L_float = float(L)
            sigma = alpha * L_float / (2 * math.pi)
            print(f"\n  Exponential fit: log10|xi_n| = {a:.2f} + {b:.4f}*n  (rms={rms:.3f})")
            print(f"  => |xi_n| ~ exp(-{alpha:.4f} * n)")
            print(f"  => analyticity strip width sigma = alpha*L/(2*pi) = {sigma:.4f}")
            print(f"     (L = {L_float:.4f})")

            results[lam_label] = {
                "alpha": alpha,
                "sigma": sigma,
                "L": L_float,
                "fit_a": a, "fit_b": b, "fit_rms": rms,
                "N_fit_range": (min(Ns_fit), max(Ns_fit)),
            }

        # Also check: do the coefficients decay like exp(-alpha*n) or exp(-alpha*n^2)?
        # Try quadratic fit: log10|xi_n| = a + b*n + c*n^2
        if len(valid) >= 6:
            from numpy import polyfit
            ns = [v[0] for v in valid]
            ys = [v[1] for v in valid]
            c2, c1, c0 = polyfit(ns, ys, 2)
            resid2 = [y - (c0 + c1*x + c2*x*x) for x,y in zip(ns, ys)]
            rms2 = math.sqrt(sum(r*r for r in resid2)/len(ns))
            print(f"  Quadratic fit: log10|xi_n| = {c0:.2f} + {c1:.4f}*n + {c2:.6f}*n^2  (rms={rms2:.3f})")
            if abs(c2) * max(ns)**2 > abs(c1) * max(ns) * 0.1:
                print(f"  => Quadratic term is SIGNIFICANT (super-exponential?)")
            else:
                print(f"  => Quadratic term is negligible (pure exponential)")

    return results


# ============================================================================
# PART 2b — WR diagonal growth analysis
# ============================================================================

def part2b_wr_growth():
    """Detailed analysis of WR diagonal behavior at large n."""
    print("\n" + "=" * 72)
    print("PART 2b — WR diagonal growth analysis")
    print("=" * 72)

    dps = 50
    mp.mp.dps = dps
    lam = mp.sqrt(13)
    L = 2 * mp.log(lam)

    # The WR diagonal involves the digamma function via the rho(x) kernel
    # rho(x) = e^{x/2} / (e^x - e^{-x})
    # Near x=0: rho(x) ~ 1/(2x) + O(x)
    # This is the key singularity. On [0,L] with L = 2*log(sqrt(13)) ~ 2.56,
    # rho has a pole-like singularity at x=0.

    # The WR diagonal is (from eq 4.4):
    # WR(n,n) = 2*[gamma + log(4pi) - log((e^L+1)/(e^L-1))] / 2
    #         + integral of [e^{x/2} * 2*(1-x/L)*cos(2*pi*n*x/L) - 2] / (e^x - e^{-x}) dx

    # For large n, the oscillatory integral kills the cos part by Riemann-Lebesgue,
    # leaving the constant piece. Let's check this.

    N = 80
    alpha, diag = precompute_abc(N, L, verbose=False)

    print("\nWR diagonal values WR(n,n) for n = 0..80:")
    wr_vals = []
    for n in range(N+1):
        val = float(diag[n])
        wr_vals.append((n, val))
        if n <= 15 or n % 10 == 0:
            print(f"  n={n:3d}  WR[n,n] = {val:+.8f}")

    # Check if WR[n,n] converges to a constant (Riemann-Lebesgue prediction)
    if N >= 70:
        v60 = float(diag[60])
        v70 = float(diag[70])
        v80 = float(diag[80])
        print(f"\n  WR[60,60] = {v60:.8f}")
        print(f"  WR[70,70] = {v70:.8f}")
        print(f"  WR[80,80] = {v80:.8f}")
        print(f"  Difference 80-70: {v80-v70:.2e}")
        print(f"  Difference 70-60: {v70-v60:.2e}")

        # The limit should be 2*[c + w] where c+w is the constant from CC1
        cw = float(mp.mpf(1)/2 * mp.log((mp.exp(L/2)-1)/(mp.exp(L/2)+1))
                    + mp.atan(mp.exp(L/2)) - mp.pi/4 + mp.euler/2
                    + mp.mpf(1)/2 * mp.log(8*mp.pi))
        limit_pred = 2 * cw
        print(f"\n  Predicted limit (Riemann-Lebesgue): 2*(c+w) = {limit_pred:.8f}")
        print(f"  WR[80,80] = {v80:.8f}")
        print(f"  Difference from limit: {v80 - limit_pred:.6e}")

    return wr_vals


# ============================================================================
# MAIN
# ============================================================================

def main():
    t_start = time.time()
    results = {}

    # Part 1: Exponential decay
    results["part1"] = part1_exponential_decay()

    # Part 2: Kernel analyticity
    results["part2"] = part2_kernel_analyticity()

    # Part 2b: WR growth
    results["part2b"] = part2b_wr_growth()

    # Part 3: Ground state decay
    results["part3"] = part3_ground_state_decay()

    elapsed = time.time() - t_start
    print(f"\n{'='*72}")
    print(f"Total elapsed: {elapsed:.1f}s ({elapsed/60:.1f}min)")

    out_path = os.path.join(CODE_DIR, "r55_analyticity_closure.json")
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, default=str)
    print(f"Saved -> {out_path}")

    return results


if __name__ == "__main__":
    main()
