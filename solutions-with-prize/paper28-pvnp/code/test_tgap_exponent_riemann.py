#!/usr/bin/env python3
"""
Search for Riemann-zero formulae reproducing the 3-SAT Taylor gap exponent
alpha ~ 0.43  (range 0.41 -- 0.45).

We scan six formula families over the first 15 non-trivial zeros of zeta(s).
"""

from mpmath import mp, mpf, log, pi, euler, zeta, sqrt, power, e as E
import itertools, json, sys

mp.dps = 60  # 60 decimal digits of working precision

# ── Riemann zeros (imaginary parts) to 30+ digits ──────────────────────
gamma = {
    1:  mpf("14.134725141734693790457251983562"),
    2:  mpf("21.022039638771554992628479593897"),
    3:  mpf("25.010857580145688763213790992563"),
    4:  mpf("30.424876125859513210311897530584"),
    5:  mpf("32.935061587739189690662368964075"),
    6:  mpf("37.586178158825671257217763480705"),
    7:  mpf("40.918719012147495187398126914633"),
    8:  mpf("43.327073280914999519496122165406"),
    9:  mpf("48.005150881167159727942472749427"),
    10: mpf("49.773832477672302181916784678564"),
    11: mpf("52.970321477714460644147296608880"),
    12: mpf("56.446247697063394804367759476706"),
    13: mpf("59.347044002602353079653648674993"),
    14: mpf("60.831778524609809844259901824524"),
    15: mpf("65.112544048081606660875054253183"),
}

N = 15
TARGET = mpf("0.43")
LO, HI = mpf("0.41"), mpf("0.45")      # full search window
TIGHT = mpf("0.01")                      # 1 % of 0.43 ~ 0.0043

# ── Useful constants ───────────────────────────────────────────────────
constants = {
    "1":        mpf(1),
    "1/pi":     1/pi,
    "1/(2*pi)": 1/(2*pi),
    "pi/4":     pi/4,
    "log2":     log(2),
    "1/e":      1/E,
    "2/pi":     2/pi,
    "pi/8":     pi/8,
    "1/log(2*pi)": 1/log(2*pi),
    "1/log(pi)": 1/log(pi),
    "3/4":      mpf("0.75"),
    "sqrt(3)/4": sqrt(3)/4,
    "1/sqrt(2*pi)": 1/sqrt(2*pi),
    "pi^2/6":   pi**2/6,   # zeta(2)
    "1/(pi^2/6)": 6/pi**2,
    "euler":    euler,
    "1/euler":  1/euler,
    "log(2)/pi": log(2)/pi,
    "pi/log(2)": pi/log(2),
    "1/4":      mpf("0.25"),
    "1/3":      mpf(1)/3,
    "1/2":      mpf("0.5"),
    "2":        mpf(2),
    "3":        mpf(3),
    "sqrt(2)":  sqrt(2),
    "1/sqrt(2)":1/sqrt(2),
}

hits = []   # (value, deviation, formula_str)

def record(val, formula):
    dev = float(abs(val - TARGET))
    if LO <= val <= HI:
        hits.append((float(val), dev, formula))

# ═══════════════════════════════════════════════════════════════════════
# Family 1 — simple ratios  gamma_a / gamma_b
# ═══════════════════════════════════════════════════════════════════════
print("Family 1: simple ratios ...")
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        v = gamma[a] / gamma[b]
        record(v, f"gamma_{a}/gamma_{b}")

# ═══════════════════════════════════════════════════════════════════════
# Family 2 — products with constants  gamma_a * c / gamma_b
# ═══════════════════════════════════════════════════════════════════════
print("Family 2: ratios * constant ...")
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        base = gamma[a] / gamma[b]
        for cname, cval in constants.items():
            if cname == "1":
                continue  # already in family 1
            v = base * cval
            record(v, f"gamma_{a}/gamma_{b} * {cname}")

# Also: c * gamma_a  (no denominator)
print("Family 2b: constant * single zero ...")
for a in range(1, N+1):
    for cname, cval in constants.items():
        v = gamma[a] * cval
        record(v, f"gamma_{a} * {cname}")

# ═══════════════════════════════════════════════════════════════════════
# Family 3 — differences  (gamma_a - gamma_b) * c
# ═══════════════════════════════════════════════════════════════════════
print("Family 3: differences * constant ...")
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        diff = gamma[a] - gamma[b]
        if diff <= 0:
            continue
        for cname, cval in constants.items():
            v = diff * cval
            record(v, f"(gamma_{a} - gamma_{b}) * {cname}")

# Also: c / (gamma_a - gamma_b)
print("Family 3b: constant / difference ...")
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        diff = abs(gamma[a] - gamma[b])
        if diff < mpf("0.01"):
            continue
        for cname, cval in constants.items():
            v = cval / diff
            record(v, f"{cname} / |gamma_{a} - gamma_{b}|")

# ═══════════════════════════════════════════════════════════════════════
# Family 4 — powers  gamma_a^p
# ═══════════════════════════════════════════════════════════════════════
print("Family 4: powers ...")
powers = {
    "-2":    -2, "-1":   -1, "-1/2": mpf("-0.5"),
    "-1/3":  mpf("-1")/3, "-1/4": mpf("-0.25"),
    "1/4":   mpf("0.25"), "1/3":  mpf("1")/3,
    "1/2":   mpf("0.5"),
}
for a in range(1, N+1):
    for pname, pval in powers.items():
        v = power(gamma[a], pval)
        record(v, f"gamma_{a}^({pname})")

# powers * constant
for a in range(1, N+1):
    for pname, pval in powers.items():
        base = power(gamma[a], pval)
        for cname, cval in constants.items():
            if cname == "1":
                continue
            v = base * cval
            record(v, f"gamma_{a}^({pname}) * {cname}")

# ═══════════════════════════════════════════════════════════════════════
# Family 5 — log structures
# ═══════════════════════════════════════════════════════════════════════
print("Family 5: log structures ...")
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        v = log(gamma[a]) / log(gamma[b])
        record(v, f"log(gamma_{a})/log(gamma_{b})")

for a in range(1, N+1):
    for cname, cval in constants.items():
        if cval <= 0:
            continue
        v = log(gamma[a]) * cval
        record(v, f"log(gamma_{a}) * {cname}")
        v2 = log(gamma[a]) / cval
        record(v2, f"log(gamma_{a}) / {cname}")
        v3 = cval / log(gamma[a])
        record(v3, f"{cname} / log(gamma_{a})")

# ═══════════════════════════════════════════════════════════════════════
# Family 6 — GUT moduli: 3/4 * f(gammas)
# ═══════════════════════════════════════════════════════════════════════
print("Family 6: (3/4) * expressions ...")
rho2 = mpf("0.75")
for a in range(1, N+1):
    for b in range(1, N+1):
        if a == b:
            continue
        v = rho2 * gamma[a] / gamma[b]
        record(v, f"(3/4)*gamma_{a}/gamma_{b}")
    # 3/4 * 1/log(gamma_a)
    v = rho2 / log(gamma[a])
    record(v, f"(3/4)/log(gamma_{a})")
    # 3/4 * log(gamma_a) / pi  etc
    for cname, cval in constants.items():
        if cname in ("3/4", "1"):
            continue
        v = rho2 * log(gamma[a]) * cval
        record(v, f"(3/4)*log(gamma_{a})*{cname}")

# ═══════════════════════════════════════════════════════════════════════
# Family 7 (bonus) — two-zero combinations
#   gamma_a / (gamma_b + gamma_c),  (gamma_a + gamma_b) / (gamma_c * k)
# ═══════════════════════════════════════════════════════════════════════
print("Family 7: two-zero combos (selected) ...")
for a in range(1, N+1):
    for b in range(1, N+1):
        for c in range(b, N+1):
            if a == b == c:
                continue
            v = gamma[a] / (gamma[b] + gamma[c])
            record(v, f"gamma_{a}/(gamma_{b}+gamma_{c})")

# gamma_a * gamma_b / (gamma_c * pi)  etc — restrict to small indices to keep runtime sane
print("Family 7b: products of two zeros / (zero * const) ...")
for a in range(1, 8):
    for b in range(a, 8):
        for c in range(1, N+1):
            v = gamma[a] * gamma[b] / (gamma[c] * pi)
            record(v, f"gamma_{a}*gamma_{b}/(gamma_{c}*pi)")
            v2 = gamma[a] * gamma[b] / (gamma[c] * 2 * pi)
            record(v2, f"gamma_{a}*gamma_{b}/(gamma_{c}*2*pi)")

# ═══════════════════════════════════════════════════════════════════════
# Family 8 (bonus) — continued-fraction style: 1/(gamma_a - floor) type
# ═══════════════════════════════════════════════════════════════════════
print("Family 8: fractional parts / special combos ...")
# pi / (gamma_a + gamma_b)
for a in range(1, N+1):
    for b in range(a, N+1):
        v = pi / (gamma[a] + gamma[b])
        record(v, f"pi/(gamma_{a}+gamma_{b})")
        v2 = 2*pi / (gamma[a] + gamma[b])
        record(v2, f"2*pi/(gamma_{a}+gamma_{b})")

# ═══════════════════════════════════════════════════════════════════════
# Sort and report
# ═══════════════════════════════════════════════════════════════════════
hits.sort(key=lambda x: x[1])

print(f"\n{'='*80}")
print(f"Total hits in [0.41, 0.45]: {len(hits)}")
print(f"{'='*80}\n")

# Show top 80 by closeness to 0.43
for i, (val, dev, formula) in enumerate(hits[:80]):
    pct = dev / 0.43 * 100
    tag = " ***" if pct < 0.1 else (" **" if pct < 0.5 else (" *" if pct < 1.0 else ""))
    print(f"{i+1:3d}. {val:.12f}  dev={dev:.2e}  ({pct:7.4f}%)  {formula}{tag}")

# ── Write results file ────────────────────────────────────────────────
out_path = "/Users/gsix/quantum-geometry-in-5d-latex/paper28-pvnp/code/results_tgap_exponent.md"
with open(out_path, "w") as f:
    f.write("# TGap exponent alpha ~ 0.43 : Riemann-zero formula search\n\n")
    f.write(f"Target: {float(TARGET)},  search window: [{float(LO)}, {float(HI)}]\n")
    f.write(f"Total matches in window: {len(hits)}\n\n")

    # Top matches (< 0.5 % deviation)
    tight = [h for h in hits if h[1]/0.43 < 0.005]
    f.write(f"## Matches within 0.5% of 0.43 ({len(tight)} found)\n\n")
    f.write("| # | Value | Deviation | % dev | Formula |\n")
    f.write("|---|-------|-----------|-------|---------|\n")
    for i, (val, dev, formula) in enumerate(tight):
        pct = dev / 0.43 * 100
        f.write(f"| {i+1} | {val:.12f} | {dev:.2e} | {pct:.4f}% | `{formula}` |\n")

    f.write(f"\n## Matches within 1% of 0.43\n\n")
    one_pct = [h for h in hits if h[1]/0.43 < 0.01]
    f.write("| # | Value | Deviation | % dev | Formula |\n")
    f.write("|---|-------|-----------|-------|---------|\n")
    for i, (val, dev, formula) in enumerate(one_pct):
        pct = dev / 0.43 * 100
        f.write(f"| {i+1} | {val:.12f} | {dev:.2e} | {pct:.4f}% | `{formula}` |\n")

    f.write(f"\n## All matches in [0.41, 0.45] — top 80 by precision\n\n")
    f.write("| # | Value | Deviation | % dev | Formula |\n")
    f.write("|---|-------|-----------|-------|---------|\n")
    for i, (val, dev, formula) in enumerate(hits[:80]):
        pct = dev / 0.43 * 100
        f.write(f"| {i+1} | {val:.12f} | {dev:.2e} | {pct:.4f}% | `{formula}` |\n")

    f.write("\n---\n*Generated by test_tgap_exponent_riemann.py*\n")

print(f"\nResults written to {out_path}")
