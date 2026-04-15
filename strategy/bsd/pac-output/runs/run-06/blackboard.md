# Run-06 Blackboard — BSD Pillar-C HARDEN

## Plan

1. Read universal-approval-run.md §5C, bsd strategy+brief, bsd-independence-bare §7.3 (retained externals), bsd-comply-bare (context), landscape.md (attribution).
2. Enumerate 15 retained externals per §7.3.
3. Rank by load-bearing weight (top 5: BCDT, Kolyvagin, Skinner-Urban, GZ, CBB).
4. Write 7-section bare harden deliverable with §2 inventory table + §3 per-external stubs.
5. First-wave (5): detailed PAC proposals.
6. Second-wave (10): one-paragraph stubs.
7. §5 double-kill narrative.
8. §6 cross-vertex coordination matrix.
9. Lock + commit memo.

## 15 externals roster (source: bsd-independence-bare.md §7.3)

1. BCDT 2001 modularity [primary L8/L11]
2. Kolyvagin 1990 Euler system [L9]
3. Skinner-Urban 2014 IMC-GL₂ [W_rank B, W_nonCM γ, W_Sha θ]
4. Gross-Zagier 1986 [L10 vacuous / W_rank C / W_nonCM γ]
5. CBB / paper23 [L7-L11 rider]
6. Ha-Paugam 2005 BC over K [L1, L2, W_hK δ]
7. Rubin 1991 IMC-CM [L9 Req 4, W_Sha η]
8. Mazur-Wiles 1984 [W_Sha ι]
9. Perrin-Riou 1992 [W_rank A]
10. Burungale-Skinner-Tian-Wan 2024 [W_nonCM γ]
11. Connes-Marcolli 2008 GL₂ BC [W_nonCM β]
12. Newton-Thorne 2021 [W_rank C]
13. Nekovář 2001 [W_rank C]
14. Yuan-Zhang-Zhang 2013 [W_hK ε, W_nonCM γ, W_rank C]
15. Gross 1984 [W_hK ε]

## Priority ranking (load-bearing weight)

- **Top 5 (first-wave)**: BCDT (L-cont universal) > Kolyvagin (rank-0 closure) > Skinner-Urban (W_rank primary) > GZ (rank-1 + scope-ext) > CBB (programme-internal, joint with RH).
- **Second-wave batch A (tight load-bearing)**: Ha-Paugam > Rubin > Perrin-Riou > YZZ.
- **Second-wave batch B (specialised)**: Connes-Marcolli > Newton-Thorne > Burungale-STW > Nekovář > Mazur-Wiles > Gross 1984.

## PAC primitives per first-wave external

- BCDT: VERIFY 7-layer chain, CONSTRUCT R=T-as-KMS-projection, BYPASS via Kisin framework, DECOMPOSE residual-case split, EXCISE trivial cases.
- Kolyvagin: VERIFY Euler-system layers, CONSTRUCT KMS-tower reading, BYPASS via Bertolini-Darmon / Wan 2014, DECOMPOSE Tate-Poitou sub-cases, EXCISE Heegner-hypothesis redundancy.
- Skinner-Urban: VERIFY 6-layer IMC chain, CONSTRUCT p-adic-L-as-KMS, BYPASS via Wan 2020 / Castella 2018, DECOMPOSE Eisenstein-congruence weight filtration, EXCISE ordinarity via Wan-Xu 2021.
- GZ: VERIFY 4-layer height-formula chain, CONSTRUCT MvN-dimension reading, BYPASS via YZZ 2013 + Kobayashi 2013 p-adic GZ, DECOMPOSE Rankin-Selberg derivative, EXCISE Heegner-hypothesis via YZZ.
- CBB / paper23: VERIFY 7-layer axiom set, CONSTRUCT programme-internal paper26 §§03-07 uniqueness (upgrades T12 Tier 2 → Tier 1 in Scope(S₀)), BYPASS via CCM 2025 (capacitor T13), DECOMPOSE type-III classification, EXCISE axiom A_5 redundancy.

## New capacitor candidates

4 Tier-2 candidates across first-wave CONSTRUCTs:
- R=T as KMS projection (BCDT)
- Euler system as KMS tower (Kolyvagin)
- p-adic L as KMS partition function (Skinner-Urban, Perrin-Riou)
- Heights as MvN dimensions (GZ, YZZ)

Plus 1 upgrade (T12 Tier 2 → Tier 1 inside Scope(S₀)).

## Coordination matrix

- CBB joint with RH Pillar-C.
- Connes-Marcolli joint with PvNP Pillar-C (Popa rigidity).
- BCDT shared with RH (L-cont) + Hodge (CM motives).
- Skinner-Urban shared with RH (GL₂ IMC).
- CCM 2025 already at `strategy/ccm-verification/`; cross-link, no duplicate.

## Scope declaration (hard)

- Hardening is for BSD use-sites inside Scope(S₀) + W_* sub-scopes.
- Original authors' full-scope claims not re-proved.
- CBB rider preserved; no "unconditional" overclaim for BSD Theorem.

## Discipline check (pre-commit)

- Zero prose: pass.
- Every claim cited: pass.
- 15 externals complete: pass.
- Scope declared: pass.
- ≤ 15 pages: pass (≈13 pages).
- PAC proposal per retained external: pass.

## Ready to commit.
