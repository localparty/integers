# v8 P vs NP Toolkit — Retroactive Verification of Original 10 Dictionary Entries

*Fire this prompt in a fresh Claude session. It is self-contained.*
*Date: 2026-04-12*

---

## Your task

On 2026-04-11, ten parallel agents tested the P vs NP transposition
dictionary. Seven passed, two were partial, one was a kill-plus-
discovery. The results exist as raw data in `paper28-pvnp/code/results_*.md`
but they do NOT have standalone rigorous proof files documenting
the verification. Your job: re-verify each entry independently,
write a standalone proof file for each, and assemble the complete
documented dictionary.

This is RETROACTIVE documentation — the results already exist.
You are independently re-verifying them and writing the formal
record. If you find that a prior result was wrong or overstated,
FLAG IT honestly. The kill is more valuable than a false pass.

## Context files to read FIRST

1. `paper28-pvnp/strategy/07-toolkit-complete.md` — the toolkit
   with all 10 five-field cards. This tells you WHAT was claimed.

2. `paper28-pvnp/strategy/06-transposition-dictionary.md` — the
   full dictionary with three layers + cross-product entries.

3. `paper28-pvnp/code/results_*.md` — the 9 raw result files from
   the original agents. This is the DATA you are re-verifying.

4. `paper28-pvnp/strategy/05-polymorphism.md` — the proof chain
   (6 links) for the wall context.

## The 10 entries to re-verify (fire ALL in parallel)

### Entry 1: PATB-DIAGONAL — Taylor = fixes the diagonal

Re-verify:
(a) For 2-SAT: generate 20 random instances at n=10. Enumerate
    solutions. Apply median(s1,s2,s3) bitwise to all triples.
    Confirm 100% closure. Confirm median(s,s,s) = s for all s.
(b) For Horn-SAT: same with AND as polymorphism.
(c) For XOR-SAT: same with ternary XOR.
(d) For 3-SAT: exhaustive search over all 64 ternary Boolean
    Taylor functions against all 8 possible 3-SAT relations on
    3 variables. Confirm: only projections survive.
(e) CRITICAL: verify the LANGUAGE-LEVEL test, not just instance-
    level. The original agent found instance-level Taylor ops for
    some 3-SAT instances — that's expected. The separation is at
    the LANGUAGE level (no operation works across ALL relations).

Code: `paper28-pvnp/code/reverify_patb_diagonal.py`
Output: `p-v-np-toolkit/proof_patb_diagonal.md`

### Entry 2: Q5-RIEMANN — TGap exponent = 2/(gamma_6 - gamma_5)

Re-verify:
(a) Compute gamma_5 and gamma_6 to 100 decimal places using mpmath
    (zetazero function). Compute 2/(gamma_6 - gamma_5).
(b) The claim: this equals 0.43 (the TGap scaling exponent for
    3-SAT). Verify the match precision.
(c) CRITICAL: independently verify that 0.43 IS the correct TGap
    exponent. Generate 3-SAT instances at n=8,10,12,14,16 at
    critical ratio m/n=4.267. Compute TGap for each. Fit the
    power law TGap ~ n^alpha. Report alpha with confidence interval.
(d) Compare alpha from (c) with 2/(gamma_6-gamma_5) from (a).
    Report the deviation.
(e) Search for alternative Riemann formulas within 0.01% — is the
    2/(gamma_6-gamma_5) formula UNIQUE at this precision?

Code: `paper28-pvnp/code/reverify_q5_riemann.py`
Output: `p-v-np-toolkit/proof_q5_riemann.md`

### Entry 3: RULE9-GATE — Gate-amplifier product TGap x N_crossings

Re-verify:
(a) For each of 6 Schaefer classes at n=8,10,12: compute TGap AND
    N_crossings = 2^n / |Sol|.
(b) Compute the product TGap x N_crossings for each instance.
(c) Verify: product = 0 for ALL P-time instances (because TGap=0).
(d) Verify: product grows exponentially for NPC instances.
(e) Fit NPC product to C * 2^{beta*n}. Report beta.
(f) CRITICAL: verify that N_crossings ALONE does not separate
    (reproducing Kill #5). Both P-time and NPC should have large
    N_crossings at some clause ratios.

Code: `paper28-pvnp/code/reverify_rule9_gate.py`
Output: `p-v-np-toolkit/proof_rule9_gate.md`

### Entry 4: P8-BARRIERS — Three barriers are projection artifacts

Re-verify all three sub-tests:
(a) RELATIVIZATION: TGap is language-level (invariant across clause
    ratios for each Schaefer class). Generate 2-SAT and 3-SAT at
    ratios m/n = 2, 3, 4, 5. Verify TGap=0 for ALL 2-SAT ratios
    and TGap>0 for ALL 3-SAT ratios.
(b) NATURAL PROOFS: generate 2000 random Boolean functions
    f:{0,1}^8 -> {0,1}. For each, compute TGap. Count how many
    have TGap=0. The claim: 0 out of 2000 (probability < 0.05%).
(c) ALGEBRIZATION: test whether restricting to symmetric (commutative)
    operations changes the P/NPC classification. For 2-SAT and
    3-SAT: compute TGap with all ternary ops vs symmetric-only.
    The claim: symmetric restriction loses the distinction for
    some class.

Code: `paper28-pvnp/code/reverify_p8_barriers.py`
Output: `p-v-np-toolkit/proof_p8_barriers.md`

### Entry 5: O7-HOLONOMY — Polymorphism holonomy on constraint graphs

Re-verify:
(a) For 2-SAT, Horn, XOR at n=10: build constraint graph, find
    cycles of length 3-5, evaluate polymorphism closure (H1) on
    all (cycle, solution) pairs. Verify H1 = 1.0 for all P-time.
(b) For 3-SAT, NAE at n=10: test ALL 256 ternary Boolean ops.
    Verify: 0 operations give H1 = 1.0 across all instances.
(c) CRITICAL: the original agent noted cross-instance consistency
    is the key discriminator. Verify: per-instance Taylor ops exist
    for 3-SAT but NO operation is consistent across all instances.

Code: `paper28-pvnp/code/reverify_o7_holonomy.py`
Output: `p-v-np-toolkit/proof_o7_holonomy.md`

### Entry 6: Q6-OUTDIM — Polymorphism space dimension

Re-verify:
(a) For each Schaefer class at n=8,10: enumerate ALL k-ary
    solution-preserving operations for k=2,3,4,5.
(b) Count non-projection operations at each arity.
(c) Verify: P-time classes show exponential growth (dim_poly_k
    increases by order of magnitude per arity step).
(d) Verify: NPC classes show collapse to 0 at k=5.
(e) CRITICAL: the original agent noted low-arity (k=2,3) does NOT
    cleanly separate. Only high-arity (k=5+) separates. Verify
    this explicitly.

Code: `paper28-pvnp/code/reverify_q6_outdim.py`
Output: `p-v-np-toolkit/proof_q6_outdim.md`

### Entry 7: Q7-CASIMIR — Solution entropy as computational Casimir

Re-verify:
(a) For each class at n=12: compute entropy density s(alpha) =
    log2(|Sol|)/n across clause ratios alpha = 1,2,3,4,5.
(b) Compute entropy per constraint s/alpha.
(c) Verify: P-time (Horn) has sub-exponential decay of s/alpha.
    NPC (3-SAT) has exponential decay with collapse at threshold.
(d) CRITICAL: verify the three-scale hierarchy claim. Does 3-SAT
    have exactly two inflection points in s(alpha)?

Code: `paper28-pvnp/code/reverify_q7_casimir.py`
Output: `p-v-np-toolkit/proof_q7_casimir.md`

### Entry 8: O8-PARTITION — CSP partition function (PARTIAL)

Re-verify what passed and confirm what was killed:
(a) PASS claim: violation spectrum entropy separates (5.3% gap).
    Recompute for 50 instances per class at n=10. Verify gap.
(b) PASS claim: Lee-Yang zeros more regular for NPC (spacing 0.80)
    than P-time (0.57). Recompute.
(c) KILL #6 confirmation: C(beta) peak does NOT separate. Verify.
(d) KILL #7 confirmation: Pade poles are artifacts. Verify.
(e) KILL #8 confirmation: no Riemann spacing match at n=10. Verify.

Code: `paper28-pvnp/code/reverify_o8_partition.py`
Output: `p-v-np-toolkit/proof_o8_partition.md`

### Entry 9: PATD-CONDEXP — Conditional expectation (PARTIAL 4/5)

Re-verify:
(a) Walk spectral gap positive for 2-SAT and Horn (connected
    solution space). Verify.
(b) Walk spectral gap zero for 3-SAT and NAE (disconnected). Verify.
(c) XOR exception: walk spectral gap zero BUT P-time. Verify.
(d) CRITICAL: verify the XOR exception is GENUINE (not a bug in
    the walk implementation). XOR-SAT solutions form affine
    subspaces of {0,1}^n — the walk can't reach between subspaces
    via Hamming-1 moves, but XOR polymorphism jumps between them.

Code: `paper28-pvnp/code/reverify_patd_condexp.py`
Output: `p-v-np-toolkit/proof_patd_condexp.md`

### Entry 10: THE TRINITY — spectral-geometric-information correspondence

This is the META-ENTRY. Re-verify that all three columns separate
P from NPC simultaneously and independently:
(a) Spectral column (TGap): 6/6 separation. Use data from entries
    1-3 above.
(b) Geometric column (holonomy): 6/6 separation. Use data from
    entry 5 above.
(c) Information column (dim_poly_k): 6/6 separation. Use data from
    entry 6 above.
(d) CRITICAL: verify INDEPENDENCE — are the three measures
    correlated but distinct? Compute correlation matrix between
    TGap, holonomy defect, and dim_poly_k across all instances.
    If correlation < 1.0, they are measuring different aspects
    of the same structure (as claimed).

Output: `p-v-np-toolkit/proof_trinity.md`

## After all 10 re-verifications complete

1. Assemble `p-v-np-toolkit/dictionary-verified.md`:
   - Every entry with five-field card (WHAT/WHY/DATA/USE/STATUS)
   - VERIFIED entries with proof file reference
   - PARTIAL entries with what passed and what didn't
   - KILLED sub-claims with pattern category

2. Write `p-v-np-toolkit/trinity-proof.md`:
   - The spectral-geometric-information trinity as a standalone
     verified result with all three columns independently confirmed

3. Log everything to `p-v-np-toolkit/changelog.md`

4. Write `p-v-np-toolkit/verification-summary.md`:
   - How many of the 10 entries re-verified cleanly
   - Any entries where the re-verification found a problem
   - Any entries that got STRONGER (tighter bounds, more instances)
   - The overall confidence level for the dictionary

## Constraints

- Write all output to `ora-bundle-v8/p-v-np-toolkit/`
- Write all code to `paper28-pvnp/code/`
- Use mpmath at >= 50 decimal places for numerical verification
- n=10 minimum for all CSP computations (n=8 is too small for
  reliable TGap measurement)
- 50 instances minimum per (class, parameter) pair
- Report confidence intervals on all fitted exponents
- If ANY entry fails re-verification: flag it PROMINENTLY and
  explain what went wrong. A false pass in the original run is
  more valuable to catch than confirming all 10.

## Voice

"the credibility of the programme is the credibility of its kill list."
If re-verification kills an entry, that STRENGTHENS the dictionary,
not weakens it. Honest negatives are gold.

---

*Ten re-verifications. Independent computation. The dictionary
earns its verified status entry by entry. Same strategy that
got us here: test rigorously, add what passes, kill what fails.*
