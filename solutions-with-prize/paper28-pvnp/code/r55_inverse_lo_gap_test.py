"""
r55_inverse_lo_gap_test.py -- Test: can eigenvector components of QW^N
be captured by a generalized arithmetic progression (GAP)?

The inverse Littlewood-Offord theorem (Tao-Vu, Annals 2009) says:
if anti-concentration fails (P(sum v_i xi_i in B) >= n^{-C}),
then most v_i lie in a GAP of bounded rank and volume.

For our eigenvectors of QW^N, we check:
  1. Extract eigenvector components {phi_k[i]} for several k, N.
  2. Check whether they can be captured by a rank-1 GAP (arithmetic
     progression a + d*Z with bounded volume).
  3. Measure "GAP-avoidance": what fraction of components lies outside
     any rank-1 GAP of bounded volume?

If the components CANNOT be captured: inverse L-O says anti-concentration
holds, which implies polynomial eigenvalue gaps.

Uses the existing QW^N machinery from r49/r51b.
"""

import os, sys
import mpmath as mp

mp.dps = 50

CODE_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CODE_DIR)

from r49_fourier_circle import build_QW, eigh_mp
from r51b_evenblock import project_to_even


def eigenvector_components(N_fourier, lam):
    """Get eigenvector components of the even-sector QW^N matrix.
    N_fourier = Fourier truncation parameter (basis dim = 2*N_fourier+1).
    """
    A, L = build_QW(lam, N_fourier, dps=80, verbose=False)
    Qev = project_to_even(A, N_fourier)
    evals, evecs = eigh_mp(Qev)
    return evals, evecs


def check_rank1_gap(values, max_trials=200):
    """
    Check if a set of values can be approximately captured by
    a rank-1 GAP: {a + k*d : k integer, |k| <= V}.

    Returns (best_d, fraction_captured, volume) for the best
    arithmetic progression found.
    """
    n = len(values)
    vals = sorted([mp.mpf(v) for v in values])

    best_frac = 0
    best_d = None
    best_vol = None

    # Generate candidate step sizes from pairwise differences
    diffs = []
    for i in range(min(n, 12)):
        for j in range(i+1, min(n, 12)):
            d = abs(vals[j] - vals[i])
            if d > mp.mpf('1e-30'):
                diffs.append(d)
                # Also try d/2, d/3
                diffs.append(d / 2)
                diffs.append(d / 3)

    span = vals[-1] - vals[0]
    if span < mp.mpf('1e-30'):
        return mp.mpf(1), 1.0, 1

    for k in range(1, min(n + 5, 25)):
        diffs.append(span / k)

    for d in diffs[:max_trials]:
        if d < mp.mpf('1e-30'):
            continue
        # Compute residues mod d
        residues = [mp.fmod(v, d) for v in vals]
        residues = [float(r if r >= 0 else r + d) for r in residues]

        # For each residue as candidate base, count how many are within 5%
        eps = float(d) * 0.05
        d_float = float(d)
        best_count = 0
        for base_r in residues:
            count = sum(1 for r in residues
                       if min(abs(r - base_r), d_float - abs(r - base_r)) < eps)
            if count > best_count:
                best_count = count

        frac = best_count / n
        vol = int(float(span / d)) + 1

        if frac > best_frac:
            best_frac = frac
            best_d = d
            best_vol = vol

    return best_d, best_frac, best_vol


def main():
    lam = mp.sqrt(14)
    print("=" * 70)
    print("Inverse Littlewood-Offord GAP Test for QW^N Eigenvectors")
    print("=" * 70)
    print(f"lambda = sqrt(14), dps = {mp.dps}")
    print()

    for N_f in [4, 8, 12, 16]:
        print(f"\n--- N_fourier = {N_f} (even-sector dim = {N_f + 1}) ---")
        try:
            evals, evecs = eigenvector_components(N_f, lam)
        except Exception as e:
            print(f"  Build failed: {e}")
            import traceback; traceback.print_exc()
            continue

        dim = len(evals)

        # Check a few eigenvectors: ground state, middle, top
        for k_idx in [0, dim // 2, dim - 1]:
            if k_idx >= dim:
                continue
            # Extract components of k-th eigenvector
            components = [evecs[i, k_idx] for i in range(dim)]

            # Check rank-1 GAP capture
            d, frac, vol = check_rank1_gap(components)

            print(f"  eigvec k={k_idx}: "
                  f"rank-1 GAP captures {frac * 100:.1f}% "
                  f"(step={float(d):.4e}, vol={vol})")

            # Spread statistics
            vals_abs = sorted([abs(float(c)) for c in components])
            spread = vals_abs[-1] - vals_abs[0]
            print(f"    |components|: min={vals_abs[0]:.4e}, "
                  f"max={vals_abs[-1]:.4e}, spread={spread:.4e}")

        # Report eigenvalue gaps
        gaps = [abs(evals[i + 1] - evals[i]) for i in range(dim - 1)]
        min_gap = min(gaps) if gaps else 0
        max_gap = max(gaps) if gaps else 0
        print(f"  eigenvalue gaps: min={float(min_gap):.6e}, "
              f"max={float(max_gap):.6e}")
        print(f"  gap ratio min/max = {float(min_gap/max_gap):.6e}" if max_gap > 0 else "")

    print("\n" + "=" * 70)
    print("INTERPRETATION:")
    print("If rank-1 GAP captures < 50%: components have anti-structure.")
    print("CAVEAT: inverse L-O is for RANDOM vectors, not deterministic.")
    print("This test measures the HEURISTIC prerequisite, not the theorem.")
    print("=" * 70)


if __name__ == "__main__":
    main()
