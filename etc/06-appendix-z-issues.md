# Appendix Z Issues — A Story and a Plan

*Written April 4, 2026. For the research team.*

---

## What We Found

While fixing a unit conversion error in Appendix Z, we uncovered
a chain of interconnected issues that affect several parts of the
framework. This document tells the story clearly so we know exactly
what is solid, what is wrong, and what needs to be fixed.

---

## Issue 1: The Unit Conversion Error (Fixed)

**Location:** Appendix Z, §Z.1.3

**What happened:** The conversion of L = 7.54 × 10⁻⁵ m to GeV⁻¹
was written as 3.83 × 10⁻⁷ GeV⁻¹. The correct value is
3.82 × 10¹¹ GeV⁻¹ — off by a factor of 10¹⁸.

**Consequence:** M₅ = (M_Pl²/L)^{1/3} was claimed to be 2.5 × 10¹⁴ GeV.
The correct value is 2.5 × 10⁸ GeV.

**Status:** Fixed in Appendix Z. The correct M₅ is now stated.

---

## Issue 2: The Seesaw Scale (Fixed)

**Location:** Appendix Z, §Z.1.4

**What happened:** The seesaw was written as m_ν = y² v² / M₅ with
M₅ = 2.5 × 10¹⁴ GeV (the wrong value), giving m_ν = y² × 0.24 eV,
and y ~ 0.45 for m_ν = 50 meV. This was internally consistent only
because the wrong M₅ happened to be at the GUT scale.

**The real situation:** With the correct M₅ = 2.5 × 10⁸ GeV, using
M_R = M₅ gives m_ν = y² × 240 keV — far too heavy. This requires
y ~ 14 to get 50 meV, which is non-perturbative.

**The fix:** M_R for the seesaw must come from the CP² compactification
scale, not the S¹ scale. M_R = 1/r₃ ~ M_GUT ~ 10¹⁵ GeV. This is
actually better physics — each compact dimension contributes at its
own energy scale:

- S¹ → dark energy scale (meV), KK graviton mass
- S² → electroweak scale (100 GeV), Higgs mechanism
- CP² → GUT scale (10¹⁵ GeV), seesaw, confinement

With M_R = 10¹⁵ GeV: m_ν = y² × 0.06 eV, y ~ 0.9 for m_ν = 50 meV.
Perturbative. Correct.

**Status:** Fixed in Appendix Z. The CP² origin of M_R is now stated.

---

## Issue 3: The K = 460 Claim in Paper 2 (Open)

**Location:** Paper 2, Appendix E, §E.3.3; Paper 2 abstract

**What happened:** Paper 2 claimed K = 460 using M_N = 2.5 × 10¹⁴ GeV
and y = 0.45. The K calculation:

    K = Γ_D / H|_{T=M_N}
    Γ_D = y² M_N / (8π) = 0.20 × 2.5 × 10¹⁴ / (8π) ≈ 2 × 10¹² GeV
    H = 1.66 √g_* M_N² / M_Pl ≈ 4.3 × 10⁹ GeV
    K ≈ 460 ✓ (internally consistent with wrong M_N)

But with y = 0.45 and M_N = 2.5 × 10¹⁴ GeV, the seesaw gives:
    m_ν = (0.45)² × (246)² / (2.5 × 10¹⁴) ≈ 5 × 10⁻⁸ meV

Not 50 meV. The K = 460 calculation and the m_ν = 50 meV claim were
never simultaneously satisfied with the same y and M_N. The unit
error in Appendix Z hid this inconsistency.

**With the corrected M_R = 10¹⁵ GeV and y ~ 0.9:**

    K = (0.9)² × 10¹⁵ / (8π × 6.9 × 10¹²) ≈ 4.7

K ~ 5 is in the WEAK washout regime, not strong washout. The
table in Appendix E shows K = 10 already gives ξ > BBN bound.
K ~ 5 is worse.

**What this means for the 1/ξ² law:**

The 1/ξ² law as a conceptual mechanism is sound — entropy asymmetry
and washout asymmetry between two branes at different temperatures
DO produce a ratio Ω_DM/Ω_b ~ 1/ξ². This is real physics.

But the specific quantitative claim that K = 460 from the framework's
parameters gives ξ ≈ 0.49, consistent with the BBN bound — that
claim is not internally consistent. To get K large enough for the
strong washout regime (K ≳ 200) with M_R = 10¹⁵ GeV requires y ≳ 9,
which is non-perturbative.

**The cosmological predictions are unaffected:** H₀, S8, t₀, θ*,
N_eff — all depend on ξ as an input, not on how ξ is derived.
The observational fits still hold.

**Status:** Open. The 1/ξ² mechanism is real but the quantitative
K ~ 460 derivation needs to be corrected or replaced.

---

## Issue 4: Propagation to Other Papers (Open)

The K = 460 and y ~ 0.45 values appear in:

- Paper 2 abstract: "washout correction (`y ~ 0.45`, `K ~ 460`)"
- Paper 4 §7.13: uses y ~ 0.45, K ~ 460 for the η_B calculation
- Paper 5 §5: uses y ~ 0.45 for the leptogenesis calculation

These all need to be updated once Issue 3 is resolved.

---

## What Is Still Solid

Despite the above issues, the following results are unaffected:

1. **The 1/ξ² law as a mechanism** — conceptually correct
2. **All CAMB cosmological predictions** — H₀, S8, t₀, θ*, r_d
3. **The Ω_DM/Ω_b = 5.36 fit** — determines ξ observationally
4. **Normal neutrino mass ordering** — from Z₃ geometry
5. **The seesaw scale from CP²** — now correctly M_R ~ 10¹⁵ GeV
6. **All of Paper 1** — the e-circle physics is unaffected
7. **Papers 3, 4, 5** — the core derivations (Higgs, confinement,
   BH information, holonomy correspondence) are unaffected

---

## The Plan

### Step 1: Find a consistent K (the research agent's task)

The agent is working on the four-equation system (etc/06) to
determine R independently of ρ_Λ. If that calculation succeeds
and gives a specific M_R and y, we can compute the correct K.

Alternatively: explore whether a different leptogenesis mechanism
(resonant leptogenesis, non-thermal, or a different sector) gives
large K with perturbative couplings at M_R ~ 10¹⁵ GeV.

Note: resonant leptogenesis (nearly degenerate M_{N_1} ~ M_{N_2})
can enhance ε by a factor of M_N/ΔM, potentially allowing smaller y
while getting larger effective K. This is worth exploring.

### Step 2: Update Paper 2 Appendix E

Once the correct K is established, update:
- The washout calculation
- The corrected ξ determination
- The abstract (remove the specific K ~ 460 claim or correct it)
- The statement about "zero free parameters" if needed

### Step 3: Update Papers 4 and 5

The η_B calculation (Paper 4 §7.13) and baryon asymmetry
(Paper 5 §5) should be updated with the correct Yukawa coupling
and K value.

### Step 4: Add honest open-problems language

Until Steps 1-3 are complete, add a note to Appendix E and the
relevant sections of Papers 4 and 5 flagging that K is not yet
self-consistently derived and is an open problem.

---

## The Honest Summary

The unit error in Appendix Z propagated into a quantitative claim
(K = 460) that is not internally consistent with the corrected
physics (M_R from CP², m_ν = 50 meV, perturbative y). The
conceptual mechanism (1/ξ² law) is real. The cosmological
predictions are unaffected. But the specific quantitative
derivation of ξ "from first principles" needs to be redone with
the correct inputs.

This is the kind of issue that peer review is supposed to catch.
We caught it ourselves, before submission of Papers 3-6.
That's the right time to find it.

The framework is not broken. One calculation needs to be redone.
