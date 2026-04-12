# v8 P vs NP Toolkit — Test Execution Prompt

*Fire this prompt in a fresh Claude session. It is self-contained.*
*Date: 2026-04-12*

---

## Your task

You are testing 6 proposed dictionary entries for the P vs NP
transposition dictionary. Each entry was discovered by two parallel
ORA runs attacking the Clone Growth ↔ Fullness Bridge theorem.
Your job: rigorously test each one, write results, and build the
verified toolkit.

## Context files to read FIRST (in this order)

1. `paper28-pvnp/strategy/07-toolkit-complete.md` — the existing
   verified toolkit (10 entries, 8 kills, the spectral-geometric-
   information trinity). This is your baseline.

2. `paper28-pvnp/strategy/08-clone-growth-fullness-bridge.md` —
   the bridge theorem brief (the proof architecture).

3. `ora-bundle-v8/p-v-np-toolkit/00-blueprint.md` — the blueprint
   for this test session (6 entries, process, structure).

4. `paper28-pvnp/strategy/06-transposition-dictionary.md` — the
   full transposition dictionary with three layers.

5. `paper28-pvnp/code/results_*.md` — the 9 computational result
   files from the original 10-agent test session.

## The 6 entries to test (fire ALL in parallel)

### Test 1: P9 — KST Duality (Pattern 7: Obstacle-Tool)

Write code to verify:
(a) For P-time CSPs (2-SAT, Horn, XOR): construct evidence that
    M_Bool^L is injective (clone is amenable monoid → crossed
    product injective by Connes). Then KST applies: all
    automorphisms approximately inner → non-full.
(b) For NPC CSPs (3-SAT, NAE): construct evidence that M_Bool^L
    is NOT injective (clone generates non-amenable group → crossed
    product non-injective). KST does NOT apply → fullness possible.
(c) The duality: same theorem (KST), opposite conclusions. Test
    whether the injectivity/non-injectivity split matches the P/NPC
    split for all 6 Schaefer classes.

Output: `p-v-np-toolkit/test_p9_kst_duality.md`
Code: `paper28-pvnp/code/test_p9_kst_duality.py`

### Test 2: O9 — Clone Amenability

Write code to verify:
(a) For each P-time Schaefer class: compute the clone at arity
    k=3,4,5. Test amenability via Folner-like condition: for each
    subset S of Clone_k, does the "boundary" (elements of S whose
    composition with a generator leaves S) grow slower than |S|?
(b) For each NPC class: show the clone generates a group containing
    a free subgroup (ping-pong lemma) or has exponential growth of
    the Cayley graph (non-amenability indicator).
(c) Test: does clone amenability (P-time) vs group non-amenability
    (NPC) separate all 6 Schaefer classes?

Output: `p-v-np-toolkit/test_o9_clone_amenability.md`
Code: `paper28-pvnp/code/test_o9_clone_amenability.py`

### Test 3: P10 — Cartan MASA

Write code/proof sketch to verify:
(a) For each Schaefer class: is D = L^∞(X_L) (the diagonal, i.e.,
    the algebra of functions on the solution space) a MASA in
    M_Bool^L? Check: is D maximal abelian? (No larger abelian
    sub-algebra contains it.)
(b) Is D regular? (The normalizer of D generates M_Bool^L.)
(c) Does a faithful normal conditional expectation M_Bool^L → D
    exist? (Takesaki's theorem: exists iff D is invariant under
    the modular flow.)
(d) If (a)+(b)+(c): D is Cartan. If not: identify which condition
    fails and for which classes.

Output: `p-v-np-toolkit/test_p10_cartan_masa.md`
Code: `paper28-pvnp/code/test_p10_cartan_masa.py`

### Test 4: O10 — Groupoid Structure

Verify Run 1's CP-1 result is consistent:
(a) Read `paper28-pvnp/clone-growth-fullness-bridge/nodes/1.3.5.7-CP1-crossed-product.md`
    (Run 1's CP-1 formal proof, if accessible) or reconstruct:
    M_Bool^L should be isomorphic to L(R_L) where R_L is the
    restriction groupoid of the Boolean BC equivalence relation
    to the L-solution sector.
(b) Check: does the Feldman-Moore theorem apply? (Need a countable
    group acting on a standard measure space with the equivalence
    relation being the orbit relation.)
(c) Check: can Run 2's hyperfinite approach (Clone amenable → R_∞)
    work WITHOUT the groupoid structure? If yes, O10 is a bonus,
    not a dependency.

Output: `p-v-np-toolkit/test_o10_groupoid.md`

### Test 5: Q9 — Concentration Strengthens

Write code to reproduce Run 1's finding:
(a) For 2-SAT and Horn-SAT at n=8,10: enumerate solutions.
(b) For each arity k=3,5,7,9: compute the polymorphism-averaged
    unitary U_f = (1/|Sol|^{k-1}) sum_{s2,...,sk} exp(i*angle(f(s1,s2,...,sk)))
    for random s1. Measure the PU-distance: d(U_f) = ||U_f - scalar||.
(c) Test: does d(U_f) INCREASE with k? (The Critic predicted
    decrease; Run 1 found increase.)
(d) For 3-SAT: does d(U_f) behave differently? (Expected: no
    meaningful polymorphism exists, so d is not well-defined or
    stays near zero.)

Output: `p-v-np-toolkit/test_q9_concentration.md`
Code: `paper28-pvnp/code/test_q9_concentration.py`

### Test 6: P11 — Bi-exactness Dual Routes

Proof sketch to verify independence:
(a) Route C (Marrakchi Theorem B): requires ergodic equivalence
    relation on a standard probability space + strong ergodicity.
    Does NOT require bi-exactness. List the exact hypotheses.
(b) Route D (Houdayer-Isono): requires bi-exact group acting
    freely + ergodically. DOES require bi-exactness. List the
    exact hypotheses.
(c) Check: do the two routes share ANY sub-gap? (A shared sub-gap
    means they're not fully independent.) List shared dependencies.
(d) Verdict: are they genuinely independent (no shared gap), or
    do they share a dependency?

Output: `p-v-np-toolkit/test_p11_biexact_routes.md`

## After all 6 tests complete

1. For each PASS: add the entry to
   `p-v-np-toolkit/framework-tools-v3.md` using the five-field
   card format (WHAT/WHY/DATA/USE/STATUS) from
   `paper28-pvnp/strategy/07-toolkit-complete.md`.

2. For each KILL: add to the kill list with pattern category and
   re-entry gate.

3. Log every result to `p-v-np-toolkit/changelog.md`.

4. Then: create retroactive proof files for the 7 previously
   verified entries (listed in the blueprint §3). Source data is
   in `paper28-pvnp/code/results_*.md`. Extract the key argument
   into a standalone proof sketch for each:
   - `proof_patb_diagonal.md`
   - `proof_q5_riemann.md`
   - `proof_rule9_gate.md`
   - `proof_p8_barriers.md`
   - `proof_o7_holonomy.md`
   - `proof_q6_outdim.md`
   - `proof_q7_casimir.md`

5. Finally: write a synthesis note
   `p-v-np-toolkit/synthesis.md` summarizing:
   - How many of the 6 new entries passed vs killed
   - Whether Pattern 7 (KST Duality) is confirmed
   - What a Run 3 toolkit would contain
   - The cross-pollination opportunities between Run 1 and Run 2

## Constraints

- Write all output to `ora-bundle-v8/p-v-np-toolkit/`
- Write all code to `paper28-pvnp/code/`
- Use mpmath at ≥50 decimal places for any numerical verification
- Use the five-field card format for verified entries
- Label everything: PASS / KILL / PARTIAL with honest assessment
- If an entry is PARTIAL (some sub-claims pass, some fail):
  split into sub-entries and test each independently

## Voice

From the brief: "from the inside out instead of trying to break
it from the outside, which is always not applicable." The tests
should verify structural identifications, not just numerical
matches. Each test asks: is this identification REAL (survives
from inside the geometry) or APPARENT (breaks when you push)?

---

*Six tests. Same strategy. Test rigorously. Add what passes.
Kill what fails. Step by step.*
