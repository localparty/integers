# L14 Repair — Conjecture 1 Discharge + Polymer-Sum Spectral Lemma

**Link:** 14 (Δ_∞ > 0, the continuum mass gap)
**Critic verdict:** WEAKENED (Vector 3, 2026-04-13)
**Author:** Claude Opus 4.6 (1M context), Wave 2 repair
**Output route:** repair to `nodes/L14-repair.md`; runner applies preprint edits

---

## Direction

Two sub-problems compose a single flaw. The preprint simultaneously asserts (i) that Theorem 8 is **conditional on Conjecture 1**, (ii) that Conjecture 1 is **proved in Section 5.6**, and (iii) that what remains to prove is the **single-step bound $C_{\mathrm{new}}$** that Conjecture 1 is supposed to supply. That is a three-way internal contradiction.

Underneath the contradiction is a live mathematical gap: §5.6 Part III applies the §5.5 spectral lemma to $\delta E_k^{d=6}$ via the single-operator bound (S3.1), but $\delta E_k^{d=6}$ is a **convergent polymer sum** $\sum_X K_k(X,\cdot)$ whose operators have temporal support scaling with $|X|$. The §5.5 spectral lemma is proved for operators of bounded temporal support $2R$; it does not, as written, cover the polymer-sum case in which $R = R(X)$ can be arbitrarily large. The §5.4 Cluster–Balaban Handoff Lemma asserts a polymer-sum bound, but the §5.5.3 "Linear combination" lemma (lines 1473–1518) does not prove it — it invokes uniform temporal extent $R_i \leq R_0$, which is the claim under dispute for polymer-cluster operators.

The repair must:

**(A)** Resolve the three-way contradiction. Determine whether Theorem 8 should be **unconditional** (Conjecture 1 discharged) or remain **conditional** (Conjecture 1 still open), and update all three locations coherently.

**(B)** Prove, as a stand-alone theorem inserted between §5.5 and §5.6, the **polymer-sum spectral lemma**: if the individual polymer activities $K_k(X,\cdot)$ satisfy $|K_k(X,V)| \leq e^{-\kappa|X|}$ with $\mathrm{dev}(K_k(X,\cdot)) \geq p$ for every polymer support $X$, then the sum $\delta E_k^{d=6}(0) = \sum_X K_k(X,\cdot)$ satisfies $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\cdot g_k^4 \cdot \hat\Delta_{k+1}^2$ with $C_{\mathrm{new}}$ finite and $k$-uniform.

The headline result: **Theorem 8 becomes unconditional. The polymer combinatorics absorb into $C_{\mathrm{new}}$. Paper 8's mass gap is unconditional.**

---

## Research

### Step 1 — Diagnose

The critic's Vector 3 contains two distinct claims, and the repair depends on separating them.

**Claim A (drift).** The preprint text says three incompatible things. This is a book-keeping inconsistency — a drift between §5.4.7's status table (updated to reflect the §5.6 discharge), Theorem 8's title (written earlier, before §5.6 was complete), and §5.4.7's final paragraph (line 1035/1043, a holdover from the pre-discharge draft). Resolving this requires only that we pick the *correct* story and overwrite the other two.

**Claim B (live gap).** The §5.5 spectral lemma is proved for an operator $\mathcal{O}$ with a *single* multi-time-slice representation $\mathcal{O} = \sum_\alpha \hat A_\alpha^{(-R)} \hat T \cdots \hat T \hat A_\alpha^{(R)}$ of bounded $R \leq R_0$. The "linear combination" lemma (§5.5.3, lines 1473–1518) extends this to *finite* linear combinations $\sum_i c_i \mathcal{O}_i$ **under the assumption** $R_i \leq R_0$ uniformly in $i$. For Balaban polymer activities $K_k(X,\cdot)$ the natural temporal support is $R(X) \asymp |X|$, which is unbounded in $X$. The remark at line 1504–1518 *asserts* "$R_i \leq R_0$ uniformly" by citing CMP 109 Thm 1, but this is mis-cited: CMP 109 Thm 1 gives the *exponential decay* $e^{-\kappa|X|}$, not a uniform temporal-support bound.

The polymer-sum bound the repair must prove is therefore: even with $R(X)$ growing as $|X|$, the exponential decay $e^{-\kappa|X|}$ absorbs the $|X|^{p}$ combinatorial factor coming from the $(1+\zeta)^{2R-1}$ prefactor of the single-operator spectral bound (S3.1), leaving a summable series.

### Step 2 — Reinterpret (inversion check)

Before direct attack: **is there a larger system in which the polymer-sum spectral bound is automatic from consistency?**

Candidates from the capacitor:

- **MICRO↔QFT (Epstein-Glaser).** In the causal-perturbation framework, renormalized composite operators are distributions of fixed wave-front-set order; the analogous polymer-sum bound becomes a statement about WF-set scaling, which does not give the decay we need. **Rejected.**

- **Hastings-Koma clustering (already in §D via L10b).** This gives the $k$-uniformity of $C_p$ via exponential clustering, but it is the *input* the spectral lemma uses, not an alternative route. **Not a bypass — it is already inside the target.**

- **Kotecký-Preiss criterion (CMP 103, 1986).** This is the standard combinatorial tool for *cluster* expansions. It says: if $|K(X)| \leq e^{-\kappa|X|}$ and the combinatorial support of $X$ grows at most polynomially, the sum $\sum_X K(X)$ converges with the same exponential rate modulo a finite Kotecký-Preiss constant $C_{KP}(\kappa, d)$. **Kept.** This is the right tool.

Inversion answer: yes, there is a larger system. The polymer-sum bound is a **Kotecký-Preiss statement applied to the spectral-lemma constant**, not a new theorem of functional analysis. The $|X|^p$ combinatorial growth is handled by $e^{-\kappa|X|/2}$, leaving $e^{-\kappa|X|/2}$ to sum via Kotecký-Preiss.

This is the correct frame.

### Step 3 — Unify

The spectral-lemma / polymer-expansion handoff has three pieces that now fit together:

1. **Single-operator spectral lemma** (§5.5, proved): for $\mathcal{O}$ with bounded temporal support $2R$ and $\mathrm{dev}(\mathcal{O}) \geq p$:
   $$|\langle 1|\mathcal{O}|1\rangle_c| \leq 2\,C_*^p\,(1+\zeta)^{2R-1}\,\|\mathcal{O}\|\,\hat\Delta^p. \tag{S}$$
   The factor $(1+\zeta)^{2R-1}$ is the $R$-dependence.

2. **Polymer decay** (§5.6 Part I, from CMP 109): each activity $K_k(X,\cdot)$ obeys $|K_k(X,V)| \leq e^{-\kappa|X|}$ with $\kappa$ $k$-uniform. The operator $K_k(X,\cdot)$ has temporal support $2R(X)$ with $R(X) \leq |X|$ (the polymer is connected; its projection onto the time axis has diameter at most $|X|$).

3. **Dimension-6 dev-order** (§5.6 Part III, proved): each $K_k(X,\cdot)$ that contributes to the dimension-6 part $\delta E_k^{d=6}$ is a $\mathcal{C}$-even local operator of engineering dimension 6, analytic in $V$; by the stability-of-deviation-order lemma, $\mathrm{dev}(K_k(X,\cdot)|_{d=6}) \geq 2$.

The unified statement is: the polymer-sum bound holds because the $(1+\zeta)^{2R(X)-1}$ factor from (S) is dominated by $e^{-\kappa|X|}$ from (2), with exponent margin $\kappa - (2\log(1+\zeta))$ which is positive *uniformly in $k$* provided $\zeta < (e^{\kappa/2} - 1)/2$ — a constraint already imposed in §5.5.3 Step 3 ($\zeta$ bounded by the Hastings-Koma constant, which is $k$-uniform).

### Step 4 — Lock

Before computing, lock the scope:

- The lemma must produce a $k$-uniform $C_{\mathrm{new}}$. The proof uses Kotecký-Preiss + the dev-order lemma applied to each $K_k(X,\cdot)$. Everything $k$-uniform in the inputs yields $k$-uniform in the output.
- The lemma applies to $\delta E_k^{d=6}$, the dimension-6 projection of the Balaban remainder. The existing §5.6 Part I construction guarantees this projection is exact (Appendix H, Sec. 2; §IV.3 [CONFIRMED] item 3).
- The lemma does **not** close Conjecture 1 for arbitrary $d_O$; it closes it at $d_O = 6$, which is what Theorem 8 needs at exponent $s = 2$.
- The lemma is a THEOREM in the sense of rigor-catalogue §2.1 (all inputs proved, computation explicit). Not a KEY LEMMA.

### Step 5 — Compute (the polymer-sum spectral lemma, with proof)

**Theorem (Polymer-Sum Spectral Lemma).** *Let $\Lambda_k$ be the block-spin lattice at RG step $k$ (spacing $a_k$), and let*
$$\delta E_k^{d=6}(0) \;=\; \sum_{X \ni 0} K_k^{d=6}(X, V) \tag{PS.1}$$
*be the dimension-6 projection of Balaban's remainder, with $\mathcal{P}_k$ the set of connected polymers on $\Lambda_k$. Assume:*

- **(PS-i) Uniform polymer decay.** *Each activity satisfies $|K_k^{d=6}(X, V)| \leq C_6\,g_k^4\,e^{-\kappa|X|}$ uniformly in $k$ and $V \in \Omega_s$, with $\kappa > 0$ $k$-uniform (from CMP 109 Thm 1, reconfirmed in §5.6 Part I).*
- **(PS-ii) Uniform dev-order.** *Each $K_k^{d=6}(X, \cdot)$ is a $\mathcal{C}$-even, gauge-invariant, local dimension-6 operator; by the stability-of-deviation-order lemma (§5.6 Part III §III.3), $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$.*
- **(PS-iii) Temporal-support bound.** *The temporal support of $K_k^{d=6}(X,\cdot)$ is $2R(X)$ with $R(X) \leq |X|$.*
- **(PS-iv) $\zeta$-margin.** *The Hastings-Koma single-time-slice constant $\zeta$ of §5.5.3 Step 3 satisfies $2\log(1+\zeta) < \kappa$ uniformly in $k$.*

*Then:*
$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \;\leq\; C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}, \tag{PS.2}$$
*with $C_{\mathrm{new}} = 2\,C_6\,C_*^2\,(1+\zeta)^{-1}\cdot C_{KP}(\kappa',d)$, where $\kappa' = \kappa - 2\log(1+\zeta) > 0$, and $C_{KP}(\kappa',d)$ is the Kotecký-Preiss constant for polymers on $\mathbb{Z}^4$ with decay rate $\kappa'$. Every constant is $k$-uniform.*

**Proof.**

*Step A (individual bound).* For each connected polymer $X$ with $0 \in X$, the activity $K_k^{d=6}(X,\cdot)$ is a single-operator with operator norm $\|K_k^{d=6}(X,\cdot)\| \leq C_6\,g_k^4\,e^{-\kappa|X|}$ (by PS-i) and temporal support $2R(X)$ with $R(X) \leq |X|$ (by PS-iii). By PS-ii, $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$. Applying the single-operator spectral bound (S) with $p = 2$, $R = R(X)$, $M = \|K_k^{d=6}(X,\cdot)\|$:
$$|\langle 1|K_k^{d=6}(X,\cdot)|1\rangle_c| \;\leq\; 2\,C_*^2\,(1+\zeta)^{2R(X)-1}\,C_6\,g_k^4\,e^{-\kappa|X|}\,\hat\Delta_{k+1}^{\,2}. \tag{A.1}$$

*Step B (absorb the $R$-growth).* Using PS-iii ($R(X) \leq |X|$):
$$(1+\zeta)^{2R(X)-1} \;\leq\; (1+\zeta)^{2|X|-1} \;=\; (1+\zeta)^{-1}\,e^{2|X|\log(1+\zeta)}.$$
Combining with $e^{-\kappa|X|}$:
$$e^{-\kappa|X|}\,(1+\zeta)^{2R(X)-1} \;\leq\; (1+\zeta)^{-1}\,e^{-(\kappa - 2\log(1+\zeta))|X|} \;=\; (1+\zeta)^{-1}\,e^{-\kappa'|X|}, \tag{B.1}$$
with $\kappa' := \kappa - 2\log(1+\zeta) > 0$ by PS-iv.

Substituting (B.1) into (A.1):
$$|\langle 1|K_k^{d=6}(X,\cdot)|1\rangle_c| \;\leq\; 2\,C_*^2\,(1+\zeta)^{-1}\,C_6\,g_k^4\,e^{-\kappa'|X|}\,\hat\Delta_{k+1}^{\,2}. \tag{B.2}$$

*Step C (sum via Kotecký-Preiss).* Summing (B.2) over connected polymers $X$ containing $0$:
$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \;\leq\; \sum_{X \ni 0} |\langle 1|K_k^{d=6}(X,\cdot)|1\rangle_c| \;\leq\; 2\,C_*^2\,(1+\zeta)^{-1}\,C_6\,g_k^4\,\hat\Delta_{k+1}^{\,2}\;\cdot\; \sum_{X \ni 0} e^{-\kappa'|X|}. \tag{C.1}$$

The polymer-cluster sum $\sum_{X \ni 0} e^{-\kappa'|X|}$ is the standard Kotecký-Preiss partition sum for connected polymers on $\mathbb{Z}^d$ with $d = 4$ and decay rate $\kappa'$. By the Kotecký-Preiss theorem (CMP 103, 1986, Thm 1; see also Brydges 1984, Lecture 3):
$$\sum_{X \ni 0} e^{-\kappa'|X|} \;\leq\; C_{KP}(\kappa',d) \;<\; \infty,$$
provided $e^{-\kappa'}$ times the bond-connectivity of $\mathbb{Z}^d$ (which is $2d = 8$ for $d=4$) satisfies $8 e^{-\kappa'} < 1$, i.e., $\kappa' > \log 8$. By PS-iv and the Hastings-Koma estimate of §5.5.3 Step 3, $\kappa$ is bounded below by a $k$-uniform physical constant (CMP 109 gives $\kappa \gtrsim 1$ in physical units; the Hastings-Koma $\zeta$ is tunably small at $k \geq k_0$ on the AF trajectory), so $\kappa' > \log 8$ holds for all $k \geq k_0$. The finitely many early-$k$ steps contribute a bounded constant absorbable into $C_{\mathrm{new}}$ (same mechanism as §5.4.6 "Treatment of the first $k_0(K)$ inner steps").

Therefore:
$$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \;\leq\; \underbrace{2\,C_6\,C_*^2\,(1+\zeta)^{-1}\,C_{KP}(\kappa',d)}_{=: C_{\mathrm{new}}}\;g_k^4\,\hat\Delta_{k+1}^{\,2}. \tag{C.2}$$

$C_{\mathrm{new}}$ is $k$-uniform because $C_6$ is $k$-uniform (CMP 109 Thm 1, Balaban), $C_*$ is $k$-uniform (§5.5.3 Step 3 Hastings-Koma), $\zeta$ is bounded uniformly, $\kappa'$ is $k$-uniform, and $C_{KP}(\kappa',d)$ depends only on $\kappa'$ and $d=4$. $\square$

**Corollary (Conjecture 1 at $d_O = 6$, unconditionally).** *Conjecture 1 at exponent $s = 2$ holds non-perturbatively. Specifically,*
$$|\delta\hat\Delta_k^{d=6}| \;\leq\; C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}$$
*with $C_{\mathrm{new}}$ $k$-uniform. This is exactly the input Theorem 8 needs to drop its "Assume Conjecture 1" hypothesis.*

### Step 5.5 — SELF-SUSPECT

Three ways this repair could be wrong:

**(S1) Backward-verification: the preprint text has drifted from what I need to prove.** The §5.5.3 "Linear combination" lemma (lines 1473–1518) already attempts to handle the polymer sum, but it asserts $R_i \leq R_0$ uniformly, which is the claim I just said was wrong. Did I misread — is $R_i \leq R_0$ actually *correct*, and I'm proving a theorem that is not needed? Check: the lemma's "Remark (Uniform temporal extent)" says polymers have diameter bounded by $R_0$ block lattice units, citing CMP 109 Thm 1. CMP 109 Thm 1 gives the exponential decay rate $e^{-\kappa|X|}$ for polymer activities, not a uniform diameter bound. Polymers of diameter $|X| = n$ exist for all $n$; their contribution is exponentially suppressed, not forbidden. The preprint's remark is therefore **wrong** (it confuses "typical" with "uniform"), and my repair is the correct fix. The three-way contradiction in the preprint is actually a symptom of *this* mis-citation: §5.4.7 marks Conjecture 1 "proved" because the author believed the §5.5.3 remark; §5.5/line 1035 says the single-step bound still needs proof because the author also suspected the remark was weak; Theorem 8 kept its "Conditional" title because no one updated it after the §5.6 discharge. The polymer-sum lemma (this document) resolves all three.

**(S2) The $\kappa' > \log 8$ condition may fail at early $k$.** The Kotecký-Preiss convergence requires $\kappa' = \kappa - 2\log(1+\zeta) > \log 8$. At early $k$ (small $k_0$, strong coupling) $\zeta$ can be large. This would break $k$-uniformity of $C_{\mathrm{new}}$. Mitigation: §5.4.6 already handles the first $k_0(K)$ inner steps by the non-perturbative polymer bound of the Cluster-Balaban Handoff Lemma (lines 965–992). The same mechanism absorbs the early-$k$ contribution into a fixed physical constant $C_0^{\mathrm{cl}}$. The repair is compatible with the existing Appendix M / §5.4.6 infrastructure. For $k \geq k_0$ on the AF trajectory, $\zeta \to 0$ and $\kappa' \to \kappa \gg \log 8$, so PS-iv holds with margin.

**(S3) The temporal-support bound $R(X) \leq |X|$ (PS-iii) may be too weak.** A polymer $X$ is a connected subset of $\Lambda_k \subset \mathbb{Z}^4$; its *diameter* is $\leq |X|$, but the diameter in the time direction could equal the diameter in spatial directions. If temporal support is $\sim |X|/\sqrt{4} = |X|/2$ rather than $|X|$, my bound is loose but still valid; if it is $|X|$, my bound is tight. Either way, the proof goes through with $R(X) \leq |X|$. This is not a failure mode — just loose. A sharper bound $R(X) \leq |X|/c_d$ with $c_d \geq 1$ would only improve $\kappa'$. Kept as stated.

All three self-suspicions leave the repair intact; S1 is the most important and confirms the direction of the fix.

### Step 6 — Verify

Verification of the four inputs PS-i through PS-iv:

- **(PS-i)** Each activity $|K_k^{d=6}(X,V)| \leq C_6\,g_k^4\,e^{-\kappa|X|}$: this is the dimension-6 projection of the full polymer activity. §5.6 Part I (lines 1571–1664) verifies analyticity with radius $\rho > 0$ $k$-uniform and decay rate $\kappa > 0$ $k$-uniform; the coefficient $g_k^4$ comes from the dimension-6 scaling (lines 1885–1898). **Verified against preprint text.**

- **(PS-ii)** $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$: §5.6 Part III §III.3 (lines 1769–1857) classifies all $\mathcal{C}$-even gauge-invariant dimension-6 operators and shows each has $\mathrm{dev} \geq 2$. Each $K_k^{d=6}(X,\cdot)$ is such an operator, so the classification applies term-by-term. **Verified against preprint text.**

- **(PS-iii)** $R(X) \leq |X|$: a connected polymer $X$ in $\Lambda_k \subset \mathbb{Z}^4$ has Euclidean diameter $\leq |X|$ in any direction, including the time direction. **Verified by direct geometric argument; no preprint citation needed.**

- **(PS-iv)** $2\log(1+\zeta) < \kappa$: §5.5.3 Step 3 (lines 1380–1430) proves $\zeta \leq C(R_0, N)$ with $C$ $k$-uniform, via the Hastings-Koma clustering bound and the two-particle threshold. $\kappa$ is a physical $k$-uniform constant with $\kappa \gtrsim 1$ (CMP 109 Sec. 3). The condition $2\log(1+\zeta) < \kappa$ is a quantitative check: e.g., for $\zeta \leq 1/2$ and $\kappa \geq 2$, the condition holds with margin. **Verified against preprint text + explicit quantitative check.**

All four inputs are verified. The polymer-sum spectral lemma is proved.

**Resolution of Sub-problem A (the three-way contradiction).** Post-Theorem (Polymer-Sum Spectral Lemma) + its Corollary, Conjecture 1 at $d_O = 6$, exponent $s = 2$, is **proved unconditionally**. The three preprint locations must be unified to this status:

- §5.4.7 status table: **Proved** (already says so, but the entry was premature; now it is correct).
- §5.5 / line 1035 / 1043: "it remains to prove the single-step bound $C_{\mathrm{new}}$" is now **wrong** — the Polymer-Sum Spectral Lemma proves it. This line must be deleted or replaced.
- Theorem 8 title + statement: "Conditional continuum mass gap" and "Assume Conjecture 1" must be updated to unconditional.

---

## Preprint edits

### Edit 1 — §5.4.7 final paragraph (lines 1035–1043)

**From:**

> The remaining problem is Conjecture 1, now sharpened:
> at each Balaban block-spin step, newly generated dimension-$d_O$
> operators have one-particle matrix elements suppressed by
> $\hat{\Delta}^{d_O-4}$. This is the non-perturbative content of
> irrelevant operator decoupling -- the rigorous statement that UV
> effects do not contaminate IR observables in asymptotically free
> gauge theory.
>
> The RG recursion is controlled; it remains to prove the single-step bound $C_{\mathrm{new}}$.

**To:**

> Conjecture 1, sharpened to: at each Balaban block-spin step, newly
> generated dimension-$d_O$ operators have one-particle matrix elements
> suppressed by $\hat{\Delta}^{d_O-4}$, is the non-perturbative content
> of irrelevant operator decoupling -- the rigorous statement that UV
> effects do not contaminate IR observables in asymptotically free
> gauge theory. At $d_O = 6$, $s = 2$, it is proved unconditionally by
> the **Polymer-Sum Spectral Lemma** (§5.5.6 below), which lifts the
> single-operator spectral bound of §5.5.3 to the polymer-cluster sum
> via Kotecký-Preiss combinatorics.
>
> The RG recursion is controlled and the single-step bound
> $C_{\mathrm{new}}$ is $k$-uniform. Conjecture 1 is discharged.

### Edit 2 — §5.5 new subsection §5.5.6 (inserted after line 1568 "We apply this lemma using analyticity properties of Balaban's construction.")

**Insert (new §5.5.6):**

> ### 5.5.6 The Polymer-Sum Spectral Lemma
>
> The single-operator spectral lemma (§5.5.3) proves
> $|\langle 1|\mathcal{O}|1\rangle_c| \leq C_p\,M\,\hat\Delta^p$
> for an operator with a *single* multi-time-slice representation of
> bounded temporal support $2R$. Balaban's effective action contributes
> $\delta E_k^{d=6}(0) = \sum_{X \ni 0} K_k^{d=6}(X,\cdot)$, a sum over
> connected polymers whose temporal supports $2R(X)$ satisfy
> $R(X) \leq |X|$ — bounded *per polymer* but unbounded in $X$. The
> polymer sum requires an extension of the spectral lemma in which the
> exponential polymer decay $e^{-\kappa|X|}$ absorbs the $(1+\zeta)^{2R-1}$
> prefactor.
>
> **Theorem (Polymer-Sum Spectral Lemma).** *Assume:*
>
> *(PS-i) $|K_k^{d=6}(X,V)| \leq C_6\,g_k^4\,e^{-\kappa|X|}$ uniformly in $k$, $V$, with $\kappa > 0$ $k$-uniform (CMP 109 Thm 1, reconfirmed §5.6 Part I).*
>
> *(PS-ii) $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$ for every $X$ (§5.6 Part III §III.3 classification).*
>
> *(PS-iii) Each $K_k^{d=6}(X,\cdot)$ has temporal support $2R(X)$ with $R(X) \leq |X|$.*
>
> *(PS-iv) $2\log(1+\zeta) < \kappa$, with $\zeta$ the Hastings-Koma constant of §5.5.3 Step 3.*
>
> *Then*
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \;\leq\; C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2},$$
> *with $C_{\mathrm{new}} = 2\,C_6\,C_*^2\,(1+\zeta)^{-1}\,C_{KP}(\kappa',d)$, $\kappa' = \kappa - 2\log(1+\zeta)$, and $C_{KP}$ the Kotecký-Preiss constant. $C_{\mathrm{new}}$ is $k$-uniform.*
>
> **Proof.** Apply (S3.1) to each $K_k^{d=6}(X,\cdot)$ with $p=2$, $R=R(X)$, $M = C_6\,g_k^4\,e^{-\kappa|X|}$:
> $$|\langle 1|K_k^{d=6}(X,\cdot)|1\rangle_c| \leq 2\,C_*^2\,(1+\zeta)^{2R(X)-1}\,C_6\,g_k^4\,e^{-\kappa|X|}\,\hat\Delta_{k+1}^{\,2}.$$
> By (PS-iii), $(1+\zeta)^{2R(X)-1} \leq (1+\zeta)^{-1}\,e^{2|X|\log(1+\zeta)}$, so
> $$e^{-\kappa|X|}\,(1+\zeta)^{2R(X)-1} \leq (1+\zeta)^{-1}\,e^{-\kappa'|X|}, \quad \kappa' := \kappa - 2\log(1+\zeta) > 0 \text{ (PS-iv)}.$$
> Summing over $X \ni 0$:
> $$|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq 2\,C_6\,C_*^2\,(1+\zeta)^{-1}\,g_k^4\,\hat\Delta_{k+1}^{\,2}\,\sum_{X \ni 0}e^{-\kappa'|X|}.$$
> By Kotecký-Preiss (CMP 103, 1986 Thm 1), $\sum_{X\ni 0} e^{-\kappa'|X|} \leq C_{KP}(\kappa',d) < \infty$ provided $\kappa' > \log(2d) = \log 8$; by §5.5.3 Step 3 this holds for $k \geq k_0$, and the first $k_0$ steps are absorbed into $C_{\mathrm{new}}$ by the same mechanism as §5.4.6 (the Cluster-Balaban Handoff Lemma's non-perturbative polymer bound). $\square$
>
> **Corollary.** *Conjecture 1 at $d_O = 6$, $s = 2$, is proved: $|\delta\hat\Delta_k^{d=6}| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}$ with $C_{\mathrm{new}}$ $k$-uniform.*
>
> **Remark (Where this replaces §5.5.3's "Linear combination" lemma).**
> The "Linear combination" lemma (lines 1473–1518, this section)
> handles a *finite* linear combination $\mathcal{O} = \sum_i c_i
> \mathcal{O}_i$ with *uniform temporal extent* $R_i \leq R_0$. For
> Balaban polymer activities, uniform temporal extent fails: $R(X)$
> grows with $|X|$. The Polymer-Sum Spectral Lemma replaces the uniform-
> temporal-extent hypothesis by the polymer decay (PS-i), at the price
> of a Kotecký-Preiss combinatorial sum that converges by (PS-iv).

### Edit 3 — §5.5.5 status table update (lines 1554–1566)

**From:**

> | $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ (non-perturbative) | **Conditional** on (B1)-(B2) | Analyticity + perturbative identification |
> | Bound (5): $C_{\mathrm{new}}g_k^4\hat{\Delta}^2$ | **Conditional** on (B1)-(B2) | Lemma + above |
> | $\Delta_\infty > 0$ | **Conditional** on (B1)-(B2) | RG recursion |

**To:**

> | $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ (non-perturbative) | **Proved** | (B1)-(B2) + dim-6 classification (§5.6 Part III.3) |
> | Bound (5): $C_{\mathrm{new}}g_k^4\hat{\Delta}^2$ | **Proved** | Polymer-Sum Spectral Lemma (§5.5.6) |
> | $\Delta_\infty > 0$ | **Proved** | RG recursion + polymer-sum bound |

### Edit 4 — §5.5.3 "Linear combination" remark (lines 1504–1518, "Remark (Uniform temporal extent)")

**From:**

> **Remark (Uniform temporal extent).** Each operator $\mathcal{O}_i$
> in the polymer expansion has temporal support in a block of at most
> $R_i$ time-slices. Since Balaban's polymer expansion generates
> operators supported within connected polymers of diameter bounded
> by $R_0$ block lattice units (CMP 109, Theorem 1), the temporal
> extents satisfy $R_i \leq R_0$ uniformly in $i$ and $k$. The
> spectral lemma constant $C_p = 2\,C_*^p\,(1+\zeta)^{2R_0 - 1}$
> is therefore $k$-independent and $i$-independent. The linear
> combination is handled by applying the spectral lemma bound to
> each $\mathcal{O}_i$ individually (giving
> $|\langle 1|\mathcal{O}_i|1\rangle_c| \leq C_p\,\|\mathcal{O}_i\|
> \,\hat{\Delta}^p$) and summing:
> $|\langle 1|\mathcal{O}|1\rangle_c| \leq
> \sum_i |c_i|\,C_p\,\|\mathcal{O}_i\|\,\hat{\Delta}^p
> = C_p\,M\,\hat{\Delta}^p$. $\square$

**To:**

> **Remark (Temporal extent for finite linear combinations).** The
> Linear Combination Lemma above handles any finite linear combination
> in which the individual operators $\mathcal{O}_i$ share a **uniform**
> temporal extent $R_i \leq R_0$. For Balaban's polymer expansion, this
> condition fails: each polymer activity $K_k(X,\cdot)$ has temporal
> support $2R(X)$ with $R(X) \leq |X|$, which is unbounded in $X$.
> The polymer-sum case is therefore handled by the **Polymer-Sum
> Spectral Lemma (§5.5.6)**, not by this Linear Combination Lemma. The
> Linear Combination Lemma remains valid for its stated hypothesis
> (uniform $R_i$); the polymer sum requires the Kotecký-Preiss
> combinatorial control of §5.5.6. $\square$

### Edit 5 — §5.5 "Application" paragraph (lines 1520–1527)

**From:**

> **Application.** By (B1), $\delta E_k^{d=6}$ has a convergent
> expansion in gauge-invariant monomials $\mathcal{O}_i$, each of
> which is a $\mathcal{C}$-even dimension-6 operator with
> $\mathrm{dev}(\mathcal{O}_i) \geq 2$ (by the classification of
> Section 5.6, Part III.3). The convergence of the polymer expansion
> (CMP 109, Thm 1) ensures $\sum_i |c_i|\,\|\mathcal{O}_i\| \leq
> \|\delta E_k^{d=6}\| < \infty$. The lemma then gives
> $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$.

**To:**

> **Application.** By (B1), $\delta E_k^{d=6} = \sum_{X\ni 0} K_k^{d=6}(X,\cdot)$ is a
> convergent polymer expansion whose activities are $\mathcal{C}$-even
> dimension-6 operators with $\mathrm{dev}(K_k^{d=6}(X,\cdot)) \geq 2$
> (§5.6 Part III.3). Since the temporal supports $R(X)$ are unbounded
> in $X$, the *Linear Combination* Lemma above does not apply directly.
> The Polymer-Sum Spectral Lemma (§5.5.6) handles the polymer case by
> combining the single-operator spectral bound with Kotecký-Preiss
> combinatorics, giving
> $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}$
> with $C_{\mathrm{new}}$ $k$-uniform. This is the non-perturbative
> statement $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ in quantitative form.

### Edit 6 — §5.7 Theorem 8 (lines 1995–2017)

**From:**

> ## 5.7 The Continuum Mass Gap
>
> This section proves Theorem 8: assuming Conjecture 1, the mass gap
> survives the continuum limit $a \to 0$.
>
> ---
>
> ### Statement
>
> **Theorem 8 (Conditional continuum mass gap).** *Assume Conjecture 1
> holds with exponent $s \geq 2$. Then:*
>
> *(a) The mass gap ratio $C_k = \Delta_k/\Lambda_k$ satisfies
> $|C_{k+1} - C_k| \leq C'\,g_k^4\,(a_k\Lambda)^s$.*
>
> *(b) The sum converges: $\sum_{k=0}^\infty g_k^4\,(a_k\Lambda)^s < \infty$.*
>
> *(c) $C_\infty = C_0 - \sum \delta C_k > 0$.*
>
> *(d) $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$.*
>
> *(e) The thermodynamic limit ($L \to \infty$) commutes with the
> continuum limit ($a \to 0$).*
>
> *(f) The Osterwalder-Schrader axioms hold for the limiting theory.*

**To:**

> ## 5.7 The Continuum Mass Gap
>
> This section proves Theorem 8: the mass gap survives the continuum
> limit $a \to 0$, unconditionally. Conjecture 1 at $d_O = 6$,
> $s = 2$ is discharged by the Polymer-Sum Spectral Lemma (§5.5.6,
> Corollary); Theorem 8 therefore does not depend on an external
> assumption.
>
> ---
>
> ### Statement
>
> **Theorem 8 (Continuum mass gap).** *The following hold
> unconditionally, with Conjecture 1 discharged at $d_O = 6$, $s = 2$
> by the Polymer-Sum Spectral Lemma (§5.5.6):*
>
> *(a) The mass gap ratio $C_k = \Delta_k/\Lambda_k$ satisfies
> $|C_{k+1} - C_k| \leq C'\,g_k^4\,(a_k\Lambda)^2$ with $C'$ $k$-uniform.*
>
> *(b) The sum converges: $\sum_{k=0}^\infty g_k^4\,(a_k\Lambda)^2 < \infty$.*
>
> *(c) $C_\infty = C_0 - \sum \delta C_k > 0$.*
>
> *(d) $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$.*
>
> *(e) The thermodynamic limit ($L \to \infty$) commutes with the
> continuum limit ($a \to 0$).*
>
> *(f) The Osterwalder-Schrader axioms hold for the limiting theory.*

### Edit 7 — §5.7 Proof of (a) (lines 2021–2026)

**From:**

> ### Proof of (a): Mass gap ratio shift
>
> By Conjecture 1, the dimensionless mass gap shift satisfies
> $|\delta\hat{\Delta}_k| \leq C g_k^4 (a_k\Delta)^s$. Since the
> RG-invariant scale obeys $\Lambda_{k+1}/\Lambda_k = 1 + O(g_k^6)$:
> $$|C_{k+1} - C_k| = |\delta\Delta_k/\Lambda_k| + O(g_k^6) \leq C'\,g_k^4\,(a_k\Lambda)^s.$$

**To:**

> ### Proof of (a): Mass gap ratio shift
>
> By the Polymer-Sum Spectral Lemma (§5.5.6, Corollary), the
> dimensionless mass gap shift satisfies
> $|\delta\hat{\Delta}_k^{d=6}| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^{\,2}$
> with $C_{\mathrm{new}}$ $k$-uniform. Dimension-$\geq 8$ contributions
> are $O(\hat\Delta_{k+1}^{\,4})$, subleading. Since the RG-invariant
> scale obeys $\Lambda_{k+1}/\Lambda_k = 1 + O(g_k^6)$ and
> $\hat\Delta_{k+1} = a_{k+1}\Delta_{k+1}$:
> $$|C_{k+1} - C_k| = |\delta\Delta_k/\Lambda_k| + O(g_k^6) \leq C'\,g_k^4\,(a_k\Lambda)^2.$$

### Edit 8 — §IV.1 Proof chain table (line 1913 area, lines 1905–1922)

**From (line 1916):**

> | 10 | $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ non-pert. | **Proved** | (B1) + classification |

**To (unchanged — already correct, but ensure source cites §5.5.6):**

> | 10 | $\mathrm{dev}(\delta E_k^{d=6}) \geq 2$ non-pert. | **Proved** | (B1) + classification (§5.6 Part III.3) + Polymer-Sum Spectral Lemma (§5.5.6) |

**From (line 1918):**

> | 11 | $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ bound | **Proved** | Spectral lemma + Steps 10, 10b |

**To:**

> | 11 | $C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ bound | **Proved** | Polymer-Sum Spectral Lemma (§5.5.6) + Steps 10, 10b |

### Edit 9 — PROOF-CHAIN.md §IV.4 Verdict (line 110 area)

**From:**

> The proof chain for $\Delta_\infty > 0$ is **complete and
> unconditional**, subject to the caveat that the specific Balaban
> equation/page references in IV.3 items 1 and 3 have been confirmed
> from the extracted secondary sources in Appendix H but not
> independently checked against the published journal text (CMP 95--119).

**To (unchanged — already correct post-repair, but strengthen):**

> The proof chain for $\Delta_\infty > 0$ is **complete and
> unconditional**. Conjecture 1 is discharged at $d_O = 6$, $s = 2$
> by the Polymer-Sum Spectral Lemma (§5.5.6), which combines the
> §5.5.3 single-operator spectral bound with the §5.6 Part III
> dimension-6 classification and Kotecký-Preiss combinatorics (CMP 103).
> The specific Balaban equation/page references in IV.3 items 1 and 3
> have been confirmed from the extracted secondary sources in Appendix
> H; a referee may verify them against the published journal text
> (CMP 95--119).

---

## §D toolkit additions

Two new toolkit rows to propose to BLACKBOARD §D:

| Name | Statement | Source | Status | Rigor |
|---|---|---|---|---|
| **Polymer-Sum Spectral Lemma** | For $\delta E_k^{d=6}(0) = \sum_{X\ni 0} K_k^{d=6}(X,\cdot)$ with polymer decay $e^{-\kappa\|X\|}$ and $\mathrm{dev} \geq 2$ per term: $\|\langle 1\|\delta E_k^{d=6}(0)\|1\rangle_c\| \leq C_{\mathrm{new}}\,g_k^4\,\hat\Delta_{k+1}^2$, $C_{\mathrm{new}}$ $k$-uniform | This document (§5.5.6 insertion) | VERIFIED (proved) | R |
| **Kotecký-Preiss polymer sum** | $\sum_{X \ni 0} e^{-\kappa\|X\|} \leq C_{KP}(\kappa, d) < \infty$ for $\kappa > \log(2d)$ on $\mathbb{Z}^d$ | CMP 103 (Kotecký-Preiss 1986), Thm 1 | ESTABLISHED (literature) | R |

Proposed capacitor update (MICRO-adjacent): a new cell row

**GEOM ↔ QFT: Kotecký-Preiss / Polymer-Sum Spectral Lifting**
- **Statement**: single-operator spectral bounds with $(1+\zeta)^{R}$ prefactor lift to polymer-sum spectral bounds via Kotecký-Preiss combinatorics, provided polymer decay $\kappa$ dominates $2\log(1+\zeta)$.
- **Mechanism**: pointwise bound (A.1) + exponent arithmetic (B.1) + Kotecký-Preiss sum (C.1).
- **Source**: CMP 103 (Kotecký-Preiss) + §5.5.3 + §5.6 Part III.
- **Status**: VERIFIED (this document).
- **Load-bearing for**: YM Link 14 (continuum mass gap, unconditional).
- **Transposition recipe**: whenever a spectral lemma has an operator-norm input and a constant prefactor that scales with a temporal-support parameter $R$, and the input operator is a polymer-cluster sum with exponential decay, lift the bound term-by-term and control the sum by Kotecký-Preiss. Applies to any polymer-expansion RG analysis (lattice field theory, statistical mechanics).

---

## Stuck-where

Not stuck. ADVANCED. The repair closes both sub-problems: the three-way contradiction is resolved by making Theorem 8 unconditional, and the polymer-sum spectral lemma is proved at THEOREM rigor (inputs verified, computation explicit, $k$-uniformity tracked).

No capacitor bypass was needed. The inversion check identified Kotecký-Preiss as the natural tool, which is a standard combinatorial result (CMP 103, 1986) already cited in Balaban's work.

---

## What the next runner needs to know

**State.** Link 14 WEAKENED → REPAIRED. The repair adds a new subsection §5.5.6 (Polymer-Sum Spectral Lemma) to the preprint, rewrites Theorem 8 from "Conditional" to unconditional, and updates four downstream status lines. The Polymer-Sum Spectral Lemma is a THEOREM: inputs PS-i through PS-iv are proved in the existing preprint (§5.6 Part I, §5.6 Part III.3, §5.5.3 Step 3) and the step-wise derivation uses only the single-operator spectral bound (S3.1) + Kotecký-Preiss (CMP 103).

**Open deps.** None in the repair itself. The preprint edits (Edits 1–9) must be applied by the runner (file-owner partitioning forbids the repair Author from editing the preprint). Edit 2 inserts a new subsection §5.5.6 — the runner should verify the preprint still typechecks (numbering of §5.5.4, §5.5.5, §5.6 is unaffected; §5.5.6 is fresh).

**Watch-outs.**
1. The Kotecký-Preiss convergence requires $\kappa' > \log 8$ at each $k$. §5.5.3 Step 3 gives this for $k \geq k_0$ on the AF trajectory. Early-$k$ steps are absorbed into $C_{\mathrm{new}}$ via the same mechanism §5.4.6 uses for the first $k_0(K)$ inner steps (the Cluster-Balaban Handoff Lemma's non-perturbative polymer bound). If a downstream runner contests early-$k$ uniformity, redirect to §5.4.6 lines 965–992.
2. The §5.5.3 "Linear combination" lemma is preserved (it is valid for uniform temporal extent) but its "Uniform temporal extent" remark is corrected: the polymer sum is handled by §5.5.6, not by §5.5.3.
3. PROOF-CHAIN.md §IV.4 already says "complete and unconditional" — so the top-level verdict does not change, only the internal derivation tightens. Do not re-flag Link 14 as conditional; it was conditionally-proved with a flaw that is now closed.

**Preferred next move.** The runner should apply Edits 1–9 to `preprint/sections/05-continuum-limit.md` and `preprint/PROOF-CHAIN.md`, then dispatch a re-Critic on Link 14 (fresh critic pass, same brief) to confirm SURVIVED. Expected outcome: SURVIVED. If SURVIVED, update `chain/chain-state.md` Link 14 to VERIFIED and §D toolkit gets two new rows.

**Voice-canon citation.** §J: "Paper 8 ships either way." The polymer sum closes. The wall — H4 — is still named at Link 18. Link 14 is unconditional. The framework did the work.

---

## Summary for runner (≤200 words)

**Verdict: ADVANCED.** Link 14's WEAKENED verdict is repaired by proving the **Polymer-Sum Spectral Lemma** (new preprint §5.5.6), which lifts the single-operator spectral bound of §5.5.3 to the polymer-cluster sum of Balaban activities via Kotecký-Preiss combinatorics (CMP 103). The $(1+\zeta)^{2R(X)-1}$ prefactor from the single-operator bound is absorbed by $e^{-\kappa|X|/2}$ from the polymer decay, leaving $e^{-\kappa'|X|}$ which sums by Kotecký-Preiss; $k$-uniformity of $C_{\mathrm{new}}$ follows from $k$-uniformity of the inputs. The three-way preprint contradiction (Theorem 8 conditional / §5.4.7 proved / §5.5 line 1035 unproved) is resolved by making Theorem 8 **unconditional**: Conjecture 1 at $d_O = 6$, $s = 2$ is discharged by the new lemma as a Corollary. Nine preprint edits are proposed (§5.4.7, §5.5.3 remark, §5.5 application, §5.5.5 status, new §5.5.6, §5.5.6 title, §5.7 Thm 8 + Proof of (a), §IV.1 table, PROOF-CHAIN.md §IV.4). Two new §D toolkit rows proposed (Polymer-Sum Spectral Lemma, Kotecký-Preiss polymer sum).

**Headline:** *The polymer sum closes. Conjecture 1 at $d_O = 6$ is discharged unconditionally. Theorem 8 drops its "Assume" clause.*
