# Navier-Stokes Existence and Smoothness — Official Problem Statement

**Author of official statement:** Charles L. Fefferman, "Existence and Smoothness of the Navier-Stokes Equation"
**Source:** https://www.claymath.org/wp-content/uploads/2022/06/navierstokes.pdf
**Local copy:** `../00-clay-rules/navier-stokes-fefferman.pdf`
**Text extract:** `../00-clay-rules/navier-stokes-fefferman.txt`
**Retrieved:** 2026-04-14

---

## The Problem (verbatim)

The 3D incompressible Navier-Stokes equations (with viscosity ν > 0, velocity u = (u_1, u_2, u_3), pressure p, external force f):

> ∂u_i/∂t + Σ_j u_j ∂u_i/∂x_j = ν Δu_i − ∂p/∂x_i + f_i(x, t)   (eq. 1)
>
> div u = Σ ∂u_i/∂x_i = 0   (eq. 2)
>
> u(x, 0) = u°(x)   (eq. 3)

Physically reasonable solutions require, for R^3 problem:
- (4) decay of u° at ∞: |∂^α u°(x)| ≤ C_{αK} (1 + |x|)^{-K}
- (5) decay of f at ∞ (space and time)
- (6) p, u ∈ C^∞(R^3 × [0, ∞))
- (7) bounded energy: ∫ |u(x,t)|^2 dx < C for all t ≥ 0

For the torus T^3 = R^3/Z^3 problem, (4)(5) are replaced by periodicity (8)(9) and (7) by periodicity (10)(11).

## The four sub-problems (any one gives the prize)

Fefferman explicitly frames the problem as four alternatives. **Proving ANY ONE earns the prize:**

> **(A) Existence and smoothness of Navier-Stokes solutions on R^3.** Take ν > 0 and n = 3. Let u°(x) be any smooth, divergence-free vector field satisfying (4). Take f(x, t) to be identically zero. Then there exist smooth functions p(x, t), u_i(x, t) on R^3 × [0, ∞) that satisfy (1), (2), (3), (6), (7).

> **(B) Existence and smoothness of Navier-Stokes solutions in R^3/Z^3.** Take ν > 0 and n = 3. Let u°(x) be any smooth, divergence-free vector field satisfying (8); we take f(x, t) to be identically zero. Then there exist smooth functions p(x, t), u_i(x, t) on R^3 × [0, ∞) that satisfy (1), (2), (3), (10), (11).

> **(C) Breakdown of Navier-Stokes solutions on R^3.** Take ν > 0 and n = 3. Then there exist a smooth, divergence-free vector field u°(x) on R^3 and a smooth f(x, t) on R^3 × [0, ∞), satisfying (4), (5), for which there exist no solutions (p, u) of (1), (2), (3), (6), (7) on R^3 × [0, ∞).

> **(D) Breakdown of Navier-Stokes Solutions on R^3/Z^3.** Take ν > 0 and n = 3. Then there exist a smooth, divergence-free vector field u°(x) on R^3 and a smooth f(x, t) on R^3 × [0, ∞), satisfying (8), (9), for which there exist no solutions (p, u) of (1), (2), (3), (10), (11) on R^3 × [0, ∞).

## Euler note

Fefferman remarks the same problems are open for the Euler equations (ν = 0) but Euler is NOT on the Clay list.

## Errata (Fefferman)

> The further condition p(x + e_j, t) = p(x, t) should be made explicit in Eqn (8).

## Clay §5(b) note

NS IS a §5(b) problem: a resolution "in either direction" (smoothness or breakdown) earns the prize through the standard §7 evaluation procedure.
