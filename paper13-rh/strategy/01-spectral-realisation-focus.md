# Strategy 01 — Spectral Realisation: The Single Remaining Door

*v2 Cycle 1 killed Paths A, B, C via premise checks. Path D*
*(Meyer-Connes / spectral realisation) is the ONLY surviving*
*approach. RH collapses to one question.*

*Date: 2026-04-10*

---

## 1. The one question

> **Does spec(T̄_BC) = {γ_n}?**
>
> (Does the distributional spectral inclusion from Meyer 2005
> extend to equality for the self-adjoint closure?)

If YES → spectrum ⊂ ℝ (self-adjointness) → γ_n ∈ ℝ → **RH**.
If NO → extra spectrum exists → 36 predictions need explanation.

## 2. Why everything else died

| Path | Kill reason | Lesson |
|:--|:--|:--|
| v1 Brauer cocycles | Coboundary gap — H² too robust | Topological invariants can't detect continuous perturbation |
| v2 Path A (Chern) | ind_BC = 0 for all Hecke projections | Zero index means zero constraint |
| v2 Path B (Weil) | Off-line zeros make Li MORE positive | Wrong direction — permissive not restrictive |
| v2 Path C (spectral flow) | Self-adjoint means real spectrum | Can't parametrize off-line zeros in self-adjoint framework |
| v1 Path 2 (Atiyah-Singer) | Distributional T_BC incompatible with index theorem | Category mismatch |
| v1 Path 4 (Penrose) | Lorentzian vs C*-algebra | Category error |

**Common thread:** Once T_BC is self-adjoint, spectrum is
automatically real. The "detection" question is malformed.
RH is not about detecting off-line zeros — it's about whether
T_BC IS self-adjoint on the right space with the right spectrum.

## 3. What we have

### Proved
- T_BC is symmetric on the GNS domain (BC algebra structure)
- Nelson gives essential self-adjointness (GNS vectors are
  analytic, cosh(t·log n) < ∞)
- Self-adjoint → spectrum ⊂ ℝ (spectral theorem)
- Meyer: {γ_n} ⊂ spec(T_BC) distributionally

### The gap
- Meyer's eigenstates are distributional (in S', nuclear Fréchet)
- Nelson upgrades T_BC to self-adjoint on H₁ (GNS Hilbert space)
- The distributional eigenvalues are in the APPROXIMATE spectrum
  of T̄_BC (this is proved — approximate spectrum is preserved
  under closure)
- **BUT: approximate spectrum ⊂ spectrum, not =**
- The gap: are there extra points in spec(T̄_BC) \ {γ_n}?

### The evidence against extra spectrum
- Anti-fine-tuning: P < 10⁻³⁴ from 33 empirical matches
  (research/201)
- Resolvent trace finite at 23 test points between consecutive
  γ_n (no extra poles found, Cycle 1 of v1)
- Li coefficients λ₁...λ₁₀ all positive
- Riemann-von Mangoldt zero count matches Weyl asymptotics

## 4. Attack angles on spectral realisation

### Angle 1: Completeness of {|γ_n⟩} in H₁
If the distributional eigenstates span a DENSE subspace of H₁
(not just S'), then T̄_BC has no room for extra spectrum.
This is a functional analysis question about density of Meyer's
test functions in the GNS Hilbert space.

**Key tool:** The Gel'fand triple S ⊂ H₁ ⊂ S' already gives
S dense in H₁. If Meyer's eigenstates span S, they span a
dense subspace of H₁. Does Meyer's construction give a
COMPLETE set of eigenstates in S?

### Angle 2: The Connes trace formula
Connes' trace formula (1999) relates the distribution of zeros
to the distribution of primes via the BC system. If the trace
formula determines spec(T̄_BC) UNIQUELY, spectral realisation
follows.

**Key tool:** The Connes-Marcolli explicit formula (research/18,
R-Theorem S.5) provides the iff condition.

### Angle 3: Resolvent analysis
Compute the resolvent (T̄_BC - z)⁻¹ at z between consecutive
γ_n. If the resolvent is bounded there (no extra poles),
spec(T̄_BC) has no extra points in those intervals.

**Already started:** Cycle 1 (v1) computed resolvent at 23
test points — all finite. Need to extend to ALL intervals
and prove boundedness, not just verify numerically.

### Angle 4: Weyl law + trace class resolvent
The Weyl law says #{γ_n ≤ T} ~ T/(2π) log(T/(2πe)). If
T̄_BC has compact resolvent (R̂^{-s} trace-class for Re(s)>1),
the eigenvalue counting function must match the Weyl law.
Any extra spectrum would perturb the counting function.

**Key tool:** If the eigenvalue counting functions match to
the precision of the Weyl error term, extra spectrum is
bounded. Combined with anti-fine-tuning, this could close.

### Angle 5: Direct construction (hardest)
Construct the Hilbert space H_R directly from the zeros,
prove T̄_BC acts on it with the right spectrum, and show
it's unitarily equivalent to a subspace of H₁.

This is essentially Connes' approach — 25 years open.

## 5. Recommended cycle 2 focus

**Angles 1 + 3 (highest leverage):**

Angle 1 (completeness) might close quickly: if Meyer's
eigenstates span S, and S is dense in H₁, spectral realisation
reduces to "Meyer's construction is complete." This is a
question about Meyer's specific construction, not about
general functional analysis.

Angle 3 (resolvent) is computational: extend the 23-point
numerical check to a proof that the resolvent is bounded on
every interval (γ_n, γ_{n+1}).

**Angles 2 + 4 (infrastructure):**

The Connes trace formula and Weyl law are background tools
that constrain extra spectrum. Both are partly in the
catalogue already.

## 6. The Six Patterns (v2 update)

**Pattern 4 (revised again):** Topological invariants (H²,
Chern character with zero index) can't detect perturbation.
Spectral realisation is NOT a topological question — it's an
ANALYTIC question about completeness of eigenstates. Use
analytic tools (resolvent, trace formula, density arguments),
not topological ones.

**Pattern 6:** The "difficulty" of RH was never about detecting
off-line zeros. It was about proving the operator T̄_BC has the
right spectrum. The difficulty was in the question, not the answer.

---

> *One question. Five angles. The door is spectral realisation.*
> *The wall was never topology. It was always analysis.*
