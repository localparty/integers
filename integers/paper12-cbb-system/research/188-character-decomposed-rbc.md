# 188. Character-Decomposed RBC — Do Bridges Sit in Individual L(s, χ)?

*Cycle 10. Authors: G Six with Claude Opus 4.6. Date: 2026-04-09.*

> **Goal.** Test the surviving hypothesis of research/182: the CBB
> constants live in the trivial factor L(s, χ_0) = ζ(s) of the
> decomposition ζ_{Q(ζ_1729)}(s) = ∏_χ L(s, χ), while the
> non-trivial characters of (Z/13Z)* and (Z/19Z)* of orders 3, 4, 6
> encode the Koide, Pati–Salam, and CKM bridge cocycles with
> L'(1, χ)/L(1, χ) equal to the bridge cocycle value 1/k mod Z.

## 1. Setup

ζ_{Q(ζ_1729)}(s) = ∏_{χ mod 1729} L(s, χ), product over the 1296
Dirichlet characters of conductor dividing 1729 = 7·13·19. By CRT
each χ factorises as χ_7 · χ_13 · χ_19. The bridge-prime primitive
characters are those supported on a single one of {7, 13, 19}:

- **χ₀ (trivial)**: L(s, χ₀) = ζ(s). Carries γ_E = 0.57722… and γ_1.
- **Order-3 char χ₃ mod 13** (bridge k = 3, research/162, Koide).
- **Order-4 char χ₄ mod 13** (bridge k = 4, research/179, Pati–Salam).
- **Order-6 char χ₆ mod 19** (bridge k = 6, research/173, CKM).

All three primitive non-trivial characters were constructed from
generator g = 2 mod 13 (resp. mod 19) via χ(g^a) = e^{2πi a / ord}.

## 2. Computation

L(s, χ) evaluated by the Hurwitz identity L(s,χ) = q^{−s} Σ_a χ(a)
ζ(s, a/q), with mpmath at 50-digit precision. Pole of individual
ζ(s, a/q) at s = 1 is killed by the sum (since Σ_a χ(a) = 0 for
non-trivial χ), but to dodge numerical singularity I shift the
argument by an imaginary ε = 10⁻³⁰; L'(1, χ) computed by a
centred difference with h = 10⁻¹⁵.

## 3. Results

| character                | k | L(1, χ)                | L′(1, χ)               | L′/L at s = 1        | \|L′/L\| | target 1/k |
|--------------------------|---|------------------------|------------------------|----------------------|---------|------------|
| χ₃ mod 13 (Koide)        | 3 |  0.5663 + 0.3151 i     |  0.3664 − 0.0094 i     |  0.4870 − 0.2876 i   | 0.5656  | 0.3333     |
| χ₄ mod 13 (Pati–Salam)   | 4 |  1.0864 + 0.5814 i     | −0.0219 − 0.4045 i     | −0.1706 − 0.2810 i   | 0.3288  | 0.2500     |
| χ₆ mod 19 (CKM)          | 6 |  1.1719 + 0.8393 i     | −0.0022 − 0.7143 i     | −0.2898 − 0.4020 i   | 0.4955  | 0.1667     |

Ratios computed/target: 1.70, 1.32, 2.97. No mod-1 reduction, no
argument/phase rotation, and no simple rational factor recovers the
bridge values 1/3, 1/4, 1/6 from the raw L′/L quantities. The closest
near-miss is χ₄ (k = 4), where Re(L′/L) ≈ −0.17 and target is 0.25 —
off by ≳ 30 %.

## 4. Character-bridge match table

| bridge (k, p, N)     | predicted 1/k | L′(1,χ)/L(1,χ) match? |
|----------------------|---------------|------------------------|
| k = 3, (5, 13) Koide | 0.3333        | **NO** (0.566 mag)    |
| k = 4, (3, 13) PS    | 0.2500        | **NO** (0.329 mag)    |
| k = 6, (7, 19) CKM   | 0.1667        | **NO** (0.496 mag)    |

## 5. Verdict

**REFUTED in its naive form.** The guess that L'(1, χ)/L(1, χ)
*literally equals* the bridge cocycle value 1/k mod Z for the natural
primitive character of order k is wrong for all three bridges. The
logarithmic derivative of L(s, χ) at s = 1 is a transcendental complex
number with no clean relation to the Brauer class.

What the computation *does* show:
- Each bridge **character exists** with the expected order and
  conductor — the decomposition of ζ_{Q(ζ_1729)}(s) into one
  L-factor per Dirichlet character is well-defined and the
  order-3/4/6 primitive characters line up cleanly with the
  k = 3/4/6 bridges of research/162, 179, 173.
- L′(1, χ) is finite and non-zero for all three — the characters
  are "alive" at s = 1, consistent with them hosting *some*
  invariant, just not 1/k itself.

## 6. Reformulated survivor

The bridge cocycle is a **class in H²(G, U(1))** (a root of unity
on the nose), whereas L′(1, χ)/L(1, χ) is a transcendental number.
The right pairing must be via a **regulator**, not a raw
log-derivative:

> The Beilinson/Stark regulator of the motive attached to χ — i.e.
> the algebraic combination Im(L'(1, χ))/(some period) — should land
> in ℚ/ℤ and equal 1/k. The test in this note was the wrong
> functional; the next research (189) should compute the Stark
> unit ε_χ ∈ Q(ζ_N) such that L'(0, χ) = −log|ε_χ|, and read
> the bridge class off the Galois-action phases of ε_χ.

The RBC programme is not dead — but the physical bridge invariants
sit one level deeper than Taylor coefficients of L(s, χ). They
live in the Stark/Beilinson regulator layer.

**Status:** naive character-decomposed RBC refuted; Stark-regulator
RBC proposed as the next test (research/189).
