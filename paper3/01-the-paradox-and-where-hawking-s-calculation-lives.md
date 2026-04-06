## 1. The Paradox and Where Hawking's Calculation Lives


---

## 1.M Methodology: The Framework's Reasoning Patterns

This paper is one of seven in a series. Each paper applies the same
small set of reasoning patterns to a different domain of physics.
The patterns are documented in full in `readme.md`; the relevant ones
for this paper are identified below. Understanding which pattern a
derivation uses lets you see *why* the result works, not just *that*
it works — and lets you apply the same move to new problems.

The six patterns of the framework:

| # | Name | Core move |
|---|------|-----------|
| 1 | **Geometric Reinterpretation** | A 4D mystery is a shadow of simpler 5D geometry |
| 2 | **Holonomy Correspondence** | Wilson line VEV around a compact dimension → gauge phase |
| 3 | **Casimir as Scale-Setter** | Quantum vacuum energy on a compact space → a fundamental scale |
| 4 | **Topological Rigidity** | Discrete invariant (winding number, χ, homotopy) → exact quantized result |
| 5 | **Zeta Regularization of KK Towers** | Compact → discrete KK sum → analytic continuation → finite result |
| 6 | **Projection Produces Apparent Pathology** | 4D looks broken because 4D is a partial trace over the geometry |

**Primary patterns in this paper:**

- **Pattern 6** is the central resolution: the information paradox
  arises because Hawking's calculation is a partial trace over the
  e-dimension. The trace produces a mixed state by construction —
  not because information is destroyed, but because the e-coordinate
  is averaged out. Restore the e-dimension and the state is pure.

- **Pattern 1** resolves the problem of time: the Wheeler-DeWitt
  equation H|Ψ⟩ = 0 appears timeless in 4D because the clock is the
  e-coordinate, which 4D observers have projected out. Time exists
  in 5D as the phase advance along the e-circle.

- **Pattern 4** makes Theorem 9.1 unconditional: the horizon vertex
  factor is fixed by S¹ Fourier orthogonality — a topological
  identity that cannot receive metric corrections regardless of
  the 4D background geometry. Pattern 6 is what made the vertex
  look uncertain: the 4D projection hid the e-circle, making the
  vertex appear to depend on the black hole geometry. Restoring
  the 5D product structure reveals that the vertex is trivially 1.


---

### 1.1 The Information Paradox

In 1974, Stephen Hawking showed that black holes radiate thermally —
emitting particles with a Planck spectrum at the Hawking temperature:

    T_H = ℏc³ / (8πGMk_B)

This radiation carries no information. As the black hole evaporates,
all infalling matter — including its quantum state — appears to be
irreversibly destroyed. This contradicts the unitarity of quantum
mechanics, which requires that information is preserved in any closed
quantum evolution.

The tension can be stated precisely: quantum mechanics demands that
the evolution operator `U` satisfies `U†U = I` (unitarity). Hawking
radiation, being exactly thermal, corresponds to a mixed final state
regardless of the purity of the initial state. No unitary operator
maps a pure state to a mixed state. Therefore either quantum mechanics
is wrong, or general relativity is wrong, or Hawking's calculation
is missing something.

This is the black hole information paradox.

### 1.2 The Current State of the Art

The Page curve (Page 1993) provides the benchmark: if information is
preserved, the entanglement entropy of the Hawking radiation `S_rad(t)`
should rise during the first half of evaporation and fall back to zero
during the second half, returning to zero when the black hole fully
evaporates. Hawking's calculation gives `S_rad(t)` rising monotonically
— never falling.

Recent work by Penington (2019) and Almheiri et al. (2019) recovers
the correct Page curve using the "island formula" derived from
AdS/CFT and quantum extremal surfaces. This is the current state of
the art. However, the island formula is derived within specific
holographic settings (AdS spacetime) and its generalization to
arbitrary spacetimes remains unclear. More importantly, it does not
provide a physical mechanism — it provides a calculational prescription.

The question of *why* information is preserved — what is the physical
mechanism by which information escapes — remains open.

### 1.3 What Hawking's Calculation Assumes

Hawking's calculation proceeds in four-dimensional spacetime. He
computes the Bogoliubov transformation between modes defined in the
asymptotic past and modes defined in the asymptotic future, across
the background of a collapsing black hole. The result is thermal
because the vacuum state of the infalling modes is a thermal state
from the perspective of the asymptotic observer.

Crucially: the calculation traces over all internal states of the
black hole. In the language of density matrices, Hawking computes:

    ρ_rad = Tr_interior [|ψ⟩⟨ψ|]

This partial trace is what produces the mixed, thermal state. It is
not an approximation or an error — it is what the calculation is
designed to do.

In the 5D framework, we will show that this partial trace is not
over "interior states" — it is over the e-dimension. And integrating
over the e-dimension of a structured 5D state necessarily produces
a thermal 4D shadow. Hawking's calculation is correct. It is also
a projection.

---

