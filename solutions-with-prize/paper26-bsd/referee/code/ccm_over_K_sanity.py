"""Sanity checks for the K = Q(i) CCM port (Route 2).

Two checks:
  1. Enumerate the first Gaussian prime ideals by norm (sub-task 1.1).
  2. Compute the first non-trivial zeros of ζ_K on Re(s) = 1/2 via
     Newton iteration — these are the ground-truth targets a future
     K-CCM operator spec(D_N^K) should approximate.

For K = Q(i):
    ζ_K(s) = ζ(s) · L(s, χ_{-4})
    non-trivial zeros at s = 1/2 + iγ where γ is a zero of
    ζ(1/2 + it) OR a zero of L(1/2 + it, χ_{-4}).
"""

from mpmath import mp, mpf, mpc, zeta, dirichlet, findroot, fabs
from sympy import isprime

mp.dps = 30


# -- 1. Gaussian prime enumeration ---------------------------------------
def gaussian_primes_by_norm(max_norm):
    """List (a, b, N) for Gaussian primes with norm ≤ max_norm.

    Convention: representatives with a ≥ 0 and (a > 0 or b > 0).
    For split primes p ≡ 1 mod 4, both (a+bi) and (a-bi) are listed.
    For inert primes p ≡ 3 mod 4, (p, 0) is listed once (norm p²).
    For the ramified prime 2, (1+i) is listed once (norm 2).
    """
    primes = []
    for p in range(2, max_norm + 1):
        if not isprime(p):
            continue
        if p == 2:
            primes.append((1, 1, 2))
        elif p % 4 == 1:
            for a in range(1, int(p**0.5) + 1):
                b2 = p - a * a
                if b2 > 0:
                    b = int(round(b2**0.5))
                    if b * b == b2:
                        # Split: two primes of norm p
                        primes.append((a, b, p))
                        primes.append((a, -b, p))
                        break
        else:  # p ≡ 3 mod 4
            if p * p <= max_norm:
                primes.append((p, 0, p * p))
    primes.sort(key=lambda t: (t[2], t[0], t[1]))
    return primes


print("=" * 66)
print("Sub-task 1.1: Gaussian prime enumeration (first few by norm)")
print("=" * 66)
print()
print(f"  {'rank':>4}  {'prime':>15}  {'norm':>6}  {'type':>10}")
print("  " + "-" * 43)
primes = gaussian_primes_by_norm(100)
for i, (a, b, N) in enumerate(primes[:20], 1):
    if a == 1 and b == 1:
        typ = "ramified"
    elif b == 0:
        typ = "inert"
    else:
        typ = "split"
    sign = "+" if b >= 0 else "-"
    print(f"  {i:>4}  ({a:>2}{sign}{abs(b):>2}i){'':>5}  {N:>6}  {typ:>10}")

print()
print(f"  Total Gaussian primes with norm ≤ 100: {len(primes)}")
print()


# -- 2. Non-trivial zeros of ζ_K ----------------------------------------
def zeta_K(s):
    return zeta(s) * dirichlet(s, [0, 1, 0, -1])


# For ζ on Re(s)=1/2: first 6 imaginary parts are well-known
gamma_zeta = [
    mpf("14.134725141734693790457251983562"),
    mpf("21.022039638771554992628479593897"),
    mpf("25.010857580145688763213790992563"),
    mpf("30.424876125859513210311897530584"),
    mpf("32.935061587739189690662368964074"),
    mpf("37.586178158825671257217763480705"),
]

# For L(s, χ_{-4}) on Re(s)=1/2: first few imaginary parts
# (these can be looked up in LMFDB; we'll rediscover via findroot)
print("=" * 66)
print("Sub-task 1.5 target: first non-trivial zeros of ζ_K")
print("=" * 66)
print()
print("First few zeros of ζ(1/2+it) (well-known):")
for i, g in enumerate(gamma_zeta, 1):
    print(f"  γ_{i:>2}^ζ = {float(g):>25.15f}")
print()

print("Finding zeros of L(1/2+it, χ_{-4}) via Newton iteration:")
# Starting points from LMFDB approximate values
start_points_L = [mpf("6.0"), mpf("10.2"), mpf("12.9"), mpf("16.3"),
                  mpf("18.8"), mpf("21.5"), mpf("24.0"), mpf("26.0")]
zeros_L = []
for t0 in start_points_L:
    try:
        def f(t):
            return dirichlet(mpc(mpf("0.5"), t), [0, 1, 0, -1])
        root = findroot(f, t0)
        gamma_val = root.real if hasattr(root, 'real') else root
        if fabs(gamma_val) > mpf("0.01") and not any(
            fabs(gamma_val - z) < mpf("0.001") for z in zeros_L
        ):
            zeros_L.append(gamma_val)
    except Exception as e:
        pass

zeros_L.sort()
for i, g in enumerate(zeros_L[:8], 1):
    print(f"  γ_{i:>2}^L = {float(g):>25.15f}")
print()

# Merged list
print("Merged: first non-trivial zeros of ζ_K by magnitude:")
merged = sorted(gamma_zeta[:6] + zeros_L[:6])
for i, g in enumerate(merged, 1):
    source = "ζ" if any(fabs(g - z) < mpf("0.001") for z in gamma_zeta) else "L(χ_{-4})"
    print(f"  γ_{i:>2}^K = {float(g):>25.15f}  (from {source})")
print()

# Spot-check: ζ_K(1/2 + i·γ) should be ≈ 0 at every zero
print("Spot-check: |ζ_K(1/2 + iγ)| should vanish at each γ above")
for i, g in enumerate(merged[:6], 1):
    val = zeta_K(mpc(mpf("0.5"), g))
    print(f"  γ_{i}: |ζ_K(1/2 + i·{float(g):.6f})| = {float(fabs(val)):.2e}")
print()

print("These are the targets for spec(D_N^K) in a future numerical")
print("verification of Route 2 Phase I.")
