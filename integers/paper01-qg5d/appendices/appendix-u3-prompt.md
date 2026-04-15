# Prompt — Add §U.3 to Appendix U: Scheme-Independence Research Summary

<!-- Vocabulary canon note (Intervention 8b, 2026-04-15, aggressive migration applied): this file is an operational prompt using "5D" as subject-matter language. Per strategy/north-star.md §0.10 (Vocabulary Canon), canonical phrasing is "4+1 coordinate structure" / "M⁵". Inline strikethrough migrations applied per Intervention 8b. -->

**Issued by:** G (principal investigator)  
**Output:** A new section §U.3 appended to the END of:
`/Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/appendices/32-appendix-u-goroff-sagnotti-verification.md`

---

## Context

Paper 1 Appendix U currently ends with §U.2c titled "Scheme Independence: An Open Problem."
That section honestly states that the Epstein Vanishing theorem is proved in zeta
regularization but scheme-independence has not been established.

Five parallel research routes have now been completed (see
`/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/`) that collectively give strong
evidence — and in two cases outright proofs — that scheme-independence holds.

## Your task

1. **Read the existing Appendix U** at:
   `/Users/gsix/quantum-geometry-in-5d-latex/integers/paper01-qg5d/appendices/32-appendix-u-goroff-sagnotti-verification.md`
   Understand the current structure and where §U.2c ends.

2. **Read the synthesis** at:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/06-synthesis.md`
   This is the primary source for what to write.

3. **Optionally read any of the five route memos** for detail:
   `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/01-number-theoretic-zeta-zeros.md`
   `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/02-heat-kernel-seeley-dewitt.md`
   `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/03-z2-parity-cancellation.md`
   `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/04-poisson-dimreg.md`
   `/Users/gsix/quantum-geometry-in-5d-latex/paper9/research/05-weyl-anomaly-kk-tower.md`

4. **Write §U.3** as a new section appended to the end of Appendix U. Use the Edit tool.

## What §U.3 must contain

**§U.3 title:** "Progress Toward Scheme-Independence (Research Notes)"

**Length:** 150–250 lines — long enough to be substantive, short enough to be an appendix
section, not a paper.

**Required content:**

**§U.3.1 — What is now established**
Concisely state the two proved results:
- Seeley-DeWitt coefficients a₂ = a₄ = 0 on flat M⁴ × S¹/Z₂ (Route 02): intrinsic
  spectral invariants, scheme-independent by construction. One-loop UV finiteness proved.
- Weyl anomaly vanishing (Route 05): KK tower contributes a_total = (43/360)×[1+2ζ(0)] = 0,
  protected by Wess-Zumino consistency. Covers the GS C³ operator scheme-independently.

**§U.3.2 — Supporting evidence**
Briefly summarize the three demonstration routes:
- Z₂ parity (Route 03): algebraic term-by-term cancellation at each KK level, before
  summation, in any Z₂-preserving scheme
- Poisson bridge (Route 04): dim-reg 1/ε coefficient equals S₀² = 0 via a provable
  exchange lemma; scheme difference is O(e^{−2πRk})
- Number-theoretic (Route 01): subleading Epstein zeros are 1/Γ(−j) = 0, a Gamma
  function fact independent of regularization

**§U.3.3 — The remaining open problem**
Be honest: one gap survives across all routes. Vertex mass-independence — whether the
GS three-graviton vertex in 5D KK gravity is mass-independent at leading UV order —
has not been explicitly computed. State what the computation requires (KK decomposition
of the three-graviton vertex, elementary trig integrals over [0, πR]), and cite Paper 10
(in preparation) for the full treatment.

**§U.3.4 — Two-sentence theorem**
End with a boxed or clearly marked theorem statement:

> **Theorem U.2 (partial).** The one-loop UV finiteness of 5D linearized gravity on
> M⁴ × S¹/Z₂ is scheme-independent: the Seeley-DeWitt coefficients a₂ = a₄ = 0 are
> intrinsic spectral invariants of the Lichnerowicz operator on this background,
> independent of regularization choice. The scheme-independence of the two-loop
> (Goroff-Sagnotti) vanishing is established up to the vertex mass-independence
> assumption; the full proof is in preparation (Paper 10).

**Tone:** This is an appendix to a published paper — precise, honest, forward-looking.
Do not oversell. §U.2c already set the right tone; §U.3 updates it without walking
anything back.

**Cross-references:** Reference `/paper9/research/` as the source of the five route
computations. Reference Paper 10 (in preparation) for the full scheme-independence proof.
