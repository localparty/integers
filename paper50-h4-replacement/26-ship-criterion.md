## §26 — Ship Criterion: Which Route to Formalize First

*Ship whichever closes first. The others become alternative verifications. Operational priority rules for the three-route parallel.*

---

## 26.1. The first-closure rule

Paper 50's shipping criterion is simple: **ship the first route that produces an adversarial-verified closure of H4**. The other two routes become alternative verifications — documented in the same paper as independent confirmations via different machinery.

The rule is first-closure rather than best-route because H4 is a binary target. H4 either holds or it does not. Once any one route produces a verified proof that H4 holds, the YM chain is 18/18 unconditional and Clay Millennium #4 is closed. There is no benefit to waiting for a "better" proof. The programme's goal is Clay closure, not proof-technique optimization.

The adversarial-verification requirement prevents premature claiming. A "closure" is not a draft — it is a draft that has survived an ORA v8 adversarial pass (four critics, at least fifteen attacks, zero BROKEN after repairs). Until this threshold is met, a route has not closed; it has only produced a candidate. The ship criterion applies to verified closures, not candidates.

---

## 26.2. What "alternative verification" means

When Route X closes first and Routes Y, Z are still in development, the latter become alternative verifications. This is a specific status, not a demotion.

**Status of X (primary proof):** X's proof chain is the paper's main result. Paper 50 presents X as the proof of H4, with full detail, full adversarial coverage, and full bibliographic attribution.

**Status of Y, Z (alternative verifications):** Y and Z are presented as independent proofs of the same target, with enough detail to show that each proof-chain's steps close. The level of detail for Y and Z is *sufficient for verification* but not *necessary for X's validity*. If Y or Z has a gap that X does not have, the gap is documented; X still stands.

The distinction matters because Paper 50 cannot wait indefinitely for all three routes to reach publication-grade completeness. The first-closure rule says: once X passes adversarial verification, ship Paper 50 with X as the main result and Y, Z as sketches with the status of each route's remaining gaps clearly marked.

Alternative-verification status is not a weakness; it is a strength. A paper with one verified proof and two independent sketch-verifications is *more* trustworthy than a paper with one proof alone. The multi-verification structure is a feature of the three-route strategy, not a compromise.

---

## 26.3. How to rank two simultaneous closures

Suppose two routes (say A and B) produce adversarial-verified closures in the same week. Which is the primary? The programme ranks by:

1. **Depth of external citation.** The route relying on more widely-accepted external results gets priority. Route B (Kim-Sarnak 2003, Langlands-Shahidi method) cites 20+ years of accepted automorphic-forms literature. Route C (Kapustin-Witten 2007, Gaitsgory-Raskin 2024) cites a more recent breakthrough. Route A (resurgence) cites a recently-active research frontier. Priority in a tie: B > C > A.

2. **Self-containedness of the proof.** The route whose proof requires the fewest programme-internal lemmas gets priority. If Route X reduces H4 to a single external theorem (e.g., Kim-Sarnak's bound), X is more portable than a route that requires programme-internal infrastructure at every step.

3. **Verifiability by non-programme experts.** The route whose proof a Yang-Mills expert outside the programme can verify without learning the full programme framework gets priority. This is a readership consideration: the widest audience gets the clearest proof.

4. **Sharpness of the claim.** If Route X proves H4 with a stronger quantitative statement (e.g., explicit bound on the OPE coefficient error) and Route Y proves the qualitative H4 only, X wins on sharpness.

The criteria are applied in order. Ties on criterion 1 go to criterion 2, and so on. The ranking is a last-resort mechanism; in practice one route typically closes first by weeks or months, and the ranking question does not arise.

---

## 26.4. Publication strategy given the ship criterion

Paper 50's publication happens in two waves.

**Wave 1: Primary closure.** The first route to close triggers the paper's publication. The paper's title — *Yang-Mills H4 Replacement: Route [X] closes the asymptotic-freedom match* — names the primary route. The abstract states that H4 is proved via Route X, with Routes Y and Z documented as alternative verifications (if complete) or as parallel programmes (if in progress).

**Wave 2: Secondary closures (if applicable).** If Routes Y and/or Z close subsequently (weeks to months after Wave 1), Paper 50 is revised to promote Y, Z from "alternative verifications" to "verified alternative proofs". The revision strengthens the paper's standing but is not required for the Clay Prize claim — Wave 1 already closes H4.

The strategy separates the *claim* (H4 proved) from the *robustness* (three independent proofs). The claim is made at Wave 1. Robustness accumulates as Wave 2 adds verified alternatives.

---

## 26.5. What happens if no route closes

The honest scenario: no route closes within the 12-24 month horizon. Paper 50 in this case documents the state of each route with precise gap identification:

- **Route A status.** The lateral Borel summation is constructed up to stage $k$; the obstruction at stage $k+1$ is the specific IR renormalon at Borel-plane location $\omega = \omega_*$, whose residue has not been rigorously computed.
- **Route B status.** The Wilson-loop L-function is constructed and shown to admit Sym$^k$ functorial lift for $k \leq 2$; the lift for $k = 4$ (required for Kim-Sarnak transfer) has obstruction at E$_6$ Eisenstein-series analysis.
- **Route C status.** The scale bridge from N=4 SYM to pure YM is constructed up to the decoupling of the adjoint scalars; the geometric-Langlands-to-short-distance extraction step remains incomplete.

Under this scenario, Paper 50 ships as a "state-of-the-attack" paper, not a closure paper. H4 remains conditional. The YM chain remains 17/18 unconditional. The paper's contribution is the parallel framework and three detailed partial attacks, which inform future work.

This fallback is the honest complement to the shipping criterion. The programme commits to publishing the paper in either outcome. A closure is ideal. A detailed partial attack is the second-best outcome — one that still advances the research programme by identifying exactly where the walls sit.

---

## 26.6. The anti-gold-plating rule

Ship first-closure even if the proof could be made shorter, more elegant, or better-bibliographed. The adversarial threshold (zero BROKEN after repairs) is the publication threshold. Any further polishing is gold-plating and delays the Clay claim.

If the primary closure is Route B's Kim-Sarnak transfer and it requires 80 pages of technical detail, Paper 50 ships 80 pages. A hypothetical Route B' that would do it in 40 pages via a cleaner argument is a future-paper project, not a Paper 50 delay.

The anti-gold-plating rule is programmatic: the programme's comparative advantage is speed under adversarial verification, not typographic perfection. Once H4 is closed, the paper ships.

---

## 26.7. Summary

The ship criterion is:

1. Run three routes in parallel.
2. First route to pass adversarial verification (zero BROKEN) becomes the primary proof.
3. Other routes are presented as alternative verifications at whatever completeness level they have achieved.
4. Paper 50 ships at primary closure, not at triple closure.
5. Subsequent closures (if any) trigger revisions, not new papers.
6. No closure triggers a "state-of-the-attack" paper with precise gap identification.

The criterion optimizes for the programme's goal (Clay Prize) not for route-parity or proof-elegance. The three-route structure is insurance (§24); the ship criterion is the cash-in rule for that insurance.

---

*Paper 50 §26. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
