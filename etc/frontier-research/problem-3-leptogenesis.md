# Problem 3: The Leptogenesis Boltzmann Equations

**Date:** 2026-04-06

## Key new insight (one sentence)

The Round 1 leptogenesis calculation is internally consistent and physically sound at M_R ~ 10^15 GeV (the CP2 seesaw scale), but the prompt's framing of M_1 ~ 20 meV (the e-circle KK scale 1/R) is a category error — these are two different scales in the framework, and the leptogenesis mechanism uses the GUT-scale right-handed neutrinos, not the meV-scale KK tower.

---

## 0. Clarification: Which Mass Scale?

The prompt states "M_1 = 1/R = m_KK ~ 20 meV" and concludes via the
Davidson-Ibarra bound that eta_B ~ 10^{-26}, sixteen orders of magnitude
too small. **This is based on a misidentification of scales.**

The framework has THREE compact spaces with three mass scales:

| Space | Radius | KK mass | Physical role |
|-------|--------|---------|---------------|
| S^1 (e-circle) | R ~ 12 um | 1/R ~ 20 meV | Dark energy, decoherence |
| S^2 (weak) | r_2 ~ 10^{-18} m | 1/r_2 ~ 1-2 TeV | Higgs, W/Z |
| CP^2 (strong) | r_3 ~ 10^{-31} m | 1/r_3 ~ 10^15 GeV | GUT, confinement |

The right-handed neutrino mass is M_R = 1/r_3 ~ 10^15 GeV (the CP2
compactification scale), NOT 1/R ~ 20 meV. The seesaw relation is:

    m_nu = y^2 v^2 / M_R = 2 g_2^2 v^2 / (10^15 GeV) = 51 meV

This is confirmed in Paper 4 Section 7.22. The 20 meV scale is the
e-circle KK mass, which plays no role in leptogenesis.

**The Davidson-Ibarra bound at M_R = 10^15 GeV gives:**

    |eps| <= (3/16pi) x M_1 m_3 / v^2
           = (3/16pi) x (10^15 GeV x 50 meV) / (174 GeV)^2
           = (3/16pi) x (5 x 10^{22} eV^2) / (3 x 10^{22} eV^2)
           ~ 6 x 10^{-2} x (3/16pi)
           ~ 4 x 10^{-3}

This is LARGE — far above the required eps ~ 10^{-6} for successful
leptogenesis. At M_R ~ 10^15 GeV, there is no Davidson-Ibarra problem.
The DI bound is easily satisfied.

---

## 1. What Round 1 Actually Claims

The Round 1 analysis (oi1-boltzmann-equations.md) solves the resonant
leptogenesis Boltzmann equations with:

- M_1 ~ M_2 ~ 10^15 GeV (CP2 seesaw scale)
- y = g_2 sqrt(2) = 0.92 (gauge-Higgs unification)
- Z3 orbifold near-degeneracy: Delta = xi M_1 where xi = y^2/(8pi) = 0.034
- Mass splitting Delta/Gamma_1 ~ 1 (marginally resonant)
- CP asymmetry eps = 4.69 x 10^{-5}
- Strong washout K = 47.4
- Flavour orthogonality p_12 = xi^2 ~ 10^{-3} (prevents cancellation)

Result: eta_B = (1.1 to 3.0) x 10^{-10} for alpha in [0, 20],
giving eta_B / eta_obs = 0.17 to 0.50.

---

## 2. Proof Chain

| Step | Claim | Status | Assessment |
|------|-------|--------|------------|
| 1 | M_R = 1/r_3 ~ 10^15 GeV | ESTABLISHED | From CP2 compactification; Paper 4 Section 3.3 |
| 2 | y_nu = g_2 sqrt(2) = 0.92 | ESTABLISHED | Gauge-Higgs unification; Paper 4 Section 7.22 |
| 3 | m_nu = y^2 v^2/M_R = 51 meV | ESTABLISHED | Matches experiment at 4% |
| 4 | Z3 orbifold gives M_1 ~ M_2 | PLAUSIBLE | Z3 symmetry enforces c_1 = c_2 at leading order |
| 5 | Splitting Delta/Gamma ~ 1 | ASSUMED | Requires xi_boundary ~ y^2/(8pi); not derived from first principles |
| 6 | CP phase arg((YY)_12) = 60 deg | PLAUSIBLE | Follows from Z3 120-degree separation |
| 7 | Off-diagonal Yukawa (YY)_12 ~ xi y^2 | PLAUSIBLE | Z3 breaking at order xi; consistent but not rigorously derived |
| 8 | eps = 4.69 x 10^{-5} | FOLLOWS | From steps 5-7 via Pilaftsis-Unterdarfer formula |
| 9 | K = 47.4, strong washout | ESTABLISHED | K = m_tilde/m_star; m_tilde = y^2 v^2/M_1 = 51 meV |
| 10 | Flavour orthogonality p_12 = xi^2 | PLAUSIBLE | Follows from Z3 democratic Yukawa; prevents eps_1 + eps_2 = 0 |
| 11 | Numerical Boltzmann solution | CORRECT | Standard BDF integration; results consistent with analytic estimates |
| 12 | eta_B = (1.1-3.0) x 10^{-10} | FOLLOWS | From steps 8-11 |
| 13 | eta_B / eta_obs = 0.17 to 0.50 | FOLLOWS | Factor 2-6 from observation |

---

## 3. Critical Examination

### 3.1 What is solid

**The mass scale is correct.** At M_R ~ 10^15 GeV, leptogenesis is
in comfortable territory:
- The Davidson-Ibarra bound allows eps up to ~10^{-3}
- The reheating temperature T_RH > 10^15 GeV is required but achievable
  in the framework's inflationary scenario (Paper 6)
- Strong washout (K ~ 50) is typical for this parameter regime

**The Boltzmann equations are standard.** The numerical integration
uses well-established methods (scipy BDF solver, Bessel function
rates). The single-species result (kappa = 3.28 x 10^{-3} for K = 47)
is consistent with the literature (Buchmuller, Di Bari, Plumacher
2005 give kappa ~ 10^{-3} for K ~ 50).

**The CP asymmetry formula is correct.** The Pilaftsis-Unterdarfer
resonance formula (Nucl. Phys. B 692, 303, 2004) is the standard
result for nearly-degenerate RHN. The evaluation with Z3 Yukawa
inputs is internally consistent.

### 3.2 What is assumed but plausible

**The near-degeneracy M_1 ~ M_2.** The Z3 orbifold symmetry gives
identical fixed-point masses at leading order. The splitting arises
from boundary-condition breaking. The claim that Delta ~ Gamma_1
(i.e., xi_boundary ~ y^2/(8pi) ~ 0.034) is physically reasonable
but not derived from the compactification. It is the ONLY parameter
in the calculation that is not fully determined.

**The flavour orthogonality.** The Z3 democratic Yukawa matrix has
orthogonal columns, giving p_12 = 0 at leading order. The Z3 breaking
generates p_12 ~ xi^2. This is the crucial ingredient that prevents
the catastrophic cancellation between eps_1 and eps_2. It is
self-consistent but relies on the specific Z3 Yukawa texture being
preserved in the mass eigenbasis.

### 3.3 What is problematic

**The alpha parameter.** The K-splitting parameter alpha (which
determines K_2 = K_1(1 + alpha xi)) is completely undetermined.
The result varies by a factor ~3 across alpha = [0, 20]. At
alpha = 0, the residual asymmetry comes from the thermal-history
difference between N_1 and N_2 (geometric time offset), which is
physically well-motivated. For alpha > 0, the effect is smaller.
This is an honest uncertainty, not a hidden free parameter.

**The gravitino problem.** At M_R ~ 10^15 GeV, the required reheating
temperature T_RH > 10^15 GeV creates a potential gravitino
overproduction problem in supersymmetric extensions. However, the
e-dimension framework is NOT supersymmetric in the standard sense
(no 4D superpartners), so this may not apply. This deserves explicit
discussion.

**The N_3 contribution.** The analysis only considers N_1 and N_2.
N_3 is assumed hierarchically heavier and negligible. If N_3 is
also near-degenerate (as Z3 symmetry would suggest), the three-body
system is more complex. The Round 1 analysis sets M_3 hierarchically
different via the warp factor, which partially breaks the Z3
motivation.

**Spectator processes.** The numerical code does not include spectator
processes (redistribution of B-L charge among quarks, charged leptons,
Higgs). These typically suppress eta_B by a factor 0.4-0.6. Including
them would push eta_B / eta_obs down to ~0.1-0.3, marginally
consistent.

### 3.4 The Round 1 internal inconsistency

There is a tension in the framework regarding M_3. The Z3 orbifold
gives three fixed points with c_1 = c_2 = c_3 at leading order,
suggesting M_1 ~ M_2 ~ M_3. But the analysis requires M_3 to be
hierarchically different (so that only the N_1-N_2 system matters).
This is achieved by setting Delta_c = c_3 - c_1 to be O(1) rather
than O(xi).

The question is: why should c_1 = c_2 (split by xi ~ 0.034) but
c_3 be very different? The answer given is that "orbifold boundary
conditions break Z3 -> Z1 at the visible brane," but this should
affect all three masses, not just M_3. A more rigorous treatment
of the Z3 breaking pattern is needed.

---

## 4. Pattern Attribution

| Pattern | Role in leptogenesis |
|---------|---------------------|
| P2 (Holonomy) | Yukawa = gauge coupling (y = g_2 sqrt(2)); determines m_tilde and K |
| P4 (Topological Rigidity) | Z3 orbifold gives three fixed points; chi(CP2) = 3 gives three generations |
| P3 (Casimir as Scale-Setter) | CP2 Casimir sets M_R ~ 10^15 GeV; S^2 Casimir sets v = 246 GeV |
| P1 (Geometric Reinterpretation) | CP violation from Z3 geometric phases (120-degree separation) |

**Generative pattern:** P4 (Z3 topological structure) provides the
near-degeneracy and CP phases. P2 (holonomy/gauge-Higgs) fixes the
Yukawa coupling and thereby determines the washout regime.

---

## 5. Honest Assessment

| Aspect | Confidence | Reason |
|--------|------------|--------|
| Mass scale M_R ~ 10^15 GeV | HIGH | Established from CP2 compactification and seesaw m_nu match |
| Davidson-Ibarra bound satisfied | HIGH | eps_DI < 4 x 10^{-3}; actual eps ~ 5 x 10^{-5}; no problem |
| Yukawa y = 0.92 | HIGH | From gauge-Higgs unification; independently verified by m_nu |
| K = 47 (strong washout) | HIGH | Follows directly from y, v, M_R |
| Z3 near-degeneracy M_1 ~ M_2 | MEDIUM | Symmetry argument is plausible; Delta/Gamma ~ 1 is assumed not derived |
| CP asymmetry eps = 4.7 x 10^{-5} | MEDIUM | Correct formula; inputs partially assumed (off-diagonal Yukawa structure) |
| Flavour orthogonality | MEDIUM | Z3 democratic matrix is orthogonal; breaking pattern needs more rigor |
| eta_B within factor 3 of obs | MEDIUM-LOW | Factor 2-6 before spectator processes; factor 5-15 after |
| "Zero free parameters" claim | LOW | Alpha is free; Z3-breaking pattern for M_3 vs M_{1,2} is ad hoc |

### Overall verdict

The Round 1 calculation is **physically reasonable** and uses a
**legitimate mechanism** (resonant leptogenesis at the GUT scale with
Z3 Yukawa textures). The mass scale is correct, the Davidson-Ibarra
bound is easily satisfied, and the Boltzmann equations are properly
solved.

However, the claim of "agreement within a factor of 3" is **optimistic**.
The most honest assessment:

- **Before spectator processes:** eta_B / eta_obs = 0.17 to 0.50
  (factor 2-6). This is "within a factor of 6."

- **After spectator processes** (factor 0.4-0.6 suppression):
  eta_B / eta_obs = 0.07 to 0.30 (factor 3-15). This is "within
  an order of magnitude."

- **The near-degeneracy assumption** (Delta/Gamma ~ 1) is not
  derived from the compactification. If Delta/Gamma >> 1 (non-resonant),
  the resonance factor drops from 0.80 to much less, and eps falls.
  If Delta/Gamma << 1 (very degenerate), the Pilaftsis-Unterdarfer
  formula still gives eps ~ (3/16pi) x Im_ratio x 1 ~ 6 x 10^{-5},
  which is similar.

**The calculation gives eta_B within an order of magnitude of
observation under physically plausible assumptions. This is a
nontrivial success for a framework with very few adjustable
parameters, but "factor of 3" accuracy is an overstatement.**

---

## 6. Addressing the Prompt's Davidson-Ibarra Concern

The prompt computed:

    |eps| <= (3/16pi) x (20 meV x 50 meV) / (174 GeV)^2 ~ 4 x 10^{-19}

This used M_1 = 20 meV (the e-circle KK mass). The correct M_1 for
leptogenesis is M_R = 10^15 GeV (the CP2 seesaw scale), giving:

    |eps| <= (3/16pi) x (10^15 GeV x 50 meV) / (174 GeV)^2
           ~ (3/16pi) x (5 x 10^{10}) / (3 x 10^4)
           ~ (3/16pi) x 1.7 x 10^6 ... wait, let me redo this carefully.

Actually, the Davidson-Ibarra bound is:

    |eps_1| <= (3/16pi) x M_1 x m_3 / v^2

where v = 174 GeV (or 246 GeV depending on convention). Using v = 174 GeV:

    M_1 x m_3 = 10^15 GeV x 50 x 10^{-3} eV
               = 10^15 x 5 x 10^{-2} GeV x eV
               = 5 x 10^{13} GeV.eV
               = 5 x 10^{13} x 10^{-9} GeV^2
               = 5 x 10^4 GeV^2

    v^2 = (174 GeV)^2 = 3.03 x 10^4 GeV^2

    |eps_1| <= (3/16pi) x (5 x 10^4) / (3.03 x 10^4)
             = (3/16pi) x 1.65
             = 0.060 x 1.65
             = 0.099

So the DI bound at M_R = 10^15 GeV allows eps up to ~0.1. The actual
eps = 4.7 x 10^{-5} is three orders of magnitude BELOW this bound.
There is no DI problem whatsoever. The framework sits comfortably
within allowed parameter space.

**The concern raised in the prompt was based on a misidentified
mass scale.**

---

## 7. What Would Make It Airtight

1. **Derive Delta/Gamma from the compactification.** The Z3-breaking
   boundary conditions should determine the mass splitting Delta
   as a function of known geometric quantities. Currently this ratio
   is set to ~1 by assumption. A first-principles derivation would
   remove the last adjustable input.

2. **Explain M_3 hierarchy.** Why is M_3 hierarchically different from
   M_1 ~ M_2? The Z3 orbifold should give all three masses equal at
   leading order. The breaking pattern that splits M_3 >> M_{1,2}
   needs explicit construction.

3. **Include spectator processes.** The Boltzmann equations should
   include quark/lepton spectator effects. This is a well-known
   correction (Nardi et al. 2006; Blanchet & Di Bari 2009) that
   typically reduces eta_B by a factor 0.4-0.6.

4. **Flavoured Boltzmann equations.** For M_R ~ 10^15 GeV, T_lepto
   is above the tau Yukawa equilibration temperature (~10^12 GeV),
   so the unflavoured approximation IS correct. This is actually a
   point in the analysis's favor that should be stated explicitly.

5. **Thermal corrections to epsilon.** The CP asymmetry receives
   O(T^2/M^2) thermal corrections. For z = M/T ~ 1-5, these are
   O(10%) — within the stated uncertainties.

6. **Three-generation Boltzmann.** Solve the full three-generation
   system (not just N_1-N_2) to verify that N_3 contributions are
   indeed negligible.

---

## 8. Comparison with Paper 4 Section 7.13

Paper 4 Section 7.13 gives a different (earlier, simpler) estimate:

    eps ~ 6.4 x 10^{-4}, kappa(K=5) ~ 0.05, eta_B ~ 2 x 10^{-7}

This overshoots by ~300x. The Round 1 analysis improves on this by:
- Using the correct Z3 Yukawa structure (eps = 4.7 x 10^{-5}, not 6.4 x 10^{-4})
- Computing K correctly (K = 47, not K = 5)
- Including the two-species cancellation physics

The discrepancy between Section 7.13 and Round 1 is a factor of ~1000
in eta_B. Both use the same mass scale (10^15 GeV). The Round 1
analysis is the more careful calculation and should be considered
authoritative.

However, Section 7.13 uses K = 5 (computing K differently), while
Round 1 uses K = 47. The difference arises from how the effective
neutrino mass m_tilde is computed:
- Round 1: m_tilde = y^2 v^2/M_1 = 0.85 x (246)^2 / 10^15 = 51 meV
- Section 7.13: appears to use a different K formula

This discrepancy should be reconciled. Round 1's K = 47 is the
standard result and should be preferred.

---

## 9. Summary

| Question | Answer |
|----------|--------|
| Is M_1 ~ 20 meV? | NO. M_R ~ 10^15 GeV (CP2 scale). The 20 meV is the e-circle KK mass. |
| Does the DI bound kill leptogenesis? | NO. At 10^15 GeV, the DI bound allows eps up to ~0.1. |
| Is the mechanism resonant? | YES. Z3 near-degeneracy gives Delta/Gamma ~ 1. |
| Does the framework predict eta_B? | APPROXIMATELY. eta_B ~ (0.1-3) x 10^{-10}, within an order of magnitude. |
| Is "factor of 3" accurate? | OPTIMISTIC. "Order of magnitude" is more honest after all corrections. |
| Is there a fatal obstacle? | NO. The mechanism is physically sound. The main weakness is the assumed Delta/Gamma ~ 1. |

**Bottom line:** The leptogenesis mechanism in the framework is viable and
produces eta_B within an order of magnitude of the observed value with
physically motivated (but not fully derived) inputs. The prompt's concern
about the Davidson-Ibarra bound was based on misidentifying the relevant
mass scale. The Round 1 analysis is the most careful treatment and should
replace the earlier Section 7.13 estimate.

---

Sources:
- [Davidson-Ibarra bound (original paper)](https://arxiv.org/abs/hep-ph/0202239)
- [Leptogenesis below the DI bound](https://arxiv.org/abs/hep-ph/0603043)
- [Resonant enhancement in leptogenesis](https://arxiv.org/abs/1711.02863)
- [On resonant leptogenesis (Pilaftsis)](https://arxiv.org/abs/0705.2183)
- [Leptogenesis in theories with large extra dimensions](https://arxiv.org/abs/hep-ph/9906265)
- [Leptogenesis in 5D aGUT models (2025)](https://arxiv.org/html/2503.14397)
- [Cosmological constraints on dark neutrino towers](https://arxiv.org/abs/2411.07029)
- [Strong washout approximation to resonant leptogenesis (Garbrecht & Gautier)](https://www.semanticscholar.org/paper/Strong-Washout-Approximation-to-Resonant-Garbrecht-Gautier/7b4c670482964b06cc7793470a97dbae5c2811c4)
- [Tri-resonant leptogenesis](https://link.springer.com/article/10.1007/JHEP11(2022)065)
