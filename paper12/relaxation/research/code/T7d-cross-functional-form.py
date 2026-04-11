# T7d — Cross-functional-form γ_n verification (Anchor 3)
# Lead 7d of relaxation strategy §4 Anchor 3.
#
# For n ∈ {1,...,20}, compute γ_n from four independent functional
# forms of the Riemann machinery, then do pairwise comparisons at 50 dps:
#
#   Form A — γ_n from mpmath.zetazero(n).imag                (reference)
#   Form B — γ_n from zeros of completed Ξ(s) on Re(s)=1/2,
#            found by root-bracketing the real-line restriction
#            t ↦ Ξ(1/2 + it)  (which is a real entire function)
#   Form C — γ_n from the log-R̂ operator dictionary of
#            research/167: L_n := ⟨n|log R̂|n⟩ = γ_n·π²/2,
#            so γ_n^(C) := (2/π²) · L_n. Because research/167
#            defines L̂ via R_n = exp(γ_n π²/2), the numerical
#            procedure is L_n ← (π²/2)·zetazero(n).imag followed
#            by the κ rescaling. This is callable but *structurally
#            tautological* relative to Form A.
#   Form D — γ_n from real zeros of Riemann-Siegel Z(t) via
#            mpmath.siegelz + findroot, bracketed around the
#            Form-A estimate.
#
# Tolerance: |Δ| < 10^(-40) is PASS.  mp.dps = 50.

from mpmath import mp, mpf, mpc, pi, gamma, zeta, zetazero, siegelz, findroot

mp.dps = 50

TOL = mpf(10) ** (-40)
N_MAX = 20

# ---------------------------------------------------------------
# Form A — reference zeros via mpmath.zetazero
# ---------------------------------------------------------------
def form_A(n):
    return zetazero(n).imag

# ---------------------------------------------------------------
# Form B — zeros of the completed Riemann Ξ function
#
# Standard definition: ξ(s) = (1/2) s (s-1) π^(-s/2) Γ(s/2) ζ(s).
# On the critical line s = 1/2 + it,
#    ξ(1/2+it) = Ξ(t)
# is a real, entire function of real t whose real zeros are the
# imaginary parts γ_n of the nontrivial zeros of ζ.
#
# Note: the prefactor (1/2)s(s-1)π^(-s/2)Γ(s/2) is nowhere zero
# on the critical line for t > 0, so zeros of Ξ(t) coincide
# exactly with zeros of ζ(1/2+it).
# ---------------------------------------------------------------
def Xi_real(t):
    s = mpf('1/2') + mpc(0, 1) * t
    val = mpf('1') / 2 * s * (s - 1) * pi ** (-s / 2) * gamma(s / 2) * zeta(s)
    # val is real up to rounding; take the real part
    return val.real

def form_B(n, bracket_from_A):
    t0 = bracket_from_A
    # Refine via high-precision root-find. Because Ξ has a simple
    # zero at t = γ_n and we seed with the Form-A value at 50 dps,
    # findroot converges to full precision.
    return findroot(Xi_real, t0, solver='newton')

# ---------------------------------------------------------------
# Form C — log-R̂ operator dictionary (research/167)
#
# L̂ := log R̂,   R_n = exp(γ_n·π²/2),   L_n = γ_n·π²/2.
# The operator is defined spectrally in terms of γ_n, so the
# only numerically callable recipe is:
#   L_n := (π²/2) · (Form-A γ_n)
#   γ_n^(C) := (2/π²) · L_n
# We must execute this recipe literally — not collapse it
# algebraically — to see what numerical noise the rescaling
# introduces at 50 dps.
# ---------------------------------------------------------------
KAPPA = 2 / pi ** 2  # (2/π²)

def form_C(n, gamma_A):
    L_n = (pi ** 2 / 2) * gamma_A
    return KAPPA * L_n

# ---------------------------------------------------------------
# Form D — Riemann-Siegel Z(t)
#
# Z(t) := e^{iθ(t)} ζ(1/2 + it) is real for real t; its real
# zeros are the γ_n. mpmath.siegelz(t) returns Z(t). We refine
# by bracketing around the Form-A seed.
# ---------------------------------------------------------------
def form_D(n, bracket_from_A):
    t0 = bracket_from_A
    return findroot(siegelz, t0, solver='newton')

# ---------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------
gamma_A = [None] * (N_MAX + 1)
gamma_B = [None] * (N_MAX + 1)
gamma_C = [None] * (N_MAX + 1)
gamma_D = [None] * (N_MAX + 1)

print(f"mp.dps = {mp.dps}")
print(f"Tolerance: |Δ| < 10^(-40)")
print()
print("Computing γ_n for n = 1..20 via four functional forms...")
print()

for n in range(1, N_MAX + 1):
    a = form_A(n)
    b = form_B(n, a)
    c = form_C(n, a)
    d = form_D(n, a)
    gamma_A[n] = a
    gamma_B[n] = b
    gamma_C[n] = c
    gamma_D[n] = d

# ---------------------------------------------------------------
# Pairwise comparison matrix
# ---------------------------------------------------------------
PAIRS = [('A', 'B'), ('A', 'C'), ('A', 'D'),
         ('B', 'C'), ('B', 'D'), ('C', 'D')]
G = {'A': gamma_A, 'B': gamma_B, 'C': gamma_C, 'D': gamma_D}

passes = 0
fails = 0
results = []

for n in range(1, N_MAX + 1):
    row = {'n': n, 'A': gamma_A[n]}
    for p1, p2 in PAIRS:
        d = abs(G[p1][n] - G[p2][n])
        ok = d < TOL
        row[f'Δ{p1}{p2}'] = d
        row[f'OK{p1}{p2}'] = ok
        if ok:
            passes += 1
        else:
            fails += 1
    results.append(row)

# ---------------------------------------------------------------
# Print per-n results
# ---------------------------------------------------------------
print(f"{'n':>3}  {'γ_n (Form A, 30 dps shown)':>40}")
print("-" * 70)
for r in results:
    gstr = mp.nstr(r['A'], 30)
    print(f"{r['n']:>3}  {gstr:>40}")
print()

print("Pairwise |Δ| (maxima across n = 1..20):")
for p1, p2 in PAIRS:
    m = max(r[f'Δ{p1}{p2}'] for r in results)
    print(f"  max |Δ_{p1}{p2}| = {mp.nstr(m, 5)}")
print()

print("Pairwise PASS counts (threshold 10^-40):")
for p1, p2 in PAIRS:
    k = sum(1 for r in results if r[f'OK{p1}{p2}'])
    print(f"  {p1}↔{p2}:  {k} / {N_MAX}")
print()

print(f"TOTAL: {passes} / {passes + fails} PASS")

# ---------------------------------------------------------------
# Detailed per-n, per-pair dump for the results table
# ---------------------------------------------------------------
print()
print("=" * 78)
print("Detailed per-n pairwise residuals:")
print("=" * 78)
hdr = f"{'n':>3} " + " ".join(f"{p1+p2:>10}" for p1, p2 in PAIRS)
print(hdr)
for r in results:
    cells = []
    for p1, p2 in PAIRS:
        d = r[f'Δ{p1}{p2}']
        cells.append(f"{mp.nstr(d, 2):>10}")
    print(f"{r['n']:>3} " + " ".join(cells))
