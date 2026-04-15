"""
Find zeros of L(s, chi_{-4}) on the critical line.
chi_{-4} is an odd character, so L(s, chi_{-4}) has the "odd" functional equation.
"""
from mpmath import mp, mpf, dirichlet, nstr, re, im, findroot, fabs, mpc

mp.dps = 30

def L_chi4(s):
    return dirichlet(s, [0, 1, 0, -1])

# chi_{-4} is an ODD character of conductor 4.
# The completed L-function has a zero at s=0 (trivial zero from Gamma).
# Non-trivial zeros are symmetric about Re(s)=1/2 and Im(s)=0.

# Method: evaluate |L(1/2 + it)| on a fine grid and look for minima
print("Scanning |L(1/2 + it, chi_{-4})| for t in [0, 40]...")
print(f"{'t':>10}  {'|L|':>15}")

dt = mpf('0.05')
t_vals = []
abs_vals = []
for k in range(1, 801):
    t = k * dt
    val = L_chi4(mpf('0.5') + 1j * t)
    av = fabs(val)
    t_vals.append(t)
    abs_vals.append(float(av))

# Find local minima
zeros = []
for i in range(1, len(abs_vals) - 1):
    if abs_vals[i] < abs_vals[i-1] and abs_vals[i] < abs_vals[i+1] and abs_vals[i] < 0.5:
        t_approx = t_vals[i]
        try:
            # Refine: find zero of L
            t_zero = findroot(lambda t: L_chi4(mpf('0.5') + 1j*t), t_approx)
            val_zero = L_chi4(mpf('0.5') + 1j * t_zero)
            if fabs(val_zero) < mpf('1e-15') and re(t_zero) > 0.5:
                # Check for duplicates
                is_dup = False
                for z in zeros:
                    if fabs(z - t_zero) < 0.01:
                        is_dup = True
                        break
                if not is_dup:
                    zeros.append(t_zero)
        except:
            pass

zeros.sort(key=lambda z: re(z))
print(f"\nFound {len(zeros)} zeros of L(s, chi_{{-4}}) on Re(s) = 1/2:")
print(f"{'n':>3}  {'gamma_n':>25}  {'|L(1/2+i*gamma)|':>20}")
for i, gamma in enumerate(zeros[:15]):
    val = L_chi4(mpf('0.5') + 1j * gamma)
    print(f"{i+1:3d}  {nstr(re(gamma), 20):>25}  {nstr(fabs(val), 8):>20}")

# Also check that these are NOT zeros at other sigma values
print("\n--- Verify zeros are ON the critical line ---")
for i, gamma in enumerate(zeros[:5]):
    for sigma in [mpf('0.3'), mpf('0.5'), mpf('0.7'), mpf('1.0')]:
        val = L_chi4(sigma + 1j * gamma)
        print(f"  Zero {i+1}: L({nstr(sigma,2)} + i*{nstr(re(gamma),8)}) = "
              f"{nstr(fabs(val), 6)}")
    print()
