"""
Deeper probes after the initial factor search.

Findings from pass 1 motivate these:

  (a) E_3(3; Q_3) / 12 = 1.20449...  vs  zeta(3) = 1.20205...
      Δ = 0.00244 ≈ 0.2%. Not an identity but suggestive — probe variants.

  (b) Residue at s = 3/2 is 8.88576587... = 2·sqrt(2)·pi, NOT 2·sqrt(2·pi).
      The PROOF-CHAIN text "2*sqrt(2π)" is ambiguous; numerically it is
      2·sqrt(2) · pi = pi^{3/2}/Γ(3/2)/sqrt(det A_3) with det A_3 = 1/2.

  (c) A_3 root system: rank = 3, |roots| = 12. Agent A's "17" equals
      rank+|roots|+2 (or uses embedding dim 4 = rank of A_3 as a lattice in
      R^4 via coordinate-sum=0 realization). Re-check numerics with both
      conventions.

We run PSLQ with more basis vectors and longer bases.
"""

import mpmath as mp
from mpmath import mpf, mpc, pi as mp_pi, nstr, sqrt
import json, os
from collections import Counter

mp.mp.dps = 60

HERE = os.path.dirname(os.path.abspath(__file__))
N_CUT = 10
T_MAX = mpf(40)
A3_det = mpf(1) / 2

# (re-import the E_3 machinery inline for self-containment)
_Q3_COUNTS = Counter()
_Q3INV_COUNTS = Counter()
for i in range(-N_CUT, N_CUT + 1):
    for j in range(-N_CUT, N_CUT + 1):
        for k in range(-N_CUT, N_CUT + 1):
            if i == 0 and j == 0 and k == 0:
                continue
            Q  = i*i + j*j + k*k + i*j + i*k + j*k
            Qi = 3*(i*i + j*j + k*k) - 2*(i*j + i*k + j*k)
            _Q3_COUNTS[Q] += 1
            _Q3INV_COUNTS[Qi] += 1
_Q3_SPECTRUM    = sorted([(mpf(Q), c) for Q, c in _Q3_COUNTS.items()])
_Q3INV_SPECTRUM = sorted([(mpf(q)/2, c) for q, c in _Q3INV_COUNTS.items()])


def theta_minus_one(t, spectrum):
    s = mpf(0)
    for Q, c in spectrum:
        s += c * mp.exp(-mp_pi * t * Q)
    return s


def F1(s, spectrum):
    integrand = lambda t: t**(s - 1) * theta_minus_one(t, spectrum)
    return mp.quad(integrand, [1, 3, 10, T_MAX])


def Lambda_E3(s):
    s_m = mpc(s)
    det_half_inv = 1 / mp.sqrt(A3_det)
    L_half = mpf(3) / 2
    f1 = F1(s_m, _Q3_SPECTRUM)
    f2 = F1(L_half - s_m, _Q3INV_SPECTRUM)
    pole = det_half_inv / (s_m - L_half) - 1 / s_m
    return f1 + det_half_inv * f2 + pole


def E3(s):
    s_m = mpc(s)
    return mp_pi**s_m * Lambda_E3(s_m) / mp.gamma(s_m)


def chi_minus3(n):
    r = n % 3
    return 0 if r == 0 else (1 if r == 1 else -1)


def chi_minus4(n):
    r = n % 4
    if r == 1: return 1
    if r == 3: return -1
    return 0


def chi_minus8(n):
    r = n % 8
    if r in (1, 3): return 1
    if r in (5, 7): return -1
    return 0


def L(s, chi, terms=4000):
    s_m = mpc(s)
    total = mpc(0)
    for n in range(1, terms + 1):
        c = chi(n)
        if c:
            total += c / mpf(n)**s_m
    return total


# ─────────────────────────────────────────────────────────────
# 1.  Revisit E_3(3) via higher-precision direct sum
#    The previous direct sum with N=40 was off by 6.4e-6, which is
#    partial-sum tail, not an algorithmic discrepancy.  For a reliable
#    comparison use Mellin throughout.
# ─────────────────────────────────────────────────────────────
e3_at_integers = {}
for s_int in [2, 3, 4, 5, 6, 7, 8]:
    e3_at_integers[s_int] = E3(mpf(s_int))
    print(f"  E_3({s_int}) = {nstr(e3_at_integers[s_int], 30)}")
print()

# ─────────────────────────────────────────────────────────────
# 2.  Extended PSLQ at s=3 with ~15 basis elements and
#    higher maxcoeff, using real parts only (everything is real).
# ─────────────────────────────────────────────────────────────
z2 = mp.zeta(2); z3 = mp.zeta(3); z4 = mp.zeta(4); z5 = mp.zeta(5)
z6 = mp.zeta(6)
L3_m3 = L(3, chi_minus3)
L3_m4 = L(3, chi_minus4)
L3_m8 = L(3, chi_minus8)
L2_m3 = L(2, chi_minus3)
L2_m4 = L(2, chi_minus4)  # Catalan
L4_m3 = L(4, chi_minus3)
L4_m4 = L(4, chi_minus4)
pi = mp_pi
e3_s3 = E3(3)
e3_s2 = E3(2)
e3_s4 = E3(4)

def r(x): return mpf(x.real) if isinstance(x, mpc) else mpf(x)

# PSLQ probe at s=3 with a rich set including known special values
labels = [
    "E_3(3)", "zeta(3)",
    "L(3,chi_-3)", "L(3,chi_-4)", "L(3,chi_-8)",
    "zeta(3)*L(3,chi_-3)", "zeta(3)*L(3,chi_-4)",
    "zeta(3)*L(3,chi_-8)",
    "pi^3", "pi*zeta(2)",
]
vals = [
    r(e3_s3), r(z3),
    r(L3_m3), r(L3_m4), r(L3_m8),
    r(z3*L3_m3), r(z3*L3_m4), r(z3*L3_m8),
    r(pi**3), r(pi*z2),
]

print(">> PSLQ (rich basis at s=3):")
for lab, v in zip(labels, vals):
    print(f"    {lab:30s} = {nstr(v, 25)}")
print()
rel = mp.pslq(vals, tol=mpf('1e-40'), maxcoeff=10**10)
print("  relation:", rel)
print()

# PSLQ at s=2 (maybe E_3(2) factors through L(2, chi_-4) = Catalan)
labels2 = [
    "E_3(2)", "zeta(2)", "L(2,chi_-3)", "L(2,chi_-4)", "L(2,chi_-8)",
    "zeta(2)*L(2,chi_-3)", "zeta(2)*L(2,chi_-4)",
    "pi^2", "Catalan",
]
vals2 = [
    r(e3_s2), r(z2), r(L2_m3), r(L2_m4),
    r(L(2, chi_minus8)),
    r(z2*L2_m3), r(z2*L2_m4),
    r(pi**2), r(mp.catalan),
]
print(">> PSLQ (s=2):")
for lab, v in zip(labels2, vals2):
    print(f"    {lab:30s} = {nstr(v, 25)}")
rel2 = mp.pslq(vals2, tol=mpf('1e-40'), maxcoeff=10**10)
print("  relation:", rel2)
print()

# PSLQ at s=4
labels4 = [
    "E_3(4)", "zeta(4)", "L(4,chi_-3)", "L(4,chi_-4)",
    "zeta(4)*L(4,chi_-3)", "zeta(4)*L(4,chi_-4)",
    "pi^4",
]
vals4 = [
    r(e3_s4), r(z4), r(L4_m3), r(L4_m4),
    r(z4*L4_m3), r(z4*L4_m4), r(pi**4),
]
print(">> PSLQ (s=4):")
for lab, v in zip(labels4, vals4):
    print(f"    {lab:30s} = {nstr(v, 25)}")
rel4 = mp.pslq(vals4, tol=mpf('1e-40'), maxcoeff=10**10)
print("  relation:", rel4)
print()

# ─────────────────────────────────────────────────────────────
# 3.  Known fact about A_3 = D_3 Epstein.
#    The A_3 theta series is related to the Dedekind zeta of Q(i)
#    or Q(sqrt(-3)) only for A_2 and D_4.  For A_3/D_3, the standard
#    result (Sarnak, Conway-Sloane) is that there is NO multiplicative
#    factorization into two 1D L-functions — A_3 is NOT a biquadratic
#    lattice.  We confirm this by searching for two-factor patterns of
#    many kinds.
# ─────────────────────────────────────────────────────────────
print("Ratios E_3(s)/[zeta(s) zeta(s-1)] and similar:")
for s_int in [2, 3, 4, 5, 6]:
    s = mpf(s_int)
    e3v = E3(s)
    zs = mp.zeta(s)
    zsm1 = mp.zeta(s-1) if s_int > 2 else mpf("inf")
    print(f"   s={s_int}: E_3/[zeta(s)zeta(s-1)] = {nstr(e3v/(zs*zsm1), 25)}  "
          f"E_3/[zeta(s)·L(s,chi_-3)] = {nstr(e3v/(zs*L(s,chi_minus3)), 25)}")

# ─────────────────────────────────────────────────────────────
# 4.  D_3 Epstein.  D_3 ≅ A_3 as lattices so same thing — skip.
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# 5.  Try: does E_3(s; Q_3) decompose as
#        E_3(s) = zeta(s) · zeta(s−1)  * (ratio to rational function of s)?
#    This is the known answer for the cubic lattice Z^3:
#       E_3^{cubic}(s) = sum over shells; well-known = 6 zeta(s) beta(s) - ...
#    (no closed factorization either).  But for A_3, maybe a 3-term
#    multiplicative factorization survives.
# ─────────────────────────────────────────────────────────────

# ─────────────────────────────────────────────────────────────
# 6.  Relation between E_3(s; Q_3) and E_3(s; Z^3)
#    (cubic lattice Epstein).  Maybe expressing the mercedes form via
#    cubic gives a handle.  E_3^{cubic}(s) = Z^3 Epstein.
# ─────────────────────────────────────────────────────────────
def E3_cubic_direct(s, ncut=30):
    s_m = mpc(s)
    total = mpc(0)
    for i in range(-ncut, ncut+1):
        for j in range(-ncut, ncut+1):
            for k in range(-ncut, ncut+1):
                if i == 0 and j == 0 and k == 0:
                    continue
                total += 1 / mpf(i*i + j*j + k*k)**s_m
    return total

print()
print("E_3^cubic(s) values (direct, N=30) — for comparison:")
for s_int in [2, 3, 4, 5]:
    ec = E3_cubic_direct(s_int, ncut=30)
    e3 = E3(s_int)
    print(f"   s={s_int}: E_3^cubic = {nstr(ec, 20)}   E_3^A3 = {nstr(e3, 20)}   ratio = {nstr(e3/ec, 20)}")

# ─────────────────────────────────────────────────────────────
# 7.  The affine Â_3 count: with rank(A_3)=3 as Lie-theoretic rank,
#    rank + |roots| + 1 = 3 + 12 + 1 = 16.  To get 17 we need rank = 4
#    = rank of Â_3 (extended affine Dynkin has one extra node).
#    Check: 4 + 12 + 1 = 17 ✔.
#    Note also: dim(SU(4)) = 15 = rank + |roots| = 3+12. 15+2=17.
#    Or: 17 = (4 nodes of Â_3) + 12 (roots) + 1 (central element) = 17.
# ─────────────────────────────────────────────────────────────
print()
print("Affine Â_3 combinatorics:")
print("   rank(Â_3) + |roots(A_3)| + 1 = 4 + 12 + 1 = 17")
print("   dim(SU(4)) + 2 = 15 + 2 = 17")
print("   (finite) rank(A_3) + |roots(A_3)| + 1 = 3 + 12 + 1 = 16")
print()
print("   E_3(3) ≈", nstr(e3_s3, 20), "=", nstr(e3_s3/17, 15), "* 17")
print("   zeta(3)*L(3,chi_-3)*6 =", nstr(6*z3*L3_m3, 20))
print("   zeta(3)*L(3,chi_-4)*6 =", nstr(6*z3*L3_m4, 20))
print("   zeta(3)*L(3,chi_-3)*12 =", nstr(12*z3*L3_m3, 20))
print("   12*zeta(3) =", nstr(12*z3, 20))
print("   E_3(3)/12 - zeta(3) =", nstr(e3_s3/12 - z3, 20))

# Save to JSON
out = {
    "E_3_at_integers": {str(k): nstr(v, 40) for k, v in e3_at_integers.items()},
    "PSLQ_s3_rich": {
        "basis": labels,
        "values": [nstr(v, 40) for v in vals],
        "relation": str(rel),
    },
    "PSLQ_s2_rich": {
        "basis": labels2,
        "values": [nstr(v, 40) for v in vals2],
        "relation": str(rel2),
    },
    "PSLQ_s4_rich": {
        "basis": labels4,
        "values": [nstr(v, 40) for v in vals4],
        "relation": str(rel4),
    },
    "key_gap_E3_3_over_12_minus_zeta3": nstr(e3_s3/12 - z3, 40),
}

with open(os.path.join(HERE, "e3_deep_probe.json"), "w") as f:
    json.dump(out, f, indent=2, default=str)

print()
print("wrote e3_deep_probe.json")
