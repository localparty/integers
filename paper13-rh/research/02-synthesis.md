# research/02 -- Cycle 2 Synthesis: Five-Angle Convergence

*Date: 2026-04-10. Spectral Realisation Cycle 2.*

## 1. The one question

Does spec(T_BC) = {gamma_n}?

## 2. What each angle found

| Angle | Finding | Status |
|:------|:--------|:-------|
| 1 (Completeness) | Meyer produces eigenstates for ALL zeros. But completeness of {phi_n} is equivalent to pure point spectrum -- circular. | CIRCULAR |
| 2 (Resolvent) | Resolvent = zeta'/zeta is formally correct, numerically verified at 26+ test points. Blocked by compact resolvent. | BLOCKED |
| 3 (Trace formula) | Connes trace formula uniquely determines spectral measure. But extracting pure-point-ness requires RH or intrinsic H_R construction. | CIRCULAR |
| 4 (Weyl counting) | Weyl error O(log T) allows at most O(log T) extra point eigenvalues. Anti-fine-tuning makes P < 10^{-34} for even one. | EVIDENCE |
| 5 (Adversarial) | All four miss singular continuous spectrum. All reduce to one obstruction: compact resolvent. | CRITICAL |

## 3. The single bottleneck

**Compact resolvent for T_BC on H_R.**

Every angle, when pushed to its logical conclusion, requires
that T_BC has purely discrete spectrum. This is equivalent to
compact resolvent. Without it:

- Agent 1 cannot prove completeness
- Agent 2 cannot make the resolvent identification rigorous
- Agent 3 cannot extract pure-point-ness from the trace formula
- Agent 4 cannot even define the counting function

Compact resolvent for T_BC on H_R is the Connes obstacle. It has
been open for 25 years.

## 4. What IS new from this cycle

### 4.1 The singular continuous spectrum threat

Agent 5 identified that none of the four construction angles
addresses singular continuous spectrum. This is a genuine
threat not previously flagged in the programme.

Singular continuous spectrum:
- Has no eigenvalues (no point spectrum)
- Has Lebesgue measure zero (not absolutely continuous)
- Is spectrally diffuse (Cantor-set-like support)
- Cannot be detected by the resolvent (no poles)
- Cannot be detected by eigenvalue counting (no eigenvalues)
- Cannot be ruled out by anti-fine-tuning (not point spectrum)

To rule out singular continuous spectrum, one needs either:
(a) Compact resolvent (forces pure point), or
(b) RAGE theorem analysis (relates spectral type to time
    evolution dynamics), or
(c) Subordinacy theory (Gilbert-Pearson, relates spectral type
    to solution asymptotics)

### 4.2 The convergence of obstructions

All five angles converge to ONE obstruction. This is itself
informative: the problem is well-defined and correctly identified.
The programme is not lost in a maze -- it has one door to open.

### 4.3 Numerical reinforcement

The resolvent check at 26+ points between gamma_1 and gamma_3
found NO anomalies. The Weyl counting matches to O(1) at T = 100,
1000, 10000. These are consistent with pure point spectrum but
do not prove it.

## 5. Feasibility update

| Route to compact resolvent | Feasibility | Notes |
|:---------------------------|:------------|:------|
| Intrinsic H_R construction (Connes-Consani) | 2/10 | 25 years, active research |
| Theta-summability upgrade | 3/10 | exp(-t*T^2) trace-class? Known theta-summable |
| From CBB axioms directly | 2/10 | Would need new spectral-action argument |
| RAGE + BC dynamics | 4/10 | Most promising new direction; needs study |

Overall feasibility for closing spectral realisation: **3/10**
(unchanged from Cycle 1).

## 6. Recommendation for Cycle 3

**Investigate RAGE theorem for BC dynamics.**

The RAGE theorem (Ruelle-Amrein-Georgescu-Enss) states:

- If psi is in H_{pp} (pure point subspace), then
  f(x) * exp(-iAt) * psi -> 0 weakly for any f vanishing at
  infinity.
- If psi is in H_{c} (continuous subspace), then
  f(x) * exp(-iAt) * psi does NOT decay.

This gives a dynamical criterion for pure point vs continuous
spectrum. For the BC system, the time evolution sigma_t is
explicitly known. If one can show that ALL states in H_1 exhibit
RAGE decay (localisation in position space), the spectrum is
pure point.

This is the most promising direction not yet explored.
