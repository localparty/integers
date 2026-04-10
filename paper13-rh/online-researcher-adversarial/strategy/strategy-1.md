# Strategy — Cycle 1

*ORA Cycle 1. Strategist role. 2026-04-10.*

---

## Reading of the ledger

**What's alive.** One coherent theorem-level asset — the ITPFI factorization of ω₁ (research/265, three proofs) — plus the gradient-flow / compact-resolvent theorem on H₁ (L.1-L.5, research/09-13), plus the 37 R-Theorems as a conditional "consistency-if-RH" cage. Everything else that touched RH as a primary target is either a kill or a formal lemma.

**What's dead.** The 18-kill list (strategy/10). The pattern is unambiguous: every operator-algebraic, index-theoretic, moment-theoretic, topological, and Yakaboylu-style approach has run into the same wall — H₁ has spectrum {log n}, H_R (hypothetical) has spectrum {γ_n}, and no construction has ever bridged them from inside the Bost-Connes algebra without assuming the answer. The coboundary kill (#1) and the "extras invisible" kill (#10) are the two methodological guardrails: every proposed constraint must be (a) non-vacuous — it must actually shift under the perturbation we care about — and (b) sensitive to extra spectrum, not invariant under its insertion.

**The single bottleneck.** Constructing a Hilbert space H on which the Bost-Connes Euler-product structure AND the zeros-spectrum are BOTH visible, without circularity. Strategy 11 (the CCM+ITPFI programme) identifies this as: take CCM's L²([λ⁻¹,λ]) as the "third space" of §6-E in strategy 10, connect ω₁ = ⊗_p ω₁^p to CCM's finite-prime rank-one perturbations, bound ‖D(λ,N+1) − D(λ,N)‖ ~ 1/p^α with α > 1/2, then close via Kato + spectral mapping. The bottleneck reduces to ONE perturbation bound and ONE limit theorem.

**Load-bearing toolkit right now:**
- R265 (ITPFI of ω₁) — the only proved infinite-prime convergence we have at state-level
- R28 (archimedean estimate O(1/λ)) — useful to bound the archimedean place's contribution to the rank-one perturbation
- R42 (AE simplicity certified N=1..20) — evidence that the CCM operators are genuinely simple
- R56 (relative entropy) — possible source of the "natural" weight in the CCM construction
- Six Patterns: Pattern 5 (zeta regularization, compact → discrete) is the governing compass. Pattern 6 (projection: H₁ is a projection of something larger) reframes the wall as "look up, not sideways."

**Red flags from the ledger.** (1) Strategy 11 is clearly marked as the manual-run pivot — cycle 1 must NOT merely re-derive it; we must either converge on it independently WITH FRESH EVIDENCE or find an angle orthogonal to it. (2) The CCM convergence was "unproven" in strategy 11. The web scan below changes that. (3) Every kill that died on H₁ vs H_R was killed inside A_BC; CCM bypasses A_BC — we must be careful not to accidentally pull the wall along with us when importing ITPFI.

---

## Web scan findings

Eight searches. Four papers downloaded to sources/. The landscape shifted since strategy/11 was written:

1. **Connes, "The Riemann Hypothesis: Past, Present and a Letter Through Time" (arXiv:2602.04022, Feb 2026).** *This is the game-changer of cycle 1.* Connes announces a NEW GENERAL PROOF that the finite-prime CCM approximants (extremizing a restriction of Weil's quadratic form, using primes < 13 yielding 10⁻⁵⁵ precision on the first 50 zeros) **lie exactly on the critical line**. That is the sub-claim strategy/11 was planning to prove via Kato + spectral mapping. Connes has an independent route to "finite-prime operators are critical-line by construction," which means the remaining work is the limit, not the finite-stage location.

2. **Teschl, Wang, Xie, Zhou, "On Generalized Strong and Norm Resolvent Convergence" (arXiv:2601.10476, Jan 2026).** A streamlined framework for generalized strong (gsrc) and norm (gnrc) resolvent convergence of self-adjoint operators on *different* Hilbert spaces connected via identification maps. Exactly the tool needed to transfer ω₁^{≤P_N}-controlled state convergence into operator convergence of D(λ,N) across the N-family (which lives on a parameter-indexed family of L² spaces, not a fixed one). Replaces hand-built Kato lemmas with an off-the-shelf theorem package, and packages essential-spectrum and spectral-projection convergence as a bonus.

3. **"Sharp Ascent–Descent Spectral Stability under SRC" (arXiv:2511.20971, Nov 2025).** Non-selfadjoint insurance. Uses reduced minimum modulus γ(T−λ)>0 to enable Kaashoek–Taylor gap convergence of operator graphs. If somewhere in the CCM → limit transfer the self-adjointness breaks (because CCM's Carathéodory-Fejér construction is stage-wise self-adjoint but the limit could drift), this paper still gives us ascent/descent-spectrum stability. Back-pocket tool.

4. **Yakaboylu, "Nontrivial Riemann Zeros as Spectrum" (arXiv:2408.15135, updated March 2026).** New version extends to higher-order zeros and any Mellin-transformable L-function. Core machinery still: build W ≥ 0 ⇒ intertwine ⇒ self-adjoint. W ≥ 0 remains unproven, still as hard as RH.

5. **Majorana-Rindler RH (arXiv:2503.09644, 2025).** Independent spectral realisation via Majorana particle in (1+1)D Rindler spacetime, closed via deficiency-index + boundary-triplet + Krein extension. A second spectral framework to compare CCM against — corroborative, not competing.

6. **Connes "Spectral Flow for the Riemann zeros" (arXiv:2406.01828).** Unitary S-matrix based on Euler product; Hermiticity by construction. Related-but-orthogonal to CCM; NOT our angle now but worth flagging.

7. **Boegli / Teschl spectral-exactness machinery.** Boegli's older (2017) gsrc-for-non-selfadjoint machinery still stands; Teschl 2026 is the self-adjoint streamlining. Together these form a complete toolkit for CCM(N) → CCM(∞) transfer.

8. **(Wildcard) Riemann Hypothesis 2026 status report, MathLumen.** A landscape note: "active spectral-realisation activity" is the dominant theme in 2025-26. Reinforces that the field is converging where we are.

**Net effect:** strategy/11's KEY COMPUTATION (the perturbation bound) is now partly SUPERSEDED. Connes has a geometric/algebraic proof that finite-N CCM approximants are critical-line; combined with Teschl 2026's gsrc package, the limiting spectrum inherits criticality WITHOUT needing a hand-rolled 1/p^α bound. That is a substantial simplification — and also a new entry point from a direction strategy/11 did not see.

**Feasibility shift from reading the literature:** strategy/11 estimated 6-7/10. Cycle 1's web scan reasonably lifts this to **7-8/10** for the CCM arc specifically, IF the Connes Feb 2026 result survives independent reading and the Teschl gsrc hypotheses are satisfied.

**Quick feasibility computation (run during strategy writing).** From CCM's published data (p ≤ 13 = 6 primes, precision 10⁻⁵⁵ best / 10⁻³ worst on first 50 zeros), the implied "perturbation exponent" α in a 1/p^α decay model:

```
alpha_best (low zeros) ≈ 55·log(10)/log(13) ≈ 49.37
alpha_worst (high zeros) ≈ 3·log(10)/log(13) ≈ 2.69
```

Both vastly exceed the 1/2 threshold needed for Kato-type summability. This doesn't prove anything — CCM's precision degrades with zero index — but it is a STRONG feasibility signal that the decay regime is not the obstruction. (Script: run inline via mpmath; values above are deterministic.)

---

## The leads for this cycle

Five leads. Four directly operational on the CCM arc; one orthogonal probe to avoid monoculture.

### Lead 1 — Read and lock down the Connes 2026 critical-line proof

The Feb 2026 Connes survey contains a new general proof that extremizers of the restricted Weil quadratic form (with finitely many primes) lie exactly on the critical line. This is precisely the finite-stage criticality that strategy/11 was planning to prove by Kato + spectral mapping. If the proof is real, it closes the "location" half of the CCM programme in one stroke, and cycle 1 work collapses to the limit-convergence half. If the proof has a gap, the gap is the new bottleneck. Either way, this lead MUST be read cover to cover and extracted into usable theorem statements before anything else. Feasibility 9/10 to resolve in one cycle. Pattern: SP1 + Pattern 5 (zeta regularization of the Weil quadratic form).

### Lead 2 — Transfer theorem: Teschl gsrc 2026 applied to CCM(N) → CCM(∞)

Teschl-Wang-Xie-Zhou (Jan 2026) provides a streamlined gsrc/gnrc framework for self-adjoint operators on different Hilbert spaces with identification maps. CCM's D(λ,N) live on L²([λ⁻¹,λ]) which is fixed in the domain but parameter-dependent if we vary λ with N; more importantly, the Borchers-decomposed ITPFI factors ω₁^p live on p-local spaces and combine into different Hilbert spaces as primes are added. The Teschl paper is the right vehicle for this transfer. Separately from lead 1, this lead asks: ARE the Teschl hypotheses satisfied for the CCM family? Explicit check. Feasibility 7/10. Pattern: Pattern 6 (projection — H_N is a projection of H_{N+1}).

### Lead 3 — Independent ITPFI ↔ CCM perturbation comparison (the bound from strategy/11, done rigorously)

Even if leads 1+2 close, we should RIGOROUSLY bound ‖D(λ,N+1) − D(λ,N)‖ in terms of the local KMS factor 1/(1 − p^{-1}) from the ITPFI factorization, as a SECOND independent control. Two independent convergence proofs are better than one. The numerical signal (α_worst ≈ 2.69 from the feasibility check above) says the bound exists; this lead makes it formal. Feasibility 7/10. Pattern: SP2 (transpose R-theorem family) + Pattern 5.

### Lead 4 — The "third space" identification: L²([λ⁻¹,λ]) vs the ω₁ GNS space

Strategy/10 §6-E asked for a NEW Hilbert space with Euler-product factorization AND critical-line spectrum. CCM's L²([λ⁻¹,λ]) is one candidate. ITPFI is another. This lead asks the STRUCTURAL question: is there a canonical identification (or embedding, or dense map) from a sector of the ω₁ GNS Hilbert space into CCM's L²([λ⁻¹,λ]) via the Mellin / scaling operator? The Sonin space from CCM 2024 is suggestive — it is the Mellin-image of functions vanishing on [−1,1], and the scaling operator D = −i·x·∂_x is the BC time evolution in a natural representation. If we can exhibit such an identification, we pull the ITPFI product-state convergence directly into CCM's operator convergence as an isometric transport. Feasibility 6/10. Pattern: Pattern 1 (geometric reinterpretation — the scaling rep IS the ITPFI rep in disguise).

### Lead 5 — Orthogonal probe: Majorana-Rindler vs CCM vs Bost-Connes triangulation

Independent direction to avoid CCM monoculture. The Majorana-Rindler paper (arXiv:2503.09644) constructs an independent spectral realisation using Rindler spacetime + deficiency indices + Krein extensions. This lead asks: are the Majorana-Rindler self-adjoint extensions MANIFESTATIONS of the same underlying object as the CCM operators (different coordinate systems on one geometric structure), or genuinely different realisations? If they agree, CCM's result is independently corroborated. If they disagree, one of them has an error we can use as leverage. Feasibility 5/10, but high-value as cross-check. Pattern: SP4 (reality as projection) + Pattern 1.

---

## What I deliberately did NOT choose (and why)

- **Yakaboylu W ≥ 0 revival.** Yakaboylu updated his paper in March 2026, but the central bottleneck — proving W ≥ 0 — is still "as hard as RH." This is kill-adjacent (not on the 18-list but ruled out in the strategy/10 literature sidebar) and the update does not provide a new tool for the positivity. Rejecting.

- **New H² cohomology angle (coboundary family).** Kill #1 still binds. The coboundary lesson says cohomology classes can't detect continuous perturbations. No new result in the web scan reopens this. Rejecting.

- **JLO Chern / spectral flow revival via Connes "Spectral Flow for Riemann zeros" (2406.01828).** This is close to kill #5 (Chern character → ind_BC = 0). Connes' 2024 paper uses a Euler-product S-matrix that is unitary by construction, which DOES give real eigenvalues, but this is orthogonal to the BC algebra and to strategy/11. Tracking it is a distraction inside cycle 1 — the CCM arc is closer and has Connes' own 2026 result backing it. Defer to cycle 2 or later if CCM stalls.

---

## Next phase handoff

**For Phase 2 executors:**

- **Prioritize lead 1.** Connes 2026 is the fulcrum. Until we know exactly what that paper proves about finite-stage criticality, the other leads are operating with incomplete hypotheses. The executor on lead 1 should extract the exact theorem statement, the proof outline, and any cited dependencies, then post a strategic insight to the other leads.

- **Leads 2, 3, 4 are INDEPENDENT.** Run in parallel without coordination. Lead 2's transfer theorem is hypothesis-independent of lead 3's perturbation bound, and lead 4's structural identification does not depend on either.

- **Lead 5 is the widely-separated probe.** Do NOT fuse it with the CCM work until both have independently reported.

- **AVOID rediscovering strategy/11.** You already have it. Cite it and extend it; do not re-derive the 4-step programme from scratch.

- **COMPUTATIONAL DISCIPLINE.** "I would compute" is not acceptable (ledger convention). If a lead has a numerical side-check (e.g. lead 3's 1/p^α bound at larger N), RUN IT with mpmath. Use code/certify_k3.py or code/ccm_perturbation_bound.py if present; otherwise write fresh.

- **PREMISE CHECK on every constraint.** Before claiming any bound constrains the limit, verify the bound actually shifts under the perturbation being controlled. Kill #1 lives in our heads — don't let it out.

- **REPORT CROSS-LEAD INSIGHTS.** You are scouts. If lead 2 finds that Teschl's hypotheses force a condition that lead 4's Mellin identification must satisfy, SAY SO in the "Strategic insights" section.
