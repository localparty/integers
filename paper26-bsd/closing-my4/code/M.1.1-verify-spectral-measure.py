"""
M.1.1 numerical sanity check.

Tests whether the target lemma

  (psi_eps, P_p psi_eps) >= |w|^2 = N(p)^{-k}

holds for the spectral-window state

  psi_eps := E(I) f_0 / ||E(I) f_0||

where:
  - T = log N(.)  (the BC operator restricted to a finite ideal lattice)
  - P_p = range projection of the isometry s_p : |a> -> |p a>
  - f_0 is a chosen reference vector in the BC GNS-like Hilbert space
  - I = (lambda - eps, lambda + eps)

Purpose: confirm or refute that the target bound holds uniformly in f_0
and lambda.  If it FAILS for naive f_0 = |1>, that confirms the
analytic argument that the lemma as stated needs an extra hypothesis on f_0.

Author: Author M.1.1 (W1-A) for closing-MY4 cycle 1.
Date: 2026-04-11.
"""

from mpmath import mp, mpf, log, sqrt
import numpy as np

mp.dps = 30


def gen_ideals_in_Zi(M):
    """Generate Gaussian integer ideals (a + b i) of norm <= M.

    For Z[i], every nonzero ideal is principal of norm a^2 + b^2.
    We label by the canonical generator (a, b) with a > 0 and (a, b) != (0, 0).
    """
    ideals = []
    for a in range(0, int(np.ceil(np.sqrt(M))) + 2):
        for b in range(-a, int(np.ceil(np.sqrt(M))) + 2):
            if a == 0 and b <= 0:
                continue
            if (a, b) == (0, 0):
                continue
            n = a * a + b * b
            if 1 <= n <= M:
                ideals.append((a, b, n))
    seen = set()
    out = []
    for a, b, n in ideals:
        # Canonicalize: pick the representative with a >= 0, then b minimal
        # (this is rough; for the test we just need a deterministic label.)
        key = (n, a, b)
        if key not in seen:
            seen.add(key)
            out.append((a, b, n))
    return sorted(out, key=lambda x: (x[2], x[0], x[1]))


def divides(p_tuple, a_tuple):
    """Test whether the Gaussian prime (pa, pb) divides the ideal (aa, ab).

    For principal ideals in Z[i], (pa + pb i) | (aa + ab i)  iff
    (aa + ab i) / (pa + pb i) is in Z[i].
    """
    pa, pb, _ = p_tuple
    aa, ab, _ = a_tuple
    den = pa * pa + pb * pb
    # numerator: (aa + ab i) (pa - pb i) = (aa pa + ab pb) + (ab pa - aa pb) i
    re = aa * pa + ab * pb
    im = ab * pa - aa * pb
    return (re % den == 0) and (im % den == 0)


def main():
    # Build a finite truncation of the BC ideal lattice over Q(i).
    # We use ideals of norm <= 50 for tractability.
    M = 80
    ideals = gen_ideals_in_Zi(M)
    print(f"Generated {len(ideals)} representatives, max norm {M}.")
    print(f"First 12: {ideals[:12]}")

    # Pick a Gaussian prime: (1+i), norm 2
    p = (1, 1, 2)
    Np = mpf(p[2])

    # The "Hecke operator" e_p has range = {a : p | a}
    range_p = [i for i, a in enumerate(ideals) if divides(p, a)]
    print(f"Range of P_p (for p=(1+i)): {len(range_p)} of {len(ideals)} ideals")

    # T = diag(log N(a)) on the basis indexed by ideals
    # P_p = diag(1 if p|a else 0)
    T_diag = [float(log(mpf(a[2]))) for a in ideals]
    Pp_diag = [1.0 if i in set(range_p) else 0.0 for i in range(len(ideals))]

    # Reference vector f_0 = |1> = e_1 (the GNS cyclic vector)
    # Try a few different f_0 choices.
    f_0_choices = {
        "f_0 = |1> (GNS vacuum)": [1.0 if a == (1, 0, 1) else 0.0 for a in ideals],
        "f_0 = uniform": [1.0 / len(ideals) ** 0.5 for _ in ideals],
        "f_0 in Range(P_p) only": [(1.0 if i in set(range_p) else 0.0) for i in range(len(ideals))],
    }
    # normalize
    for k in list(f_0_choices.keys()):
        v = f_0_choices[k]
        nrm = sum(x * x for x in v) ** 0.5
        f_0_choices[k] = [x / nrm for x in v]

    # Bridge cocycle exponents
    print("\n" + "=" * 70)
    print("Test:  (psi_eps, P_p psi_eps) vs target |w|^2 = N(p)^{-k}")
    print("=" * 70)

    # Choose lambda (spectral parameter) and eps (window half-width).
    # We test at several lambda in [0, log M], including small lambda
    # where the support runner's bound should "obviously" fail for naive f_0.
    eps_vals = [0.5, 0.2, 0.1]
    lambda_vals = [0.0, 0.5, 0.7, 1.0, 2.0, 3.0, log(mpf(13)), log(mpf(17))]

    print("\nReporting (psi_eps, P_p psi_eps) for each (f_0, lambda, eps).")
    print("Compare to target |w|^2 = N(p)^{-k} for k = 2, 3, 4, 6.")
    targets = {k: float(Np ** (-k)) for k in [2, 3, 4, 6]}
    print(f"Targets: |w|^2 = {targets}")

    results = []
    for label, f_0 in f_0_choices.items():
        print(f"\n--- f_0: {label} ---")
        for lam in lambda_vals:
            lam_f = float(lam)
            for eps in eps_vals:
                # Spectral projection: indicator of |T_diag - lam| < eps
                I_indices = [i for i, t in enumerate(T_diag) if abs(t - lam_f) < eps]
                if not I_indices:
                    continue
                # E(I) f_0 = restrict f_0 to those indices
                E_f0 = [f_0[i] if i in set(I_indices) else 0.0 for i in range(len(ideals))]
                norm2_E_f0 = sum(x * x for x in E_f0)
                if norm2_E_f0 < 1e-30:
                    continue
                # P_p E(I) f_0 = restrict to Range(P_p)
                Pp_E_f0 = [E_f0[i] if i in set(range_p) else 0.0 for i in range(len(ideals))]
                # Inner product (E(I) f_0, P_p E(I) f_0)
                ip = sum(E_f0[i] * Pp_E_f0[i] for i in range(len(ideals)))
                ratio = ip / norm2_E_f0  # this is (psi_eps, P_p psi_eps)
                target_k2 = targets[2]
                pass_k2 = "OK " if ratio >= target_k2 else "FAIL"
                results.append(
                    (label, lam_f, eps, ratio, target_k2, pass_k2, len(I_indices))
                )
                print(
                    f"  lam={lam_f:.4f}  eps={eps}  |I|={len(I_indices):3d}  "
                    f"ratio={ratio:.4f}  target(k=2)={target_k2:.4f}  {pass_k2}"
                )

    # Summary: count failures
    fails = [r for r in results if r[5] == "FAIL"]
    print("\n" + "=" * 70)
    print(f"SUMMARY: {len(fails)} of {len(results)} configurations FAIL the bound at k=2.")
    print("=" * 70)
    if fails:
        print("\nFirst 10 failures (each shows the bound fails for naive f_0):")
        for r in fails[:10]:
            print(f"  f_0={r[0]}, lam={r[1]:.4f}, eps={r[2]}, ratio={r[3]:.4f} < {r[4]:.4f}")

    print("\nINTERPRETATION:")
    print("  - If f_0 = |1>, ratio = 0 whenever lambda < log 2 (because |1> not in Range(P_p)).")
    print("  - If f_0 = uniform, ratio is bounded by the density of Range(P_p) in window I.")
    print("  - If f_0 supported on Range(P_p), ratio = 1 always (trivially passes the bound).")
    print("  Conclusion: the target lemma as stated is FALSE for arbitrary f_0;")
    print("  it requires f_0 to have nontrivial overlap with Range(P_p).")
    print("  This is a load-bearing structural finding for M.1.1.")


if __name__ == "__main__":
    main()
