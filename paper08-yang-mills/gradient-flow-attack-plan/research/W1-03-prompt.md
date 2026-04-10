# W1-03: Heat Kernel Factorization on M⁴ × S¹/Z₂ (Lemma 2.1)

## Task
Write a rigorous proof memo establishing that the gradient-flow heat kernel factorizes on the product manifold M⁴ × S¹, and that the method of images gives the orbifold propagator on S¹/Z₂, reproducing S₀ = 1 + 2ζ(0) = 0.

## Statement to prove
On M⁴ × S¹: K_{M⁴×S¹}(t; x,y; φ,φ') = K_{M⁴}(t; x,y) · K_{S¹}(t; φ,φ'). On S¹/Z₂: K_{S¹/Z₂}(t; φ,φ') = K_{S¹}(t; φ,φ') + K_{S¹}(t; φ,-φ'). The KK mode sum from the orbifold propagator gives S₀ = 1 + 2ζ_R(0) = 0.

## Key inputs
- Paper 1, Appendix S, Section S.3.1: spectral zeta factorizes on product geometries
- The Laplacian on product: Δ_{M⁴×S¹} = Δ_{M⁴} + Δ_{S¹}, so e^{-t(Δ₁+Δ₂)} = e^{-tΔ₁} ⊗ e^{-tΔ₂}
- Paper 10, Lemma A3 (Section 5.2c): method of images on S¹/Z₂
- K_{S¹}(t; φ,φ') is the Jacobi theta function θ₃
- ζ_R(0) = -1/2 (Riemann zeta)
- The "1" in S₀ is the n=0 zero mode; "2ζ(0)=-1" is the image-doubled n≥1 tower

## What to read
- `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/30-appendix-s-finiteness-theorem.md` — Section S.3.1
- `/Users/gsix/quantum-geometry-in-5d-latex/paper10/preprint/04-poisson-weyl.md` — Lemma A3, Section 5.2c
- `/Users/gsix/quantum-geometry-in-5d-latex/paper1/appendices/22-appendix-k-higher-loop-epstein.md` — Section K.2.1

## What to write
1. Output: `/Users/gsix/yang-mills/gradient-flow-attack-plan/research/W1-03-heat-kernel-factorization.md`
2. Code: `/Users/gsix/yang-mills/gradient-flow-attack-plan/code/heat-kernel-factor/` — Compute: (a) K_{S¹}(t,φ,φ') via theta function for several t values, (b) verify S₀ = 1+2ζ(0) = 0, (c) verify method of images reproduces orbifold propagator numerically

## Output format
Self-contained proof memo with numerical verification. Include explicit formulas for K_{M⁴}, K_{S¹} (theta function form), and the orbifold propagator. Verify S₀ = 0 both analytically and numerically (mpmath, 50-digit precision).
