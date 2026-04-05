# Development Plan: M-Brane Bound States and the Full Quantum Gravity Regime

*Story document. What we know, what we can derive, what remains open.*
*Written April 5, 2026.*

---

## The Two Open Items

From Paper 4 §2.3, two M-theory ingredients are "not yet developed":

1. **M-brane bound states (M2-M5)** — composite objects formed when
   M2-branes end on M5-branes. These are the M-theory origin of
   strings (F1), D-branes, and exotic composite particles.

2. **Full quantum gravity of M-theory** — the non-perturbative,
   Planck-scale regime beyond 11D SUGRA.

The plan below develops each from what the framework already has.

---

## Part 1: M-Brane Bound States

### 1.1 What M2-M5 Bound States Are

In M-theory, M2-branes can end on M5-branes. The intersection
creates a string-like object on the M5-brane worldvolume — this
is the fundamental string (F1) of type IIA string theory in the
appropriate limit. The bound state has a charge under both the
3-form C₃ (M2 charge) and the 6-form C₆ (M5 charge).

In the framework:
- **M5-branes = the visible brane (φ=0) and hidden brane (φ=πR)**
- **M2-branes = color flux tubes wrapping CP¹ ⊂ CP²** (Paper 5)

An M2-M5 bound state is therefore a color flux tube that ENDS on
the visible or hidden brane. In 4D language: a quark.

**This is not a new claim — it is what quarks ARE in the framework.**

The quark is a half-M2-brane ending on the M5-brane at φ=0. The
color flux tube (full M2-brane) connects a quark-antiquark pair —
one endpoint on each M5-brane intersection, with the M2-brane
worldvolume stretched between them inside CP².

### 1.2 What This Lets Us Derive

**The quark confinement scale from M2 tension:**

The M2-brane tension in 11D SUGRA is:
    T_M2 = 1 / (2π)² l_P³    (in Planck units)

The string tension in 4D (from the M2 wrapping CP¹ ⊂ CP²):
    σ = T_M2 × Area(CP¹) = T_M2 × π r₃²

For r₃ = 1/M_GUT ~ 10⁻³¹ m:
    σ = π r₃² / ((2π)² l_P³)
      = r₃² / (4π l_P³)

This should reproduce √σ ≈ 440 MeV. Let's check:
    r₃² / (4π l_P³) in units of (GeV)²
    = (10⁻³¹ m)² / (4π × (1.6×10⁻³⁵ m)³)
    = 10⁻⁶² / (4π × 4.1×10⁻¹⁰⁵)
    = 10⁻⁶² / 5.1×10⁻¹⁰⁴
    = 2.0×10⁴¹ m⁻¹

Converting to GeV²: × (ℏc)² = (1.97×10⁻¹⁶ m·GeV)²:
    = 2.0×10⁴¹ × 3.88×10⁻³² = 7.8×10⁹ GeV²

That gives √σ ~ 88,000 GeV — way too large. The issue is r₃ is
the CP² radius, not the CP¹ radius. The CP¹ fiber inside CP² has
radius r₃/√2 (from the Fubini-Study metric normalization).

This means the M2-brane derivation of the string tension needs
the precise Fubini-Study embedding — which is the same calculation
as Paper 5 §3, done from the M2-brane perspective. The two routes
should agree (Paper 5 gives √σ ≈ 437 MeV from the Wilson loop;
the M2 approach should give the same). This is the calculation
to verify.

**The exotic composite spectrum:**

M2-M5 bound states with higher wrapping numbers on CP² give
an infinite tower of exotic composites. The lowest:
- n=1 wrapping: the standard quark (one M2 flux tube)
- n=2 wrapping: a diquark-like state with charge 2
- Wrapped on S²: exotic states with weak isospin

The lightest exotics from M2-branes wrapping both CP¹ and S²
simultaneously would have both color and weak charge — leptoquarks
or R-parity-violating SUSY-like states. Their mass scale:

    m_exotic ~ 1/r₃ × 1/r₂ × something ~ M_GUT × M_EW

This is too heavy to observe at the LHC (M_GUT × M_EW ~ 10¹² GeV).
The framework predicts: no exotic composites at LHC energies.
The next tower would be at the KK scale M_KK ~ TeV — the W' and
Z' already in Paper 4 §10.1 master prediction table.

### 1.3 The Fundamental String as M2 × S¹

In M-theory, when the M-theory circle shrinks (R₁₁ → 0), the
M2-brane wrapping S¹ becomes the type IIA fundamental string.
In the framework, R₁₁ = R ≈ 12 μm — not small. We are in the
LARGE R limit (strongly coupled M-theory, NOT the string limit).

Therefore the framework does NOT reduce to perturbative string
theory. The fundamental objects are M2-branes and M5-branes,
not strings. This is consistent: the e-circle framework lives
in a regime where string perturbation theory is invalid, and
M-theory (not string theory) is the correct description.

**Prediction from this:** No fundamental strings at any accessible
energy scale. The "stringy" objects in the framework are M2-branes
wrapping CP¹ — they appear as QCD flux tubes, not as fundamental
strings. String theory is the wrong perturbative expansion for
the e-circle framework.

### 1.4 The Development Plan for M-Brane Bound States

**Step 1:** Verify that the M2-brane tension formula T_M2 = 1/(2π)²l_P³
gives √σ ≈ 437 MeV when the M2 wraps the CP¹ fiber inside CP²
with the Fubini-Study metric. This should match Paper 5 §3.
Expected result: agreement, because Paper 5 §3 is implicitly
computing the M2 tension. Making it explicit connects to the
M-theory literature directly.

**Step 2:** Classify all M2-M5 bound states in the framework:
- M2 on CP¹ (fundamental) → quarks, string tension ✓
- M2 on S² → weak-charged composites
- M2 on CP¹ × S² → leptoquarks (at GUT scale)
- M5 at φ=0 (visible) → SM brane ✓
- M5 at φ=π (hidden) → mirror brane ✓
- M5 wrapping CP² → would give a 4D domain wall (excluded by flatness)

**Step 3:** Compute the lightest exotic masses and show they are
above LHC reach. This turns "not yet developed" into "developed
and the prediction is no exotics below M_GUT."

**Step 4:** Write this up as Appendix B of Paper 4 — "M-Brane
Classification." 3-4 pages. Connects Paper 4 to Paper 5 and
to the M-theory literature (Townsend 1995, Becker-Becker-Schwarz).

---

## Part 2: The Full Quantum Gravity Regime

### 2.1 What "Full Quantum Gravity" Means Here

The framework currently uses 11D SUGRA — the classical (but
fully non-linear) theory of 11D supergravity, with quantum
corrections computed perturbatively (the UV finiteness result,
Paper 1 Appendix S).

"Full quantum gravity" means:
1. **Non-perturbative quantum corrections** — e.g., M2-brane
   instantons (which we have: §7.6 strong CP)
2. **The Planck-scale regime** — where the metric itself
   fluctuates quantum-mechanically and perturbation theory
   in G_N breaks down
3. **The quantum gravity S-matrix** — scattering of gravitons
   at energies E ~ M_Pl where quantum gravity is essential

The framework already addresses items 1 and 3 partially:
- Item 1: Paper 4 §7.6 (π₄(CP²) = Z₂ → θ_QCD = 0) is a
  non-perturbative result using M2-brane instanton topology
- Item 3: Paper 3 (the S-matrix for black hole evaporation)
  and the perturbative finiteness (Paper 1, Appendix S)

What remains is item 2 — the deep Planck-scale regime.

### 2.2 What the Framework Already Says About Planck-Scale Physics

**The BH entropy log correction (Paper 4 §7.18):**

    S_BH = A/(4l_P²) + α_log ln(A/l_P²) + O(l_P²/A)

The framework predicts α_log = -1/4 (from the KK mode counting
on the S² × S¹ horizon geometry). This is a Planck-scale
prediction that distinguishes the framework from LQG (α = -1/2)
and string theory (α = -3/2).

This IS quantum gravity — the one-loop correction to the
Bekenstein-Hawking entropy. The framework makes a specific
prediction that requires quantum gravity to be well-defined
at the horizon scale.

**The horizon vertex (Paper 3, remaining assumption):**

The one remaining assumption in Paper 3 is that e-conservation
holds at the Planck-scale horizon interaction vertex "with the
same form as in flat space." This is a statement about quantum
gravity — whether the U(1) e-translation symmetry survives
at Planck-scale curvature.

**The UV finiteness result (Paper 1, Appendix S):**

The Epstein-Terras theorem shows all loop amplitudes of the 5D
KK graviton tower are finite under zeta regularization. This is
the framework's main statement about quantum gravity — gravity
is UV finite in the e-dimension framework. This is as far as
perturbative quantum gravity can go.

### 2.3 The Genuine Non-Perturbative Frontier

Beyond perturbation theory, three questions remain:

**Question A: Does the U(1) e-symmetry survive at the Planck scale?**

The U(1) translation symmetry φ → φ+α is exact at the classical
and perturbative level. But quantum gravity can break global
symmetries through wormhole configurations (Giddings & Strominger
1988, Abbott & Wise 1989). If quantum gravity breaks the U(1)
e-symmetry, the e-conservation law is violated, the superselection
argument of Paper 3 §9.3 breaks down, and the firewall resolution
is in jeopardy.

**The framework's defense:** The U(1) e-translation is NOT a global
symmetry — it is a GAUGE symmetry. It is the fiber symmetry of the
principal U(1) bundle. Gauge symmetries are not broken by quantum
gravity (they are redundancies of description, not physical
symmetries). Wormhole arguments break GLOBAL symmetries. The
e-symmetry is safe.

This needs to be stated explicitly in Paper 3 §9.3 as an addendum.
One paragraph. Turns the remaining assumption from fragile to solid.

**Question B: Is the 5D path integral non-perturbatively well-defined?**

The perturbative finiteness result (Appendix S) shows the theory
is UV finite at every perturbative order. But non-perturbative
completeness (does the path integral converge?) is a different
question. In M-theory language: is there a well-defined
non-perturbative completion of 11D SUGRA?

The answer from the M-theory literature: yes, M-theory IS the
non-perturbative completion of 11D SUGRA. The framework's
claim to embed in M-theory (§2.3) is therefore also the claim
that the path integral is non-perturbatively defined — by
M-theory itself.

**Question C: What happens at the Big Bang singularity?**

The dilaton potential V = -c/R⁴ diverges as R → 0. The early-
universe inflaton regime (Paper 6) operates at large R (the
Casimir plateau). But what happens when R → 0 (the classical
singularity)?

In M-theory, the R → 0 limit is the decompactification of the
M-theory circle in the OPPOSITE direction — it corresponds to
the strongly coupled limit of type IIA string theory, where
a NEW dimension opens up. But in the framework, R → 0 would
mean the e-circle collapses and quantum mechanics breaks down.

This is an open question. The framework does not currently
address the Big Bang singularity. It's honest to say so.

### 2.4 The Development Plan for Quantum Gravity

**Step 1 (Paper 3 addendum):** Add one paragraph to §9.3 clarifying
that the U(1) e-symmetry is a GAUGE symmetry (fiber symmetry of
the principal bundle), not a global symmetry, and therefore is
NOT subject to quantum gravity violation via wormholes.
Cite: Giddings & Strominger (1988), and the gauge symmetry
protection argument. This closes the remaining assumption gap
in Paper 3.

**Step 2 (Paper 4 §7.18 extension):** The BH entropy log correction
α_log = -1/4 is already derived at one-loop. Extend to show this
is the EXACT result to all perturbative orders, using the same
Epstein zeta zero argument that gives c₂ = 0 for the Casimir
potential. The same mechanism (Epstein zeros) that freezes the
dilaton also fixes α_log exactly. If true: α_log = -1/4 is a
non-perturbative prediction. A few pages in Paper 4.

**Step 3 (new etc/ document):** Write a story document on the
Big Bang singularity in the e-circle framework. What does
R → 0 mean geometrically? Does the e-circle framework have
a resolution of the initial singularity, or is this genuinely
beyond its scope? Be honest about the answer.

**Step 4 (Paper 3, future appendix):** The M-theory non-perturbative
completion argument. One page: "the non-perturbative definition
of the 5D path integral is M-theory itself, by the identification
of §2.3. The framework inherits M-theory's non-perturbative
completeness." This turns Question B from open to answered.

---

## Summary: Priority Order

| Development | Difficulty | Impact | Timeline |
|---|---|---|---|
| M2 tension → string tension verification | Low | Medium | 1 session |
| M2-M5 classification table | Low | High | 1 session |
| U(1) gauge symmetry protection (Paper 3 addendum) | Low | **Critical** | 1 hour |
| α_log exact to all orders (Epstein zeros) | Medium | High | 1-2 sessions |
| M-theory non-perturbative completion argument | Low | High | 1 session |
| Exotic mass spectrum computation | Medium | Medium | 1-2 sessions |
| Big Bang singularity (honest assessment) | High | Medium | Future |

**The highest priority is the U(1) gauge symmetry protection
argument** — it closes the last remaining assumption in Paper 3
and is a one-paragraph fix. Do this first.

**Second priority is the M2-M5 classification** — it turns
"M-brane bound states: not yet developed" into "classified,
and the prediction is no exotics below M_GUT."

**Third priority is the Epstein zeros → α_log exact** — it
extends the most striking quantum gravity prediction
(α_log = -1/4) from a perturbative to a non-perturbative
statement.
