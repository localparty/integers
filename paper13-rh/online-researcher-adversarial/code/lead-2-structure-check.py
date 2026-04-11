"""Structural sanity check on the QW^N_lambda matrix from
lead-2-verify-cf-even-simple.py.

Per Lemma 5.1 of CCM-2025, the matrix has the special form
   tau_{i,i} = a_i,    tau_{i,j} = (b_i - b_j) / (i - j)  for j != i
with a_{-j} = a_j and b_{-j} = -b_j.

Also: tau_{i,j} should be real, and the matrix should commute with the
grading gamma : V_j -> V_{-j}. Equivalently J*tau*J = tau where J is
the antidiagonal flip.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from importlib import import_module

mod = import_module('lead-2-verify-cf-even-simple')
from mpmath import mp, mpf

mp.dps = 60
T = mod.build_QW(4, 5)  # lambda=4, N=5, dim=11
N = 5
dim = 2*N + 1

print("Structural test on QW^N_lambda for lambda=4, N=5")
print(f"dim = {dim}")

# 1. real check
max_imag = mpf(0)
for i in range(dim):
    for j in range(dim):
        v = T[i,j]
        if hasattr(v, 'imag'):
            if abs(v.imag) > max_imag: max_imag = abs(v.imag)
print(f"max |imag part| in matrix : {mp.nstr(max_imag, 5)}")

# 2. symmetry check
sym_err = mpf(0)
for i in range(dim):
    for j in range(i+1, dim):
        d = abs(T[i,j] - T[j,i])
        if d > sym_err: sym_err = d
print(f"max |T_ij - T_ji|         : {mp.nstr(sym_err, 5)}")

# 3. gamma-commute: T_{ij} should equal T_{(2N-i)(2N-j)}
gamma_err = mpf(0)
for i in range(dim):
    for j in range(dim):
        d = abs(T[i,j] - T[2*N - i, 2*N - j])
        if d > gamma_err: gamma_err = d
print(f"max |T_ij - T_{{-i,-j}}|    : {mp.nstr(gamma_err, 5)}  (gamma-commute)")

# 4. CF structure: tau_{i,j} = (b_i - b_j)/(i - j) for off-diagonal
#    Pick b_n := -tau_{0,n} * (n - 0) for n != 0; b_0 = 0.
#    Then check whether tau_{i,j} matches (b_i - b_j)/(i - j).
#    Index map: row_index r -> n = r - N, so n in {-N..N}.
def n_of(r): return r - N
def r_of(n): return n + N

b = {}
b[0] = mpf(0)
# Use middle column (n=0, r = N) as anchor
for n in range(-N, N+1):
    if n == 0: continue
    # tau_{0, n} = (b_0 - b_n)/(0 - n) = b_n / n
    # so b_n = n * tau_{0, n}
    val = T[r_of(0), r_of(n)]
    b[n] = n * val

# Check b_{-n} = -b_n
b_anti_err = mpf(0)
for n in range(1, N+1):
    d = abs(b[n] + b[-n])
    if d > b_anti_err: b_anti_err = d
print(f"max |b_n + b_{{-n}}|        : {mp.nstr(b_anti_err, 5)}  (b should be odd)")

# Check all off-diagonal entries match (b_i - b_j)/(i - j)
cf_err = mpf(0)
for i in range(dim):
    for j in range(dim):
        if i == j: continue
        ni = n_of(i); nj = n_of(j)
        if ni == nj: continue
        pred = (b[ni] - b[nj]) / (ni - nj)
        d = abs(T[i,j] - pred)
        if d > cf_err: cf_err = d
print(f"max |tau_ij - (b_i-b_j)/(i-j)|  : {mp.nstr(cf_err, 5)}  (CF structural form)")

# 5. Diagonal: a_n should satisfy a_{-n} = a_n
a_sym_err = mpf(0)
for n in range(1, N+1):
    d = abs(T[r_of(n), r_of(n)] - T[r_of(-n), r_of(-n)])
    if d > a_sym_err: a_sym_err = d
print(f"max |a_n - a_{{-n}}|        : {mp.nstr(a_sym_err, 5)}  (a should be even)")

# 6. Print a few values
print()
print("First few diagonal entries (a_n) :")
for n in range(0, min(N+1, 6)):
    print(f"  a_{n:2d} = {mp.nstr(T[r_of(n), r_of(n)], 18)}")
print("First few b_n values:")
for n in range(0, min(N+1, 6)):
    print(f"  b_{n:2d} = {mp.nstr(b[n], 18)}")
