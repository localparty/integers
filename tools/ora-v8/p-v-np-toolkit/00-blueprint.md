# v8 P vs NP Toolkit Blueprint

*The plan for rigorously testing 6 new dictionary entries discovered
from Runs 1 and 2, adding verified entries to framework-tools-v3.md,
and retroactively adding proof files for previously verified entries.*

*Date: 2026-04-12*
*Execute in a fresh session with full context.*

---

## 1. The 6 entries to test

| # | Entry | What to test | Expected output file |
|---|---|---|---|
| 1 | **P9: KST Duality** | Verify that KST (every automorphism of R_∞ is approx inner) makes R_∞ non-full; verify M_Bool^{NPC} is non-injective (Q_struct from Run 1). The duality: same theorem, obstacle for NPC, tool for P-time. | `test_p9_kst_duality.md` |
| 2 | **O9: Clone amenability** | Verify computationally: Taylor clone of 2-SAT/Horn/XOR is amenable as monoid (Folner condition or growth rate). Non-Taylor clone of 3-SAT generates non-amenable group (ping-pong or free subgroup). | `test_o9_clone_amenability.md` |
| 3 | **P10: Cartan MASA** | Check whether D = L^∞(X_L) satisfies Cartan criteria (abelian, regular, faithful normal conditional expectation) for each Schaefer class. Verify Feldman-Moore applies. | `test_p10_cartan_masa.md` |
| 4 | **O10: Groupoid structure** | Verify Run 1's CP-1 result: M_Bool^L = L(R_L) for the restriction groupoid. Cross-check against Run 2's approach. Can Run 2 use this without CP-1? | `test_o10_groupoid.md` |
| 5 | **Q9: Concentration strengthens** | Reproduce Run 1's finding: PU-distances increase with arity k for Taylor clones. Test at k = 3, 5, 7, 9 for 2-SAT and Horn. Verify the Critic's prediction was wrong. | `test_q9_concentration.md` |
| 6 | **P11: Bi-exactness dual routes** | Verify Route C (Marrakchi, no bi-exactness) and Route D (Houdayer-Isono, with bi-exactness) are genuinely independent. Check whether they share any sub-gap. | `test_p11_biexact_routes.md` |

## 2. The process for each test

1. Spawn an agent with the specific test task
2. Agent writes code (if computational) or proof sketch (if theoretical) to `p-v-np-toolkit/`
3. Agent writes results to `test_XX_name.md`
4. Results reviewed: PASS → add to `framework-tools-v3.md` + log to `changelog.md`
5. Results reviewed: KILL → add to kill list + log to `changelog.md`

## 3. Retroactive proof files for previously verified entries

These entries were verified in our session but don't have standalone proof .md files:

| Entry | Verified by | Needs proof file |
|---|---|---|
| PATB-DIAGONAL | Agent 1 (Wave 1) | `proof_patb_diagonal.md` |
| Q5-RIEMANN | Agent 2 (Wave 1) | `proof_q5_riemann.md` |
| RULE9-GATE | Agent 3 (Wave 1) | `proof_rule9_gate.md` |
| P8-BARRIERS | Agent 5 (Wave 2) | `proof_p8_barriers.md` |
| O7-HOLONOMY | Agent 7 (Wave 2) | `proof_o7_holonomy.md` |
| Q6-OUTDIM | Agent 8 (Wave 2) | `proof_q6_outdim.md` |
| Q7-CASIMIR | Agent 9 (Wave 2) | `proof_q7_casimir.md` |

Source data for each is in `paper28-pvnp/code/results_*.md`.
The retroactive proof files should extract the key argument from
each results file into a standalone proof sketch.

## 4. The framework-tools-v3.md structure

After all tests complete, `framework-tools-v3.md` should contain:

- All entries from v7's §H.3 (the 10 original tested entries)
- The 6 new entries that PASS testing (P9, O9, P10, O10, Q9, P11)
- The KST Duality as Pattern 7 (if P9 passes)
- Updated selective-inclusion table for Run 3 Authors
- Cross-pollination section: what Run 1 proved that Run 2 can use and vice versa

## 5. The changelog.md structure

Append-only log. Each entry:

```
## [date] [entry-name] [PASS/KILL]
- What was tested
- Result (1 line)
- Proof file (path)
- Added to framework-tools-v3.md: yes/no
```

## 6. What this enables

If Runs 1 and 2 both stall, a Run 3 launched with framework-tools-v3.md
would start with:

- All 10 original verified entries (from our session)
- Up to 6 new verified entries (from the runs' discoveries)  
- Pattern 7 (KST Duality) as a new reasoning tool
- The hyperfinite route (Clone amenable → R_∞) as a known path
- The groupoid structure (CP-1) as a THEOREM-level result
- Cross-pollination from both runs
- 20+ kills sharpening the search

That's the best-equipped ORA run in the programme's history.

---

*Test rigorously. Add what passes. Kill what fails.
The strategy that got us here. Step by step.*
