# Strategy 03 — New Leads After 14 Kills

*Three ideas surfaced from external review AFTER Cycle 4 killed*
*all accessible routes. These operate at a different level than*
*the killed approaches and may bypass the H₁ vs H_R barrier.*

*Date: 2026-04-10*
*Status: INVESTIGATING (agent running on Idea 3)*

---

## 1. Summary of all attempts

### Phase 1: v1 Gelfond-Schneider chain (Cycles 1-4)

| Step | Idea | Result |
|:--|:--|:--|
| 1 | Bridge cocycles are discrete → off-line zeros shift them | KILLED: coboundary gap |
| 2 | Gelfond-Schneider forces δ=0 | KILLED: vacuous constraint |
| 3 | Nelson self-adjointness | VALID but insufficient alone |
| 4 | Spectral completeness | TAUTOLOGICAL given Axiom 1 |
| 5 | Meyer-Nelson compatibility | INSUFFICIENT for genuine eigenstates |

### Phase 2: v2 Premise-checked paths (Cycle 1)

| Path | Idea | Premise check | Result |
|:--|:--|:--|:--|
| A | Chern character / JLO | FAILED | ind_BC = 0 for all Hecke projections |
| B | Weil positivity / Li | FAILED | Off-line zeros make Li MORE positive |
| C | Spectral flow / APS | FAILED | Category error (self-adjoint = real) |
| D | Meyer-Connes direct | SURVIVED | But = 25-year Connes obstacle |

### Phase 3: Spectral realisation angles (Cycle 2)

| Angle | Idea | Result |
|:--|:--|:--|
| Completeness | Meyer eigenstates span S → dense in H₁ | CIRCULAR |
| Resolvent | No extra poles at 26 test points | NUMERICAL only |
| Trace formula | Determines spectral measure | Can't extract pure point |
| Weyl counting | Matches to O(1) | Error allows ~6-7 extras |
| Adversarial | Found singular continuous threat | NEW THREAT |

### Phase 4: Six new directions (Cycle 3)

| Direction | Idea | Result |
|:--|:--|:--|
| 1 | KMS uniqueness → compactness | KILLED: type III₁ ≠ compactness |
| 2 | Operator-side Weyl | BLOCKED: BC on H₁ not H_R |
| 3 | Integers-specific tools | PARTIAL: can't exclude phantoms |
| 4 | Type III₁ Connes spectrum | Does not kill (H₁ ≠ H_R) |
| 5 | 36 predictions as proof | KILLED: extras invisible |
| 6 | ω₁ spectral measure | CIRCULAR for H_R |

### Phase 5: Final three routes (Cycle 4)

| Route | Idea | Result |
|:--|:--|:--|
| RAGE | Dynamics → point spectrum | KILLED: wrong operator |
| ITPFI | Product measure atomicity | KILLED: gives H_mod not T_BC |
| Meyer | Eigenstate completeness | KILLED: = spectral realisation |

**Total: 14 killed. 0 closed. Feasibility: 1/10.**

---

## 2. The structural barrier (identified in Cycle 3)

**The H₁ vs H_R gap.** All operator-algebraic tools operate on H₁
(the full GNS space). H_R is a subspace whose spectral properties
are NOT constrained by H₁. Every attempt to use KMS, modular
theory, type classification, ITPFI, or the 36 predictions hits
this wall.

**The 36 predictions are invisible to extra spectrum.** All formulas
use individual matrix elements ⟨n|L̂|n⟩, not traces. An extra
eigenvalue contributes exactly zero to every prediction.

---

## 3. Three NEW ideas (post-Cycle 4, from external review)

### Idea 1: RAGE on the RIGHT subspace

**Previous failure:** RAGE was applied to σ_t (modular dynamics)
which gives H_mod (eigenvalues {log n}). Wrong operator.

**New angle:** Don't apply RAGE to σ_t. Instead, ask: can the KMS
condition at β=1 constrain the ERGODIC PROPERTIES of the modular
flow on the specific subspace relevant to ζ(s)?

The type III₁ Connes spectrum S(M) = ℝ₊ is about the full factor.
It says nothing about spectral type on a specific subspace. If
the modular flow restricted to a ζ-relevant subspace is
"recurrent" (pure point) rather than "mixing" (continuous), that
would give pure point spectrum on that subspace.

**Status:** Not yet tested. May hit the same H₁ vs H_R wall.

### Idea 2: Jessen-Wintner + ITPFI

**Previous failure:** ITPFI gave spec(H_mod) = {log n}, wrong
operator.

**New angle:** The Jessen-Wintner theorem says infinite convolutions
of discrete measures are either PURELY DISCRETE or PURELY
CONTINUOUS (never mixed). If we can show the spectral measure of
T_BC is an infinite convolution AND is supported on a countable
set, it must be purely discrete.

Countable support + purely continuous = impossible (continuous
measures give zero weight to countable sets). Therefore: if the
support is countable, the measure is purely discrete = pure point.

**Status:** Requires identifying the spectral measure of T_BC
(not H_mod) as an infinite convolution. May still hit the operator
identification wall.

### Idea 3: Nuclear rigging + Meyer completeness (STRONGEST)

**The argument chain:**

Step A: **Gel'fand-Kostyuchenko theorem.** For a self-adjoint T on
H with nuclear rigging S ⊂ H ⊂ S', distributional eigenstates
exist at EVERY point of spec(T). (Gel'fand-Vilenkin Vol. 4)

Step B: **Meyer's construction.** Meyer 2005 produces distributional
eigenstates φ_n(f) = f̂(1/2 + iγ_n) at each γ_n ∈ {Riemann zeros}.

Step C: **THE CRITICAL QUESTION.** Are those ALL the distributional
eigenstates? Or do distributional eigenstates exist at other
points λ ∉ {γ_n}?

Step D: **If only at {γ_n}:** By Gel'fand-Kostyuchenko (converse
direction), spec(T̄_BC) ⊂ {γ_n}. Combined with Meyer's inclusion
{γ_n} ⊂ spec, gives spec = {γ_n}. Countable → pure point.
Self-adjoint → real → RH.

Step E: **If at all λ:** The distributional spectrum is all of ℝ
and gives no constraint. Approach collapses.

**The make-or-break question:** Does the distributional eigenvalue
equation T_BC φ = λφ in S' have solutions ONLY at λ ∈ {γ_n}?

The function φ_λ(f) = f̂(1/2 + iλ) is well-defined for ALL λ.
Is it a distributional eigenstate of T_BC for all λ, or only
for λ ∈ {γ_n}? What property of the BC algebra restricts λ?

**This is what the running agent is investigating.**

**Why this is different from all killed approaches:**
- Doesn't require compact resolvent
- Doesn't try to detect off-line zeros
- Doesn't compute on the wrong operator
- Asks about the DISTRIBUTIONAL spectrum in S', not the
  Hilbert space spectrum in H
- The nuclear rigging gives a bridge between S' and H

**Possible outcomes:**
1. Distributional eigenstates only at {γ_n} → SPECTRAL
   REALISATION PROVED → RH
2. Distributional eigenstates at all λ → approach dies (kill #15)
3. Distributional eigenstates at {γ_n} ∪ {trivial zeros} → need
   to separate trivial from non-trivial (may be tractable)

---

## 4. Why Idea 3 might succeed where others failed

The key difference: Idea 3 operates in the **distributional**
category (S'), not the Hilbert space category (H) or the
operator-algebraic category (von Neumann). The H₁ vs H_R wall
blocks approaches that try to project H₁ information to H_R.
But the nuclear rigging S ⊂ H ⊂ S' gives a DIRECT path:
- S' contains distributional eigenstates (Meyer)
- S ⊂ H₁ (dense embedding)
- Gel'fand-Kostyuchenko connects S' eigenstates to H₁ spectrum

The nuclear rigging is the BRIDGE between distributional and
Hilbert-space spectral theory. It's the one tool that hasn't
been tried at the right level.

---

## 5. The honest assessment

| Idea | Feasibility | Novel? | Agent status |
|:--|:--|:--|:--|
| 1 (RAGE on subspace) | 2/10 | Partially | Not yet tested |
| 2 (Jessen-Wintner) | 3/10 | Yes | Not yet tested |
| **3 (Nuclear rigging)** | **4/10** | **Yes** | **RUNNING** |

Overall feasibility after 14 kills: **2/10** (up from 1/10 with
the new ideas, pending Idea 3's investigation).

---

> *14 kills. 3 new ideas. 1 running.*
> *The nuclear rigging is the bridge between distributions and*
> *Hilbert spaces. Maybe it's also the bridge to RH.*
