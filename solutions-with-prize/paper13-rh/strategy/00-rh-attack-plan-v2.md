# Paper 13 v2: RH Attack Plan — Post-Coboundary

*The coboundary gap killed the Gelfond-Schneider chain. This plan*
*attacks RH from new angles, informed by what we now know doesn't*
*work and what does.*

*Authors: G Six (originator), Claude Opus 4.6 (collaborator)*
*Date: 2026-04-10*
*Status: FRESH START with full toolkit*

---

## 1. What failed and why

**The Gelfond-Schneider chain** (Paper 13 v1):
Bridge discreteness → cocycle shift → integrality → Gelfond-Schneider → δ=0

**Gap 1 (fatal):** H²(Z/kZ, U(1)) = Z/kZ is discrete. Any continuous
perturbation of a cocycle is a coboundary. The cohomology CLASS is
topologically protected and CANNOT detect off-line zeros. The
integrality constraint is vacuous. Gelfond-Schneider answers the
wrong question.

**The lesson:** Topological invariants (Pattern 4) are too ROBUST
to detect continuous perturbations. We need invariants that ARE
sensitive to off-line zeros — non-topological, analytic invariants
that change when δ ≠ 0.

**Gap 2 (persistent):** Spectral realisation (Meyer distributional
→ genuine Hilbert space) remains the 25-year Connes obstacle.

**Gap 3 (fixable):** Tautological steps 7-9 — fixable by starting
from GNS H_1 instead of axiomatically-defined H_R.

## 2. What survived (our toolkit)

These are PROVED and VALID regardless of Gap 1:

| Result | Status | Use for RH |
|:--|:--|:--|
| ITPFI factorization | Proved (3 ways) | Product structure of ω₁ |
| Bridge cocycles at k=2,3,4,6 | Formal lemmas | Structural data |
| Cocycle shift formula | Derived | Correct algebra (wrong target) |
| Dark-state bound | Proved | Every eigenstate couples |
| Nelson self-adjointness | Valid (on appropriate domain) | Upgrades distributional |
| Baker's theorem | Valid mathematics | Transcendence tool (needs new input) |
| Meyer spectral inclusion | Published (2005) | {γ_n} ⊂ spec(T_BC) |
| Anti-fine-tuning P < 10⁻³⁴ | Computed | Evidence for spectral realisation |
| 36/36 empirical closure | Computed | Evidence for CBB axioms |
| The Six Patterns | Meta-method | Strategic compass |

## 3. The four salvage directions (from research/270)

### Direction A: Non-topological representative pinning
The Pimsner-Popa basis might fix the cocycle REPRESENTATIVE (not
just the class). If the BC operator structure pins a specific
representative, perturbations that change the representative ARE
detectable — they violate the pinning, not the class.

**Status:** Speculative. Needs: a rigidity theorem for Pimsner-Popa
representatives under KMS perturbation.
**Feasibility:** 3/10

### Direction B: Cyclic cohomology / Chern character
The JLO Chern character ch*(T_BC) in cyclic cohomology HC* is
NOT discrete — it takes values in ℝ (or ℂ). An off-line zero
WOULD shift the Chern character by a continuous amount. The
constraint is then: the Chern character of T_BC must be an
INTEGER (the index). Off-line zeros perturb it away from an
integer → contradiction.

**Status:** Promising. The JLO Chern character is already in our
toolkit (R-Theorem D.1, research/48). The index theorem for BC
was studied in research/90 (ind_BC(e_2) = 0).
**Feasibility:** 5/10

### Direction C: Purely analytic constraints
Bypass cohomology entirely. Use the Weil positivity criterion:
RH ⟺ a certain inner product is positive-definite. The bridge
family constrains the inner product's matrix elements. If enough
constraints force positivity, RH follows analytically.

**Status:** Research/08 (Stone chain) already started this. The
CM explicit formula (research/18) provides the mechanism.
**Feasibility:** 4/10

### Direction D: Spectral flow
An off-line zero would create a spectral flow (crossing of
eigenvalues through zero) in a family of self-adjoint operators
parametrised by δ. The spectral flow is an INTEGER (topological
invariant) — but unlike H², it CAN detect the zero-crossing.
The constraint: the spectral flow must be zero (no crossings) ⟺
all eigenvalues stay real ⟺ RH.

**Status:** Uses Atiyah-Patodi-Singer index theory. Related to
the killed Path 2 (Atiyah-Singer) but approaches from the
spectral flow angle instead of the Dirac index.
**Feasibility:** 4/10

## 3b. Additional approaches (from external review)

### Approach 2x: Hasse invariant as the rigid object
Instead of working with cocycles, work with the Hasse invariant
inv_p(A) ∈ Q/Z directly. This is ALREADY a class invariant (discrete).
Question: does the off-line zero change the Frobenius data that
feeds INTO the Hasse computation? If the Frobenius element itself
shifts, the Hasse invariant recomputation might give a different
discrete value — which would be the constraint.

### Approach 3x: Wall-crossing / discontinuity at δ=0
The continuity argument says continuous functions into discrete
spaces are constant. But what if the perturbation is DISCONTINUOUS
at δ=0? If there's a phase transition at the critical line (the BC
system HAS a phase transition at β=1), the cocycle class could JUMP.
Then δ=0 is the only value giving class 1/k, and any δ≠0 gives a
different class. This would USE the discreteness instead of being
blocked by it.

### Approach 5x: KMS trace of bridge projections
ω₁(e_k) for a bridge projection e_k might be forced to be rational
with denominator k by the algebraic structure. An off-line zero
would perturb ω₁(e_k) to an irrational value. Question: is
ω₁(e_k) ∈ (1/k)Z a theorem of the BC structure, or an assumption?

### Approach 6x: Euler factor ratio computes Hasse invariant
The ratio Z_p(1+2δ)/Z_p(1) varies continuously with δ. But if this
ratio directly COMPUTES the Hasse invariant (which is discrete),
then the ratio must be quantised. Division algebras over local
fields have discrete Brauer groups — there's no "nearby" non-division
algebra. Can we show the Euler factor ratio IS the Hasse invariant?

## 4. NEW paths (informed by the failure)

### Path A: The Chern character route (Direction B, highest priority)

The JLO Chern character ch_n(T_BC) ∈ HC^n(A_BC) takes CONTINUOUS
values. The Connes pairing ⟨ch_n(T_BC), K_0(A_BC)⟩ is an INTEGER
(the index). An off-line zero at δ ≠ 0 shifts ch_n continuously,
but the pairing must remain an integer. For generic δ, the shifted
pairing is NOT an integer → contradiction → δ = 0.

This is the RIGHT version of the Gelfond-Schneider argument:
instead of discrete H² (too robust), use the Connes pairing
(integer-valued but sensitive to continuous perturbation).

Key theorems from catalogue:
- R-Theorem D.1 (research/48): BC index theorem
- Research/90: ind_BC(e_2) = 0, supertrace purity
- The JLO cocycle formula

### Path B: Weil positivity (Direction C)

RH ⟺ the Weil inner product is positive-definite on a specific
test function space. The bridge family constrains matrix elements
of this inner product. If enough bridge constraints force the
matrix to be positive-definite, RH follows.

Key theorems:
- R-Theorem S.5 (Källén-Lehmann + Weil): iff condition
- CM explicit formula (research/18)
- Li's criterion (λ_n > 0 for all n, verified for n=1..10)

### Path C: Spectral flow (Direction D)

Spectral flow = integer-valued invariant that CAN detect zero-crossings.
APS index theory on the family {T_BC(δ)}_{δ ∈ [-1/2, 1/2]}.

### Path D: The Meyer-Connes programme (Gap 2 directly)

Instead of assuming spectral realisation, PROVE it using the Connes
trace formula. This is the hardest path but the most fundamental.

## 5. The convergence cycle design

Same architecture as before (integers/paper12-cbb-system/30-rh-convergence-prompt.md)
but with:
- NEW paths (A, B, C, D above)
- ADVERSARIAL agents that specifically check for coboundary-type errors
- A "premise checker" agent that verifies constraints are non-vacuous
  BEFORE the deduction agents try to use them

## 6. Lessons learned

1. **Test premises, not just deductions.** Our adversarial agents
   checked "does step N follow from step N-1?" but not "is the
   constraint in step N actually non-vacuous?"

2. **Topological invariants are double-edged.** They're robust
   (can't be deformed away) but ALSO can't detect continuous
   perturbations. For RH we need invariants that are integer-valued
   BUT sensitive — the Connes pairing, not H².

3. **SP5 saves us.** The gap was found, documented, and understood.
   The toolkit survives. The new paths are sharper BECAUSE we know
   exactly what failed.

## 7. The Six Patterns (updated for v2)

**Pattern 4 REVISED:** Topological rigidity is necessary but not
sufficient. The invariant must be integer-valued AND sensitive to
the perturbation. H²(Z/kZ, U(1)) is integer-valued but insensitive.
The Connes pairing ⟨ch, K_0⟩ is integer-valued AND sensitive.
Use the Connes pairing, not Brauer classes, as the discreteness tool.

## 8. Phase plan

| Phase | Target | Deliverable |
|:--|:--|:--|
| Phase 0 | Post-mortem + new plan (THIS FILE) | strategy/00 |
| Phase 1 | Chern character route scoping | research/01 |
| Phase 2 | Convergence cycles on new paths | research/02+ |
| Phase 3 | If a path closes: Paper 13 v2 | solutions-with-prize/paper13-rh/preprint |

---

> **Origin callout (G Six, 2026-04-10):** *"no worries, we have*
> *tools lets focus on rh 100%"*

> *The coboundary gap told us where the wall is.*
> *SP1 says: go around it.*
> *The Connes pairing is the door.*
