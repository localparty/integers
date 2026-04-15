# Research 47 -- The Continuous Cartwright Argument

*Date: 2026-04-09. Status: DEVELOPMENT + ADVERSARIAL*

---

## 1. The argument (Strategy 25, Steps 1-6)

**Step 1.** QW_L on L^2([L^-1, L]) has eigenfunctions phi_k: smooth, supported on [L^-1, L], analytic.
**Step 2.** g_k(xi) = int phi_k(x) cos(x xi) dx. Compactly supported => entire of type sigma = L (Paley-Wiener).
**Step 3.** g_k not identically 0 (claimed: cosine transform injective on L^2([L^-1, L])).
**Step 4.** {log p} has infinite upper density (PNT).
**Step 5.** Cartwright-Levin: g_k vanishes at finitely many {log p}. Bound: n(T) <= (sigma/pi)T + C.
**Step 6.** Overlap <phi_k, v_p> = g_k(log p) != 0 for all but finitely many p. C depends on ||phi_k|| = 1
and |g_k(0)| <= sqrt(L - L^-1), both independent of N.

## 2. Step verification

**Step 2:** VERIFIED. phi_k in L^2 of a compact interval, extended by zero to L^2(R). Standard Paley-Wiener.
**Step 3:** SEE ATTACK 3 BELOW -- has a gap.
**Step 5:** VERIFIED. g_k entire of finite type, nonzero. Primes have infinite density. Standard Cartwright.
**Step 6:** VERIFIED. If g_k(0) = 0, use modified Jensen (divide by z^m). Modified constant still bounded
by norms of phi_k on [L^-1, L]. Depends on L, not on N.

## 3. Spectral convergence and the bypass claim

The continuous argument attempts to bypass induction entirely: apply Cartwright to QW^infty directly,
get simplicity via DPTZ in one shot, conclude RH. Chain: QW^infty eigenfunctions -> Paley-Wiener ->
Cartwright -> nonzero overlaps -> DPTZ simplicity -> Even-Sector -> CCM 5.10 -> RH.

This eliminates Wound 2 (discretization gap), K_0(N), and finite verification. See attacks below.

## 4. Feasibility: 5/10

Eliminates Wound 2 completely. But introduces new critical questions about QW^infty existence and
DPTZ applicability. Net gain unclear.

---

## ADVERSARIAL ATTACK

### Attack 1: Does QW^infty exist? -- CRITICAL

CCM define QW_L^N for finitely many primes. QW^infty = lim QW_L^N is the open gap in the CCM+ITPFI
programme (Strategy 11). ITPFI proves convergence at the STATE level, not the OPERATOR level.
Kato-Rellich needs sum_p ||D(N+1) - D(N)|| < infty, estimated as ~1/p^alpha, requiring alpha > 1/2.
If QW^infty does not exist, it has no eigenfunctions, and the argument collapses at Step 1. The
continuous Cartwright argument ASSUMES what the discrete version does not need. Going continuous makes
the existence problem HARDER, not easier. **Severity: CRITICAL.**

### Attack 2: Compact support -- SURVIVES

Eigenfunctions of QW^infty on L^2([L^-1, L]) are zero outside the interval by definition. Extend by
zero to L^2(R): compactly supported, Paley-Wiener applies. No issue.

### Attack 3: Cosine transform injectivity -- HIGH SEVERITY GAP

g_k(xi) = int phi_k(x) cos(x xi) dx is only the COSINE part of the Fourier transform. For phi_k
real-valued on [L^-1, L] subset (0,infty): if g_k = 0 for all xi, the full FT G_k = int phi_k e^{ixxi} dx
satisfies Re(G_k) = 0 on R. But G_k(-xi) = conj(G_k(xi)) for real phi_k, so G_k is purely imaginary
on R. This does NOT force G_k = 0. A nonzero function CAN have vanishing cosine transform while having
nonzero sine transform (e.g., phi_k(x) = sin(ax) on [L^-1, L]).

The claim "g_k = 0 implies phi_k = 0" is WRONG as stated. The cosine transform is NOT injective on
L^2([L^-1, L]). The FULL Fourier transform is injective, but g_k is only the cosine part.

Fix would require: (a) use the full FT instead (changes the overlap structure), or (b) show QW^infty
eigenfunctions cannot lie in ker(cosine transform), which requires structural knowledge of QW^infty
that we do not have. **Severity: HIGH.**

### Attack 4: DPTZ does not apply to QW^infty directly -- HIGH SEVERITY

DPTZ gives simplicity for RANK-ONE perturbations: if D(N+1) = D(N) + alpha_p |v_p><v_p| and
<phi_k, v_p> != 0, then eigenvalues split. This is inherently INDUCTIVE (one prime at a time).

For QW^infty = A + sum_p alpha_p |v_p><v_p|, the sum over all primes is part of the operator, not a
perturbation. "Apply DPTZ directly to QW^infty" is not a well-defined operation. Simplicity of QW^infty
eigenvalues cannot be concluded without decomposing into rank-one steps, i.e., without the induction
that Section 3 claims to bypass. The bypass is ILLUSORY. **Severity: HIGH.**

### Attack 5: If we keep induction, Wound 2 returns

If induction is required (Attack 4), we add primes one by one in L^2 (not on a grid -- no Cauchy
conditioning). But we still need QW^N -> QW^infty to conclude RH. This is the same operator convergence
problem as Attack 1. The continuous setting avoids Cauchy conditioning at each finite step, but the
limit problem remains open.

### Attack 6: Levin constant -- SURVIVES

Even for QW^infty eigenfunctions, ||phi_k|| = 1 and the modified Jensen formula handles g_k(0) = 0.
C depends on L, not on the eigenfunction. No issue here.

---

## HONEST VERDICT

Three genuine wounds found:

1. **Cosine injectivity (Attack 3):** Step 3 contains a mathematical error. The cosine transform is not
   injective on L^2([L^-1, L]). Fixable in principle but requires structural information about QW^infty.

2. **DPTZ bypass (Attack 4):** The "bypass induction" claim is unjustified. DPTZ is intrinsically
   inductive (rank-one perturbation theory). Cannot be applied to the full operator directly.

3. **Existence of QW^infty (Attack 1):** The argument assumes what the CCM programme has not proved.
   Paradoxically, the continuous version needs MORE than the discrete version, not less.

What survives: Paley-Wiener (Step 2), Cartwright-Levin (Step 5), uniform Levin constant (Step 6).
The core Cartwright mechanism remains correct and powerful.

**VERDICT: WOUNDED (confidence 7/10)**

The most promising path forward: keep the secular INDUCTION but perform it in L^2 (continuous integral
operators, not matrices). This avoids Cauchy conditioning at each finite step while not requiring
QW^infty to exist a priori. The limit follows from induction succeeding at every finite stage plus
ITPFI convergence. This hybrid approach preserves strengths of both versions.
