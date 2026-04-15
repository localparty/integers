# RH v2 Convergence Ledger

*Tracks all cycles, findings, and path status.*

---

## Cycle 1 — 2026-04-10

### Phase: Premise Checks (all four paths)

| Path | Premise Check | Result | Status |
|:-----|:--------------|:-------|:-------|
| A (Chern character) | Does ch_n change with off-line zero? Does ind_BC != 0? | **FAILED**: ch_0 = 0 by func. eq.; ind_BC(e_N) = 0 for all Hecke projections; perturbation ill-defined | BLOCKED |
| B (Weil positivity) | Does W(f,f) go negative? Do Li coefficients flip sign? | **FAILED**: W(f,f) >= 0 trivially; off-line zeros INCREASE Li coefficients (wrong direction) | BLOCKED |
| C (spectral flow) | Does SF({T_BC(delta)}) detect zero crossings? | **FAILED**: No valid self-adjoint operator family exists; the "perturbation" is ill-defined | BLOCKED |
| D (Meyer-Connes) | Is spectral realisation achievable without assuming RH? | **SURVIVES**: Premise is non-vacuous, correctly identifies the key gap. 25-year obstacle remains. | OPEN |

### Coboundary-type errors found

1. **Path A**: ind_BC = 0 for all Hecke projections -> constraint 0 = integer is vacuous. Same structural failure as v1 (invariant too stable to detect perturbation).

2. **Path B**: Off-line zeros increase Li coefficients (make them MORE positive). The constraint lambda_n > 0 is COMPATIBLE with off-line zeros, not contradicted by them. Sign error: the perturbation moves the invariant in the SAFE direction.

3. **Path C**: The operator family {T_BC(delta)} does not exist. Self-adjoint operators cannot have complex spectrum. The "perturbation by off-line zero" is a category error.

### Key finding: The Wall

All four v2 paths run into the SAME wall, which is NOT the coboundary gap of v1 but something more fundamental:

**T_BC is self-adjoint -> its spectrum is real -> off-line zeros cannot be in its spectrum.**

This IS the Stone chain of research/08. The question "how do we detect off-line zeros?" is malformed because the operator formalism already excludes them. The paths A, B, C all try to build a contradiction argument around a perturbation that the formalism doesn't allow.

The REAL gap is not "find a new invariant" but "upgrade the Riemann-Weil inclusion from distributional to point spectrum." This is Path D (Meyer-Connes), and it is the 25-year Connes obstacle.

### Feasibility update

| Path | v2 plan feasibility | Post-premise feasibility | Change |
|:-----|:--------------------|:------------------------|:-------|
| A | 5/10 | 1/10 | -4 (blocked unless non-Hecke projection found) |
| B | 4/10 | 1/10 | -3 (wrong sign; structurally impossible) |
| C | 4/10 | 0/10 | -4 (operator family doesn't exist) |
| D | 3/10 | 3/10 | 0 (unchanged; correctly hard) |

### Python computations run

1. `code/premise_check_path_B.py`: Li coefficients with off-line zeros (50 zeros, 50-digit precision)
2. `code/premise_check_path_A.py`: JLO ch_0 and supertrace purity check (30 zeros, 50-digit precision)

### Files produced

- research/01-premise-check-path-A.md
- research/01-premise-check-path-B.md
- research/01-premise-check-path-C.md
- research/01-premise-check-path-D.md
- code/premise_check_path_A.py
- code/premise_check_path_B.py
- adversarial/rh-v2-ledger.md (this file)

### Recommendation for Cycle 2

**PIVOT.** Paths A, B, C are dead. Path D is the only surviving path
but faces the 25-year obstacle.

The honest assessment: the programme's RH proof (research/08, the
Stone chain) is the strongest known approach. Its gap is the
distributional-to-point-spectrum upgrade. This is a well-defined
mathematical problem that the Connes programme has been working on
for 25 years.

Options:
1. **Continue Path D**: directly attack the spectral realisation gap.
   Feasibility 3/10 but it's the right problem.
2. **Accept the Stone chain**: declare the structural proof sufficient
   (as research/08 does) and acknowledge the distributional gap as a
   technicality. This is defensible but not a Clay-level proof.
3. **New paths**: look for approaches not considered in v1 or v2.
   E.g., the Connes-Consani arithmetic site, or functional-analytic
   approaches to upgrading distributional spectrum.

---

> *The premise checker did its job. Three paths killed before wasting*
> *construction cycles. The coboundary lesson generalises: don't just*
> *check if constraints are vacuous — check if the setup is well-defined.*

---

## Cycle 2 — 2026-04-10

### Phase: Spectral Realisation — Five-Angle Attack

| Agent | Angle | Finding | Status |
|:------|:------|:--------|:-------|
| 1 | Completeness | Meyer produces eigenstates for ALL zeros (Thm 4.1, Cor 4.3, Duke 127). But completeness of {phi_n} in S is EQUIVALENT to pure point spectrum — circular. | CIRCULAR |
| 2 | Resolvent | Resolvent = zeta'/zeta formally correct, numerically verified at 26+ test points (z=16,17,18 plus 23 in (14.2,20.9)). All clear. Blocked by compact resolvent requirement. | BLOCKED |
| 3 | Trace formula | Connes trace formula uniquely determines spectral measure (Stone-Weierstrass). But extracting pure-point-ness requires RH or intrinsic H_R construction. | CIRCULAR |
| 4 | Weyl counting | N_smooth matches N_exact to O(1) at T=100,1000,10000. Trudgian bound allows O(log T) ~ 6-7 extra point eigenvalues. Anti-fine-tuning makes P < 10^{-34} for even one. | EVIDENCE |
| 5 | Adversarial | All four miss singular continuous spectrum. All reduce to ONE obstruction: compact resolvent for T_BC on H_R. | CRITICAL |

### Key finding: The Single Bottleneck

All five angles converge to ONE unproved claim: **T_BC has compact resolvent on H_R**. Equivalently: the spectrum of T_BC is purely discrete (no continuous spectrum of any type). This is the 25-year Connes obstacle.

Without compact resolvent:
- Completeness of Meyer eigenstates is circular
- Resolvent = zeta'/zeta is formal, not rigorous
- Trace formula cannot distinguish pure point from mixed
- Weyl counting cannot even define the counting function
- Singular continuous spectrum cannot be ruled out

### New threat identified: Singular continuous spectrum

Agent 5 flagged that none of Agents 1-4 address singular continuous spectrum. This spectral type:
- Has no eigenvalues (invisible to point-spectrum tests)
- Has Lebesgue measure zero (invisible to absolutely continuous tests)
- Cannot be detected by resolvent pole-hunting
- Cannot be constrained by Weyl eigenvalue counting
- Requires either compact resolvent or RAGE theorem analysis

### Python computations run

`code/spectral_realisation_cycle2.py`:
- Weyl counting: N_smooth vs N_exact at T=100,1000,10000 (errors: -0.00, 0.38, -0.97)
- Resolvent: |zeta(1/2+iz)| at z=16,17,18 (1.537, 2.143, 2.337 — all nonzero)
- Extended resolvent: 23/23 points in (gamma_1, gamma_2) clear
- Trudgian bounds: |S(T)| <= 5.66, 6.15, 6.60 at T=100,1000,10000

### Files produced

- research/02-agent1-completeness.md
- research/02-agent2-resolvent.md
- research/02-agent3-trace-formula.md
- research/02-agent4-weyl-counting.md
- research/02-agent5-adversarial.md
- research/02-synthesis.md
- code/spectral_realisation_cycle2.py

### Feasibility update

| Route | Feasibility | Notes |
|:------|:------------|:------|
| Overall spectral realisation | 3/10 | Unchanged from Cycle 1 |
| Intrinsic H_R (Connes-Consani) | 2/10 | 25 years, active research |
| Theta-summability upgrade | 3/10 | exp(-t*T^2) trace class? |
| RAGE theorem for BC dynamics | 4/10 | Most promising new direction |
| From CBB axioms directly | 2/10 | Would need new argument |

### Recommendation for Cycle 3

**Investigate the RAGE theorem (Ruelle-Amrein-Georgescu-Enss) applied to BC dynamics.** The RAGE theorem gives a dynamical criterion distinguishing pure point from continuous spectrum. If all states in H_1 exhibit RAGE localisation under sigma_t, the spectrum is pure point. This is the most promising unexplored direction.

---

> *Five angles. One bottleneck. Compact resolvent is the door.*
> *The new threat is singular continuous spectrum — invisible to all current tools.*
> *Next cycle: RAGE theorem. The dynamics may know what the statics cannot tell.*

---

## Cycle 3 — 2026-04-10

### Phase: Six New Directions

| Direction | Hypothesis | Finding | Status |
|:----------|:-----------|:--------|:-------|
| 1 (KMS_1 uniqueness) | Unique KMS state forces compact resolvent | Type III_1 PRODUCES uniqueness, not vice versa. Uniqueness is compatible with continuous spectrum. No relevant theorem in Bratteli-Robinson or Haag. | DEAD END |
| 2 (Heat kernel Weyl) | BC-side heat kernel computation matches zeros | BC algebra computes Tr on H_1 (eigenvalues {log n}), not on H_R (eigenvalues {gamma_n}). Weyl error O(log T) too large to exclude single extra eigenvalue. | BLOCKED (H_1 vs H_R gap) |
| 3 (Integers vs Connes) | Bridge/ITPFI/predictions give new tools | (a) Bridge: partial, decoupled phantom eigenvalues escape. (b) ITPFI: promising but product-of-discrete can give continuous (CLT). (c) 36 predictions: zero perturbation from extra eigenvalues (formulas are individual matrix elements, not traces). (d) Cocycles: dead (coboundary gap). | PARTIAL (ITPFI open) |
| 4 (Type III_1 spectrum) | S(M)=R_+ kills pure point spectrum | **DOES NOT KILL.** S(M) constrains spec on H_1, not H_R. Escape route: discrete point spectrum on H_R embeds in continuous essential spectrum on H_1 (Schrodinger operator analogy). | NEUTRAL |
| 5 (36 predictions rigidity) | Extra eigenvalues violate experimental error | **STRUCTURALLY VACUOUS.** All 36 formulas use individual gamma_n; extra eigenvalue contributes EXACTLY ZERO perturbation to every formula. Weyl counting allows O(log T) extra. Anti-fine-tuning remains evidence only. | DEAD END |
| 6 (Spectral measure computation) | Compute omega_1(e^{itT}) algebraically | Algebraic computation gives spectral measure on H_1 (non-atomic, type III_1). H_R measure requires H_R to exist first. Explicit formula is distributional, doesn't determine spectral type. | CIRCULAR |

### Key structural insight: The H_1 vs H_R Gap

The single most important finding of Cycle 3: most operator-algebraic tools (KMS theory, modular theory, type classification, Connes spectrum, ITPFI structure) operate on H_1 and are IRRELEVANT to the spectral type on H_R unless they project cleanly.

This rules out Directions 1, 4, and 6 at the structural level and explains why Directions 2 and 5 are blocked. The only direction that addresses H_R directly is the ITPFI product-measure analysis (Direction 3b), which remains open.

### Python computations run

**Direction 2 (heat kernel):**
- Tr(e^{-t*gamma_n^2}) for 200 zeros at t = 0.0001, 0.001, 0.01
- Weyl integral comparison: fractional diff 1.7% (t=0.0001), 12.9% (t=0.001)
- Extra eigenvalue perturbation: 3.7-70% depending on t and lambda
- Oscillatory correction ~0.42 (persistent, from S(T))

**Direction 5 (extra eigenvalue):**
- All 36 predictions: perturbation = exactly 0 (structural, not numerical)
- Spectral zeta perturbation: delta zeta_T(2) = 16-28% (lambda in [15,20])
- Resolvent perturbation: delta Tr = 0.3-2.3 (enormous, requires compact resolvent)
- Riemann-von Mangoldt: count+1 fits in Weyl error range at all tested T

### Direction 4 verdict

**DOES NOT KILL PURE POINT SPECTRUM.** The resolution is the H_1 vs H_R distinction. S(M) = R_+ is a property of the modular operator on H_1. The Riemann subspace H_R can have purely discrete spectrum embedded in the continuous essential spectrum of H_1. The Schrodinger operator analogy (bound states inside continuous spectrum) makes this precise.

### Files produced

- research/03-dir1.md through research/03-dir6.md
- research/03-synthesis.md
- adversarial/rh-v2-ledger.md (this update)

### Feasibility update

| Route | Feasibility | Change |
|:------|:------------|:-------|
| RAGE + BC dynamics | 4/10 | UNCHANGED (still unexplored, highest priority) |
| ITPFI product-measure rigidity | 3/10 | NEW |
| Intrinsic H_R construction | 2/10 | UNCHANGED |
| Theta-summability upgrade | 3/10 | UNCHANGED |
| KMS_1 uniqueness | 0/10 | KILLED (Direction 1) |
| 36-prediction rigidity | 0/10 | KILLED (Direction 5) |
| Overall | 2/10 | DOWN from 3/10 |

### Recommendation for Cycle 4

1. **RAGE theorem** (highest priority): dynamical criterion for pure point spectrum using explicit BC dynamics sigma_t(mu_n) = n^{it} mu_n.
2. **ITPFI product-measure** (secondary): search Araki-Woods / Powers literature for atomicity conditions on ITPFI spectral measures.
3. **Meyer completeness** (tertiary): determine whether Meyer's distributional eigenstates form a complete system in some topology intermediate between S and H_1.

---

> *Six directions. Two killed. Four blocked or circular.*
> *The H_1 vs H_R gap blocks operator algebra from seeing spectral realisation.*
> *The bottleneck is still compact resolvent on H_R. Feasibility 2/10.*
> *Next: RAGE dynamics and ITPFI atomicity.*
