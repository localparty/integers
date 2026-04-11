"""LEAD 7 — Ladder-tail factor separation verification.

Attacks SB-4 (ladder-truncation tail) via the CCM Theorem 5.10 factorization:

    detreg(D^(λ,N)_log − z) = Det(D^(λ,N)_log|_{E_N'} − z)
                              · detreg(D^(λ)_log|_{E_N^⊥} − z)             (*)

where (CCM 2025, Thm 5.10(iii) proof, page 24, lines 1343-1350):
  - the FIRST (useful) factor is the characteristic polynomial of a
    self-adjoint (2N)-dimensional matrix — its zeros are real and
    numerically coincide with γ_1..γ_K for K ≈ min(2N, Weyl count);
  - the SECOND (ladder) factor has zero set exactly
    {2πj/L : j ∈ ℤ, |j| > N}.

This script:
  1. Confirms numerically that on a window [0, T_N] with T_N = 2π(N+1)/L
     the ladder factor contributes nothing (its smallest zero is
     2π(N+1)/L = T_N), so the count N_op(T) for T < T_N is exactly the
     number of "useful" zeros in [0,T] — i.e. N(T) (L3's result).
  2. Verifies the factorization by evaluating the ladder factor
     explicitly (as a ratio of entire functions) and the useful factor
     via the finite-matrix characteristic polynomial, then checking the
     product equals the full -i λ^{-iz} ξ̂(z).
  3. Checks that extending N (keeping λ fixed) extends T_N linearly and
     the L3 exact-match result extends along with it.

CCM factorization identities used:
  detreg(D^(λ)_log − z) = 1 − exp(−izL)       [eq 5.17, line 1130]
                       = 2i exp(−izL/2) sin(zL/2)
  detreg(D^(λ,N)_log − z) = −i λ^{−iz} ξ̂(z)    [Thm 5.10(ii), line 1260]
  ξ̂(z) = 2 L^{−1/2} sin(zL/2) Σ_{|j|≤N} ξ_j / (z − 2πj/L)  [eq 5.25]

From these:
  detreg(D^(λ,N)_log − z)
      = −i λ^{−iz} · 2 L^{−1/2} sin(zL/2) · Σ_{|j|≤N} ξ_j / (z − 2πj/L)
      = −i exp(−izL/2) · 2 sin(zL/2) L^{−1/2} · Σ_j ξ_j/(z−2πj/L)
      = L^{−1/2}(1 − exp(−izL)) · Σ_j ξ_j/(2πj/L − z)            (line 1332)

Equating to detreg(D^(λ)_log − z) · [the rational factor Σ ξ_j/(…)]:
  detreg(D^(λ,N)_log − z) = [detreg(D^(λ)_log − z)]
                          · [L^{−1/2} Σ_j ξ_j/(2πj/L − z)]
which is the strategist's interpretation — BUT this not yet (*).

The correct factorization (*) is: split det_reg(D^(λ)_log − z) as
  det_reg(D^(λ)_log − z) = Π_{|j|≤N}(2πj/L − z) · det_reg(D^(λ)_log|_{E_N^⊥} − z)
up to normalization (since D^(λ)_log decomposes on L²([0,L]) =
span{U_j : |j|≤N} ⊕ complement as E_N ⊕ E_N^⊥). Then
  Det(D^(λ,N)_log|_{E_N'} − z) = Π_{|j|≤N}(2πj/L − z) · (L^{−1/2} Σ_j ξ_j/(2πj/L − z))
which is indeed the characteristic polynomial of a 2N-dim self-adjoint
matrix (the (2N+1)-dim E_N block quotiented by ξ, equivalent to a
rank-one deformation; see Lemma 5.4(iii) → the polynomial has degree
2N, the full E_N block det has degree 2N+1, and the rank-one factor
accounts for the quotient). Zeros of this factor are real and by CCM's
numerics match γ_1..γ_k.

  detreg(D^(λ)_log|_{E_N^⊥} − z) = (1 − exp(−izL)) / Π_{|j|≤N}(2πj/L − z)

whose zeros are exactly {2πj/L : |j| > N} (the sin factor's lattice
zeros minus those cancelled by the finite polynomial).

THIS IS THE ladder factor. This script verifies it numerically.

Precision:  mp.dps = 150 (above the CF precision floor for N up to ~65).
Script runtime: several minutes per (λ, N).
"""

import json
import os
import sys
import time

import mpmath as mp

mp.mp.dps = 150  # above the CCM CF simplicity-gap precision floor for N≤80

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
P13_CODE_DIR = os.path.normpath(os.path.join(CODE_DIR, "..", "..", "code"))
sys.path.insert(0, P13_CODE_DIR)

# Reuse the infrastructure from Lead 3 / paper13 /code:
from r49_fourier_circle import build_QW, eigh_mp  # noqa: E402
from r51b_evenblock import project_to_even, even_eigvec_to_full  # noqa: E402


# ---------------------------------------------------------------------------
# Building blocks for the factorization.
# ---------------------------------------------------------------------------

def xi_hat(z, xi_full, L, N):
    """ξ̂(z) = 2 L^{-1/2} sin(zL/2) · Σ_{|j|≤N} ξ_j / (z − 2πj/L)."""
    twopi = 2 * mp.pi
    pre_sin = mp.sin(z * L / 2)
    s = mp.mpf(0)
    for j in range(-N, N + 1):
        s += xi_full[j + N] / (z - twopi * j / L)
    return 2 * mp.power(L, mp.mpf(-1) / 2) * pre_sin * s


def det_reg_full(z, lam, xi_full, L, N):
    """−i λ^{−iz} ξ̂(z) = detreg(D^(λ,N)_log − z), the FULL regularized det.
    CCM Thm 5.10(ii)."""
    lam_mp = mp.mpf(lam)
    return mp.mpc(0, -1) * mp.power(lam_mp, mp.mpc(0, -1) * z) * xi_hat(
        z, xi_full, L, N)


def det_full_free(z, L):
    """detreg(D^(λ)_log − z) = 1 − exp(−izL)  [CCM eq 5.17 line 1130].
    Its zeros are the FULL lattice 2πZ/L."""
    return 1 - mp.exp(mp.mpc(0, -1) * z * L)


def poly_EN(z, L, N):
    """Finite polynomial P_N(z) := Π_{|j|≤N}(2πj/L − z). (Degree 2N+1.)

    This is the characteristic polynomial of the "free" E_N block
    Det(D^(λ)_log|_{E_N} − z) up to the constant (2π/L)^{2N+1} from
    eq (5.26) of CCM. Its zeros are {2πj/L : |j|≤N}.
    """
    twopi = 2 * mp.pi
    p = mp.mpf(1)
    for j in range(-N, N + 1):
        p *= (twopi * j / L - z)
    return p


def det_ladder_factor(z, L, N):
    """The LADDER factor:
          detreg(D^(λ)_log|_{E_N^⊥} − z)
            = (1 − exp(−izL)) / Π_{|j|≤N}(2πj/L − z)
    Zero set: {2πj/L : j ∈ ℤ, |j| > N}.

    Note: the pole at z=0 in the denominator (from j=0 term) cancels
    with the numerator's zero at z=0. So the function is regular
    everywhere.
    """
    num = det_full_free(z, L)
    den = poly_EN(z, L, N)
    return num / den


def det_useful_factor(z, L, N, xi_full):
    """The USEFUL factor:
          Det(D^(λ,N)_log|_{E_N'} − z)
            = L^{−1/2} · Π_{|j|≤N}(2πj/L − z) · Σ_{|j|≤N} ξ_j / (2πj/L − z)

    This is a polynomial in z of degree 2N (poly_EN has degree 2N+1; one
    factor cancels against the sum's residue). Its zeros are real
    (CCM Thm 5.10(iii)) and coincide with the "useful" spectrum (γ_n
    plus ladder points at integer multiples of 2π/L NOT killed by ξ_j).

    We compute it as (product × sum) in O(N) per point — NOT the double
    sum, which is O(N^2) per point.
    """
    twopi = 2 * mp.pi
    prod = poly_EN(z, L, N)
    s = mp.mpf(0)
    for j in range(-N, N + 1):
        s += xi_full[j + N] / (twopi * j / L - z)
    return mp.power(L, mp.mpf(-1) / 2) * prod * s


def det_full_factorized(z, lam, L, N, xi_full):
    """The CCM factorization re-assembled:
        −i λ^{−iz} · [useful factor] · [ladder factor]
       (this should equal det_reg_full(z, ...) up to the CCM phase
       normalization −i exp(−izL/2) vs −i λ^{−iz} = −i exp(−izL/2),
       which are identical.)
    """
    lam_mp = mp.mpf(lam)
    u = det_useful_factor(z, L, N, xi_full)
    l = det_ladder_factor(z, L, N)
    return mp.mpc(0, -1) * mp.power(lam_mp, mp.mpc(0, -1) * z) * u * l


# ---------------------------------------------------------------------------
# Verification routines.
# ---------------------------------------------------------------------------

def verify_factorization(lam, N, L, xi_full, test_points):
    """Check det_full(z) == det_full_factorized(z) at a set of z's."""
    print(f"\n  Factorization check at {len(test_points)} test points:")
    print(f"  {'z':>20} {'|full − factorized|':>25} {'log10 rel err':>18}")
    max_err = mp.mpf(0)
    for z in test_points:
        lhs = det_reg_full(z, lam, xi_full, L, N)
        rhs = det_full_factorized(z, lam, L, N, xi_full)
        diff = abs(lhs - rhs)
        scale = max(abs(lhs), abs(rhs), mp.mpf(1))
        rel = diff / scale
        max_err = max(max_err, rel)
        rel_f = float(mp.log10(rel)) if rel > 0 else -300
        print(f"  {mp.nstr(z, 12):>20} {mp.nstr(diff, 8):>25} {rel_f:>18.2f}")
    return max_err


def ladder_zeros_check(L, N, j_range):
    """Verify det_ladder_factor(2πj/L) = 0 for |j| > N  and
       det_ladder_factor(2πj/L) ≠ 0 for |j| ≤ N  (the latter is
       a REGULAR point, not a pole)."""
    print(f"\n  Ladder-factor zero check (L = {float(L):.6f}):")
    print(f"  {'j':>5} {'2πj/L':>14} {'|ladder_factor|':>20} {'expected':>14}")
    for j in j_range:
        twopi = 2 * mp.pi
        zj = twopi * j / L
        # Evaluate at zj + tiny epsilon to avoid 0/0
        eps = mp.mpf("1e-30")
        val = det_ladder_factor(zj + eps, L, N)
        expected = "ZERO" if abs(j) > N else "REGULAR"
        print(f"  {j:>5d} {float(zj):>14.6f} {mp.nstr(abs(val), 6):>20} "
              f"{expected:>14}")


def useful_factor_root_count(lam, N, L, xi_full, T_N):
    """Count real zeros of det_useful_factor on [0, T] and compare with
    Riemann N(T) both BELOW and ABOVE the ladder threshold T_N.

    The useful factor (polynomial degree 2N) has zeros at both the γ_n
    and at SOME ladder points 2πj/L where ξ_j happens to be nonzero;
    because ξ is the smallest-eigenvalue eigenvector of QW^N_λ, the
    ladder contributions below T_N are the ones that "absorb" ladder
    poles and become true spectral γ_n — so on [0, T_N] the count
    equals N(T). ABOVE T_N, the useful factor has no further zeros (the
    polynomial degree cap is 2N); all remaining count inflation seen
    in L3's N_op comes from the ladder factor.
    """
    import mpmath
    print(f"\n  Useful-factor zero count vs Riemann N(T):")
    print(f"  T_N = 2π(N+1)/L = {float(T_N):.4f}")
    T_test_points = [30, 50, 60, 65, 68, 80, 100]
    print(f"  {'T':>6} {'N(T)':>7} {'N_useful(T)':>14} {'status':>10} {'label':>12}")
    a_f = 0.5
    # One coarse grid scan up to T=100, then slice.
    T_global = 100.0
    n_grid = 6000
    grid_f = [a_f + (T_global - a_f) * i / n_grid for i in range(n_grid + 1)]
    vals = []
    for zf in grid_f:
        zm = mp.mpf(zf)
        vals.append(det_useful_factor(zm, L, N, xi_full))
    cumulative_sc = [0] * (n_grid + 1)
    for k in range(n_grid):
        delta = 0
        v0, v1 = vals[k], vals[k + 1]
        if (v0 > 0 and v1 < 0) or (v0 < 0 and v1 > 0):
            delta = 1
        cumulative_sc[k + 1] = cumulative_sc[k] + delta
    for T in T_test_points:
        Tm = mp.mpf(T)
        try:
            N_exact = int(mp.nzeros(Tm))
        except Exception:
            N_exact = -1
        # Find index in grid_f
        idx = int((T - a_f) / (T_global - a_f) * n_grid)
        sc = cumulative_sc[idx]
        status = "OK" if sc == N_exact else f"Δ={sc-N_exact:+d}"
        label = "(< T_N)" if T < float(T_N) else "(> T_N)"
        print(f"  {T:>6d} {N_exact:>7d} {sc:>14d} {status:>10} {label:>12}")


# ---------------------------------------------------------------------------
# Runner
# ---------------------------------------------------------------------------

def run_one(lam, N, T_max):
    print()
    print("=" * 78)
    print(f"  λ = {lam}   N = {N}   dps = {mp.mp.dps}")
    print("=" * 78)
    lam_mp = mp.mpf(lam)
    L = 2 * mp.log(lam_mp)
    T_N = 2 * mp.pi * (N + 1) / L
    print(f"  L = 2 log λ = {float(L):.6f}")
    print(f"  T_N = 2π(N+1)/L = {float(T_N):.4f}")
    print(f"  ladder-tail onset at z = {float(T_N):.4f}")

    t0 = time.time()
    A, L_ret = build_QW(lam_mp, N, dps=mp.mp.dps, verbose=False)
    t1 = time.time()
    print(f"  build_QW: {t1 - t0:.1f}s")

    Aev = project_to_even(A, N)
    vals_ev, Q_ev = eigh_mp(Aev)
    t2 = time.time()
    print(f"  even-block eigh: {t2 - t1:.1f}s")

    mu1 = vals_ev[0]
    print(f"  ε_N = μ_1^ev = {mp.nstr(mu1, 12)}")

    xi_ev = [Q_ev[i, 0] for i in range(N + 1)]
    xi_full = even_eigvec_to_full(xi_ev, N)

    # Part A: Factorization numeric check at a handful of points.
    test_points = [
        mp.mpf("14.134725"),   # near γ_1
        mp.mpf("21.022040"),   # near γ_2
        mp.mpf("25.010858"),   # near γ_3
        mp.mpf("42.0"),        # generic
        mp.mpf("50.0"),        # generic
        float(T_N) - 1.0,      # just below ladder onset
        float(T_N) + 0.5,      # just above ladder onset
    ]
    max_err = verify_factorization(lam_mp, N, L, xi_full,
                                   [mp.mpf(str(t)) for t in test_points])
    print(f"\n  MAX FACTORIZATION REL ERR: {mp.nstr(max_err, 6)}")
    fact_ok = max_err < mp.mpf("1e-60")  # well above precision floor
    print(f"  Factorization consistent? {fact_ok}")

    # Part B: Ladder-factor zeros
    j_check = list(range(max(1, N - 3), N + 6))
    ladder_zeros_check(L, N, j_check)

    # Part C: Useful-factor root count
    useful_factor_root_count(lam_mp, N, L, xi_full, T_N)

    return {
        "lam": float(lam),
        "N": N,
        "dps": mp.mp.dps,
        "L": float(L),
        "T_N": float(T_N),
        "max_fact_rel_err": float(max_err),
        "factorization_ok": bool(fact_ok),
    }


def main():
    schedule = [
        (16, 60, 100),  # T_N ≈ 69.11 — the main L3 extension test point
        (16, 70, 100),  # T_N ≈ 80.4 — extended window
    ]

    results = []
    t0 = time.time()
    for lam, N, T_max in schedule:
        try:
            r = run_one(lam, N, T_max)
        except Exception as e:
            import traceback
            traceback.print_exc()
            r = {"lam": lam, "N": N, "error": str(e)}
        results.append(r)

    print()
    print("=" * 78)
    print("LEAD 7 SUMMARY")
    print("=" * 78)
    for r in results:
        if "error" in r:
            print(f"  λ={r['lam']} N={r['N']}: ERROR {r['error']}")
        else:
            print(f"  λ={r['lam']} N={r['N']}: T_N={r['T_N']:.2f}, "
                  f"fact_err={r['max_fact_rel_err']:.2e}, "
                  f"OK={r['factorization_ok']}")

    out_path = os.path.join(CODE_DIR, "lead-7-verify-ladder-separation.json")
    with open(out_path, "w") as f:
        json.dump({"results": results, "elapsed_s": time.time() - t0},
                  f, indent=2, default=str)
    print(f"\nJSON -> {out_path}")
    print(f"Total: {time.time() - t0:.1f}s")


if __name__ == "__main__":
    main()
