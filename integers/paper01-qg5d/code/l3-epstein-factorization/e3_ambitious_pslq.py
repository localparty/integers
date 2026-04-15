"""
Ambitious PSLQ: very large basis, very high maxcoeff, see if any non-trivial
relation involving E_3(3; Q_3) and zeta(3) emerges.
"""

import mpmath as mp
from mpmath import mpf, mpc, pi as mp_pi, nstr
import os, json
from collections import Counter

mp.mp.dps = 80  # higher precision for larger PSLQ
HERE = os.path.dirname(os.path.abspath(__file__))

N_CUT = 12
T_MAX = mpf(50)
A3_det = mpf(1) / 2
_Q3_COUNTS = Counter(); _Q3INV_COUNTS = Counter()
for i in range(-N_CUT, N_CUT + 1):
    for j in range(-N_CUT, N_CUT + 1):
        for k in range(-N_CUT, N_CUT + 1):
            if i == 0 and j == 0 and k == 0: continue
            Q  = i*i + j*j + k*k + i*j + i*k + j*k
            Qi = 3*(i*i + j*j + k*k) - 2*(i*j + i*k + j*k)
            _Q3_COUNTS[Q] += 1
            _Q3INV_COUNTS[Qi] += 1
_Q3S = sorted([(mpf(Q), c) for Q, c in _Q3_COUNTS.items()])
_Q3IS = sorted([(mpf(q)/2, c) for q, c in _Q3INV_COUNTS.items()])

def theta(t, sp):
    s = mpf(0)
    for Q, c in sp: s += c*mp.exp(-mp_pi*t*Q)
    return s
def F1(s, sp):
    return mp.quad(lambda t: t**(s-1)*theta(t,sp), [1,3,10,T_MAX])
def Lam(s):
    s_m = mpc(s); d = 1/mp.sqrt(A3_det); L_half = mpf(3)/2
    return F1(s_m, _Q3S) + d*F1(L_half - s_m, _Q3IS) + d/(s_m - L_half) - 1/s_m
def E3(s):
    s_m = mpc(s); return mp_pi**s_m * Lam(s_m) / mp.gamma(s_m)

def chi3(n):
    r = n%3; return 0 if r==0 else (1 if r==1 else -1)
def chi4(n):
    r = n%4
    if r==1: return 1
    if r==3: return -1
    return 0
def chi8(n):
    r = n%8
    if r in (1,3): return 1
    if r in (5,7): return -1
    return 0

def L(s, chi, terms=6000):
    s_m = mpc(s); total = mpc(0)
    for n in range(1, terms+1):
        c = chi(n)
        if c: total += c / mpf(n)**s_m
    return total

def r(x): return mpf(x.real) if isinstance(x, mpc) else mpf(x)

# Build a big basis for s=3 alone.
e3 = E3(3); z3 = mp.zeta(3); z2 = mp.zeta(2); z5 = mp.zeta(5)
l3m3 = L(3, chi3); l3m4 = L(3, chi4); l3m8 = L(3, chi8)
l2m3 = L(2, chi3); l2m4 = L(2, chi4)
pi = mp_pi
log2 = mp.log(2); log3 = mp.log(3)

basis = {
    "E_3(3)":          e3,
    "zeta(3)":         z3,
    "z3*L(3,chi_-3)":  z3*l3m3,
    "z3*L(3,chi_-4)":  z3*l3m4,
    "z3*L(3,chi_-8)":  z3*l3m8,
    "L(3,chi_-3)*L(3,chi_-4)": l3m3*l3m4,
    "L(3,chi_-3)^2":   l3m3**2,
    "L(3,chi_-4)^2":   l3m4**2,
    "pi*L(2,chi_-3)":  pi*l2m3,
    "pi*L(2,chi_-4)":  pi*l2m4,  # pi * Catalan
    "pi^3":            pi**3,
    "log(2)*z2":       log2*z2,
    "log(3)*z2":       log3*z2,
}

labels = list(basis.keys())
vals = [r(v) for v in basis.values()]

print("PSLQ on expanded basis at s=3:")
for lab, v in zip(labels, vals):
    print(f"  {lab:30s} = {nstr(v, 30)}")

# Try PSLQ with big maxcoeff
for mc in [10**6, 10**8, 10**10, 10**12]:
    rel = mp.pslq(vals, tol=mpf('1e-50'), maxcoeff=mc)
    print(f"  maxcoeff={mc}: relation = {rel}")

# Subset: only E_3(3), z3, z3*L(3,chi) — the L=2 analogue family
print()
print("Subset (L=2 analogue): E_3(3), z3, z3*L(3,chi_-3):")
sub = [r(e3), r(z3), r(z3*l3m3)]
for mc in [10**4, 10**6, 10**8, 10**10, 10**12, 10**14]:
    rel = mp.pslq(sub, tol=mpf('1e-50'), maxcoeff=mc)
    print(f"  maxcoeff={mc}: relation = {rel}")

print()
print("Subset: E_3(3), z3, z3*L(3,chi_-3), z3*L(3,chi_-4):")
sub2 = [r(e3), r(z3), r(z3*l3m3), r(z3*l3m4)]
for mc in [10**4, 10**6, 10**8, 10**10, 10**12, 10**14]:
    rel = mp.pslq(sub2, tol=mpf('1e-50'), maxcoeff=mc)
    print(f"  maxcoeff={mc}: relation = {rel}")

# The L=2 formula's '6' prefactor is 6 = |units Z[ω]| = order of dihedral
# group of A_2.  For A_3 / SU(4), order of Weyl group W(A_3) = 4! = 24.
# Try coefficient hint:
print()
print("Does 24 · zeta(3) · L(3,chi) match E_3(3) for some chi?")
for name, l3v in [("chi_-3", l3m3), ("chi_-4", l3m4), ("chi_-8", l3m8)]:
    ratio = e3 / (24 * z3 * l3v)
    print(f"   E_3(3) / (24*z3*L(3,{name})) = {nstr(ratio, 25)}")
# Also try Weyl-group factors for extended forms:
for k in [6, 8, 12, 17, 24, 48]:
    for name, l3v in [("chi_-3", l3m3), ("chi_-4", l3m4), ("chi_-8", l3m8)]:
        v = k * z3 * l3v
        if abs(v - e3) / abs(e3) < mpf('0.05'):
            print(f"   {k}*z3*L(3,{name}) = {nstr(v,25)}  (close to E_3(3) = {nstr(e3,15)})")

# Numerically closest simple combinations with |coeffs| <= 20
print()
print("Brute-force search: integer combos with small coefficients")
best = []
z3L3 = z3 * l3m3
for a in range(1, 25):
    for b in range(-40, 41):
        for c in range(-10, 11):
            if c == 0:
                v = mpf(a) * z3L3 + b * z3
            else:
                v = mpf(a) * z3L3 + b * z3 + c * (z3 * l3m4)
            diff = e3 - v
            if abs(diff) < mpf('0.001'):
                best.append((abs(diff), a, b, c, v))
best.sort()
for row in best[:10]:
    print(f"   a={row[1]}, b={row[2]}, c={row[3]}: combo = {nstr(row[4],20)}, diff = {nstr(row[0],10)}")

# Final: even longer brute force
print()
print("No-op if nothing found.")
