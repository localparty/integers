# Research Note 206 — Convergence Round 4, Agent C

*Tension / correction-channel analysis.*

## Main-tally rows outside 1σ

Two rows in the main tally sit in [1σ, 3σ]:

1. **ξ (row 8).** ~1.4σ from P2 central. Sector: cosmology / CP² × S²
   moduli. Not spectral. No action; within framework-level noise
   floor. Channel: moduli (research/171/175/178) — no port needed.
2. **N_eff (row 2).** ~1.8σ from Planck 2018. Sector: cosmology.
   Driven by wide σ_exp (0.17). Hold for CMB-S4 / LiteBIRD narrowing;
   framework will likely re-absorb at CMB-S4 1σ ≈ 0.03.

Neither is a falsification candidate.

## Bookkeeping-gap rows (ESCALATED)

m_Z and v have now carried the `raw+stale` tag for three consecutive
rounds (1, 2, 3). Per the escalation rule added after round 3, I
must elevate them to Phase 4 with the specific port action:

> **Port research/154's (a, b) = (−γ_E(1+γ_E), γ_E²+ζ(2)−2π·γ_1)
> numerically into research/23's m_Z and v closed forms.**

### Sector attribution

Both rows are spectral-sector (γ_n operator matrix elements). Neither
is geometric, so the CP² × S² moduli correction channel is
inapplicable. Neither is interface (no CP²/spectral mixing in these
two rows). The channel is unambiguously research/154.

### Why research/167 doesn't resolve them

research/167 is a tautological operator-dictionary rewrite: at 50
dps every "Op value" equals the raw γ_n placeholder. Routing the
stale rows through research/167 does nothing (Agent A, three rounds
running). research/154 is the only active numerical correction
source in the corpus, and its (a, b) have never been ported.

### What "port" means concretely

For the v row: apply
`v_corrected = v_raw · (1 + a·ε + b·ε²)`
where ε is the Laurent expansion parameter identified in research/154
§2, and (a, b) are the closed forms above. Same shape for m_Z.
Port = insert the two Python/mpmath lines that compute this into
research/23's numerical evaluator, then re-tag both rows
`laurent-shifted` in sigma-exp-table.md.

## Recommendation

Hold round 5 until G executes the port. No other correction channel
is appropriate for these two rows.
