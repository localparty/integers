# Strategy 05 — Literature Leads and New Approaches

*16 approaches killed using only internal tools. The web search*
*revealed three external leads that our kills haven't touched.*
*One of them (gradient flow) is our native tool that nobody else*
*has applied to RH. Another (ITPFI → Connes gap) directly uses*
*a theorem we already proved.*

*Date: 2026-04-10*

---

## 1. What the literature search found

### The state of the art (April 2026)
- **Nobody has closed spectral realisation.** 167 years open.
- **Connes-Consani-Moscovici (2024):** Prolate wave operator +
  Sonin space. Access to low-lying zeros. Gap: finite-to-infinite
  Euler product convergence.
- **Yakaboylu (2024-2026):** Berry-Keating + Bessel operator.
  RH ⟺ W ≥ 0 for intertwining operator W. Published JHEP/ATMP.
- **LeClair (2024):** Scattering model, S-matrix from Euler product.
- **Rodgers-Tao:** de Bruijn-Newman Λ = 0 (proof must be exact).
- **Negative results:** Certain kernel-based operator classes ruled
  out (2026 spectral-dimension obstruction).

### What nobody has tried
- Gradient flow / heat kernels for spectral realisation
- Gel'fand triple techniques with the BC algebra
- KK-geometric operator origins (our CP²×S²×S¹ structure)
- The moment problem (we tried — kill #16, tautological)

## 2. The three new leads

### Lead 1: Yakaboylu W ≥ 0 (external, 2024-2026)

**What it is:** A non-symmetric operator R built from the
Berry-Keating xp Hamiltonian plus a Bessel regularisation.
An intertwining operator W connects R to a self-adjoint comparison.
RH ⟺ W ≥ 0 (W is positive semi-definite).

**Why it's different from our kills:**
- Kill #6 (Weil/Li): off-line zeros make Li MORE positive.
  Yakaboylu's W is a DIFFERENT operator with DIFFERENT positivity.
- Kill #7 (spectral flow): required parametrizing off-line zeros.
  Yakaboylu doesn't parametrize — W's positivity is a STATIC check.

**Integers connection:** Can W be computed from the BC algebra?
If the bridge family constrains W's eigenvalues, Integers would
add something nobody else has.

**Feasibility:** 3/10 (depends on whether W connects to BC)

### Lead 2: Gradient flow on T_BC (our unique tool)

**What it is:** The gradient flow ∂_t u = -T_BC² u on the GNS space.
Our Yang-Mills proof uses gradient flow extensively (Lemmas L.1-L.5
in the preprint): well-posedness, contractivity, small-field
preservation, K-uniform polymer decay.

**Why it's different from our kills:**
- None of our 16 kills used gradient flow. Every kill was about
  detecting off-line zeros or constraining spectral type via
  algebraic/topological tools.
- Gradient flow is ANALYTIC — it addresses the spectrum through
  DYNAMICS (long-time behavior), not topology or algebra.
- The flow's fixed-point structure determines spectral gaps.
- If the flow on T_BC² contracts to a fixed point, the spectrum
  is discrete with a gap — exactly pure point.

**Why nobody else has tried it:**
- Gradient flow for spectral problems is a PHYSICS tool (lattice
  gauge theory, Balaban's RG). Number theorists don't use it.
- We are the only group that has BOTH the BC algebra AND gradient
  flow expertise. The Yang-Mills preprint proves we can control
  gradient flow rigorously.

**Integers connection:** DIRECT. The gradient flow technology
from the Yang-Mills proof (contractivity, small-field, polymer
decay) is a PROVED toolkit. Applying it to T_BC² instead of the
Yang-Mills Laplacian is a change of operator, not a change of
method.

**Feasibility:** 4/10 (our strongest unique tool)

### Lead 3: ITPFI → Connes' gap (our proved theorem)

**What it is:** Connes identifies "finite-to-infinite Euler product
convergence" as THE remaining gap in his programme. We PROVED the
ITPFI factorization: ω₁ = ⊗_p ω₁^p (product state across primes).
This is LITERALLY an infinite Euler product convergence result.

**Why it's different from our kills:**
- Kill #13 (ITPFI atomicity) applied ITPFI to the wrong operator
  (H_mod not T_BC). But the factorization ITSELF is about ω₁,
  not about any specific operator.
- Connes' gap is about convergence of the trace formula as the
  number of primes increases. Our ITPFI proves the STATE converges.
  The question: does state convergence imply trace convergence?

**Why this is promising:**
- Connes HIMSELF identified this as the gap. We have a theorem
  (ITPFI) that's directly relevant. Nobody else has proved the
  state-level convergence that we have.
- The Sonin space (Connes' 2024 construction) might be the
  space where our ITPFI factorization lives.

**Integers connection:** DIRECT. ITPFI is our theorem. If it
closes Connes' gap, the proof comes from inside Integers.

**Feasibility:** 4/10 (depends on state → trace convergence)

## 3. Comparison: why these leads survive

| Lead | Category | Kills it avoids | Our advantage |
|:--|:--|:--|:--|
| Yakaboylu W ≥ 0 | Static positivity | #6 (different W), #7 (no parametrization) | Bridge might constrain W |
| Gradient flow | Analytic dynamics | ALL 16 (none used flow) | YM preprint proved the method |
| ITPFI → Connes | State convergence | #13 (wrong operator, but factorization is right) | ITPFI is our theorem |

## 4. The plan

| Priority | Lead | Agent | Target |
|:--|:--|:--|:--|
| 1 | Gradient flow on T_BC | Scoping + computation | Does the flow contract? |
| 2 | ITPFI → Connes' gap | Analysis | Does state convergence → trace convergence? |
| 3 | Yakaboylu W ≥ 0 | Scoping | Can W be computed from BC? |

## 5. Why we're still in the game

After 16 kills, we know MORE about what doesn't work than anyone
in the world. That knowledge is a tool. The gradient flow lead
exists because our Yang-Mills expertise gives us a method nobody
else has applied. The ITPFI lead exists because we proved a
theorem nobody else has. The Yakaboylu lead exists because the
literature has a new result we can try to connect to Integers.

16 kills made us the most informed attackers of spectral
realisation on Earth. Lead 17 is running.

---

> *16 kills made the question sharper.*
> *Gradient flow made Yang-Mills fall.*
> *ITPFI made the state converge.*
> *Maybe they make the spectrum discrete.*
