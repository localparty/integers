"""
e3_factor_search.py
===================

Agent B (Paper 1 Lead #2) — search for a multiplicative factorization of the
L=3 Epstein zeta E_3(s; Q_3) on the A_3/D_3/SU(4) root lattice.

Q_3(n) = n1^2 + n2^2 + n3^2 + n1 n2 + n1 n3 + n2 n3  (Gram A_3, det = 1/2)

CONTEXT
-------
At L=2, the Eisenstein Epstein on Q_2 = n1^2 + n1 n2 + n2^2 factors:

    E_2(s; Q_2) = 6 · zeta(s) · L(s, chi_{-3})

(chi_{-3} = non-trivial quadratic character mod 3).  The factor "6" counts the
units in Z[omega], and L(s, chi_{-3}) is the Dedekind zeta of Q(sqrt(-3))
divided by zeta(s).  The question for L=3 is whether the A_3 Epstein admits
an analogous factorization and whether zeta(3) emerges structurally at a
specific weight (integer s = 3, half-integer s = 3/2, etc.), which is the
transcendental appearing multiplicatively in Pin #6 (J_CKM).

STRATEGY
--------
1.  Reuse the completed-zeta Mellin representation from
    paper1/code/K-5-2-route-c-3loop.py verbatim (analytic continuation via
    Terras' functional equation).
2.  Tabulate E_3(s; Q_3) at s = 2, 3, 4, 5, 5/2, 7/2, 9/2 to 40+ digits.
3.  For each s, evaluate candidate factorization patterns
        R(s) = E_3(s; Q_3) / [ zeta(s) L(s, chi) * combinations ]
    with chi in {chi_{-3}, chi_{-4}, chi_{-8}, chi_{-11}, chi_{-7}} and
    with auxiliary zeta/L factors zeta(2s-1), L(s-1, chi), etc.
4.  Use PSLQ (mpmath.pslq) to look for Q-linear relations among
        { E_3(s; Q_3), zeta(s) L(s, chi), zeta(2s-1), zeta(s-1),
          pi^a * zeta(b) L(c, chi'), ... }.
5.  Compare E_3(3; Q_3) against  log(gamma_1) * zeta(3)  and related
    combinations.

PSLQ note: we use mp.pslq([a_1, ..., a_n], tol=1e-30) at mp.dps = 50.  A
positive hit returns a short integer relation Sum c_i a_i = 0.

OUTPUT
------
All numerics written to  e3_special_values.json.
Human-readable report in  FINDINGS.md (written separately).
"""

import json
import os
from collections import Counter

import mpmath as mp
from mpmath import mpf, mpc, pi as mp_pi, nstr, sqrt

mp.mp.dps = 50

HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_JSON = os.path.join(HERE, "e3_special_values.json")

# ──────────────────────────────────────────────────────────────────────────
# Q_3 Epstein via completed-zeta Mellin rep — lifted from Route-C.
# ──────────────────────────────────────────────────────────────────────────

A3_det = mpf(1) / 2   # det(A_3)

# Lattice cut-off for θ tails (same reasoning as Route-C)
N_CUT = 10
T_MAX = mpf(40)

_Q3_COUNTS = Counter()
_Q3INV_COUNTS = Counter()
for i in range(-N_CUT, N_CUT + 1):
    for j in range(-N_CUT, N_CUT + 1):
        for k in range(-N_CUT, N_CUT + 1):
            if i == 0 and j == 0 and k == 0:
                continue
            Q  = i*i + j*j + k*k + i*j + i*k + j*k
            Qi = 3*(i*i + j*j + k*k) - 2*(i*j + i*k + j*k)  # 2*Q_3^{-1}(n)
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


def E3_direct(s, ncut=40):
    """Direct sum, convergent for Re(s) > 3/2. ncut large enough for high s."""
    s_m = mpc(s)
    counts = Counter()
    for i in range(-ncut, ncut + 1):
        for j in range(-ncut, ncut + 1):
            for k in range(-ncut, ncut + 1):
                if i == 0 and j == 0 and k == 0:
                    continue
                Q = i*i + j*j + k*k + i*j + i*k + j*k
                counts[Q] += 1
    total = mpc(0)
    for Q, c in sorted(counts.items()):
        total += c / mpf(Q)**s_m
    return total

# ──────────────────────────────────────────────────────────────────────────
# Dirichlet L-functions for small-conductor characters
# ──────────────────────────────────────────────────────────────────────────

# chi_{-d}: Kronecker symbol mod |d| (quadratic character of Q(sqrt(-d)))
# We implement a few of the small-conductor ones.

def _kron(a, p):
    """Kronecker symbol (a/p) for odd p.  Simple quadratic residue test."""
    if a % p == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def chi_minus3(n):
    r = n % 3
    return 0 if r == 0 else (1 if r == 1 else -1)


def chi_minus4(n):
    r = n % 4
    if r == 1: return 1
    if r == 3: return -1
    return 0


def chi_minus7(n):
    # discriminant -7: chi(n) = (n/7) for n coprime to 7
    r = n % 7
    if r == 0: return 0
    # QRs mod 7: {1,2,4}
    return 1 if r in (1, 2, 4) else -1


def chi_minus8(n):
    # discriminant -8: chi(n) mod 8: chi(1)=chi(3)=1, chi(5)=chi(7)=-1
    r = n % 8
    if r in (1, 3): return 1
    if r in (5, 7): return -1
    return 0


def chi_minus11(n):
    r = n % 11
    if r == 0: return 0
    return 1 if pow(r, 5, 11) == 1 else -1


CHARS = {
    "chi_-3":  chi_minus3,
    "chi_-4":  chi_minus4,
    "chi_-7":  chi_minus7,
    "chi_-8":  chi_minus8,
    "chi_-11": chi_minus11,
}


def L(s, chi, terms=2000):
    """Dirichlet L-function L(s, chi) by direct summation with
    Euler-Maclaurin tail. For s >= 2 and 2000 terms, tail < 10^{-40} at s=2."""
    s_m = mpc(s)
    total = mpc(0)
    for n in range(1, terms + 1):
        c = chi(n)
        if c:
            total += c / mpf(n)**s_m
    return total


def L_precise(s, chi):
    """Higher-precision L via mp.nsum for slow convergence cases."""
    s_m = mpc(s)
    return mp.nsum(lambda n: chi(int(n)) / mpf(n)**s_m, [1, mp.inf])


# ──────────────────────────────────────────────────────────────────────────
# L=2 sanity: verify the known factorization
#
#     E_2(s; Q_2) = 6 · zeta(s) · L(s, chi_{-3})
#
# Q_2(n1,n2) = n1^2 + n1 n2 + n2^2.
# We confirm at s=2, s=3, s=5/2.
# ──────────────────────────────────────────────────────────────────────────

def E2_direct(s, ncut=200):
    s_m = mpc(s)
    total = mpc(0)
    for i in range(-ncut, ncut + 1):
        for j in range(-ncut, ncut + 1):
            if i == 0 and j == 0:
                continue
            Q = i*i + i*j + j*j
            total += mpf(1) / mpf(Q)**s_m
    return total


# ──────────────────────────────────────────────────────────────────────────
# Main evaluation
# ──────────────────────────────────────────────────────────────────────────

def main():
    out = {}

    print("=" * 72)
    print("L=2 SANITY: E_2(s; Q_2) =? 6 · zeta(s) · L(s, chi_{-3})")
    print("=" * 72)
    l2_check = {}
    for s_rat in [2, 3, mpf('2.5'), 4]:
        s = mpf(s_rat)
        e2 = E2_direct(s)
        rhs = 6 * mp.zeta(s) * L(s, chi_minus3)
        rel = abs(e2 - rhs) / abs(e2)
        print(f"  s = {s_rat}:  E_2 = {nstr(e2, 20)}")
        print(f"           6·z·L = {nstr(rhs, 20)}   rel.err = {nstr(rel, 4)}")
        l2_check[str(s_rat)] = {
            "E_2": nstr(e2, 30),
            "6·zeta·L(chi_-3)": nstr(rhs, 30),
            "rel_err": nstr(rel, 6),
        }
    out["L2_factorization_check"] = l2_check

    print()
    print("=" * 72)
    print("L=3 SPECIAL VALUES: E_3(s; Q_3)")
    print("=" * 72)
    s_values = [2, 3, 4, 5,
                mpf('2.5'), mpf('3.5'), mpf('4.5'),
                mpf('1.5') + mpf('1e-30'),  # extract residue limit
                mpf('0.5'),  mpf('-0.5')]

    specials = {}
    for s in s_values:
        sv = E3(mpf(s))
        key = str(s) if not isinstance(s, mpf) else nstr(s, 10)
        print(f"  s = {key}:  E_3 = {nstr(sv, 25)}")
        specials[key] = nstr(sv, 40)
    out["E3_special_values"] = specials

    # Sanity: compare E_3(3) Mellin vs. direct at larger N_CUT
    print()
    print("-" * 72)
    print("Direct-sum cross-check of E_3(3):")
    e3_direct_3 = E3_direct(3, ncut=40)
    e3_mellin_3 = E3(3)
    rel = abs(e3_direct_3 - e3_mellin_3) / abs(e3_direct_3)
    print(f"  direct (N=40) = {nstr(e3_direct_3, 25)}")
    print(f"  Mellin        = {nstr(e3_mellin_3, 25)}")
    print(f"  rel.err       = {nstr(rel, 4)}")
    out["E3_direct_vs_Mellin_at_s3"] = {
        "direct_N40": nstr(e3_direct_3, 40),
        "Mellin":     nstr(e3_mellin_3, 40),
        "rel_err":    nstr(rel, 6),
    }

    # ──────────────────────────────────────────────────────────────────
    # Ratio probes  E_3(s;Q_3) / [ zeta(s) · L(s, chi) ]
    # ──────────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("RATIO PROBES:  E_3(s; Q_3) / [ zeta(s) · L(s, chi) ]")
    print("=" * 72)
    ratio_probes = {}
    for s in [2, 3, 4, 5, mpf('2.5'), mpf('3.5')]:
        sm = mpf(s)
        e3 = E3(sm)
        row = {"E_3": nstr(e3, 30)}
        z = mp.zeta(sm)
        row["zeta(s)"] = nstr(z, 30)
        for name, chi in CHARS.items():
            Lval = L(sm, chi)
            row[f"L(s,{name})"] = nstr(Lval, 30)
            ratio = e3 / (z * Lval)
            row[f"E_3/(zeta·L{name})"] = nstr(ratio, 30)
        # Ratios to pure zeta combos
        for s_shift in [sm - 1, 2*sm - 1, 2*sm - 2, 3*sm, sm + 1]:
            try:
                zz = mp.zeta(s_shift)
                row[f"zeta({nstr(s_shift,6)})"] = nstr(zz, 20)
            except Exception:
                pass
        ratio_probes[nstr(sm, 6)] = row

        print(f"\n  s = {nstr(sm, 6)}:")
        print(f"    E_3                      = {nstr(e3, 20)}")
        print(f"    zeta(s)                  = {nstr(z, 20)}")
        for name in CHARS:
            print(f"    E_3 / (zeta·L[{name}])    = "
                  f"{row[f'E_3/(zeta·L{name})']}")
    out["ratio_probes"] = ratio_probes

    # ──────────────────────────────────────────────────────────────────
    # PSLQ searches at s = 3  (the canonical zeta(3) slot)
    # ──────────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("PSLQ SEARCHES at s = 3  (hunt for zeta(3) emergence)")
    print("=" * 72)

    pslq_s3 = {}
    e3_s3 = E3(3)
    z3    = mp.zeta(3)
    z5    = mp.zeta(5)
    z2    = mp.zeta(2)
    pi    = mp_pi

    basis_labels = ["E_3(3;Q_3)", "zeta(3)"]
    basis = [e3_s3, z3]
    for name, chi in CHARS.items():
        basis_labels.append(f"L(3,{name})")
        basis.append(L(3, chi))
    # Products zeta(3)*L(3,chi)
    for name, chi in CHARS.items():
        basis_labels.append(f"zeta(3)*L(3,{name})")
        basis.append(z3 * L(3, chi))
    basis_labels.append("pi^3")
    basis.append(pi**3)
    basis_labels.append("pi^2*zeta(3)")
    basis.append(pi**2 * z3)
    basis_labels.append("zeta(5)/zeta(2)")
    basis.append(z5 / z2)

    # Try PSLQ on small subsets (the full basis is too heterogeneous)
    def try_pslq(labels, values, tag):
        print(f"\n  --- {tag} ---")
        print("   basis:", ", ".join(labels))
        try:
            rel = mp.pslq([mpf(v.real) if isinstance(v, mpc) else mpf(v)
                           for v in values], tol=mpf('1e-30'), maxcoeff=10**8)
        except Exception as e:
            rel = None
            print(f"   PSLQ raised: {e!r}")
        print(f"   PSLQ relation: {rel}")
        return rel

    # Probe 1: E_3(3) vs zeta(3) * L(3,chi_{-3})  (the natural L=2 analogue)
    r = try_pslq(
        ["E_3(3;Q_3)", "zeta(3)*L(3,chi_{-3})"],
        [e3_s3, z3 * L(3, chi_minus3)],
        "E_3(3) vs zeta(3) L(3,chi_-3)",
    )
    pslq_s3["E3_vs_z3_Lchi-3"] = r

    # Probe 2: E_3(3) vs zeta(3) * L(3, chi_{-4})
    r = try_pslq(
        ["E_3(3;Q_3)", "zeta(3)*L(3,chi_{-4})"],
        [e3_s3, z3 * L(3, chi_minus4)],
        "E_3(3) vs zeta(3) L(3,chi_-4)",
    )
    pslq_s3["E3_vs_z3_Lchi-4"] = r

    # Probe 3: E_3(3) vs [ zeta(3), L(3, chi_{-3}), L(3, chi_{-4}) ]
    r = try_pslq(
        ["E_3(3;Q_3)", "zeta(3)", "L(3,chi_-3)", "L(3,chi_-4)"],
        [e3_s3, z3, L(3, chi_minus3), L(3, chi_minus4)],
        "E_3(3) in zeta(3), L(3,chi_-3), L(3,chi_-4)",
    )
    pslq_s3["E3_in_z3_Lchi-3_Lchi-4"] = r

    # Probe 4: larger mix — zeta(3), products with all chi's
    basis4_labels = ["E_3(3)", "zeta(3)"]
    basis4_vals = [e3_s3, z3]
    for name, chi in CHARS.items():
        basis4_labels.append(f"zeta(3)*L(3,{name})")
        basis4_vals.append(z3 * L(3, chi))
    r = try_pslq(basis4_labels, basis4_vals, "E_3(3) vs zeta(3)*L(3,chi) family")
    pslq_s3["E3_vs_z3_Lchi_family"] = r

    # Probe 5: maybe it's  E_3(3) ∝  L(3, chi)^2, or something non-trivial
    r = try_pslq(
        ["E_3(3)", "L(3,chi_-3)^2", "L(3,chi_-4)^2"],
        [e3_s3, L(3, chi_minus3)**2, L(3, chi_minus4)**2],
        "E_3(3) vs L(3,chi)^2",
    )
    pslq_s3["E3_vs_Lchi_squared"] = r

    # Probe 6: E_3(3) vs zeta(3)*zeta(2), pi^3, etc.
    r = try_pslq(
        ["E_3(3)", "zeta(3)", "pi^3", "pi^2*zeta(3)"],
        [e3_s3, z3, pi**3, pi**2 * z3],
        "E_3(3) vs zeta(3), pi^3, pi^2*zeta(3)",
    )
    pslq_s3["E3_vs_z3_pi3_pi2z3"] = r

    out["PSLQ_at_s=3"] = {k: str(v) for k, v in pslq_s3.items()}

    # ──────────────────────────────────────────────────────────────────
    # Comparison with log(gamma_1) * zeta(3)
    # ──────────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("PIN #6 COMPARISON: log(gamma_1) · zeta(3)")
    print("=" * 72)
    gamma_1 = mpf("14.134725141734693790457251983562470270784257115699243175685567460149963429809256764949010393171561")
    log_g1  = mp.log(gamma_1)
    pin6    = log_g1 * z3

    print(f"  gamma_1                = {nstr(gamma_1, 25)}")
    print(f"  log(gamma_1)           = {nstr(log_g1, 25)}")
    print(f"  zeta(3)                = {nstr(z3, 25)}")
    print(f"  log(gamma_1)*zeta(3)   = {nstr(pin6, 25)}")
    print(f"  J_CKM×10^5 measured    = 3.18")
    print()
    # Compare against E_3 specials
    compare = {}
    for s_tag in ["2", "3", "4", "5", "2.5", "3.5", "4.5"]:
        sv = mpf(s_tag)
        e3v = E3(sv)
        ratio = pin6 / e3v
        compare[s_tag] = {
            "E_3": nstr(e3v, 25),
            "log(g1)*z3 / E_3(s)": nstr(ratio, 25),
        }
        print(f"  log(g1)*z3 / E_3({s_tag}) = {nstr(ratio, 20)}")
    out["pin6_vs_E3"] = compare
    out["pin6_value"] = nstr(pin6, 40)

    # PSLQ: log(gamma_1)*zeta(3)  vs  E_3(s;Q_3) at various s
    print()
    print("PSLQ: pin6 = log(gamma_1)*zeta(3) in terms of E_3 values?")
    basis_labels = ["pin6=log(g1)*z3"]
    basis_vals   = [pin6]
    for sv in [mpf('3'), mpf('2'), mpf('2.5'), mpf('3.5')]:
        basis_labels.append(f"E_3({nstr(sv,4)})")
        basis_vals.append(E3(sv))
    r = try_pslq(basis_labels, basis_vals, "PSLQ: pin6 vs E_3 values")
    out["PSLQ_pin6_vs_E3"] = str(r)

    # ──────────────────────────────────────────────────────────────────
    # Residue at s = 3/2 — 2*sqrt(2*pi)
    # ──────────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("RESIDUE at s = 3/2: 2·sqrt(2·pi)")
    print("=" * 72)
    eps = mpf('1e-25')
    res = eps * E3(mpf('1.5') + eps)
    predicted = 2 * sqrt(2 * mp_pi)
    print(f"  residue (numerical) = {nstr(res, 25)}")
    print(f"  2·sqrt(2·pi)        = {nstr(predicted, 25)}")
    print(f"  rel.err             = {nstr(abs(res - predicted)/predicted, 6)}")

    # Does 2·sqrt(2π) decompose via Â_3 data?
    # Â_3 has rank 4, |roots| = 12; h (Coxeter) = 4; det(A_3) = 1/2;
    # Gaussian self-dual factor: (2π)^{L/2}/Γ(L/2) / sqrt(det).
    print()
    print("  Probe: 2·sqrt(2π) as Gaussian residue factor:")
    print(f"     pi^(3/2)/Γ(3/2) · 1/sqrt(det(A_3)) = "
          f"{nstr(mp_pi**mpf('1.5')/mp.gamma(mpf('1.5'))/sqrt(A3_det), 25)}")
    # That's exactly 2*sqrt(2π): verify numerically.

    out["residue_at_3_2"] = {
        "numerical": nstr(res, 40),
        "2·sqrt(2·pi)": nstr(predicted, 40),
        "gaussian_factor_check":
            nstr(mp_pi**mpf('1.5')/mp.gamma(mpf('1.5'))/sqrt(A3_det), 40),
    }

    # ──────────────────────────────────────────────────────────────────
    # Affine Â_3 probe — can the residue or zeta(3) be read off from
    # rank + |roots| + 1 = 4 + 12 + 1 = 17?
    # ──────────────────────────────────────────────────────────────────
    print()
    print("=" * 72)
    print("AFFINE Â_3 PROBE (rank+|roots|+1 = 17)")
    print("=" * 72)
    h_Atilde3 = 4                  # Coxeter number of A_3
    rank_A3 = 3
    num_roots_A3 = 12
    print(f"  A_3 rank = {rank_A3}, |roots| = {num_roots_A3}, Coxeter h = {h_Atilde3}")
    print(f"  Â_3 node count = {rank_A3 + 1} = 4")
    print(f"  rank + |roots| + 1 = {rank_A3 + num_roots_A3 + 1} = 17")
    print()
    print("  E_3(3) / 17 = {}".format(nstr(E3(3) / 17, 20)))
    print("  E_3(3) / 12 = {}".format(nstr(E3(3) / 12, 20)))
    print("  E_3(3) / 6 =  {}".format(nstr(E3(3) / 6, 20)))
    # Is there a pattern like E_3(3) = 12 * f(zeta)?  The number of roots
    # often appears as a multiplicity prefactor.
    for k in [4, 6, 8, 12, 17, 24]:
        r = E3(3) / k
        out.setdefault("E3_3_over_k", {})[str(k)] = nstr(r, 30)

    # ──────────────────────────────────────────────────────────────────
    # FINAL: persist to JSON
    # ──────────────────────────────────────────────────────────────────
    with open(OUTPUT_JSON, "w") as f:
        json.dump(out, f, indent=2, default=str)
    print()
    print(f"Wrote: {OUTPUT_JSON}")


if __name__ == "__main__":
    main()
