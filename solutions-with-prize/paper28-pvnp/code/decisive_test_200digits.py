"""
DECISIVE TEST: Eigenvalue gap saturation at 200-digit precision.

Question: does min|spec(B) - spec(M_a)| saturate at ~10^{-51},
or does it drop to ~10^{-201} (the new precision floor)?

If saturation: genuine gap -> Wound 2 closed -> proof stands.
If floor-tracking: artefact of finite precision -> proof wounded.
"""

import time
from mpmath import mp, mpf, matrix, cos, log, pi, sqrt, fabs, inf, eigsy

mp.dps = 200  # 200 decimal digits

L = mpf(10)
primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
K = len(primes_list)

N_values = [10, 15, 20, 25, 30, 35, 40]

print("=" * 80)
print("DECISIVE TEST: Eigenvalue gap at 200-digit precision")
print(f"mp.dps = {mp.dps}")
print(f"L = {L}, K = {K} primes, N_values = {N_values}")
print("=" * 80)
print()

reg = mpf('0.01')  # Cauchy kernel regularization

results = []

for N in N_values:
    t0 = time.time()
    print(f"--- N = {N} ---")

    # Step 1: Chebyshev nodes
    x = [L / 2 * (1 - cos(pi * (2 * i + 1) / (2 * N))) for i in range(N)]

    # Step 2: B_arch (Cauchy kernel with regularization)
    B_arch = matrix(N, N)
    for i in range(N):
        for j in range(N):
            B_arch[i, j] = 1 / (x[i] + x[j] + reg)

    # Step 3: B_prime = sum_p (log(p)/sqrt(p)) * outer(v_p, v_p)
    B_prime = matrix(N, N)
    for p in primes_list:
        p_mp = mpf(p)
        coeff = log(p_mp) / sqrt(p_mp)
        v = [cos(x[i] * log(p_mp)) for i in range(N)]
        for i in range(N):
            for j in range(N):
                B_prime[i, j] += coeff * v[i] * v[j]

    # Step 4: B = B_arch + B_prime
    B = B_arch + B_prime

    # Step 5: Eigenvalues of B via eigsy (symmetric)
    print(f"  Computing eigenvalues of B ({N}x{N})...", flush=True)
    eig_B_vals, _ = eigsy(B)
    eig_B = sorted([eig_B_vals[i] for i in range(N)])
    print(f"  B eigenvalues computed. Range: [{mp.nstr(eig_B[0], 6)}, {mp.nstr(eig_B[-1], 6)}]")

    # Step 6: Archimedean vector a = first column of B_arch, normalized
    a_raw = [B_arch[i, 0] for i in range(N)]
    a_norm = sqrt(sum(ai ** 2 for ai in a_raw))
    a = [ai / a_norm for ai in a_raw]

    # Step 7: Householder reflection
    # w = a - ||a|| * e_0;  but ||a|| = 1 since we normalized
    e0 = [mpf(1) if i == 0 else mpf(0) for i in range(N)]
    # sign convention: w = a - sign(a[0])*e_0
    sign_a0 = mpf(1) if a[0] >= 0 else mpf(-1)
    w = [a[i] - sign_a0 * e0[i] for i in range(N)]
    w_dot = sum(wi ** 2 for wi in w)

    if w_dot < mpf(10) ** (-190):
        # a is already aligned with e_0, Q = I (or -I on first component)
        print("  WARNING: a nearly aligned with e_0, Householder trivial")
        B_rot = B.copy()
    else:
        # Q = I - 2 * outer(w,w) / dot(w,w)
        # B_rot = Q * B * Q^T = Q * B * Q (Q symmetric)
        # Compute Q*B first, then (Q*B)*Q
        def apply_householder(M, w, w_dot, N):
            """Compute Q * M * Q where Q = I - 2*outer(w,w)/w_dot."""
            # First: R = Q * M = M - 2*w*(w^T * M)/w_dot
            R = matrix(N, N)
            for j in range(N):
                # column j of M
                col_j = [M[i, j] for i in range(N)]
                dot_w_col = sum(w[i] * col_j[i] for i in range(N))
                factor = 2 * dot_w_col / w_dot
                for i in range(N):
                    R[i, j] = col_j[i] - factor * w[i]
            # Second: S = R * Q = R - 2*(R*w)*w^T/w_dot
            S = matrix(N, N)
            for i in range(N):
                row_i = [R[i, j] for j in range(N)]
                dot_row_w = sum(row_i[j] * w[j] for j in range(N))
                factor = 2 * dot_row_w / w_dot
                for j in range(N):
                    S[i, j] = row_i[j] - factor * w[j]
            return S

        B_rot = apply_householder(B, w, w_dot, N)

    # Step 8: M_a = B_rot[1:, 1:] (the (N-1)x(N-1) submatrix)
    Nm1 = N - 1
    M_a = matrix(Nm1, Nm1)
    for i in range(Nm1):
        for j in range(Nm1):
            M_a[i, j] = B_rot[i + 1, j + 1]

    print(f"  Computing eigenvalues of M_a ({Nm1}x{Nm1})...", flush=True)
    eig_Ma_vals, _ = eigsy(M_a)
    eig_Ma = sorted([eig_Ma_vals[i] for i in range(Nm1)])
    print(f"  M_a eigenvalues computed. Range: [{mp.nstr(eig_Ma[0], 6)}, {mp.nstr(eig_Ma[-1], 6)}]")

    # Step 9: gap = min |eig_B[k] - eig_Ma[j]|
    gap = inf
    for k in range(len(eig_B)):
        for j in range(len(eig_Ma)):
            d = fabs(eig_B[k] - eig_Ma[j])
            if d < gap:
                gap = d

    if gap > 0:
        log10_gap = float(log(gap, 10))
    else:
        log10_gap = float('-inf')

    elapsed = time.time() - t0
    results.append((N, gap, log10_gap, elapsed))

    print(f"  GAP = {mp.nstr(gap, 15)}")
    print(f"  log10(gap) = {log10_gap:.2f}")
    print(f"  Time: {elapsed:.1f}s")
    print()

print("=" * 80)
print("SUMMARY")
print("=" * 80)
print(f"{'N':>4s}  {'log10(gap)':>12s}  {'gap (15 digits)':>30s}  {'time(s)':>8s}")
for N, gap, lg, t in results:
    print(f"{N:4d}  {lg:12.2f}  {mp.nstr(gap, 15):>30s}  {t:8.1f}")

print()
print("=" * 80)
print("VERDICT")
print("=" * 80)
last_lg = results[-1][2]
if last_lg > -100:
    print(f"log10(gap) at N={results[-1][0]} is {last_lg:.2f} (> -100)")
    print("SATURATION CONFIRMED at a level far above precision floor (10^{-200})")
    print("=> WOUND 2 CLOSED => PROOF STANDS")
elif last_lg > -180:
    print(f"log10(gap) at N={results[-1][0]} is {last_lg:.2f}")
    print("Gap is intermediate -- neither clearly saturated nor at precision floor.")
    print("=> INCONCLUSIVE -- need larger N or different analysis")
else:
    print(f"log10(gap) at N={results[-1][0]} is {last_lg:.2f} (near -200 precision floor)")
    print("PRECISION FLOOR => GAP STILL DECAYING => PROOF WOUNDED")

print()
print("Detailed check:")
print(f"  If gap at largest N is ~10^{{-51}}: SATURATION CONFIRMED -> WOUND 2 CLOSED -> PROOF STANDS")
print(f"  If gap at largest N is ~10^{{-201}}: PRECISION FLOOR -> GAP STILL DECAYING -> PROOF WOUNDED")
print(f"  Actual: gap ~ 10^{{{last_lg:.1f}}}")
