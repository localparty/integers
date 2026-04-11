"""
Adversarial extension of Lead 8 rebuild — Cycle 2 Phase 3.

Runs the L8 rebuild machinery at parameter points OUTSIDE the
executor's grid (Round 003 d.1 mandatory extension test) and also
performs the cross-lead consistency spot-check at 5 DIFFERENT matrix
entries (Round 003 d.2).

mp.dps = 200 throughout (inherits from lead-8-cf-even-simple-rebuild.py).
"""

import sys
import time
import importlib.util

# Dynamically import the L8 rebuild module
spec = importlib.util.spec_from_file_location(
    "l8",
    "/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/online-researcher-adversarial/code/lead-8-cf-even-simple-rebuild.py",
)
l8 = importlib.util.module_from_spec(spec)
l8.__name__ = "l8"

# Also import L5 (for cross-lead new-entries check)
spec5 = importlib.util.spec_from_file_location(
    "l5",
    "/Users/gsix/quantum-geometry-in-5d-latex/paper13-rh/online-researcher-adversarial/code/lead-5-verify-ccm-convergence.py",
)
l5 = importlib.util.module_from_spec(spec5)
l5.__name__ = "l5"

# Prevent their __main__ blocks from running
import builtins
_original_name_check = None

# Exec both modules; the '__main__' guard ensures their drivers won't run
# because __name__ is "l8"/"l5".
spec.loader.exec_module(l8)
spec5.loader.exec_module(l5)

from mpmath import mp, mpf, pi, e, nstr

print("=" * 72)
print(f"Lead 8 ADVERSARIAL extension    mp.dps = {mp.dps}")
print("=" * 72)

# ---------------------------------------------------------------------
# (c) Cross-lead spot-check at 5 NEW entries (λ=4, N=30)
# ---------------------------------------------------------------------
print("\n[adv.c] Cross-lead L8 vs L5 at 5 NEW entries, (λ=4, N=30)")
N = 30
lam = mpf(4)
t0 = time.time()
T8 = l8.build_QW_matrix_rebuild(N, lam, verbose=False)
print(f"  [adv] L8 build done in {time.time()-t0:.1f}s")
t0 = time.time()
T5 = l5.build_QW_matrix(N, lam, verbose=False)
print(f"  [adv] L5 build done in {time.time()-t0:.1f}s")

idx = lambda n: n + N
new_entries = [(0, 3), (7, 11), (15, 20), (22, 28), (29, 0)]
print(f"  (n,m)    L8                                  L5                                  |diff|")
max_diff_new = mpf(0)
for (n, m) in new_entries:
    a = T8[idx(n), idx(m)]
    b = T5[idx(n), idx(m)]
    d = abs(a - b)
    if d > max_diff_new:
        max_diff_new = d
    print(f"  ({n:2d},{m:2d})  {nstr(a,14):>34}  {nstr(b,14):>34}  {nstr(d,4):>10}")
print(f"  max diff (new 5 entries) = {nstr(max_diff_new, 4)}")

# Also do the FULL matrix agreement check: max over all entries
maxall = mpf(0)
for i in range(2 * N + 1):
    for j in range(2 * N + 1):
        d = abs(T8[i, j] - T5[i, j])
        if d > maxall:
            maxall = d
print(f"  MAX over ALL {2*N+1}x{2*N+1} entries = {nstr(maxall, 4)}")

# ---------------------------------------------------------------------
# (b) Extension test at values L8 did NOT test
# ---------------------------------------------------------------------
print("\n[adv.b.1] Higher N: (λ=4, N=100)")
try:
    r = l8.run_point(mpf(4), 100)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.2] Higher N: (λ=4, N=150)")
try:
    r = l8.run_point(mpf(4), 150)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.3] Non-integer λ: (λ=π, N=30)")
try:
    r = l8.run_point(pi, 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.4] Non-integer λ: (λ=e, N=30)")
try:
    r = l8.run_point(e, 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.5] (λ=2.718, N=30)  [decimal for comparison with e]")
try:
    r = l8.run_point(mpf("2.718"), 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

# Near sign-change region
print("\n[adv.b.6] Sign-change region: (λ=1.2, N=30)")
try:
    r = l8.run_point(mpf("1.2"), 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.7] (λ=1.3, N=30)")
try:
    r = l8.run_point(mpf("1.3"), 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.8] (λ=1.4, N=30)")
try:
    r = l8.run_point(mpf("1.4"), 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

# Very high λ
print("\n[adv.b.9] Very high λ: (λ=20, N=30)")
try:
    r = l8.run_point(mpf(20), 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\n[adv.b.10] Very high λ: (λ=30, N=30)")
try:
    r = l8.run_point(mpf(30), 30)
except Exception as ex:
    print(f"  EXCEPTION: {ex}")

print("\nDONE.")
