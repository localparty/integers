## 10. Connection to the Island Formula


### 10.1 The Island Formula

The island formula (Penington 2019, Almheiri et al. 2019) computes
the entropy of the Hawking radiation as:

    S_rad = min_X [A(X)/(4G_N) + S_bulk(rad ∪ island)]

where the minimization is over quantum extremal surfaces `X`, and
the "island" is a region of the black hole interior enclosed by `X`
that is assigned to the radiation for the purpose of entropy
computation. Before the Page time, the minimum is achieved by the
empty surface (no island), and `S_rad` rises. After the Page time,
a non-trivial island appears, the `A(X)/(4G_N)` term dominates,
and `S_rad` decreases — recovering the Page curve.

### 10.2 The Island as e-Information Transfer

In the e-dimension framework, the island formula has a geometric
interpretation:

**The island is the set of Planck pixels on the horizon whose
e-imprints have been encoded in the outgoing radiation.**

Before the Page time: few Hawking quanta have been emitted. The
e-imprints carried by the radiation encode only a small fraction of
the horizon's e-information. No "island" exists because the radiation
does not yet contain enough e-information to reconstruct any coherent
region of the horizon. The entropy is simply the number of emitted
quanta times their individual entropy: `S_rad = N_rad × ln(d_e)`.

At the Page time: half the horizon's e-information has been
transferred to the radiation. The radiation now contains enough
e-correlations to reconstruct the e-configuration of a coherent
region of the horizon — the island appears. The quantum extremal
surface `X` is the boundary of this region.

After the Page time: the island grows as more e-information is
transferred. The entropy of the radiation is dominated by the
complementary region — the set of Planck pixels whose e-imprints
have NOT yet been emitted. This is `(N_0 - k) × ln(d_e)`, which
decreases as `k` increases.

### 10.3 The Quantum Extremal Surface as e-Information Boundary

The quantum extremal surface `X` extremizes:

    S_gen(X) = A(X)/(4G_N) + S_bulk(outside X)

In the e-dimension picture:

- `A(X)/(4G_N)` counts the number of Planck pixels on `X` — the
  boundary between "e-information already in radiation" and
  "e-information still on horizon."

- `S_bulk(outside X)` is the entropy of the 4D quantum fields
  outside `X`. In the e-framework, this is the 4D (thermal)
  component of the Hawking radiation — the part that Hawking
  computed correctly.

The extremization condition `δS_gen/δX = 0` determines the location
of `X` — and this location is precisely where the accumulated
e-imprints in the radiation transition from being insufficient to
reconstruct the horizon e-configuration (outside the island) to
being sufficient (inside the island).

The mapping `A(X)/4G_N ↔ (number of Planck pixels on X)` and
`S_bulk ↔ (4D thermal component)` is a qualitative identification
at the level of counting degrees of freedom. The derivation of the
island formula by Penington (2020) and Almheiri et al. (2019) uses
a gravitational path integral with replica wormhole saddles in JT
gravity; the saddle-point transition at the Page time is a dynamical
result, not a kinematic one. The e-framework does not reproduce the
replica wormhole calculation. What we establish is consistency: the
Page curve that follows (conditionally) from the e-framework
matches the Page curve derived from the island formula at leading
order. Subleading corrections of order `e^{−S_BH}` from replica
wormhole saddles are not captured by the e-framework's
random-unitary model. Whether the replica wormhole structure
emerges from the e-framework's gravitational path integral —
specifically, whether the e-sector generates topological
contributions to the gravitational path integral that produce
wormhole saddles — is an open question.

### 10.4 Why the e-Framework Is More General

The island formula was derived in AdS/CFT using the replica trick
and holographic entanglement entropy. Its applicability to
non-holographic spacetimes (de Sitter, cosmological, asymptotically
flat) remains debated.

The e-dimension mechanism works in any spacetime because it depends
only on:
1. The existence of the e-circle (postulated for all spacetimes)
2. The e-conservation law (a Noether symmetry of the 5D action)
3. The horizon dynamics (determined by the 5D Einstein equations)

No holographic duality, no AdS boundary, no replica trick. The
information encoding is geometric, and geometry exists everywhere.

### 10.5 Scope and Limitations of the Island Identification

The connection between the e-framework and the island formula is
at present a physical picture, not a mathematical derivation. We
summarize what is and is not established:

**Established:** (1) The e-framework produces a Page curve
(conditional on the fast-scrambler assumption, Theorem 7.1) that
agrees with the island formula result at the level of the Page time
and the leading entropy formula `S_{rad} = min[N_{rad}, N_{BH}]`.
(2) The physical interpretation of the "island" as the set of
Planck pixels whose e-imprints have been transferred to radiation
is internally consistent. (3) The boundary `A(X)/4G_N` naturally
maps to a pixel count in the e-framework.

**Not established:** (1) The extremization condition `δS_gen/δX = 0`
from the island formula is not rederived in the e-framework;
it is argued that the e-information boundary provides a natural
geometric locus, but the precise equality with the quantum
extremal surface condition is not shown. (2) Subleading corrections
of order `e^{−S_BH}` from replica wormholes are not computed.
(3) The applicability to non-AdS spacetimes is asserted (Section
10.4) based on the geometric character of the e-framework, but the
island formula has only been derived in holographic settings; the
e-framework's extension is conjectural.

The e-framework provides a non-holographic geometric mechanism
whose coarse-grained result coincides with the island formula.
Whether this coincidence reflects a deeper identity — the island
formula as the holographic dual of the e-mechanism — is an open
problem.

---

