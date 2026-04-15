#!/usr/bin/env python3
"""Additional structural checks for 17 in A_3 invariants."""
import math

# A_3 theta through n=15 (from enumerate_a3.py output)
theta = [1, 12, 6, 24, 12, 24, 8, 48, 6, 36, 24, 24, 24, 72, 0, 48]

# Check 1: r(1) + r(2) - 1 = 12 + 6 - 1 = 17? -> that's just the first shells minus zero
print("r(1)+r(2)-1 =", theta[1]+theta[2]-1)  # 17
print("r(1)+r(2)   =", theta[1]+theta[2])    # 18 = kissing + next shell

# Check 2: non-zero positive-orthant vectors with Q_3 <= small bound
# 1 + 12/2 + 6/2 + ... ?
print("Half of (r(1)+r(2)) =", (theta[1]+theta[2])//2)  # 9

# Check 3: number of orbits of the Weyl group on short shells
# r(1) = 12 = |roots|, r(2) = 6 = six long vectors, r(3)=24 = next shell
# Classical: theta_{A_3}(q) = 1 + 12q + 6q^2 + 24q^3 + ...
# This is standard; OEIS A008384?

# Check 4: 17 = Euler characteristic of some bundle over A_3?
# S_4 acting on something: dim of reflection rep is 3, regular rep dim 24
# 17 = 24 - 7? nope

# Check 5: Heegner-class / Brauer? 17 is prime; first prime with h=4? A_3's fundamental group is Z/4.
# 17 is 1 mod 4, first prime of the form 1+4k > 13... 17. Coincidence.

# Check 6: the number 17 and SU(4) in grand-unified theories
# In Pati-Salam, the fermion content (16 per family = one Weyl spinor of SO(10)) + 1 singlet = 17?
# SO(10) 16-dim spinor of one family + right-handed neutrino? The 16 already contains nu_R.
# But in Pati-Salam: (4,2,1) + (bar{4},1,2) = 8 + 8 = 16 fermions + ???
# Actually the Pati-Salam multiplet is 16 complex = exactly one SM family.
# 17 = 16 (one family) + 1 (PQ/lepton number scalar)? Not standard.

# Check 7: dim of Pati-Salam gauge bosons = 15 + 3 + 3 = 21, not 17

# Check 8: A_3 extended Dynkin diagram has 4 nodes (A_3~ = cycle). h = 4.
# 17 as a 'something mod 4'?

# Check 9: First hit of 17 in the NONZERO partial sum?
import itertools
cum = 0
for n in range(1, 16):
    cum += theta[n]
    if cum == 17 or cum - theta[n] == 17:
        print(f"partial nonzero at n={n}: cum={cum}")
# Partial nonzero sums: 12, 18, 42, 54, 78, 86, 134, 140, 176, 200, 224, 248, 320, 320, 368
# => 17 not hit; jumps 12 -> 18

# Check 10: 1 + theta[1] + something = 17? e.g. v=0 + kissing + ??
# 1 + 12 + 4 = 17? The number 4 = Coxeter/dual Coxeter number h
print("1 + |roots A_3| + h(A_3) =", 1 + 12 + 4)  # 17 !!!
print("1 + |roots A_3| + h*(A_3) =", 1 + 12 + 4)  # 17 (same, h = h* for A_n)
print("1 + |roots A_3| + |Z(SU(4))| =", 1 + 12 + 4)  # 17 (center Z/4, order 4)

# This is the same number three different ways: 1 + 12 + 4 = 17.
# The interpretation ambiguity is semi-fatal unless one is geometrically preferred.

# Check 11: Hirzebruch signature / L-genus of CP^3 = SU(4)/S(U(3)xU(1))?
# chi(CP^3) = 4, signature = 0. Not 17.

# Check 12: Dimension of fundamental reps of SU(4): 1, 4, 6, 4-bar, 10, 15, 20, 20', 20'', 35, 45, 56, 64, ...
# 4 + 6 + 4 + 1 + 1 + 1 = 17? That's trivial + fund + antisym + fund-bar + two singlets.
# Or: 15 (adjoint) + 1 + 1 = 17 (adjoint + two singlets / U(1) factors)
print("Adjoint(SU(4)) + 2 singlets = 15 + 2 =", 17)

# Check 13: look for 17 up to very large N
# Re-run only theta calc
def Q3(a,b,c): return a*a+b*b+c*c+a*b+a*c+b*c
from collections import Counter
NMAX=200
bound=int(math.ceil(math.sqrt(2*NMAX)))+2
C=Counter()
for a in range(-bound,bound+1):
    for b in range(-bound,bound+1):
        for c in range(-bound,bound+1):
            q=Q3(a,b,c)
            if 0<=q<=NMAX:
                C[q]+=1
# any r == 17?
hits = [n for n in range(NMAX+1) if C[n]==17]
print(f"r_Q3(n)==17 for n<={NMAX}: {hits}")
# partial sums
s=0; hits2=[]
for n in range(NMAX+1):
    s += C[n]
    if s == 17: hits2.append(n)
print(f"partial sum (incl 0) == 17 in n<={NMAX}: {hits2}")

# differences
for n in range(1, NMAX+1):
    if C[n] - C[n-1] == 17:
        pass  # no print unless hit
