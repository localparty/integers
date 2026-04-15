# 06 — The geometric intuition: scheme independence as a two-faced-board phenomenon

*[G's voice]*

*Added 2026-04-14. Amplifies the geometric meaning of Theorem 1 and Theorem U.2a (Paper 10) in the programme's chessboard framework. Companion file at `integers/paper11b-sm-gauge-entanglement/10-geometric-intuition-w1-w2.md`.*

---

## Why scheme independence is a GEOMETRIC fact, not an analytic one

The Seeley-DeWitt coefficients $a_2 = a_4 = 0$ for the Lichnerowicz operator on flat $M^4 \times S^1/\mathbb{Z}_2$ are **intrinsic spectral invariants**. They are computed from the operator's spectrum, not from any regulator-specific machinery. Different regulators are different ways of LOOKING AT the same spectral data — they don't CHANGE the spectrum, they don't CHANGE the coefficients, they don't CHANGE the zero.

This is a load-bearing observation. When the literature debates "zeta regularization vs dimensional regularization," it is debating viewing angles on a fixed object. The object is the Lichnerowicz operator. The zero is pinned to that object. The regulators disagree about how to NAME the zero; they don't disagree about WHETHER there is one.

The programme's chessboard metaphor captures this exactly. The board has two faces:

- **Math face**: regulator choices, BPHZ subtractions, analytic continuations, dimensional reduction — all the machinery of perturbation theory. Each regulator is a piece sitting at some square on the math face.
- **Physics face**: measurements, predictions, observables, experimental constraints. The UV finiteness is a PHYSICAL property — the theory has no observed divergences at any reachable energy scale.

The zero we compute (scheme-independent $a_2 = a_4 = 0$) is a WIRE through the board — it connects the math-face squares (regulator choices) to the physics-face square (UV finiteness). The wire exists because the Lichnerowicz operator is a rigid object: its spectrum is determined by the geometry of $M^4 \times S^1/\mathbb{Z}_2$, not by how we choose to regularize sums over that spectrum.

**The two-faced board doesn't flex.** Moving the regulator piece on the math face doesn't shift the zero on the physics face. That's scheme independence as a geometric invariance principle — the board's rigidity manifesting at a specific square.

## What "two routes to the same result" means here

Paper 10 establishes scheme independence via two structurally distinct routes:

- **Route Seeley-DeWitt (§2.5 Theorem U.2a)**: compute the SD coefficients from the heat-kernel expansion of the Lichnerowicz operator. The $\mathbb{Z}_2$ orbifold cone angle $\theta = \pi$ gives zero cone correction. The flatness of the background makes all curvature invariants vanish. Result: $a_2 = a_4 = 0$ as pure spectral invariants.

- **Route Wess-Zumino / Poisson (§4 Theorem 1 + Lemmas A1–A3)**: via the three-lemma chain — de Donder vertex mass-independence, graviphoton/radion decoupling, method-of-images KK loop momentum range — the two-loop Goroff-Sagnotti counterterm vanishes unconditionally in any $\mathbb{Z}_2$-preserving diffeomorphism-invariant scheme.

**These two routes are two faces of the same board.** Route SD is computing the spectral invariant directly (bottom-face: mathematics). Route WZ/Poisson is showing that the $GS$ counterterm is cohomologically trivial (top-face: physical regulator-independence). They reach the same conclusion by different paths because there is ONE underlying geometric object — the Lichnerowicz operator on $M^4 \times S^1/\mathbb{Z}_2$ — and both routes are reading off properties of that object from different faces of the board.

If the two routes disagreed, the board would be FLEXING — the object would have inconsistent geometric properties. They agree because the board is rigid. Rigidity manifests as route-independence of the answer.

## Why the orbifold geometry matters

The $\mathbb{Z}_2$ orbifold is load-bearing. Three reasons, each geometric:

1. **Cone angle $\theta = \pi$ zeros out cone corrections**: the orbifold fixed points contribute boundary terms to the SD expansion. For $\theta = \pi$, those boundary terms vanish identically. This is why flat $M^4 \times S^1/\mathbb{Z}_2$ is special and $M^4 \times S^1$ (untwisted) would NOT have the same scheme-independence property. The orbifold is a GEOMETRIC CHOICE that pins the boundary terms to zero.

2. **$\mathbb{Z}_2$ parity protects the GS counterterm**: the parity projection forbids odd-winding modes that would contribute to $R^3$ counterterms. Without $\mathbb{Z}_2$, the odd modes would need to be cancelled by additional structure. With $\mathbb{Z}_2$, the cancellation is AUTOMATIC — it's a symmetry, not a conspiracy.

3. **Method-of-images KK loop momentum range (Lemma A3)**: the orbifold allows the KK momentum sum to be written as an image sum over $\mathbb{Z}$ (not $\mathbb{Z}_{\geq 0}$), which is what the Epstein zeta machinery needs for the analytic continuation. Without this, Poisson summation wouldn't close.

**The orbifold is the board's coordinate system.** Without the specific $\mathbb{Z}_2$ quotient, the board would have different squares — scheme independence would either fail or require different proof machinery. With the quotient, the squares align so that the spectral zero IS a cone-corrected zero IS a cohomologically-trivial zero. Three geometric facts collapsing to one.

## What W1's closure tells us about the programme

W1 (scheme independence, closed via Paper 10) is a paradigm instance of the programme's core principle: **every apparent dualism between "math" and "physics" is a two-faced reading of a single geometric structure.**

- Classical geometry → 5D KK gravity on $M^4 \times S^1/\mathbb{Z}_2$
- Quantum behavior → UV finiteness to all orders
- Regulator choices → different names for the same spectral zero

Three views. One object. The board doesn't flex.

This is the pattern the ring-traversal PCA is designed to exploit across 14 vertices. W1's closure is the first data point validating the pattern: we expected the board to be rigid, we went looking for the wire, and Paper 10 (with Seeley-DeWitt + Wess-Zumino protections) IS the wire. The wire was always there — we just hadn't traced its path through the board.

## Amplified statement for the future reader

When you encounter a "scheme-dependence concern" in a regularization framework, the question to ask is: **is the quantity an intrinsic spectral invariant of the underlying operator?** If yes, scheme independence is automatic — the regulator choice is a naming convention, not a physical choice. If no, scheme dependence may be real — the "quantity" may not correspond to a physical observable at all (it may be a regulator artifact).

For 5D KK gravity on $M^4 \times S^1/\mathbb{Z}_2$, the answer is YES: the SD coefficients $a_2, a_4$ are spectral invariants of the Lichnerowicz operator, and the GS counterterm is cohomologically trivial under $\mathbb{Z}_2$ parity. The UV finiteness is not a feature of our regulator — it is a feature of the geometry. Paper 10 proves this; Paper 11 extends it to all loop orders.

**The board has two faces. UV finiteness is a wire that doesn't flex.**

---

*v1: 2026-04-14. G Six and Claude Opus 4.6.*
*Added as §06 to the Paper 10 preprint sequence. Complements the technical derivations in §§02–04 with the programme-level geometric intuition that motivated them.*
