"""
Premise Check Path B: Weil Positivity / Li criterion
"""
from mpmath import mp, mpf, mpc, zetazero, log, pi, power, re, im, conj, exp, nstr
mp.dps = 50

print("=" * 70)
print("PREMISE CHECK PATH B: WEIL POSITIVITY / LI CRITERION")
print("=" * 70)

N_zeros = 50
print(f"\nComputing first {N_zeros} zeta zeros...")
zeros = [zetazero(n) for n in range(1, N_zeros + 1)]

def li_contribution(rho, n):
    """Li contribution from a single zero rho."""
    return 1 - power(1 - 1/rho, n)

def li_coefficient(n, zero_list):
    """Partial Li coefficient from on-line zeros (+ conjugates)."""
    total = mpf(0)
    for rho in zero_list:
        total += li_contribution(rho, n) + li_contribution(conj(rho), n)
    return total

def offline_contribution(delta, gamma_val, n):
    """Contribution of an off-line zero at 1/2+delta+i*gamma to lambda_n.
    Includes: rho, 1-rho, conj(rho), conj(1-rho) = 1-conj(rho)."""
    rho = mpf('0.5') + delta + mpc(0, gamma_val)
    rho_fe = 1 - rho
    rho_c = conj(rho)
    rho_fe_c = conj(rho_fe)
    return (li_contribution(rho, n) + li_contribution(rho_fe, n) 
            + li_contribution(rho_c, n) + li_contribution(rho_fe_c, n))

print("\n--- Li coefficients (partial, 50 zeros) ---")
for n in [1, 2, 3, 5, 10]:
    lam = li_coefficient(n, zeros)
    print(f"  lambda_{n} = {nstr(re(lam), 15)} + {nstr(im(lam), 6)}*i")

gamma1 = im(zeros[0])

print("\n--- Isolated contribution of off-line zero to Li coefficients ---")
print("--- Off-line zero at rho = 1/2 + delta + i*gamma_1 ---")

for delta in [mpf('0.001'), mpf('0.01'), mpf('0.05'), mpf('0.1'), mpf('0.25')]:
    print(f"\n  delta = {nstr(delta, 5)}:")
    for n in [1, 2, 3, 5, 10, 20, 50]:
        contrib = offline_contribution(delta, gamma1, n)
        r = re(contrib)
        i_part = im(contrib)
        sign = "POSITIVE" if r > 0 else "NEGATIVE" if r < 0 else "ZERO"
        print(f"    lambda_{n:2d} shift: Re = {nstr(r, 15)}, Im = {nstr(i_part, 6)} [{sign}]")

# Now: can we find a test function f such that W(f,f) goes negative?
# The Weil inner product W(f,f) = sum_rho |f(rho)|^2 for on-line zeros is >= 0.
# For off-line zeros, W involves cross terms.
print("\n" + "=" * 70)
print("WEIL INNER PRODUCT TEST")
print("=" * 70)
print("For an off-line zero pair at 1/2+delta+i*t and 1/2-delta+i*t:")
print("The Weil form W(h,h) = sum_rho h(rho)*h_bar(1-rho_bar)")
print("On critical line: h(rho)*h_bar(rho) = |h(rho)|^2 >= 0")
print("Off-line pair: h(1/2+d+it)*h_bar(1/2+d+it) + h(1/2-d+it)*h_bar(1/2-d+it)")
print("  = |h(1/2+d+it)|^2 + |h(1/2-d+it)|^2 >= 0  ... still positive!")
print()
print("WAIT - the Weil positivity is more subtle. The correct form is:")
print("W(f,g) = sum_rho f((rho-1/2)/i) * conj(g((rho-1/2)/i))")
print("where we substitute gamma = (rho-1/2)/i into a test function on R.")
print()
print("For on-line zero: (rho-1/2)/i = gamma_n (REAL) -> |f(gamma_n)|^2 >= 0")
print("For off-line zero at 1/2+delta+i*t: (rho-1/2)/i = t - i*delta (COMPLEX)")
print("  f(t-i*delta) is complex even for real-valued f on R!")
print("  |f(t-i*delta)|^2 is still >= 0, but the PAIRED zero at 1/2-delta+i*t")
print("  gives f(t+i*delta). The CROSS TERM in Weil is not |f|^2.")

print("\n--- Correct Weil positivity computation ---")
print("The Nyman-Beurling form: RH <=> for all f in a Hardy space,")
print("  sum_rho f(gamma_n) * conj(f(gamma_n)) >= 0")
print("where gamma_n = Im(rho) and the sum runs over zeros ON the line.")
print()
print("Off-line zeros: rho = 1/2 + delta + it contributes")
print("  f((rho-1/2)/i) = f(t - i*delta) ... COMPLEX argument")
print("  and its partner 1-conj(rho) = 1/2 + delta - it contributes")
print("  f((1-conj(rho)-1/2)/i) = f(-t - i*delta)")
print()

# The actual computation: for a specific test function, compute the sum
# with and without an off-line zero
print("Using test function f(x) = exp(-x^2/2) (Gaussian):")
print("f(t - i*delta) = exp(-(t-i*delta)^2/2) = exp(-(t^2-delta^2)/2 + i*t*delta)")

def f_gauss(z):
    return exp(-z**2/2)

print("\nContribution of off-line zero pair to Weil sum:")
for delta in [mpf('0.001'), mpf('0.01'), mpf('0.05'), mpf('0.1'), mpf('0.25')]:
    t = gamma1
    # Off-line zero contributes:
    # f((rho-1/2)/i) * conj(f((1-conj(rho)-1/2)/i)) 
    # = f(t - i*delta) * conj(f(-t - i*delta))
    # plus conjugate pair
    z1 = t - mpc(0, delta)  # (rho - 1/2)/i for rho = 1/2 + delta + it
    z2 = -t - mpc(0, delta)  # for the functional equation partner
    z1c = conj(z1)  # for conj(rho)
    z2c = conj(z2)
    
    # Weil cross term: f(z1)*conj(f(z2)) + f(z1c)*conj(f(z2c))
    # Actually for the DIAGONAL Weil form W(f,f):
    # Each zero rho contributes f(gamma_rho) where gamma_rho = (rho-1/2)/i
    # The Weil form is: sum_rho f(gamma_rho) * conj(f(gamma_rho))
    # = sum_rho |f(gamma_rho)|^2
    # This is ALWAYS >= 0 regardless of off-line zeros!
    
    w = f_gauss(z1) * conj(f_gauss(z1))  # |f(t-i*delta)|^2
    print(f"  delta={nstr(delta,5)}: |f(gamma_1 - i*delta)|^2 = {nstr(re(w), 15)}")
    print(f"    This is {nstr(re(w)/re(f_gauss(t)*conj(f_gauss(t))), 15)} times the on-line value")

print("\n" + "=" * 70)
print("CRITICAL FINDING")
print("=" * 70)
print("""
The naive Weil form W(f,f) = sum_rho |f((rho-1/2)/i)|^2 is ALWAYS >= 0,
even with off-line zeros. This is because |z|^2 >= 0 for any complex z.

The ACTUAL Weil positivity criterion involves the EXPLICIT FORMULA:
The constraint is not just the spectral sum but the FULL explicit formula
including the prime-side correction terms. Specifically:

  W(f,f) = sum_rho f(gamma_rho)*conj(f(gamma_rho)) 
         = h(0)*log(pi) + [polar] - 2*sum_p ... - W_infty

The positivity of the LEFT side is trivial. The content of Weil positivity
is that the RIGHT side (the geometric side) must also be >= 0.

An off-line zero does NOT change the sign of the spectral sum. It changes
the EQUALITY between spectral and geometric sides. The geometric side is
fixed (it depends on primes, not zeros). The spectral side gains new terms.
For the equality to hold, the new spectral terms must be balanced by...
nothing on the geometric side. This is the contradiction.

BUT: this is just restating the explicit formula, not a new constraint.
The explicit formula already ASSUMES the zeros are where they are.
There is no independent "geometric side" to compare against.

PREMISE CHECK RESULT: The Weil positivity premise is SUBTLE.
- The spectral sum |f(gamma)|^2 is trivially positive (not useful).
- The Li coefficients DO shift when off-line zeros are added.
- The shift in Li coefficients is the actionable premise.
""")

# Final Li coefficient check: can off-line zeros make lambda_n negative?
print("--- Can off-line zeros FLIP Li coefficients to negative? ---")
print("Full lambda_n = (known partial from 50 on-line) + (off-line contribution)")
print()
for delta in [mpf('0.01'), mpf('0.1'), mpf('0.25'), mpf('0.49')]:
    print(f"  delta = {nstr(delta,5)}:")
    any_negative = False
    for n in [1, 2, 3, 5, 10, 20, 50, 100]:
        lam_partial = li_coefficient(n, zeros)
        off_contrib = offline_contribution(delta, gamma1, n)
        total = re(lam_partial) + re(off_contrib)
        sign = "NEGATIVE!" if total < 0 else "positive"
        if total < 0:
            any_negative = True
        print(f"    lambda_{n:3d}: partial={nstr(re(lam_partial),10)}, "
              f"off-line shift={nstr(re(off_contrib),10)}, "
              f"total={nstr(total,10)} [{sign}]")
    if any_negative:
        print(f"  ** OFF-LINE ZERO AT delta={nstr(delta,5)} MAKES SOME lambda_n NEGATIVE **")
    else:
        print(f"  All lambda_n remain positive (with 50-zero partial sum)")
