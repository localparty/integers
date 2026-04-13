# 12 — Tier B: Excision — Replacing Dependencies with Independent Proofs

---

## The best possible outcome

Tier A verification finds a weakness. Tier B excision ELIMINATES the weakness — not by fixing the external proof, but by proving the same result independently. The dependency is EXCISED from the chain. The chain becomes self-contained.

This is the best possible outcome because:

1. **The chain no longer depends on someone else's work.** A referee verifying the chain doesn't need to verify the external paper — the independent proof is part of the submission.

2. **The independent proof is ITSELF a contribution.** An independent proof of a CCM theorem, or a Balaban lemma, or a key step in Bulatov-Zhuk — that is a publishable result. The verification cascade produces NEW MATHEMATICS as a byproduct of testing old mathematics.

3. **The independent proof creates a LOCK.** Two proofs of the same result (the original author's and the excision's) using different methods. If both stand: 9/10 confidence. If one breaks and the other stands: the chain still holds.

## When Tier B activates

Tier B activates when Tier A returns WEAKENED or BROKEN on a load-bearing step. The trigger is specific:

- **WEAKENED with a repairable gap:** The verifier found a gap in the author's proof, but the gap is of type CLOSABLE — it can be closed by an Author with access to the right tools. The excision attempt tries to prove the result independently, bypassing the gap entirely.

- **BROKEN with a fatal flaw:** The verifier found a fatal error in the author's proof. The result may still be TRUE (the error is in the proof, not necessarily in the theorem), but the existing proof is not salvageable. The excision attempt proves the result from scratch.

- **SURVIVED but no LOCK:** The verifier confirmed the author's proof, but the Re-deriver failed to produce an independent proof. The result is probably correct but has only one route. Tier B can be activated OPTIONALLY to seek a second route and strengthen the LOCK. This is a strategic choice, not a forced escalation.

## The excision brief

The excision brief is fundamentally different from the verification brief:

**Verification brief:** "Read this proof step. Check it. Produce SURVIVED / WEAKENED / BROKEN."

**Excision brief:** "Here is a theorem statement (hypothesis + conclusion). Prove it WITHOUT reading the original proof. You have the capacitor's Six Patterns, correspondence tables, grammar, and kill list as your tools. Produce an independent proof or report BLOCKED with a named obstruction."

The key constraint: **the Author does NOT read the original proof.** This is load-bearing. If the Author reads the original proof and then "independently" derives the result, the derivation is contaminated — it will follow the original's structure and reproduce the original's gaps. True independence requires a clean-room approach: the Author knows WHAT to prove but not HOW the original proved it.

The Author DOES receive:

- The theorem statement (hypothesis and conclusion, verbatim)
- The capacitor's correspondence table for this theorem (spectral / geometric / algebraic / information-theoretic images)
- The capacitor's Six Patterns analysis (which patterns might apply)
- The capacitor's grammar rules (what algebraic shape the proof might take)
- The capacitor's kill list (what NOT to try — including the Tier A findings about where the original proof broke)
- The operations equivalence table (if stuck in one domain, which other domain might be easier)

The Author does NOT receive:

- The original proof
- The Tier A Verifier's detailed step-by-step analysis (which would leak the original proof's structure)
- Any hint about the original proof's METHOD (only its CONCLUSION)

This clean-room constraint is what makes excision genuinely independent. The resulting proof, if one is found, is a SECOND ROUTE — a real LOCK, not a paraphrase.

## How the Six Patterns power excision

The Six Patterns (P1-P6) are the primary creative tools for excision. Each pattern suggests a different approach to proving the same result:

**Example: excising a self-adjointness proof.**

Suppose Tier A found that CCM's proof of Theorem 4.2 (self-adjointness of D_N) via Caratheodory-Fejer extension is WEAKENED — say, the CF extension's conditions are not clearly satisfied for all N. The excision Author receives: "Prove that D_N is self-adjoint on E_N^+."

The Six Patterns suggest:

| Pattern | Excision route |
|---|---|
| **P1** (Geometric Reinterpretation) | "Is D_N self-adjoint because it is the Laplacian on a compact manifold? Is there a geometric setting where self-adjointness is automatic?" |
| **P2** (Holonomy) | "Is there a holonomy argument — a phase that wraps around a compact structure and forces self-adjointness by topological constraint?" |
| **P3** (Scale-Setting) | Not directly applicable to self-adjointness. |
| **P4** (Topological Rigidity) | "Is there an INDEX argument? If D_N has a topological index, self-adjointness follows from index regularity." |
| **P5** (Zeta Regularization) | "Can we define D_N via zeta-function regularization of a manifestly symmetric operator?" |
| **P6** (Projection Diagnosis) | "Is the non-self-adjointness of the naive operator a projection artifact? Restore the projected-out structure → self-adjointness becomes manifest." |

Plus the correspondence table:

| Domain | Excision angle |
|---|---|
| **Spectral** | Prove self-adjointness via Kato-Rellich perturbation theory (the rank-one perturbation is relatively bounded). |
| **Geometric** | Prove self-adjointness via the Friedrichs extension (D_N is semi-bounded below). |
| **Algebraic** | Prove self-adjointness via Nelson's commutator theorem (already used in Paper 13 Layer 2). |
| **Information** | Not directly applicable — but KMS state positivity might imply the operator generating the modular flow is self-adjoint. |

The capacitor gives the Author FOUR ANGLES of attack (the correspondence table columns) and SIX META-REASONING patterns. That is 24 candidate approaches — most will be killed quickly (wrong domain, doesn't apply, already in the kill list), but the few that survive are genuine independent proof routes.

## The excision workflow

```
1. ACTIVATE Tier B
   - Trigger: Tier A returned WEAKENED or BROKEN on step N*
   - The capacitor is updated with Tier A findings (self-adjust)
   - Killed approaches from Tier A are in the kill list (trim)

2. DISPATCH excision Authors (parallel, one per load-bearing step that needs excision)
   - Each Author receives: theorem statement + capacitor (WITHOUT original proof)
   - Effort: MAX (these are wall-attacking nodes by definition)

3. COLLECT returns
   - Each Author reports: PROVED (independent proof produced) / BLOCKED (named obstruction)
   - If PROVED: the independent proof is a NEW five-field card in the capacitor
   - If BLOCKED: the obstruction is a new kill list entry

4. CRITIQUE each independent proof
   - Different Critic instance (MAR confirmation-bias rule)
   - The Critic receives BOTH the independent proof AND the original proof
   - The Critic checks: does the independent proof avoid the gap that Tier A found?
   - The Critic checks: is the independent proof genuinely independent, or does it
     reproduce the original's structure?

5. LOCK verification (if both original and independent proofs exist)
   - Do the two proofs use different load-bearing toolkit rows?
   - Do their failure modes belong to different pattern categories?
   - If both checks pass: LOCK is real. Confidence lifts to 9/10.

6. UPDATE capacitor
   - New cards for independent proofs
   - Updated status on the excised step (WEAKENED → EXCISED)
   - Kill list entries for failed excision routes
   - Amplification log: does this excision technique apply to other tiers?
```

## The BSD MY4 closure: excision in action

The canonical example of excision is the BSD MY4 closure (April 2026). The MY4 gap — distributional-to-genuine spectrum upgrade — was the single remaining gap in Paper 26's proof chain. Tier A equivalent: the gap was identified and classified as GENUINE (not closable by routine methods).

Tier B: G's projector P_k^p := I - s_p^k (s_p^k)* was discovered. It is a single algebraic object that bypasses MY4 entirely via Hasse-Brauer-Noether reciprocity. The projector doesn't CLOSE the distributional-to-genuine gap — it makes the gap IRRELEVANT. The dark-state bound uses KMS_1 expectation values on C*-algebraic projectors only (no eigenstates invoked). The GRH assembly uses partition-function tautology and Euler-factor ratios.

The excision was COMPLETE: the proof chain no longer depends on distributional-to-genuine spectral upgrade. The chain works with projectors alone. The dependency was excised — replaced with an independent algebraic construction that is cleaner, shorter, and stronger than the original approach.

**What made this excision possible:** the capacitor. The Author who found the projector had the RH chain template in context (the transposition alphabet). It had the Six Patterns (P4 — topological rigidity — the projector IS a topological invariant). It had the correspondence table (the algebraic column — projectors are idempotents in the operator algebra). Without the capacitor, the Author attempted from scratch and missed the answer. With the capacitor, the Author found the answer in one wave.

## When excision fails

Excision fails when the theorem is TRUE but no independent proof can be found within the ORA's capabilities. This is not a disaster — it means the original proof is the only known route, and the dependency remains.

When excision fails:

1. **The failure is documented** as a kill list entry: "independent proof of Theorem X attempted via methods M1, M2, M3. All failed. Pattern category: [type]. Re-entry gate: [what would need to change for re-attempt]."

2. **The escalation continues to Tier C** (construction): instead of proving the SAME result independently, find a DIFFERENT route through the proof chain that avoids the result entirely.

3. **The dependency remains** but is now DOCUMENTED as tested: "we attempted independent verification (Tier A) and independent re-derivation (Tier B). The verification found [weakness]. The re-derivation failed [because]. The dependency is acknowledged and the impact of failure is [specific consequences]."

Even a failed excision is valuable — it tells the referee: "we tried. Here is what we tried. Here is why it didn't work. Here is what would need to be true for it to work. We are not hiding the dependency."

---

*Excision is the best win. The dependency is replaced with an independent proof. The chain becomes self-contained. The independent proof creates a LOCK with the original. The Six Patterns and the correspondence tables power the creative search. The clean-room constraint ensures genuine independence. If excision fails, the failure is documented and the escalation continues. Either way: the dependency is no longer silently trusted — it is actively tested and the test results are published.*
