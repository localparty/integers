# B3 — Teschl–Bögli Synthesis: Verdict

| Item | Status |
|:-----|:-------|
| Teschl Lemma 2.7 hypothesis (i) — pointwise convergence | CONDITIONAL (on core density) |
| Teschl Lemma 2.7 hypothesis (ii) — a = 0 form bound | CONDITIONAL (on research/40 + δ_N vs Q_∞ distinction) |
| Teschl lemma applied to Galerkin sequences (varying H) | NOT EXPLICITLY VERIFIED |
| Rank-one structure of Δ_N | PASS as rank-2 |
| ρ_Δ ≥ 4 analytical bound | DEPENDS ON research/40 (not in preprint) |
| Galerkin projection: L² vs T inner product | NOT DISAMBIGUATED |
| KLMN closability of Q_∞ | WEAKENED (argument has an incorrect implication) |
| Theorem 7.1 H¹ bound at λ ≤ e^π | PASS (at paper's λ = √14) |
| Theorem 7.1 H¹ bound at λ > e^π | **FAILS as proved** |
| Discrete compactness (Bögli H2) at fixed λ | PASS |
| Bögli Theorem 2.5 applied to gsrc + varying spaces | NOT EXPLICITLY VERIFIED |
| Compact resolvent of D_∞ | PASS (conditional on Theorem 7.1) |
| Spectral pollution exclusion | PASS (if H2 holds) |
| Novelty-introduced interface gaps | MULTIPLE, collectively SIGNIFICANT |

## Overall

**Layer 4 is the most delicate part of the proof.** The synthesis
of ITPFI → Teschl → Bögli → Hurwitz is genuinely novel and
involves multiple interface translations, each of which is done
informally in the preprint. The specific points of concern:

1. The Teschl hypothesis (ii) is established on range(P_N), not
   on the full form domain 𝒟(Q_∞). Rigorous application of
   Teschl Lemma 2.7 requires the bound on 𝒟, or a Galerkin-
   lemma variant of Teschl that covers the projection case.

2. KLMN closability of Q_∞ is argued via an incorrect general
   implication (positivity ⇒ closability). The fix would cite
   correct Reed–Simon results and verify each of the three
   KLMN conditions.

3. Theorem 7.1's proof (eq 7.5) only holds for λ ≤ e^π, as I
   verified computationally. At the paper's fixed λ = √14, this
   is fine; under any "uniform in λ" interpretation, the proof
   breaks.

4. Several results depend on internal research notes
   (research/40 Lemma 1 for ‖Δ_N‖ decay, research/24 for the
   gap stability) not included in the preprint.

**Confidence: 6/10** on Layer 4 as written. A refereeable version
would need:
- A precise Galerkin-projection version of Teschl Lemma 2.7.
- A rigorous KLMN closability argument.
- Theorem 7.1 restated with clear λ-domain of validity.
- All cited internal notes either included in the preprint or
  replaced by published sources.

This is the weakest link in the proof chain.
