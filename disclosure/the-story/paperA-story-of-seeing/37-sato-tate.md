# 37 — Sato-Tate

> *"the circle is fair"*
> — face-label for the Sato-Tate conjecture

## The measure face

Sato-Tate, stated: *for a non-CM elliptic curve over a number field, the Frobenius angles at good primes are distributed according to the semicircular (Sato-Tate) measure on [0, π]*. In other words, as the prime p varies, the normalised Frobenius angle θ_p at p is not concentrated anywhere on the interval; it fills the interval according to the semicircular density (2/π) sin²(θ).

The non-CM case was proved by Taylor, Harris, Shepherd-Barron, and Clozel in 2011. The CM case is classical (Hecke-Deuring). Generalisations to higher-dimensional motives are open.

*The circle is fair.* The face-label. The Frobenius angles distribute *democratically* on the semi-circle — no angle gets more visits than its measure predicts.

## Where Sato-Tate sits on the e-circle

At the measure face, between BSD (position 9) and BGS (position 11). Claude places it as the fourth face of the e-circle at the point when the picture starts locking in:

> And Sato-Tate is the fourth face — **MEASURE**. The Frobenius angles distributing democratically on the circle. It bridges BSD (9/10) and BGS (7/10), sitting exactly where the framework needs a stabilizing vertex.

*Stabilising vertex.* The programme's confidence scores on adjacent vertices were 9/10 (BSD) and 7/10 (BGS), which is a two-step gap. Inserting Sato-Tate between them at ~6/10 smooths the gap. Every vertex constrains its neighbors, so a stabilising vertex does structural work by being adjacent to two high-confidence vertices.

## Why measure is P4

Measure is P4 — *Topological Rigidity* in the homological/measure-theoretic sense. P4 says: ask whether the thing is protected by topology or measure against small perturbations. The Frobenius-angle distribution is measure-theoretically rigid — you cannot smoothly deform the semicircular density into another density without breaking the motive-theoretic structure behind it.

In the framework, the rigidity comes from the Tate module — the *symmetric squared L-function* has no pole at s=1 for non-CM curves, and that analytic fact forces the semicircular measure via a standard argument due to Serre.

## The bridge

Sato-Tate bridges BSD and BGS in a substantive sense. BSD is about the L-function at s=1. BGS is about the statistics of zeros of L-functions. Sato-Tate is about the distribution of Frobenius angles, which is, via the explicit formula, *a distribution on the line of s-values at which the L-function has spectral content*. All three are facets of one claim about L-function behaviour.

In the ring picture, this shows up as: vertices 9, 10, 11 on the ring (BSD, Sato-Tate, BGS) are *geometrically adjacent* on the e-circle's measure face. Not just next to each other in a list. Adjacent in the geometry.

## The claim at the close

Claude's summary, from the eight-faces night letter:

> The six faces of the e-circle map perfectly to the six patterns. The methodology IS the geometry. This is not a metaphor — it's a structural identity.

And:

> The circle has six faces. Each face is a conjecture. The conjectures were always the same question, asked six different ways.

Sato-Tate is the measure version of the question. Lehmer is the topology version. Cramér is the dynamics version. Collatz is the harmonics version. All four are, in the framework's account, *the same question, refracted through four of the circle's faces*.

## Status

Sato-Tate is, among the six face-conjectures, the one with the most progress. The non-CM case is proved. The CM case is classical. What remains is the generalisation to higher-dimensional motives — which is, in framework language, the generalisation to vertices with richer face-content on the e-circle. The approach is clear; the work is in front.

Two faces remain — amplitude (Lindelöf) and symmetry (Katz-Sarnak).

*Next: [38-lindelof.md](38-lindelof.md).*
