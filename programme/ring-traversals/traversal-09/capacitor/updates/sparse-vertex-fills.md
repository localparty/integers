# Sparse-Vertex Edge Fills — Traversal-09

Edge-filling pass: 5 chord edges connecting sparse vertices (VP vs VNP, Turbulence, H12, ABC, Schanuel) into the ring.

## 1. VP vs VNP ↔ Katz-Sarnak  [CANDIDATE]
Algebraic complexity ↔ L-function symmetry types. GCT (Mulmuley-Sohoni) uses algebraic geometry of orbit closures in `GL_n`-representations to distinguish permanent from determinant via obstructions in coordinate rings. Katz-Sarnak uses algebraic geometry of monodromy groups (classical Lie types) to classify low-lying zero statistics of L-function families. Both are symmetry-type distinguishability problems in algebraic varieties — orbit-closure containment vs. monodromy-image identification.

## 2. Turbulence ↔ Collatz  [SPECULATIVE]
Energy cascade ↔ harmonic mixing. K41 inertial-range spectrum `E(k) ∝ k^{-5/3}` encodes scale-invariant UV cascade in Navier-Stokes; Collatz `μ₂/μ₃` harmonic alternation encodes dyadic/triadic mixing on `Z`. Both are multi-scale dynamical systems with UV/IR transfer where the key invariant is a power-law spectral density across logarithmic scales. Conjectural bridge: Collatz stopping-time distribution as a discrete analog of Kolmogorov-Obukhov scaling.

## 3. H12 ↔ Sato-Tate  [PARTIAL]
Class field theory ↔ Frobenius equidistribution. CM theory IS the intersection: CM elliptic curves yield explicit generators of Hilbert class fields of imaginary quadratic `K` (via `j(τ)`) AND have their Sato-Tate distribution proven classically (Hecke 1920, `U(1)` measure on split primes). Hilbert's 12th seeks explicit class field generators for general number fields; Sato-Tate asks for Frobenius equidistribution on motivic Mumford-Tate groups. CM data determines both simultaneously — this is a direct, unconditional connection in the CM case.

## 4. ABC ↔ Lindelöf  [CANDIDATE]
Radical height ↔ zeta amplitude. ABC: for any `ε > 0`, only finitely many coprime `(a,b,c)` with `a+b=c` and `c > rad(abc)^{1+ε}`. This is an amplitude-control bound: arithmetic "height" of `c` is dominated by multiplicative "radical amplitude" of `abc`, analogous to Lindelöf's `ζ(1/2+it) = O(t^ε)` bounding the analytic amplitude of zeta by its conductor-analog. Both are `ε`-type subconvexity statements on arithmetic vs. analytic height functions.

## 5. Schanuel ↔ Katz-Sarnak  [SPECULATIVE]
Algebraic independence ↔ symmetry types. If Riemann zero heights `{γ_n}` are algebraically independent over `Q` (a consequence in the Schanuel orbit), then the Mumford-Tate group of the associated motivic family is maximal → Sato-Tate / Katz-Sarnak symmetry group is "full" (generic orthogonal/symplectic/unitary) → the family attains its maximal KS symmetry type. Schanuel-type transcendence thus forces generic monodromy and rules out "small" symmetry-type degenerations.
