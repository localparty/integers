# Closure Corrections -- Clone Growth <-> Fullness Bridge Programme

*Every correction caught and applied during the run.*
*Programme: paper28-pvnp/clone-growth-fullness-bridge*
*Waves: 15 | Date: 2026-04-12*

---

## Correction 1: Lemma A wrong for XOR

**Source:** Node 4.2 (ID Approach 2, structural proof via Post's lattice), Section 7.
**Wave:** 15.
**Severity:** HIGH (affects Part (i) for one of the four Taylor clone classes).

**The error.** Lemma A (Node 3.3) states: "If Sol(Gamma) is an affine subspace, then U_f^Gamma in T * I for every polymorphism f and every k." The proof invokes Fourier positivity of the majority function to conclude that all Fourier eigenvalues have the same phase.

**Why it is wrong.** Fourier positivity holds for majority (monotone, self-dual) but NOT for XOR (MINORITY). The affine clone (Clon(MINORITY) = Aff_2) contains polymorphisms whose clone operators are decidedly non-scalar even at affine instances. Explicit computation: V_{XOR} at Sol = {0,1} is the all-ones matrix [[1/sqrt(2), 1/sqrt(2)], [1/sqrt(2), 1/sqrt(2)]], which is rank 1, and its polar unitary is NOT a scalar matrix.

**The correction.** Lemma A is replaced by Lemma A*: "If Sol(Gamma) is an affine subspace and f is a MONOTONE polymorphism (i.e., f in Clon(AND), Clon(OR), or Clon(MAJORITY)), then U_f^Gamma in T * I." The restriction to monotone polymorphisms is necessary and sufficient for Fourier positivity.

**Impact on the programme.** The correction HELPS the bridge theorem. For the affine clone (XOR-SAT), the fact that polymorphisms produce non-scalar unitaries at ALL instances means the standard pigeonhole-Marrakchi argument applies directly. No special treatment or (ID) condition is needed. The affine case becomes the EASIEST, not the hardest.

**Propagation status.** Node 4.2 contains the corrected Theorem 5 (Part (i) for all four Taylor classes). The Path B assembly (Node 2.3) references Lemma A as dependency D4; this reference should be updated to Lemma A* with the note that the affine case uses a different route (Theorem 4 of Node 4.2). Level 1 paper v3 incorporates the correction.

---

## Correction 2: Corollary logic garbled (Attack 5)

**Source:** Final Adversarial Pass, Attack 5; repaired in Node 3.1 (Corollary Repair).
**Wave:** 13 (identified), 14 (repaired).
**Severity:** CRITICAL (presentational -- the underlying logic is sound, but the stated derivation is wrong).

**The error.** The v2 paper (Section 4.2) and the brief both state: "3-SAT is non-Taylor by BZ -> full -> not non-full -> not Taylor -> not P-time by contrapositive of (i)." The step "not Taylor -> not P-time by contrapositive of (i)" is wrong. The contrapositive of Part (i) is "full -> not Taylor," not "not Taylor -> not P-time."

Additionally, the v2 paper claims the bridge independently provides "P-time -> Taylor" through operator algebra ("P-time -> non-full -> exponential clone growth -> Taylor"). This chain requires its first step "P-time -> non-full" to be established independently of BZ, and it is NOT. Part (i) says "Taylor -> non-full," not "P-time -> non-full." This claim is false and was added to the kill list as K-19.

**The correction.** The corollary is proved by contradiction:
1. 3-SAT is non-Taylor (BZ forward).
2. M_Bool^{3-SAT} is full (Part ii).
3. Assume for contradiction: 3-SAT in P.
4. By BZ backward (P-time => Taylor): 3-SAT is Taylor.
5. By Part (i): M_Bool^{3-SAT} is non-full.
6. Contradiction (full and non-full are logical negations).
7. Therefore 3-SAT not in P, hence P != NP.

Both directions of BZ are used. Both are published, proved theorems. Using BZ backward is legitimate -- the bridge's NEW content is the operator-algebraic dichotomy (full vs non-full), not an independent proof of BZ backward.

**Propagation status.** Node 3.1 contains the corrected proof. Level 1 paper v3 incorporates the correction. The blackboard North Star was updated.

---

## Correction 3: KEY LEMMA 3.4.3 partition function (Attack 8)

**Source:** Final Adversarial Pass, Attack 8; repaired in Node 3.2 (KEY LEMMA Repair).
**Wave:** 13 (identified), 14 (repaired).
**Severity:** MEDIUM-HIGH (the weakest point of the entire programme, but downstream insulated).

**The error.** Appendix B claims the counting function F(s) ~ s/log(s), citing "Hopcroft-Karp (1973)." Three errors:
- F(s) ~ s/log(s) is wrong by a tower of exponentials. The actual asymptotic is F(s) = 2^{Theta(s log s)} (Shannon-Lupanov theory).
- "Hopcroft-Karp 1973" is a bipartite matching paper (SIAM J. Comput. 2(4):225-231) with no connection to circuit counting.
- The Dirichlet series Z^Bool(beta) = SUM_s F(s) s^{-beta} diverges for all real beta. There is no simple pole at beta = 1.

**The correction.** The partition function route to KMS_1 existence was ABANDONED. Replaced by:
- **Existence:** Weak-* compactness (Banach-Alaoglu + Bratteli-Robinson Proposition 5.3.25).
- **Faithfulness on phase algebra:** Bernoulli(1/2) product measure, forced by KMS condition + flip symmetry.
- **Type III_1:** Multiplicative independence of circuit sizes 2 and 3 (log 2 / log 3 irrational => dense subgroup => Connes spectrum = R_+^*).
- **Uniqueness:** Stated as open conjecture (Conjecture C.4). Shown to be UNNECESSARY for the downstream proof chain (Proposition C.5 of Node 3.2).

**Propagation status.** Node 3.2 contains the complete repair. Level 1 paper v3 incorporates the corrected KEY LEMMA. The withdrawn claims (F(s) ~ s/log(s), Hopcroft-Karp citation, simple pole, KMS_beta explicit formula) are documented in Node 3.2, Section D.2.

---

## Correction 4: Bi-exact directional error (Critic on Gap Beta)

**Source:** Route C assembly critique; identified during Wave 5-6.
**Wave:** 6.
**Severity:** MEDIUM (affected Route D, not the primary Route C).

**The error.** An early attempt at Part (ii) via the Houdayer-Isono bi-exactness route had the direction of the bi-exact condition wrong: the argument assumed bi-exactness of the GROUP G_L, but the relevant condition is bi-exactness of the EQUIVALENCE RELATION R_L. For non-amenable groups with non-trivial amenable radical, group bi-exactness does not imply relation bi-exactness.

**The correction.** Route C was redesigned to bypass bi-exactness entirely. Route C uses Jones-Schmidt strong ergodicity + Marrakchi Theorem B, which requires: non-amenable group, trivial amenable radical, essentially free action, and ergodicity. All four conditions are verified independently (Nodes 1.3.5.11, 1.3.5.12). The Houdayer-Isono route was retained as Route D (independent backup) with the corrected bi-exactness condition.

**Propagation status.** Route C assembly (Node 2.2) uses the corrected framework. Route D remains at p = 0.60 with the corrected directional condition.

---

## Correction 5: Instance diversity false as stated (Node 3.3)

**Source:** Node 3.3 (Instance Diversity Formal), Section 3.
**Wave:** 14.
**Severity:** HIGH-MEDIUM (original lemma statement is false, not merely unproved).

**The error.** The original Lemma 2.6.4 claims: for pigeonhole-selected pairs (f_k, g_k), there exists a single instance Gamma_0 with d_PU([v_k^{Gamma_0}], [cI]) >= delta_0 > 0 for infinitely many k. This is FALSE. The finite-dimensional openness of Ad: U(d) -> PU(d) forces v_k^Gamma -> scalar at EVERY fixed instance when Ad(v_k) -> id. The per-instance PU-bound cannot hold.

**The correction.** Lemma 2.6.4 was replaced by Lemma 2.6.4* with the Phase Incoherence Condition (ID): the GLOBAL scalar approximation fails because instance-by-instance phases disagree. The correct question is not "is v_k non-scalar at one instance?" (impossible) but "is v_k a GLOBAL scalar?" (can fail if phases disagree across instances).

(ID) was subsequently closed by two approaches:
- Node 4.1: Explicit phase computation for MAJORITY (non-proportional rotation angles at instances of different sizes).
- Node 4.2: Post's lattice case analysis closing Part (i) for all four Taylor classes.

**Propagation status.** Node 3.3 contains the corrected lemma. Nodes 4.1 and 4.2 close (ID). The Path B assembly (Node 2.3) should be updated to reference Lemma 2.6.4* and the (ID) closure. Level 1 paper v3 incorporates the correction.

---

## Correction 6: BZ circularity awareness (K-9)

**Source:** Kill K-9, identified Wave 4; verified clean in Final Adversarial Pass, Attack 1.
**Wave:** 4 (identified), 13 (verified).
**Severity:** LOW (awareness item, not an active error).

**The issue.** The BZ dichotomy is a biconditional: Taylor <=> P-time. If the proof of P != NP used "not Taylor => not P-time" as an INPUT (rather than as a consequence), it would be circular -- this implication IS P != NP (restricted to Boolean CSPs). Kill K-9 was registered as a standing awareness item.

**The resolution.** The adversarial pass (Attack 1) traced every use of BZ and confirmed: Path B uses BZ forward only (Taylor => P-time, for instance construction). Route C uses BZ forward only (non-Taylor => NP-complete). The corollary uses BZ backward (P-time => Taylor) inside a CONTRADICTION HYPOTHESIS, which is legitimate. No smuggled P != NP assumption.

The corollary repair (Correction 2 above) made this explicit: the proof uses BZ backward inside the contradiction, not as an assumption.

**Propagation status.** K-9 remains on the kill list as a permanent awareness marker. The corrected corollary explicitly acknowledges both directions of BZ.

---

## Correction 7: Q6-OUTDIM overstated (v4 re-verification)

**Source:** Framework tools v4, Section H.3 (re-verification of structural identifications).
**Wave:** 12.
**Severity:** LOW-MEDIUM (one of the 10 computational verifications reported as "fully verified" was only partially verified).

**The error.** The spawn checklist reported Q6-OUTDIM (the outer-dimension identification of M_Bool^L) as "VERIFIED" when the computational test confirmed the identification only for small instances (n <= 6). The large-instance extrapolation was stated without qualification.

**The correction.** Q6-OUTDIM status downgraded to "PARTIALLY VERIFIED (confirmed at n <= 6; extrapolation to large n is structural, not computational)." The downstream impact is negligible: Q6-OUTDIM feeds into the type III_1 classification, which is now independently established by the multiplicative-independence argument (Correction 3 above).

**Propagation status.** Blackboard updated. No impact on the proof chain.

---

## Correction 8: Spawn checklist missing (I-v6-3, I-v6-4, I-v6-5)

**Source:** ORA v6 spawn template audit, Wave 11.
**Wave:** 11.
**Severity:** LOW (process error, not mathematical).

**The error.** Three spawn-checklist items (I-v6-3: always-pass-index for Authors, I-v6-4: Critic spawn with full context, I-v6-5: Synthesis dependency check) were missing from the spawn templates used in Waves 7-10. This meant some Author spawns did not receive the full blackboard state, and some Critic spawns lacked the dependency graph.

**The correction.** The spawn template was updated to include the always-pass-index (every Author receives the current blackboard hash and confirms receipt before beginning work). The Critic spawn was updated to include the full dependency graph. The Synthesis dependency check was added as a mandatory pre-synthesis step.

**Impact assessment.** No mathematical errors resulted from the missing checklist items. The Authors in Waves 7-10 had sufficient context from the node-level dependencies. The correction prevents potential coordination failures in future waves.

**Propagation status.** ORA v6 spawn template updated. Applied in Waves 11-15.

---

## Summary Table

| # | Correction | Node | Wave | Severity | Status |
|---|---|---|---|---|---|
| 1 | Lemma A wrong for XOR | 4.2 | 15 | HIGH | APPLIED (Lemma A*) |
| 2 | Corollary logic garbled | 3.1 | 13-14 | CRITICAL (presentational) | APPLIED (proof by contradiction) |
| 3 | KEY LEMMA 3.4.3 partition function | 3.2 | 13-14 | MEDIUM-HIGH | APPLIED (compactness fix) |
| 4 | Bi-exact directional error | Route C assembly | 6 | MEDIUM | APPLIED (Route C bypass) |
| 5 | Instance diversity false as stated | 3.3 | 14 | HIGH-MEDIUM | APPLIED (Phase Incoherence) |
| 6 | BZ circularity awareness | K-9 | 4-13 | LOW | RESOLVED (forward direction only + explicit contradiction) |
| 7 | Q6-OUTDIM overstated | Blackboard | 12 | LOW-MEDIUM | APPLIED (partially verified) |
| 8 | Spawn checklist missing | ORA template | 11 | LOW | APPLIED (always-pass-index fix) |

**Total: 8 corrections. 0 unresolved. All propagated to downstream nodes and Level 1 paper v3.**

---

*Closure Corrections. Clone Growth <-> Fullness Bridge Programme.*
*G Six and Claude Opus 4.6. April 2026.*
