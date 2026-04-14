# NS Repair Trial -- Paste-and-Go Invocation

*Paper 27 Navier-Stokes. EXCISE + CONSTRUCT mode. Targeting Steps 8, 11, 13b.*
*Date: 2026-04-13*

---

## Invocation (paste these 4 lines)

```
read your instructions from
paper27-navier/repair-trial/01-ora-instructions.md

the run brief is
paper27-navier/repair-trial/02-run-brief.md

the toolkit for this run is
paper27-navier/repair-trial/03-capacitor.md

the run output directory is
paper27-navier/repair-trial/output/
```

---

## Expected behavior

### Wave structure (target 3-5 waves, ~20-40 agents)

**Wave 1 (bootstrap + first attack):**
- 3 Authors on Step 8 (Approaches B, C, D from the brief -- all Tier B)
- 1 Author on Step 11 (Approach C -- Tier C P6, no quotient)
- 1 Author on Step 13b (Approach B -- Tier C P5, pure zeta bypass)
- 1 Author on Step 6 (meromorphic continuation -- likely closes with Sobolev care)
- = 6 parallel agents

**Wave 2 (critics attack Wave 1 output):**
- 1 Critic per Author output that returned ADVANCED (up to 6 Critics)
- Every Critic applies the Tao filter FIRST (K-NS-4)
- Any output that also applies to averaged NS is KILLED immediately
- = 3-6 parallel agents

**Wave 3+ (Tier B excision or Tier C construction):**
- Dispatched based on Wave 2 results
- If Step 8 Tier B fails: Constructor dispatched for Tier C (free probability, or embed in SDiff(R4))
- If Step 11 Tier B fails: P6 Constructor (full dissipative algebra stays type III_1)
- If Step 13b Tier B fails: P5 Constructor (pure zeta bypass via functional equation)
- Re-derivers on any step that ADVANCED to lock the result
- = 4-10 parallel agents

### Runtime optimizations

- **Locked steps are locked.** Steps 1, 2, 3, 4, 5, 7, 10, 15 are ESTABLISHED. No agents dispatched on them. This saves ~40% of agent budget compared to a full verification run.
- **Priority ordering.** Step 8 gets 3 parallel Authors because everything downstream depends on it. Steps 11 and 13b each get 1 Author because they have fewer viable Tier B routes.
- **Kill list pre-loaded.** 11 kills already in the capacitor. Agents skip dead approaches without re-discovering them.
- **Capacitor pre-compiled.** 1,117 lines of TOON-format domain knowledge. No compilation needed at runtime.

### What success looks like

| Outcome | Description | Chain confidence |
|---|---|---|
| BEST CASE | Steps 8 and 13b close via Tier B. Step 11 dissolves via P6. | 5/10 -> 8/10 |
| GOOD CASE | Step 8 closes. Step 11 decomposes. Step 13b identifies viable bypass. | 5/10 -> 6-7/10 |
| HONEST CASE | All three walls named precisely. Kill list grows by 5-10. Escalation routes ranked. | stays 5/10, sharper obstacles |
| ALL CASES | Kill list grows. Escalation routes tested. Next run starts stronger. | monotonic progress |

### What failure looks like

- An agent claims Step 8 closes but the Critic finds the construction also works for averaged NS (Tao filter kills it). This is a KILL, not a failure -- the kill list grew.
- All Tier B routes for Step 13b fail. This is an HONEST-STALL with named blockers. The pure zeta bypass (Tier C) becomes the next run's primary target.
- The runner asks "should I continue?" instead of continuing. This is a protocol failure -- the instructions say never ask, always continue.

---

*This is a REPAIR run, not a verification run. The goal is to CLOSE open steps or to make the obstacles sharper. Both outcomes are progress.*
