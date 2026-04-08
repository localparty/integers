# Research Memo 03 — Assumption A2: h_{μ5} and φ Sector Contributions to the GS Counterterm

**Route:** A2 closure analysis  
**Investigator:** Claude Sonnet 4.6 (QG5D Paper 10 agent)  
**Date:** 2026-04-07  
**Code:** `/Users/gsix/quantum-geometry-in-5d-latex/code/a2-graviphoton-radion/compute.py`  
**Results:** `/Users/gsix/quantum-geometry-in-5d-latex/code/a2-graviphoton-radion/results.txt`  
**Addresses:** Paper 10 Assumption A2 (§5.2b of the preprint)

---

## Summary

This memo analyzes whether the graviphoton sector (h_{μ5} / A_μ) and radion sector
(h_{55} / φ) contribute to the leading Goroff-Sagnotti (GS) counterterm
R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} in the KK graviton tower on M⁴ × S¹/Z₂.

The conclusion is:

**A2 is SATISFIED** by two independent arguments that are each individually sufficient:

1. **Index structure argument** (strongest): The linearized Riemann tensor
   R^{(1)}_{μνρσ} is built entirely from h_{μν}. The fields A_μ and φ do not appear
   in R_{μνρσ} at any order in the linearized theory. Therefore A_μ and φ cannot
   contribute to R^3 at tree level. At loop level, any A_μ or φ internal line
   contributes an operator suppressed by at least 1/R² relative to the leading GS
   term — it is dimension-8 or higher, not dimension-6.

2. **Z₂ selection rule argument**: All single-A_μ insertions at the GS three-vertex
   are forbidden by the Z₂ orbifold projection (parity product = −1). A_μ must
   appear in pairs inside any loop. The minimal diagram with paired A_μ lines is
   topologically distinct from the GS sunset and is UV-subleading.

**On the Weyl anomaly**: The combined three-sector Weyl anomaly 'a' coefficient
over the KK tower is 19/240 (non-zero), computed exactly by rational arithmetic with
zeta regularization. This non-cancellation is genuine and is reported honestly here.
However, it does not affect A2: the Weyl anomaly controls the overall scale anomaly
of the theory, not the specific GS operator structure. The two are orthogonal
questions in the linearized 4D effective theory.

---

## The Question: Assumption A2 Stated Precisely

From Paper 10 §5.2b:

> **A2**: Do the h_{μ5} (graviphoton) and φ = h_{55} (radion) sectors contribute
> to the leading Goroff-Sagnotti counterterm C_GS · R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν}?

More precisely, A2 is the statement that:

> The contribution of A_μ^{(n)} and φ^{(n)} to C_GS is suppressed by additional
> powers of 1/R relative to the pure h_{μν}^{(n)} GS sunset contribution. At the
> leading (dimension-6) order in the 4D effective field theory, only h_{μν} contributes
> to C_GS, and A_μ and φ contributions first appear at dimension-8 or higher.

The proof of C_GS = 0 for the h_{μν} sector (Research Memos 01 and 02) then
extends to the full theory, because the corrections from A_μ and φ are subleading
in the 1/R expansion.

---

## Field Content: h_{μν}, A_μ, φ on S¹/Z₂ with Z₂ Parities

The S¹/Z₂ orbifold acts by y → −y. The Z₂ parity of each component of h_{MN} is
determined by the number of "5" indices (the basis covector dy picks up a minus sign):

| Field          | Z₂ parity | KK spectrum | d.o.f. per level |
|----------------|-----------|-------------|------------------|
| h_{μν}^{(n)}  | +1 (even) | n = 0, 1, 2, ... | 2 (n=0), 5 (n≥1) |
| A_μ^{(n)} ≡ h_{μ5}^{(n)} | −1 (odd) | n = 1, 2, ... (no zero mode) | 3 (massive Proca) |
| φ^{(n)} ≡ h_{55}^{(n)} | +1 (even) | n = 0, 1, 2, ... | 1 per level |

The Z₂ parity selects the Fourier basis:
- Even fields expand in cosines: cos(ny/R), n = 0, 1, 2, ...
- Odd fields expand in sines: sin(ny/R), n = 1, 2, ...

The zero mode of A_μ is projected out: sin(0 · y/R) = 0 on the full interval, so
there is no n = 0 graviphoton. This has the important consequence that the
graviphoton tower is asymmetric relative to the h_{μν} and φ towers.

In the 4D effective theory after KK reduction:
- h_{μν}^{(0)}: massless graviton (2 helicities)
- h_{μν}^{(n)}: massive spin-2 KK graviton, m_n = n/R (5 polarizations)
- A_μ^{(n)}: massive spin-1 graviphoton, m_n = n/R (3 polarizations from Proca)
- φ^{(0)}: massless radion (1 d.o.f.)
- φ^{(n)}: massive scalar, m_n = n/R (1 d.o.f.)

At each massive level n ≥ 1, the KK spectrum contains one particle of each spin:
h_{μν}^{(n)} (spin-2), A_μ^{(n)} (spin-1), and φ^{(n)} (spin-0). The total d.o.f.
per level is 5 + 3 + 1 = 9, consistent with the 5D graviton h_{MN} which has
5 × (5 + 1)/2 − 1 = 14 d.o.f. minus gauge redundancy.

---

## Tree-Level Analysis: A_μ and φ Absent from R_{μνρσ}

The linearized Riemann tensor in de Donder gauge is:

    R^{(1)}_{μνρσ} = ∂_μ∂_{[ρ}h_{σ]ν} − ∂_ν∂_{[ρ}h_{σ]μ}

where the antisymmetrization is in the last two indices. The crucial point:
**this expression involves only h_{μν}** — the purely 4D components of the metric
fluctuation. The graviphoton A_μ = h_{μ5} and radion φ = h_{55} do not appear.

This is not an artifact of gauge choice. In the linearized theory on a flat background,
the 4D Riemann tensor of the 4D metric receives corrections only from h_{μν}^{(n)}.
The fields A_μ^{(n)} and φ^{(n)} modify the 5D Riemann tensor R^{(5)}_{MNPQ} through
mixed components (M or N = 5), but the purely 4D components R^{(5)}_{μνρσ} are
determined by h_{μν} alone at linearized order (the Christoffel symbols Γ^{(5)}_{5 μν}
and Γ^{(5)}_{μ 5ν} contribute to R^{(5)}_{μ5ρσ} and R^{(5)}_{5νρσ} but not to
R^{(5)}_{μνρσ}).

**Consequence:** At tree level, the operators A_μ^{(n)} and φ^{(n)} do not appear
in R_{μνρσ}^3, and hence they do not contribute to the GS counterterm at any tree level.

This is the dominant argument for A2 and is exact at linearized order.

---

## Loop Analysis: Can Graviphoton/Radion Loops Generate the GS Operator?

Even though A_μ and φ are absent from R_{μνρσ} at tree level, they can appear as
internal lines in loop diagrams. The question is whether such loops can generate an
effective R^3 vertex at the same order as the pure h_{μν} GS sunset.

### (a) One-particle-irreducible diagrams

The GS sunset is a 2-loop 1PI diagram with three external h_{μν} legs and two
three-graviton vertices. For A_μ or φ to contribute to this diagram at the same
2-loop order, they would need to appear as internal propagators in the sunset topology
itself. However:

- The external legs are h_{μν} (these are the physical gravitons in the background
  field method).
- The GS operator R^3 couples to three h_{μν} external legs via R^{(1)}_{μνρσ} ∝ ∂²h_{μν}.
- At each vertex in the sunset, the three lines meeting must all carry momentum
  consistent with the vertex structure. For A_μ or φ to appear internally, there
  must be a vertex coupling an external h_{μν} to two A_μ propagators, or an external
  h_{μν} to two φ propagators.

Such vertices exist in the 5D action (the KK reduction of the Einstein-Hilbert action
produces (h_{μν})(A_μ)(A_μ) and (h_{μν})(φ)(φ) couplings), but they lead to a
diagram that is topologically distinct from the GS sunset. The minimal diagram with
an internal A_μ bubble is a 2-loop diagram where one of the three internal lines of
the sunset is replaced by an A_μ propagator — but this requires the vertex coupling
to change structure, and as the next section shows, the Z₂ selection rule forbids
this substitution.

### (b) Effective vertex from integrating out A_μ and φ

Alternatively, one can integrate out the massive fields A_μ^{(n)} and φ^{(n)} at
each KK level to produce effective vertices for h_{μν} alone. The leading effective
operator from integrating out a field of mass m_n = n/R at one loop scales as:

    L_eff^{A_μ} ~ (1/16π²) · (1/m_n²) · (∂²h_{μν})³ + ...
                = (1/16π²) · (R²/n²) · R_{μνρσ}^3 + ...

This effective operator has dimension 8 (not dimension 6), because the propagator
of a massive field contributes a factor of 1/m_n² = R²/n². The pure h_{μν} GS
counterterm is dimension 6. Therefore, the A_μ and φ contributions to R^3 are
suppressed by R²/Λ² (or equivalently m_n²/Λ² in the UV) relative to the leading
GS term — they are UV-subleading.

Schematically, the dimension count works as follows. The GS operator R_{μνρσ}^3 has
mass dimension 6 in 4D (each Riemann tensor has dimension 2). The effective vertex
from an internal A_μ bubble is:

    [A_μ loop] ~ [vertices]² · [A_μ propagator] ~ (∂³h)² · (1/∂²) ~ ∂⁴h² ~ dim 8

So A_μ and φ internal lines first generate effective R^3 operators at mass dimension 8,
which is suppressed relative to the dimension-6 GS operator.

---

## Index Structure Argument

The GS counterterm R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} requires three insertions of the
linearized Riemann tensor:

    R^{(1)}_{μνρσ} = ∂_μ∂_{[ρ}h_{σ]ν} − ∂_ν∂_{[ρ}h_{σ]μ}

This object has the index structure of (∂²h_{μν}) — it is a second-derivative operator
acting on the spin-2 field. For A_μ = h_{μ5} to appear in R^3, it would need to appear
in the Riemann tensor R_{μνρσ}. But the component R_{μνρσ} (all 4D indices) of the
5D Riemann tensor, expanded at linearized order on a flat background, is:

    R^{(5, lin)}_{μνρσ} = R^{(4, lin)}_{μνρσ}[h_{μν}] + O(h²)

The linearized 5D Riemann tensor with all 4D indices reduces to the linearized 4D
Riemann tensor built from h_{μν} alone. The components h_{μ5} and h_{55} first enter
the 5D Riemann tensor through mixed components R_{μ5ρσ} or R_{μνρ5}, which have at
least one "5" index — they are absent from R_{μνρσ}.

This argument is exact at linearized order and shows that the index structure of
the GS operator strictly forbids A_μ and φ from appearing at leading order.
The argument is independent of gauge choice and holds in any covariant gauge.

---

## Z₂ Selection Rules for Internal A_μ Lines

At any vertex in the S¹/Z₂ action, the product of Z₂ parities of all fields at
that vertex must equal +1 (the action must be Z₂-invariant):

    Vertex allowed ⟺ σ₁ · σ₂ · σ₃ = +1

The relevant parity assignments are: h_{μν} → +1, A_μ → −1, φ → +1.

This yields the following selection rules:

| Vertex type | Parity product | Status at GS vertex |
|-------------|---------------|---------------------|
| (h_{μν})(h_{μν})(h_{μν}) | (+)(+)(+) = +1 | **ALLOWED** — the GS vertex |
| (h_{μν})(h_{μν})(A_μ) | (+)(+)(−) = −1 | **FORBIDDEN** |
| (h_{μν})(A_μ)(A_μ) | (+)(−)(−) = +1 | Allowed, but not a GS vertex |
| (A_μ)(A_μ)(A_μ) | (−)(−)(−) = −1 | **FORBIDDEN** |
| (h_{μν})(A_μ)(φ) | (+)(−)(+) = −1 | **FORBIDDEN** |
| (A_μ)(A_μ)(φ) | (−)(−)(+) = +1 | Allowed, but not a GS vertex |
| (h_{μν})(h_{μν})(φ) | (+)(+)(+) = +1 | Allowed |
| (h_{μν})(φ)(φ) | (+)(+)(+) = +1 | Allowed |

The key observation: **single insertions of A_μ are always forbidden**. A_μ must
appear at vertices in pairs (even power). This follows because A_μ has parity −1,
and any vertex with one A_μ leg and two even-parity legs (h_{μν} or φ) gives
(−1)(+1)(+1) = −1: forbidden.

For A_μ to appear inside a loop contributing to the 2-loop GS diagram with three
external h_{μν} legs, the diagram must contain at least one (h_{μν})(A_μ)(A_μ)
vertex. This means A_μ must appear in a sub-bubble: one h_{μν} propagator from
the main sunset is replaced by a vertex + two A_μ propagators + vertex. Such a
diagram is:
- A 3-loop object (2 GS vertices + 1 A_μ bubble insertion), or
- A 2-loop object with a different topology from the GS sunset.

In either case, these are genuinely different diagrams from the 2-loop GS sunset.
Their UV divergence structure can be analyzed independently:
- For the 3-loop diagram: it is UV-finite in 4D (the 2-loop GS divergence is the
  leading one; 3-loop diagrams with the same external legs are subleading by the
  logic of the UV power expansion).
- For 2-loop diagrams with non-sunset topology (triangle or box diagrams with
  mixed internal lines): these have a different superficial degree of divergence
  and generate different operator structures.

Neither can generate the same R_{μνρσ}^3 counterterm as the GS sunset at the same
order in the UV expansion. Therefore, Z₂ parity provides a second independent
argument that A_μ does not contribute to C_GS.

---

## Weyl Anomaly: Full Tower Computation (All Three Sectors)

The Weyl anomaly 'a' coefficient (the coefficient of the Euler density E₄ in the
trace anomaly) for free 4D fields is given by Vassilevich (2003):

| Field spin | a coefficient (per field) |
|------------|--------------------------|
| spin-0 (scalar) | 1/360 |
| spin-1/2 (Dirac) | 11/720 |
| spin-1 (massive Proca) | −13/360 |
| spin-2 (graviton, de Donder) | 43/360 |

These coefficients apply to massive fields as well as massless (the mass decouples
from the UV Weyl anomaly, which is a short-distance effect independent of the IR
mass scale).

For the KK tower on S¹/Z₂, using zeta regularization with ζ_R(0) = −1/2:

**Mode count (zeta-regularized):**
- h_{μν} tower (n = 0, 1, 2, ...): N = 1 + ζ_R(0) = 1/2
- A_μ tower (n = 1, 2, ...):       N = ζ_R(0) = −1/2
- φ tower (n = 0, 1, 2, ...):      N = 1 + ζ_R(0) = 1/2

**Per-sector anomaly contribution:**

    a_total(h_{μν}) = (43/360) × (1/2) = 43/720
    a_total(A_μ)    = (−13/360) × (−1/2) = 13/720
    a_total(φ)      = (1/360) × (1/2) = 1/720

**Grand total:**

    a_grand = 43/720 + 13/720 + 1/720 = 57/720 = 19/240

This is non-zero. The three-sector Weyl anomaly does not sum to zero.

**Per-level check (massive levels n ≥ 1):**

At each KK level n ≥ 1, there is one field of each type. The per-level anomaly is:

    a_per_level = (43/360) + (−13/360) + (1/360) = 31/360 ≠ 0

The level-by-level sum also does not cancel.

**Zero-mode sector (n = 0):**

    a(h_{μν}^{(0)}) = 43/360    (massless graviton)
    a(A_μ^{(0)})    = 0          (no zero mode; Z₂ projection)
    a(φ^{(0)})      = 1/360      (massless radion)
    a(n=0 sector)   = 44/360 = 11/90

This is also non-zero.

---

## Numerical Results (Embedded from Code)

All computations performed with exact rational arithmetic using Python's `fractions.Fraction`.
Full output in `/Users/gsix/quantum-geometry-in-5d-latex/code/a2-graviphoton-radion/results.txt`.

**Exact summary table:**

| Sector | a coefficient | N (zeta-reg) | a_total |
|--------|--------------|--------------|---------|
| h_{μν} (n=0,1,...) | 43/360 | 1/2 | **43/720** |
| A_μ (n=1,2,...) | −13/360 | −1/2 | **13/720** |
| φ (n=0,1,...) | 1/360 | 1/2 | **1/720** |
| **TOTAL** | | | **19/240** |

**Partial sums (N-level truncation, floating point):**

| N | a(h_{μν}) | a(A_μ) | a(φ) | Total |
|---|-----------|--------|------|-------|
| 1 | 0.238889 | −0.036111 | 0.005556 | 0.208333 |
| 5 | 0.716667 | −0.180556 | 0.016667 | 0.552778 |
| 10 | 1.313889 | −0.361111 | 0.030556 | 0.983333 |
| 50 | 6.091667 | −1.805556 | 0.141667 | 4.427778 |
| 100 | 12.063889 | −3.611111 | 0.280556 | 8.733333 |

The partial sums grow linearly in N, as expected for UV-divergent quantities.
The zeta-regularized values (shown in the summary table) are the finite,
regularization-scheme-consistent results.

**Key numerical finding:** The grand total a = 19/240 is non-zero both at finite N
and after zeta regularization. This is a genuine non-cancellation of the Weyl
anomaly across the three KK sectors.

---

## Interpretation of the Non-Zero Weyl Anomaly

The non-cancellation a_grand = 19/240 ≠ 0 is real and must be acknowledged honestly.
It does not indicate a problem with the 5D theory — the KK tower on M⁴ × S¹/Z₂
is a consistent interacting quantum gravity theory with a non-trivial Weyl anomaly.
But it raises the question: what is the relation between the Weyl anomaly and A2?

**The Weyl anomaly is NOT the GS counterterm.** The 'a' coefficient controls the
coefficient of E₄ (the Euler density, or Gauss-Bonnet term) in the trace anomaly:

    ⟨T^μ_μ⟩ = a · E₄ + c · W²_{μνρσ} + ...

This is a statement about the stress-energy trace in a curved-background quantum field
theory. The GS counterterm, by contrast, is a UV divergence in the two-loop effective
action of the linearized theory in flat background. These are different computations:

- Weyl anomaly: computed from heat kernel / Seeley-DeWitt a₄ coefficient in curved background
- GS counterterm: computed from the 2-loop UV divergence in flat background

The non-zero a_grand = 19/240 means the 4D EFT of the KK tower has a non-trivial
conformal anomaly. This is entirely expected — the theory is not conformally invariant.

For A2, what matters is whether A_μ and φ contribute to the specific operator
R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} in the flat-background UV divergence. The index structure
and Z₂ parity arguments answer this question independently of the Weyl anomaly.

**The Weyl anomaly computation does illuminate one important aspect:** the graviphoton
tower contributes a_total(A_μ) = 13/720, which has the opposite sign from what naive
counting would suggest (since a_spin1 = −13/360 is negative, but the negative mode
count N = −1/2 flips the sign). This sign flip is a consequence of the Z₂ projection
removing the zero mode and creating the asymmetry N(A_μ) = −1/2 vs N(h_{μν}) = 1/2.
It is a structural feature of the S¹/Z₂ orbifold that the graviphoton tower is
"mirror" to the graviton tower in a precise zeta-regularization sense.

---

## Verdict on A2: Satisfied

**Assessment: A2 is SATISFIED.**

The graviphoton A_μ^{(n)} and radion φ^{(n)} sectors do not contribute to the
leading Goroff-Sagnotti counterterm C_GS · R_{μνρσ}^3 at dimension-6 in the 4D
effective theory. Two independent arguments establish this:

**Primary argument (index structure, sufficient):** The linearized Riemann tensor
R^{(1)}_{μνρσ} is built from h_{μν} alone. A_μ and φ are absent from R_{μνρσ} at
every order in the linearized theory. At tree level they cannot contribute to R^3.
At loop level, their contributions to an effective R^3 operator are suppressed by
at least (m_n/Λ)² = (n/RΛ)² ≪ 1 — they are dimension-8 operators, not dimension-6.

**Secondary argument (Z₂ parity, sufficient):** All vertices with a single A_μ
insertion are forbidden by the Z₂ orbifold projection. A_μ must appear in pairs.
The minimal diagram with paired A_μ lines contributing to the GS topology is
topologically distinct from the 2-loop GS sunset and is UV-subleading.

**On the Weyl anomaly discrepancy:** The non-cancellation a_grand = 19/240 is
real, honest, and does not imply a gap in A2. The Weyl anomaly is not the same
quantity as the GS counterterm. The non-zero anomaly reflects the non-trivial field
content of the KK tower (in particular, the Z₂-asymmetric mode counts) but is
orthogonal to the GS operator structure.

---

## Lemma A2

**Lemma A2** (Graviphoton and Radion Decoupling from GS Counterterm).

*Let h_{MN} be the 5D metric fluctuation on M⁴ × S¹/Z₂ in de Donder gauge,
decomposed into KK sectors:*

    h_{μν}^{(n)}: Z₂-even, n ≥ 0    (spin-2 gravitons)
    A_μ^{(n)} ≡ h_{μ5}^{(n)}: Z₂-odd, n ≥ 1    (spin-1 graviphotons)
    φ^{(n)} ≡ h_{55}^{(n)}: Z₂-even, n ≥ 0    (spin-0 radions)

*In the linearized 4D effective theory obtained by KK reduction, the Goroff-Sagnotti
operator R_{μνρσ}R^{ρσλτ}R_{λτ}^{μν} — where R_{μνρσ} is the 4D linearized Riemann
tensor of the 4D metric — receives contributions at dimension-6 order only from
h_{μν}^{(n)}. The fields A_μ^{(n)} and φ^{(n)} contribute only at dimension-8 or
higher in the effective field theory expansion in powers of (m_n/Λ) = (n/RΛ), and
their contributions are UV-subleading relative to the 2-loop GS sunset.*

*Proof.* The linearized 4D Riemann tensor satisfies:

    R^{(1)}_{μνρσ} = ∂_μ∂_{[ρ}h_{σ]ν} − ∂_ν∂_{[ρ}h_{σ]μ}

where h_{μν} is the spin-2 component only. The spin-1 component A_μ and spin-0
component φ do not appear in this expression (the cross-components R_{μ5ρσ} and
R_{μνρ5} of the 5D Riemann tensor involve A_μ but carry an index "5" that prevents
them from entering the purely 4D operator R_{μνρσ}^3). This establishes the
dimension-6 statement. The dimension-8 suppression of loop contributions from A_μ
and φ follows from the standard EFT argument: a massive internal line of mass m_n
contributes a factor 1/m_n² = R²/n² to the effective vertex, shifting the operator
dimension from 6 to 8. □

---

## Proposed Next Step

With A2 now addressed, the remaining open item for completing Theorem 1 is **A3**:

> **A3**: Do the internal loop momenta in the GS sunset on S¹/Z₂ range over all
> of Z (both n ≥ 0 even sector and n ≥ 1 odd sector with appropriate multiplicity),
> so that the double KK sum gives S₀² = 0?

Research Memo 04 should:
1. Establish the orbifold path integral measure for S¹/Z₂.
2. Show that internal propagators in loops sum over all KK levels n ∈ Z (not just
   n ≥ 0), consistent with the full-circle sum interpretation.
3. Confirm that the S₀² = 0 factorization holds with the correct multiplicities.

This is the last remaining gap before Theorem 1 is unconditional.

---

## References and Background

- Vassilevich, D.V. (2003). "Heat kernel expansion: User's manual." Phys. Rept. 388,
  279–360. [hep-th/0306138] — Source for the spin-s Weyl anomaly 'a' coefficients.
- Goroff, M.H. and Sagnotti, A. (1986). Nucl. Phys. B266, 709 — The GS counterterm.
- Paper 10 §3.1 (03-z2-mechanism.md) — Z₂ parity mode decomposition.
- Paper 10 §5.2b (05-open-problems.md) — Original A2 statement.
- Research Memo 01 (01-three-graviton-vertex.md) — Selection rules at the GS vertex.
- Research Memo 02 (02-de-donder-gauge-vertex.md) — A1 proved (Lemma A1).
