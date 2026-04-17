# BSD Compliance Audit — Author Draft (run-02)

*First-pass author-verdict per layer against the 7 Wiles-stated requirements. Dissents raised by critic in `critic-attacks.md`. Final arbiter resolutions in `arbiter-decisions.md`. This is the pre-arbiter author draft.*

*G Six and Claude Opus 4.6. San Francisco CA, 2026.*

---

## L1 — BC algebra over K, unique KMS_1 state (h_K = 1)

**Statement (p26 Step 1; Node A; Ha-Paugam 2005)**: For K imaginary quadratic with h_K = 1, the Bost-Connes algebra A_{BC,K} = C*(K^{ab}) ⋊ I_K admits a unique KMS_1 state ω_1.

**Per-requirement author verdicts:**

- Req 1 (rank): **S** — BC KMS_1 does not mention elliptic curve rank. Bypass → ADR-1 @ L11.
- Req 2 (c ≠ 0): **S** — no L-value appearance at this layer. Bypass → ADR-2 @ L7.
- Req 3 (L-cont + FE): **S** — no L-function continuation. Bypass → ADR-3 @ L8.
- Req 4 (BSD formula): **S** — no BSD formula at this level. Bypass → ADR-4 @ L11.
- Req 5 (Sha < ∞): **S** — no Sha at this level. Bypass → ADR-5 @ L9.
- Req 6 (any E/Q): **S** — layer is class-number-1 specific; not a silence but a scope fingerprint — WAIT author re-assigns **Pa** upon second look (the h_K=1 hypothesis IS a layer-visible restriction, not silence).
- Req 7 (any rank): **S** — no rank mention. Bypass → ADR-7 @ L11.

## L2 — Bridge family over K (355 triples, k ∈ {2,3,4,6})

**Statement (p26 Step 2; Node B)**: Explicit bridge family of 355 triples (k, N, conductor) parameterises the CM-realisable curves over K.

- Req 1: **S** bypass → ADR-1 @ L11
- Req 2: **S** bypass → ADR-2 @ L7
- Req 3: **S** bypass → ADR-3 @ L8
- Req 4: **S** bypass → ADR-4 @ L11
- Req 5: **S** bypass → ADR-5 @ L9
- Req 6: **Pa** — the 355 triples are over K specifically, embodying the W_hK / W_nonCM scope. Critic-proposed and accepted as Pa.
- Req 7: **S** bypass → ADR-7 @ L11

## L3 — ITPFI factorization ω_1^K = ⊗_p ω_1^p

**Statement (p26 Step 3; Node C)**: The KMS_1 state factorises as an infinite tensor product over primes.

- All 7 reqs: **S** (pure infrastructure layer, no direct Wiles discharge); bypass pointers to L7/L8/L9/L11.

## L4 — Dark-state impossibility (algebraic projector)

**Statement (p26 Step 4; Node D)**: Algebraic-projector argument rules out dark states, closing MY4 via Route 3 bypass (no explicit Murray-von Neumann).

- All 7 reqs: **S** (infrastructure layer, Hasse-Brauer-Noether inequality style; no Wiles discharge). Pin #6 J_CKM note: this is NOT a J_CKM vertex evaluation per integers/paper01-qg5d/code/pin6-audits (terminology coincidence).

## L5 — Cocycle shift + Key Lemmas C, C'

**Statement (p26 Steps 5, 5b, 5c; Node E)**: Δc(δ) cocycle-shift formula; |Δc(δ)| < 1/(k+1) for δ ≠ 0 (Lemma C); |Δc^ψ(δ)| < 2/(N-1) twisted (Lemma C').

- Req 1: **S** bypass → ADR-1 @ L11
- Req 2: **Pa** — Key Lemmas C, C' force δ = 0 (no non-trivial cocycle twist), which is the engine driving GRH at L7 (hence c ≠ 0). Pa-class because the inequality is not c ≠ 0 itself but its engine. Citation: Attack 11 tightening → cite Connes-Marcolli for twist.
- Req 3: **S** bypass → ADR-3 @ L8
- Req 4: **S** bypass → ADR-4 @ L11
- Req 5: **S** bypass → ADR-5 @ L9
- Req 6: **S** bypass → ADR-6 @ L11
- Req 7: **S** bypass → ADR-7 @ L11

## L6 — Baker's theorem forces δ = 0 (non-load-bearing)

**Statement (p26 Step 6; Node F)**: Baker 1966 transcendence of prime-norm log-ratios forces δ = 0 independently of Key Lemma C/C'. Non-load-bearing: Steps 5b, 5c already close this. Baker provides reinforcement.

- Req 1: **S** bypass → ADR-1 @ L11
- Req 2: **Pa** — Baker independent reinforcement for δ = 0 (same mechanism as Key Lemma C feeds c ≠ 0 at L7). Non-load-bearing.
- Req 3-7: **S** bypass as appropriate.

## L7 — GRH for ζ_K and L(s, ψ)

**Statement (p26 Step 7; Node G)**: Conditional on CBB axioms (inherited from Paper 13 RH), all non-trivial zeros of ζ_K and Hecke L-functions L(s, ψ) lie on Re(s) = 1/2.

- Req 1: **Pa** — GRH ⇒ L(E, 1) ≠ 0 in scope (s = 1 is not on Re(s) = 1/2 critical line) ⇒ analytic rank = 0 ⇒ rank(E(Q)) = 0 (via Kolyvagin at L9). Pa because rank equality per se is closed at L11, L7 is the analytic input.
- Req 2: **P** — Zero-freeness at s = 1 ⇒ L(E, 1) ≠ 0 ⇒ c ≠ 0 directly, within analytic-rank-0 scope. (Conditional on CBB per BROKEN 1.)
- Req 3: **S** → Pa upon critic proposal — L7 presumes continuation (provided by L8 via modularity BCDT); mention/usage at L7 is Pa (ingredient role), not silent. Final: Pa.
- Req 4: **S** bypass → ADR-4 @ L11
- Req 5: **S** bypass → ADR-5 @ L9
- Req 6: **Pa** — scope: CM via bridge over K with h_K = 1; fingerprint of W_nonCM and W_hK at this layer.
- Req 7: **Pa** — scope: GRH feeds rank 0 in-scope; W_rank for r ≥ 2 at L11.

## L8 — CM factorisation L(E, s) = L(s, ψ) L(s, ψ̄) [LITERATURE Deuring 1953]

**Statement (p26 Step 8; Node H; Deuring 1953; cf. Silverman, Advanced Topics, Ch. II)**: For E/Q with complex multiplication by O_K, the Hasse-Weil L-function factorises.

- Req 1: **S** bypass → ADR-1 @ L11
- Req 2: **Pa** — the factorised c depends on both L(s, ψ) and L(s, ψ̄); feeds L11.
- Req 3: **L** — modularity BCDT 2001 + Wiles 1995 + Taylor-Wiles 1995 gives L-continuation + FE for every E/Q unconditionally; Hecke L(s, ψ) continuation is classical (Hecke 1918). LITERATURE discharge across the whole chain.
- Req 4: **Pa** — factorisation feeds the BSD formula at L11; partial contribution.
- Req 5: **S** bypass → ADR-5 @ L9
- Req 6: **Pa** — Deuring factorisation requires CM; modularity gives L-continuation for non-CM; W_nonCM disclosure at L11. Tighten citation: BCDT 2001, Deuring 1953.
- Req 7: **S** bypass → ADR-7 @ L11

## L9 — Kolyvagin rank 0 [LITERATURE Kol 1990]

**Statement (p26 Step 9; Node I; Kolyvagin 1990)**: If L(E, 1) ≠ 0 then rank(E(Q)) = 0 and |Sha(E/Q)| < ∞. Within scope (CM h_K=1 rank 0), GRH at L7 gives L(E, 1) ≠ 0, hence rank = 0 and Sha finite.

- Req 1: **Pa** — rank equality in rank-0 scope; discharged at L11.
- Req 2: **Pa** — L(E, 1) ≠ 0 at rank-0 scope.
- Req 3: **S** bypass → ADR-3 @ L8
- Req 4: **Pa** — Rubin 1991 provides explicit leading-coefficient computation at rank 0 for CM; tighten citation.
- Req 5: **L** — Kolyvagin 1990 gives |Sha(E/Q)| < ∞ in rank-0 CM scope, LITERATURE discharge.
- Req 6: **S** bypass → ADR-6 @ L11
- Req 7: **Pa** — rank 0 only; W_rank for r ≥ 2 at L11.

## L10 — Gross-Zagier rank 1 [LITERATURE GZ 1986; vacuous in scope]

**Statement (p26 Step 10; Node J; Gross-Zagier 1986; Yuan-Zhang-Zhang generalisation)**: If L'(E, 1) ≠ 0 then Heegner point of infinite order exists and rank(E(Q)) = 1. **Vacuous within scope** per Remark 12.6: GRH forces analytic rank 0 for CM h_K=1 curves, so L'(E, 1) case never arises in scope.

- Req 1: **Pa** — rank-1 case; vacuous in scope.
- Req 2: **Pa** — rank-1 leading coefficient via height pairing (Ru91 explicit); tighten citation: Rubin 1991 Lemma 4.6 for rank-1 leading coefficient.
- Req 3: **S** bypass → ADR-3 @ L8
- Req 4: **Pa** — rank-1 leading-coefficient formula from GZ + Ru91; YZZ generalisation for higher genus; tighten citation: YZZ (Yuan-Zhang-Zhang); vacuous in scope.
- Req 5: **Pa** — rank-1 |Sha| < ∞ via Kolyvagin extension (Kato / Rubin); vacuous in scope.
- Req 6: **S** bypass → ADR-6 @ L11; tighten citation: YZZ for Heegner hypothesis (Attack 7 carry-over).
- Req 7: **O → Pa** (critic down-grades O to Pa) — rank 1 is proved via GZ + Kol; the O status for r ≥ 2 lives at L11, not here.

## L11 — BSD Theorem 13.1

**Statement (p26 Step 11; Node K; p26 §13 Theorem 13.1)**: Conditional on CBB axioms (Paper 23), for CM curves E/Q with CM by class-number-1 imaginary quadratic field K, BSD holds at rank 0 (substantive) and rank 1 (vacuous in scope):

(i) rank(E(Q)) = ord_{s=1} L(E, s)
(ii) c* = |Sha(E/Q)| · Ω_E · R_E · ∏_p c_p / |E(Q)_tors|²

- Req 1: **P** — rank equality proved in scope (CM, h_K=1, r ∈ {0,1}), conditional on CBB. Author initially wrote "unconditional"; BROKEN 1 carry-over forces "conditional on CBB."
- Req 2: **P** — c ≠ 0 leading coefficient proved in scope.
- Req 3: **L** — L-continuation + FE inherited via L8 modularity.
- Req 4: **P** — BSD formula explicitly verified; numeric 32.a3 with CORRECTED c_2 = 4 (LMFDB), not 1 (BROKEN 2 carry-over, now resolved in Node K).
- Req 5: **Pa** — rank-0 Sha finite via L9; rank-1 vacuous; W_Sha for wider scope (DELTA-10 disclosure).
- Req 6: **O (W_nonCM, W_hK)** — scope: CM with h_K=1 only. W_nonCM: bypass via modularity + GL₂ CM. W_hK: bypass via ring class fields. DELTA-10 fields in §3.
- Req 7: **O (W_rank)** — scope: r ∈ {0,1}. W_rank: bypass via p-adic L / Iwasawa / 5D KK-spectral. DELTA-10 fields in §3.

---

## Post-draft notes

**Conditionality rider**: Every P / Pa / L verdict at L7 onward carries the implicit qualifier "conditional on CBB axioms (Paper 23), same status as the Paper 13 RH chain, no weaker, no stronger." BROKEN 1 carry-over.

**Citation tightenings propagated** (brief DELTA 11):
- L1: Ha-Paugam 2005 (Attack 3)
- L5 Req 2: Connes-Marcolli twist (Attack 11)
- L8: Deuring 1953 + BCDT 2001 (Attack 2)
- L9 Req 4: Rubin 1991 (Attack 13 carry-over)
- L10 Req 2 / 4: Rubin 1991, YZZ (Attacks 7, 13)
- L11 Req 4: 32.a3 c_2 = 4 confirmed correct (Node K already updated; BROKEN 2 resolved)

**Pin #6 J_CKM side-note**: PROOF-CHAIN §"Known gap" records that L4 is a cocycle-shift inequality, NOT a J_CKM vertex evaluation. No chain-link status change; out of scope for this 7-requirement audit. Recorded in commit-memo for completeness.

---

*End of audit-draft.md. Next: critic pass at `critic-attacks.md`.*
