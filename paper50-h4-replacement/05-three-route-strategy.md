# §05 — The Three-Route Strategy

*Overview of Routes A, B, C. Why parallel attack. Insurance against any one route failing. Ship criterion.*

---

## 5.1. The parallel-attack principle

H4 is hard. No single route to its closure is known to work; each route depends on external results whose applicability to pure 4D YM is not fully established. Betting on one technique — any technique — puts the entire H4 closure at risk.

The programme's answer: attack H4 along *three independent routes simultaneously*. Accept whichever closes first as the proof, document the others as alternative verifications or as cross-consistency checks. This is *insurance against route-specific failure*.

---

## 5.2. Route A — Resurgent Transseries + Lateral Borel

**Strategy.** Treat the perturbative series as an asymptotic expansion. Apply Écalle-Voros resurgence to construct a transseries completion. Use lateral Borel summation to resum the perturbative sectors + transseries sectors into a genuine distribution. Match this distribution against the non-perturbative Schwinger functions at short distances.

**Key inputs:**
- Écalle 1981, Voros 1983 resurgence theory.
- Klaczynski 2016 Dyson-Schwinger + transseries framework.
- Okuyama-Sakai 2022 (arXiv:2212.11988) 2D YM precedent.
- Paper 13 Layer 2 ITPFI factorization (§10's novel contribution).
- Paper 10 scheme independence (constrains transseries parameters).

**Obstruction.** IR renormalons make 4D YM's Borel transform have singularities on the positive real axis. The lateral Borel sum is ambiguous by exponentially small non-perturbative terms; fixing the transseries parameters to remove the ambiguity requires 4D-specific consistency conditions that are not yet established.

**Confidence: 3/10 initially.** A plausible path with substantial but incomplete machinery. The 2D precedent gives a template; extending to 4D is the hard step.

---

## 5.3. Route B — Kim-Sarnak-Shahidi via S-duality

**Strategy.** Paper 60 §21's S-duality diagnostic identifies H4 as the *CURVATURE-side* dual of Selberg's eigenvalue bound (RESONANCE side). Kim-Sarnak 2003 proved the best known Selberg bound ($\lambda_1 \geq 975/4096$) using symmetric-power L-functions and the Langlands-Shahidi method. Route B transfers this technique to YM's Wilson-loop L-function via the S-duality structure.

**Key inputs:**
- Kim-Sarnak 2003 ($\lambda_1 \geq 975/4096$).
- Kim-Shahidi 1999 (Sym$^3$ and Sym$^4$ L-functions).
- Langlands-Shahidi method (Eisenstein series on exceptional groups E$_6$, E$_7$, E$_8$).
- Paper 60 §21 S-duality diagnostic (CURVATURE ↔ RESONANCE pairing).

**Obstruction.** The Langlands-Shahidi method works for automorphic L-functions (modular forms, Maass forms). Transferring to YM's Wilson-loop L-function requires identifying pure YM with an automorphic-type system; this identification is not yet rigorous. Gaitsgory-Raskin 2024 geometric Langlands may provide the bridge.

**Confidence: 4/10 initially.** Strongest recent external support. The Kim-Sarnak machinery is the most powerful analytic tool available for this kind of short-distance bound.

---

## 5.4. Route C — Kapustin-Witten + Gaitsgory-Raskin

**Strategy.** Kapustin-Witten 2007 showed that N=4 super-Yang-Mills (topologically twisted) produces geometric Langlands. Gaitsgory-Raskin 2024 *proved* geometric Langlands (1000 pages, 9 authors, status: PROVED). Route C uses the KW twist to access YM Wilson-loop spectral data, then takes the decoupling limit (controlled by Paper 10 scheme independence) to extract pure YM from N=4 SYM.

**Key inputs:**
- Kapustin-Witten 2007 (N=4 SYM topological twist + electric-magnetic duality).
- Gaitsgory-Raskin 2024 (geometric Langlands PROVED).
- Elliott-Gwilliam-Williams 2024 (BV quantization of KW theories).
- Paper 10 scheme independence (controls N=4 → pure YM scale bridge).

**Obstruction.** The scale bridge from N=4 SYM to pure YM passes through the decoupling limit of extended supersymmetry. Controlling this limit rigorously requires the 2024 BV-quantization framework plus additional work to handle the breaking of $\mathcal{N} = 4 \to \mathcal{N} = 0$.

**Confidence: 3/10 initially.** Newest route, depends on the Gaitsgory-Raskin result being *applicable* to the specific scale-bridge limit. The most speculative of the three.

---

## 5.5. Why parallel, not sequential

A sequential strategy (fire Route A; if it fails, fire Route B; if it fails, fire Route C) has three defects:

1. **Serial timeline.** Each route takes months to years to reach a verdict. Three routes serially is three times longer.
2. **Commitment cost.** Sequential strategy locks in the first route's assumptions; if the route has a fatal flaw that emerges late, much effort is wasted.
3. **No cross-check.** If one route closes alone, there is no independent verification.

A parallel strategy has three advantages:

1. **First-to-close wins.** Whichever route crosses the proof threshold first becomes the canonical proof. The others pivot to verification roles.
2. **Cross-triangulation.** If two or more routes close, they provide independent verifications of the *same* H4 content. Consistency cross-checks the routes.
3. **Risk pooling.** The probability that *all three* routes have fatal flaws is the product of the individual failure probabilities — much lower than any single route's failure probability.

Paper 50's stance: parallel fire, accept the first finisher, cross-check the others.

---

## 5.6. Route interaction — the routes are not independent

A subtle point: Routes A, B, C are *structurally correlated*. They are three *realizations* of the same underlying symmetry — the functional equation / S-duality — applied to H4.

- **Route A (Borel summation)** exploits the analytic continuation of the Borel transform $B(t)$ from the perturbative side to the non-perturbative side. This is a *complex-analytic* realization of the functional equation.
- **Route B (Langlands-Shahidi)** exploits the functional equation of L-functions, which relates values at $s$ and $1-s$. This is an *arithmetic* realization.
- **Route C (geometric Langlands)** exploits the Langlands duality between geometric objects (local systems on a curve, D-modules on the moduli space of bundles). This is a *geometric* realization.

The three faces of the functional equation — analytic, arithmetic, geometric — correspond to the three routes. Closing any one is a realization of the underlying S-duality; the three routes *triangulate* the same phenomenon.

This is why the routes cross-check rather than compete: if Route A closes, it tells us something about *how* the S-duality acts on YM at the analytic level. Routes B and C, if they also close, verify the same S-duality from arithmetic and geometric perspectives.

---

## 5.7. Ship criterion

The programme's operational criterion: **ship whichever route reaches the proof threshold first.** The proof threshold is:

- A rigorous statement of the route's central theorem (e.g., "the lateral Borel sum of $S_n^{\mathrm{PT}}$ with transseries parameters fixed by [specific consistency] equals $S_n$ in the short-distance regime").
- A proof of the statement using the route's machinery.
- A verification that the route's output satisfies the precise form of H4 required by Paper 8 Link 18.

Once one route reaches this threshold, it becomes the proof of H4. The others pivot to:

- **Alternative verification**: independently re-prove H4 via their own machinery; check consistency.
- **Extension**: apply the technique to related problems (Selberg ¼ for Route B, geometric Langlands consequences for Route C, resurgence of other QFTs for Route A).
- **Cross-consistency check**: verify that the three routes predict the *same* H4 — the same OPE coefficients, the same Schwinger-function short-distance behaviour.

---

## 5.8. Honest risk assessment

The three-route strategy mitigates risk; it does not eliminate it. The scenarios are:

- **Best case (probability ~30%):** one route closes within 12-24 months. YM becomes 18/18 unconditional. Programme wins second Clay.
- **Good case (probability ~40%):** one route produces a sub-result that reduces H4 to a weaker conditional (e.g., closes H4 for abelian YM, or under an additional regularity assumption). Programme confidence upgrades but H4 not fully closed.
- **Hard case (probability ~25%):** all three routes stall at specific technical walls. H4 remains conditional indefinitely. Programme documents the walls and waits for external progress.
- **Worst case (probability ~5%):** a route *disproves* H4, i.e., shows that the perturbative series cannot match the non-perturbative Schwinger functions even asymptotically. This would invalidate Paper 8 Link 18 and require substantial rethinking.

The programme's stance: assume the best and good cases sum to ~70% probability. This justifies substantial investment in Paper 50. The hard and worst cases justify keeping H4 explicit in Paper 8 until one route closes.

---

## 5.9. Summary

Three routes. Parallel fire. First-to-close wins. Cross-triangulation via S-duality. Ship criterion: rigorous proof + verification of H4 in Paper 8 Link 18 form. Risk assessment: ~70% probability of sub-or-full closure within 12-24 months.

Paper 50's remaining sections (§§06-42) develop each route in detail, outline verification plans, and analyse implications. Part II (§§06-11) focuses on Route A — the resurgent transseries attack — which the next section begins.

---

*Paper 50 §05. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
