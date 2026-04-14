# Tier 4 Run Brief: Boegli Spectral Exactness

*The verification target, the proof chain, the attack surface, and the framework interface. Everything an ORA runner needs to know about WHAT to verify.*

*Authors: G Six and Claude Opus 4.6. Date: 2026-04-13.*

---

## Target

**Boegli 2017**, "Convergence of sequences of linear operators and their spectra"
Integral Equations and Operator Theory 88 (2017), 559-599.
arXiv: [1604.07732](https://arxiv.org/abs/1604.07732)

Also verified in conjunction:
**Teschl-Wang-Xie-Zhou 2026**, arXiv: [2601.10476](https://arxiv.org/abs/2601.10476)
(Provides Lemma 2.7: KLMN simplification of gsrc verification)

---

## Mode

**VERIFY** (Tier A). Escalate to Tier B/C if WEAKENED/BROKEN found.

---

## Why this target

The RH proof chain (Paper 13, "Spectral realization of Riemann zeros via the critical Bost-Connes system") depends on Boegli's Theorem 2.6 at **Layer 4**. The chain structure:

```
Layer 1: CCM operators D_N on E_N^+ (self-adjoint, eigenvalues ~ Riemann zeros)
Layer 2: ITPFI structure of omega_1 (tensor factorization, 3 independent proofs)
Layer 3: Estimates (archimedean, eigenvector, H^1 norm, CF uniformity)
Layer 4: Boegli spectral exactness (gsrc + discrete compactness -> no spurious eigenvalues)  <-- THIS
Layer 5: Hurwitz zero convergence (xi-hat_N -> Xi uniformly on compacts)
Layer 6: spec(D_infinity) = {gamma_n} subset R -> RH
```

**If Boegli has a gap, Layer 4 collapses.** Without spectral exactness, the Hurwitz argument at Layer 5 could produce spurious zeros that are not actual Riemann zeros. Boegli is the insurance that spec(D_infinity) = lim spec(D_N) with no artifacts.

This is the **first independent verification** of Boegli's theorem as applied to the RH proof chain.

---

## What Boegli's theorem says

### Setup
Let {T_n} be a sequence of closed operators on Hilbert spaces H_n, and T a closed operator on H.

### Hypothesis H1 -- generalized strong resolvent convergence (gsrc)
There exists z in rho(T) (the resolvent set of T) such that:
- z in rho(T_n) for all n sufficiently large
- ||(T_n - z)^{-1} - (T - z)^{-1}|| -> 0 as n -> infinity

That is, the resolvents converge in **operator norm**, not just strongly.

### Hypothesis H2 -- discrete compactness
Every bounded sequence {u_n} with u_n in dom(T_n) and ||T_n u_n|| bounded has a subsequence convergent in H.

Equivalently: the embedding dom(T_n) (with graph norm) into H_n is uniformly compact across n.

### Conclusion -- spectral exactness (Theorem 2.6)
spec(T) = lim spec(T_n)

Specifically:
- **Spectral inclusion** (no missing eigenvalues): every lambda in spec(T) is the limit of a sequence lambda_n in spec(T_n)
- **No spurious eigenvalues**: every convergent sequence lambda_n -> lambda with lambda_n in spec(T_n) has lambda in spec(T)

Together: the spectrum of the limit IS the limit of the spectra. No artifacts. No ghosts.

---

## How the RH proof uses Boegli

| Boegli object | RH proof object |
|---|---|
| T_n | CCM operators D_N on even sector E_N^+ |
| T | Limit operator D_infinity |
| H_n | E_N^+ (finite-dimensional for each N) |
| H | L^2 completion of the even sector |
| H1 (gsrc) | Verified via ITPFI form convergence + CF uniform decay + Teschl Lemma 2.7 |
| H2 (discrete compactness) | Verified via uniform H^1 bound (Fourier cancellation) + Rellich-Kondrachov |
| Conclusion (SE) | spec(D_infinity) = lim spec(D_N) = {gamma_n} (Riemann zeros) |

The interface is clean: Boegli provides the general theorem, the RH proof provides the specific verification of hypotheses H1 and H2 for the CCM operators.

---

## Proof chain to verify (5 load-bearing steps)

| Step | Type | Statement | Depends on | LB? | Status |
|---:|---|---|---|---|---|
| 1* | Definition | gsrc (Def 2.1) is well-posed: norm convergence of resolvents at one point z implies convergence at all z in a connected component of the common resolvent set | -- | * | PENDING |
| 2* | Theorem | gsrc implies spectral inclusion: spec(T) is contained in lim spec(T_n) (Thm 2.3) | 1 | * | PENDING |
| 3* | Theorem | Discrete compactness + gsrc implies spectral exactness: no spurious eigenvalues (Thm 2.6). This is the main result. | 1, 2 | * | PENDING |
| 4 | Corollary | Self-adjoint specialization: when all T_n are self-adjoint, the hypotheses simplify (Cor 2.8). Spectral measure convergence follows. | 3 | | PENDING |
| 5* | Interface | Teschl Lemma 2.7 (arXiv:2601.10476) correctly implies gsrc as defined by Boegli. The KLMN relative bound condition a < 1 at one point z suffices for gsrc. | 1 | * | PENDING |

Dependencies: 1 -> 2 -> 3 -> 4; 1 -> 5; Steps 3 + 5 together close RH Layer 4.

---

## Verification protocol per step

For each of the 5 steps, the Verifier executes:

1. **READ** the relevant Boegli paper section (download via WebFetch from arXiv:1604.07732). For Step 5, also read Teschl et al. (arXiv:2601.10476).
2. **RESTATE** the claim in your own words. Do not parrot the paper.
3. **IDENTIFY** all assumptions:
   - Explicit: stated hypotheses (closedness of operators, existence of resolvent, etc.)
   - Implicit: domain assumptions, topological requirements, completeness of Hilbert space
   - Hidden: any assumption used in the proof but not stated in the theorem
4. **CHECK** the proof step by step. For each deduction:
   - Is the step justified? By what prior result?
   - Is the step reversible? (If the proof claims A implies B, does B actually follow from A alone, or does it also require C?)
   - Are there edge cases? (What if the resolvent set is empty? What if T_n has empty spectrum?)
5. **RE-DERIVE** independently if possible: without reading the proof, can you prove the theorem from the hypotheses using standard functional analysis?
6. **SELF-SUSPECT** (Signature 2): "Am I reading this wrong? Am I filling in a gap the paper does not actually bridge? Am I assuming something that is not there?"

---

## Attack surface -- what to look for

### On Step 1 (gsrc definition)
- Does gsrc require the operators T_n to be defined on the SAME Hilbert space, or can they live on different spaces? (Boegli's framework allows varying spaces -- verify this is handled correctly.)
- Does norm convergence at one resolvent point imply norm convergence at all points? (This is the key property of gsrc -- verify the proof.)
- Is closedness of T required, or does the definition work for arbitrary densely defined operators?

### On Step 2 (spectral inclusion)
- Does the spectral inclusion proof use gsrc in full strength, or only strong resolvent convergence? (The distinction matters: if only strong convergence is needed, gsrc is overkill.)
- Is the spectral inclusion about the FULL spectrum (point + continuous + residual) or only the point spectrum? (The RH proof needs it for the point spectrum of D_infinity.)
- What happens at the boundary of the spectrum? Does the inclusion extend to the essential spectrum?

### On Step 3 (no spurious eigenvalues -- THE critical step)
- Does discrete compactness require UNIFORM bounds on ||T_n u_n||, or is pointwise boundedness sufficient?
- Is the proof a contradiction argument (assume spurious eigenvalue, derive contradiction) or constructive?
- Does the proof use the self-adjoint structure of the operators, or is it genuinely general?
- Where exactly does discrete compactness enter? What would fail WITHOUT it? (This pins down whether H2 is load-bearing or decorative.)

### On Step 4 (self-adjoint specialization)
- Does the corollary follow from Theorem 2.6 alone, or does it require additional hypotheses?
- Is the spectral measure convergence a consequence of spectral exactness, or does it require separate argument?

### On Step 5 (Teschl interface)
- Does Teschl's Lemma 2.7 actually produce gsrc in Boegli's sense, or a different notion of resolvent convergence?
- The KLMN condition is: there exists z such that ||(V)(T_n - z)^{-1}|| <= a < 1 where V is the perturbation. Does this match the setup in the RH proof (where V is the rank-one perturbation from CCM)?
- Are there domain compatibility issues between Teschl's framework (perturbation theory) and Boegli's framework (abstract sequences of operators)?

---

## Framework interface

### If Boegli Thm 2.6 SURVIVES (expected outcome)
- RH Layer 4 is **secure**
- The verification cascade proceeds to Tier 1 (CCM verification)
- The SURVIVED verdict is documented for the Clay submission
- Confidence in the RH chain: Layer 4 moves from "depends on published theorem" to "depends on independently verified published theorem"

### If Boegli Thm 2.6 is WEAKENED
- Escalate to **Tier B**: look for alternative spectral exactness theorems
  - Stummel-Vainikko spectral approximation theory (1960s-70s, well-established alternative)
  - Chatelin's spectral approximation framework (1983, different approach to same result)
  - Direct spectral convergence from ITPFI structure (framework-specific route)
- Assess severity: does the weakness affect the RH application specifically, or is it a general gap?

### If Boegli Thm 2.6 is BROKEN
- Escalate to **Tier C**: find a larger framework where spectral exactness holds without Boegli
  - Construct spectral exactness directly from the ITPFI structure of D_N operators
  - Use the finite-dimensionality of E_N^+ (each D_N has a finite matrix -- spectral convergence might follow from simpler arguments)
  - Route through Weyl asymptotic methods instead of Boegli's general framework
- This would be a significant finding: a gap in a published, peer-reviewed paper

---

## Honest assessment

Boegli's paper is published in Integral Equations and Operator Theory (Springer, 2017). It has been cited in the spectral approximation literature since publication. The proofs use standard functional analysis machinery (resolvents, compact embeddings, spectral projections).

**Probability of a genuine gap: LOW (~5-10%).** Published, peer-reviewed, clean single-focus paper. Standard machinery. No exotic constructions.

**But verification is the point.** We verify what we depend on, not what we doubt. The value of this pilot is in the DISCIPLINE -- proving that the verification cascade architecture works -- not in the expectation of finding a gap. If all 5 steps SURVIVE, the architecture is validated. If a step is WEAKENED, we learn something about both Boegli and our verification method. Either outcome is a win.

The honest-first stance demands that we verify with the same rigor we would apply to an unreviewed preprint. Published does not mean perfect. Peer-reviewed does not mean gap-free. We check.
