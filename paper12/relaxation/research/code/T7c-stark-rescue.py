#!/usr/bin/env python3
"""
T7c -- Stark rescue verification for Anchor 5 (Lead 7c).

Tests six rescue candidates for the identification
    arg( <some L-function-side object> ) / (2*pi) == 1/k  mod Z
on the three CBB bridges:
    (p, N, k) in { (5, 13, 3), (3, 13, 4), (7, 19, 6) }.

Candidates (from research/267 section 6):
  C1a  arg( exp(-L'(0,chi)) / tau(chi) )      / (2 pi)
  C1b  arg( exp(-L'(0,chi)) / (tau(chi)/sqrtN) ) / (2 pi)
  C1c  arg( L'(0,chi) / tau(chi) )            / (2 pi)
  C2p  arg( exp(-L'(0,chi)) * W(chi)       )  / (2 pi)
  C2m  arg( exp(-L'(0,chi)) * W(chi)^(-1)  )  / (2 pi)
  C3a  Im( log(eps_chi) / (2 pi i) )              ( == arg(eps)/(2 pi) mod 1 )
  C3b  Im( log(eps_chi) / (2 pi i * log_N(genus)) )
  C4   arg( L'(0,chi) / (tau(chi) * W(chi)) )  / (2 pi)
  C5   arg( theta(chi) )                      / (2 pi)    [Stickelberger]
  C6   ( arg(eps_chi)/(2 pi) ) * ( k / f(chi) )   mod 1

Per the task specification:
  - C1 has three sub-candidates (raw, sqrtN-normalized, no exp).
  - C2 has two sub-candidates (W^+1 and W^-1).
  - C3 has two sub-candidates.
So the test count is 6 logical candidates but 10 numerical tests per bridge.
We report all of them; the pass/fail verdict per candidate uses "any sub-test
passes" semantics.

Precision: mp.dps = 50.
Tolerance: |value - 1/k|  <  1e-40   (strict; near-misses logged as FAIL).
"""

from mpmath import mp, mpf, mpc, mpmathify, pi, exp, log, sqrt, zeta, arg, re, im
from fractions import Fraction

mp.dps = 50
TOL = mpf('1e-40')

# -------------------------------------------------------------------------
# Dirichlet character construction
# -------------------------------------------------------------------------
def primitive_root(N):
    """Smallest primitive root of prime N."""
    from sympy import factorint, totient
    phi = int(totient(N))
    fac = list(factorint(phi).keys())
    for g in range(2, N):
        if all(pow(g, phi // q, N) != 1 for q in fac):
            return g
    raise RuntimeError(f"no primitive root mod {N}")

def char_of_order_k(N, k):
    """
    Return chi : (Z/NZ)* -> C of order exactly k, defined by
      chi(g^j) = zeta_k^j   where g = primitive_root(N).
    N prime, k | phi(N) = N-1.
    Returns a dict {a : chi(a)} for a=1..N-1 (and chi(0)=0).
    """
    assert (N - 1) % k == 0, f"k={k} does not divide phi({N})={N-1}"
    g = primitive_root(N)
    # discrete log base g mod N
    dlog = {}
    x = 1
    for j in range(N - 1):
        dlog[x] = j
        x = (x * g) % N
    two_pi_i = mpc(0, 1) * 2 * pi
    zeta_k = exp(two_pi_i / k)
    chi = {0: mpc(0)}
    for a in range(1, N):
        chi[a] = zeta_k ** dlog[a]
    return chi, g

# -------------------------------------------------------------------------
# L(s, chi) and L'(0, chi)
# -------------------------------------------------------------------------
def L_value(s, chi, N):
    """
    L(s, chi) = N^{-s} sum_{a=1}^{N-1} chi(a) * Hurwitz_zeta(s, a/N).
    mpmath.zeta(s, a) gives Hurwitz zeta zeta(s, a).
    """
    total = mpc(0)
    for a in range(1, N):
        total += chi[a] * zeta(s, mpf(a) / N)
    return N ** (-s) * total

def L_prime_at_0(chi, N):
    """Central difference L'(0, chi) with h = 1e-25 at 50 dps."""
    h = mpf('1e-25')
    return (L_value(h, chi, N) - L_value(-h, chi, N)) / (2 * h)

# -------------------------------------------------------------------------
# Gauss sum, root number, Stickelberger element
# -------------------------------------------------------------------------
def gauss_sum(chi, N):
    """tau(chi) = sum_{a mod N} chi(a) * exp(2 pi i a / N)."""
    two_pi_i_over_N = mpc(0, 1) * 2 * pi / N
    s = mpc(0)
    for a in range(1, N):
        s += chi[a] * exp(two_pi_i_over_N * a)
    return s

def chi_at_minus1(chi, N):
    return chi[(N - 1) % N]  # chi(-1)

def root_number(chi, N):
    """
    W(chi) = tau(chi) / ( i^a * sqrt(N) ),  a = (1 - chi(-1))/2.
    For chi(-1) = +1 (even): a = 0; for chi(-1) = -1 (odd): a = 1.
    For primitive chi mod prime N, |W(chi)| = 1.
    """
    cm1 = chi_at_minus1(chi, N)
    # cm1 is +1 or -1 (as mpc); decide
    if abs(cm1 - 1) < mpf('1e-30'):
        a = 0
    elif abs(cm1 + 1) < mpf('1e-30'):
        a = 1
    else:
        raise RuntimeError(f"chi(-1) is neither 1 nor -1 (got {cm1})")
    ia = mpc(0, 1) ** a
    return gauss_sum(chi, N) / (ia * sqrt(mpf(N)))

def stickelberger(chi, N):
    """theta(chi) = sum_{a=1}^{N-1} chi(a) * (a/N)."""
    s = mpc(0)
    for a in range(1, N):
        s += chi[a] * (mpf(a) / N)
    return s

# -------------------------------------------------------------------------
# Phase helpers
# -------------------------------------------------------------------------
def phase_mod1(z):
    """arg(z) / (2 pi) reduced to [0, 1)."""
    p = arg(z) / (2 * pi)
    return p - mp.floor(p)

def check(value, k):
    target = mpf(1) / k
    delta = abs(value - target)
    return delta, delta < TOL

# -------------------------------------------------------------------------
# Per-bridge rescue tests
# -------------------------------------------------------------------------
def run_bridge(p, N, k, label):
    print(f"\n========== {label}  (p,N,k) = ({p},{N},{k}) ==========")
    chi, g = char_of_order_k(N, k)
    print(f"  primitive root g = {g}, chi of order {k} via chi(g^j) = zeta_{k}^j")

    Lp0 = L_prime_at_0(chi, N)
    eps = exp(-Lp0)
    tau = gauss_sum(chi, N)
    tau_norm = tau / sqrt(mpf(N))
    W = root_number(chi, N)
    theta = stickelberger(chi, N)
    cm1 = chi_at_minus1(chi, N)

    print(f"  L'(0,chi)     = {mp.nstr(Lp0, 20)}")
    print(f"  eps = exp(-L') = {mp.nstr(eps, 20)}")
    print(f"  tau(chi)      = {mp.nstr(tau, 20)}      |tau| = {mp.nstr(abs(tau),15)}")
    print(f"  W(chi)        = {mp.nstr(W, 20)}         |W|   = {mp.nstr(abs(W),15)}")
    print(f"  theta(chi)    = {mp.nstr(theta, 20)}")
    print(f"  chi(-1)       = {mp.nstr(cm1, 10)}")

    target = mpf(1) / k
    tests = []

    # Candidate 1a: arg(eps / tau) / (2 pi)
    v = phase_mod1(eps / tau)
    tests.append(('C1a  arg(eps/tau)/(2pi)', v))

    # Candidate 1b: arg(eps / (tau/sqrtN)) / (2 pi)
    v = phase_mod1(eps / tau_norm)
    tests.append(('C1b  arg(eps/(tau/sqrtN))/(2pi)', v))

    # Candidate 1c: arg(L'(0,chi) / tau) / (2 pi)
    v = phase_mod1(Lp0 / tau)
    tests.append(('C1c  arg(Lprime/tau)/(2pi)', v))

    # Candidate 2+: arg(eps * W) / (2 pi)
    v = phase_mod1(eps * W)
    tests.append(('C2+  arg(eps * W)/(2pi)', v))

    # Candidate 2-: arg(eps / W) / (2 pi)
    v = phase_mod1(eps / W)
    tests.append(('C2-  arg(eps / W)/(2pi)', v))

    # Candidate 3a: Im(log(eps)/(2 pi i))  (=arg(eps)/(2 pi) mod 1, but as real Im)
    lg = log(eps)  # = -L'(0,chi)
    val3a = im(lg / (2 * pi * mpc(0, 1)))
    val3a_mod = val3a - mp.floor(val3a)
    tests.append(('C3a  Im(log eps / (2 pi i)) mod 1', val3a_mod))

    # Candidate 3b: Im(log(eps)/(2 pi i * log_N(genus)))
    # "log_N(genus)" is parsed as log base N of genus of the cyclotomic field.
    # For Q(zeta_N), N prime, the genus (in the sense of "genus field" / class
    # field genus) is 1 for the prime cyclotomic case (class number of the genus
    # field equals 1 here). Paper 267 does not pin down the intended "genus";
    # to be honest we test two readings:
    #   (i)  "genus = N" (i.e. conductor), giving log_N(N) = 1 and reducing to C3a.
    #   (ii) "genus = N-1" (degree of cyclotomic extension), giving log_N(N-1).
    # We report (ii) as the non-trivial reading.
    genus = mpf(N - 1)
    denom = 2 * pi * mpc(0, 1) * (log(genus) / log(mpf(N)))
    val3b = im(lg / denom)
    val3b_mod = val3b - mp.floor(val3b)
    tests.append(('C3b  Im(log eps / (2 pi i * log_N(N-1))) mod 1', val3b_mod))

    # Candidate 4: arg(L' / (tau * W)) / (2 pi)
    v = phase_mod1(Lp0 / (tau * W))
    tests.append(('C4   arg(Lprime/(tau*W))/(2pi)', v))

    # Candidate 5: arg(theta(chi))/(2 pi)  -- Stickelberger
    v = phase_mod1(theta)
    tests.append(('C5   arg(theta(chi))/(2pi)', v))

    # Candidate 6: (arg(eps)/(2 pi)) * (k/f(chi))
    # f(chi) = conductor. For primitive chi mod prime N, f(chi) = N.
    f = mpf(N)
    base = phase_mod1(eps)
    scaled = base * (mpf(k) / f)
    v = scaled - mp.floor(scaled)
    tests.append(('C6   (arg(eps)/(2pi)) * (k/f) mod 1', v))

    results = []
    print(f"\n  Target: 1/k = {mp.nstr(target, 45)}")
    print(f"  Tolerance: {TOL}")
    print()
    for name, val in tests:
        delta = abs(val - target)
        passed = (delta < TOL)
        tag = "PASS" if passed else "FAIL"
        print(f"    {tag}  {name:44s} = {mp.nstr(val, 40)}   d={mp.nstr(delta, 6)}")
        results.append((name, val, target, delta, passed))
    return results


if __name__ == '__main__':
    print(f"mpmath dps = {mp.dps}")
    print(f"tolerance  = {TOL}")
    bridges = [
        (5, 13, 3, "Bridge 1  (5,13) k=3  three generations"),
        (3, 13, 4, "Bridge 2  (3,13) k=4  Pati-Salam SU(4)_c"),
        (7, 19, 6, "Bridge 3  (7,19) k=6  CKM six quark flavours"),
    ]
    all_results = {}
    for (p, N, k, label) in bridges:
        all_results[label] = run_bridge(p, N, k, label)

    # Final summary
    print("\n========== FINAL SUMMARY ==========")
    total = 0
    passed = 0
    for label, rows in all_results.items():
        print(f"\n{label}")
        for (name, val, target, delta, ok) in rows:
            total += 1
            if ok:
                passed += 1
            tag = "PASS" if ok else "FAIL"
            print(f"  {tag}  {name:44s}  d = {mp.nstr(delta, 6)}")
    print(f"\nTotals: {passed}/{total} tests PASS at tolerance {TOL}")
