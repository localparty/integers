"""Analyze the Part A.5 decay data from lead-5-output.log.

The decay |γ_1 - eig_1(λ)| vs λ² is not actually linear in log(err) vs λ².
Check the full fit and sub-range fits.
"""
import math

pts = [
    (2.0, 4.0, 1.648e-09),
    (3.0, 9.0, 2.198e-33),
    (4.0, 16.0, 1.784e-49),
    (5.0, 25.0, 3.600e-58),
    (6.0, 36.0, 2.556e-64),
    (7.0, 49.0, 6.907e-69),
    (8.0, 64.0, 2.065e-72),
]

def lsq(pts, key_x=lambda p: p[1], key_log10=lambda p: math.log10(p[2])):
    xs = [key_x(p) for p in pts]
    ys = [key_log10(p) for p in pts]
    n = len(xs)
    mx = sum(xs)/n
    my = sum(ys)/n
    num = sum((xs[i]-mx)*(ys[i]-my) for i in range(n))
    den = sum((xs[i]-mx)**2 for i in range(n))
    slope = num/den
    intercept = my - slope*mx
    resid = [ys[i] - (slope*xs[i] + intercept) for i in range(n)]
    ssr = sum(r*r for r in resid)
    return slope, intercept, ssr, resid

print("Decay data (|γ_1 - eig_1(λ)|, log₁₀):")
for lam, lamsq, err in pts:
    print(f"  λ={lam}  λ²={lamsq}   err={err:.3e}   log₁₀={math.log10(err):7.3f}")

print("\n=== log₁₀|err| vs λ² linear fits ===\n")
print("FULL RANGE (λ²∈[4,64]):")
s, b, ssr, r = lsq(pts)
print(f"  slope = {s:.4f}  intercept = {b:.4f}  SSR = {ssr:.4f}")
print(f"  residuals: {[f'{x:.2f}' for x in r]}")

print("\nL1-range (λ²∈[4,16]):")
s, b, ssr, r = lsq(pts[:3])
print(f"  slope = {s:.4f}  intercept = {b:.4f}  SSR = {ssr:.4f}")
print(f"  residuals: {[f'{x:.2f}' for x in r]}")

print("\n"f"Middle range (λ²∈[9,25]):")
s, b, ssr, r = lsq(pts[1:4])
print(f"  slope = {s:.4f}  intercept = {b:.4f}  SSR = {ssr:.4f}")

print("\nHigh range (λ²∈[25,64]):")
s, b, ssr, r = lsq(pts[3:])
print(f"  slope = {s:.4f}  intercept = {b:.4f}  SSR = {ssr:.4f}")

# Check if log|err| vs λ (not λ²) works better
print("\n=== log₁₀|err| vs λ (not λ²) linear fits ===\n")
print("FULL RANGE (λ∈[2,8]):")
s, b, ssr, r = lsq(pts, key_x=lambda p: p[0])
print(f"  slope = {s:.4f}  intercept = {b:.4f}  SSR = {ssr:.4f}")

# log|err| vs λ log λ?
print("\n=== log₁₀|err| vs λ·log(λ) linear fits ===\n")
s, b, ssr, r = lsq(pts, key_x=lambda p: p[0]*math.log(p[0]))
print(f"  slope = {s:.4f}  intercept = {b:.4f}  SSR = {ssr:.4f}")
