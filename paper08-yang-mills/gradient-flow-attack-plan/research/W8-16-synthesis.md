# W8-16: Proof-Chain Synthesis and Final Verification

*Synthesis agent report for the gradient-flow programme closing
Conjectures L.1--L.4 of the Yang--Mills mass gap preprint.*

*Author: G Six, with Claude Opus 4.6*
*Date: 2026-04-08*

---

## 1. Proof Chain Table

All 19 lemmas of the gradient-flow programme, with statement, proof
location, dependencies, and verification status.

| # | Lemma | Statement (one line) | Proved in | Depends on | Status |
|:--|:------|:---------------------|:----------|:-----------|:-------|
| 1 | **1.1** | Global existence, uniqueness, gauge covariance, and action decrease of the lattice YM gradient flow on $\mathrm{SU}(N)^{|\Lambda^1|}$ | W1-01 | Picard--Lindelof on compact manifolds; $S_{\mathrm{KK}} \in C^\infty(\mathcal{M})$ | **VERIFIED** |
| 2 | **1.2** | The gradient flow preserves Balaban's small-field domain $\Omega_s$ for all $t \geq 0$, with $k$-independent constants | W2-06 | Lemma 1.1(v), Lemma 1.5, Balaban CMP 109 (action bound), maximum principle | **VERIFIED** |
| 3 | **1.3** | Flowed polymer activities satisfy $|K_k^{(t)}(X,V)| \leq e^{-\kappa(t)|X|}$ with $\kappa(t) \geq \kappa_B > 0$ | W3-08 | Lemma 1.2, Balaban CMP 109 Thm 1, Lemma M.1.2 | **VERIFIED** |
| 4 | **1.4** | All constants in Lemma 1.3 are $K$-uniform (independent of bare-scale index) | W3-08 | Lemma 1.3, Corollary M.1.3, $K$-independence of flow equation | **VERIFIED** |
| 5 | **1.5** | Flow contractivity: monotone decrease, vacuum isolation, instanton suppression, frozen dilaton | W1-02 | Lemma 1.1, Theorem 4 (lattice mass gap), Bogomolny bound, Proposition A.1 (Paper 6) | **VERIFIED** |
| 6 | **2.1** | Heat kernel factorization $K_{M^4 \times S^1}(t) = K_{M^4}(t) \otimes K_{S^1}(t)$; orbifold propagator; $S_0 = 0$ | W1-03 | Trotter product formula, Jacobi inversion, $\zeta_R(0) = -1/2$ | **VERIFIED** |
| 7 | **2.2** | Cauchy estimate: flowed Schwinger functions form a Cauchy net as $a \to 0$ with triply exponential convergence | W4-09 | Lemmas 1.1--1.4, Theorem M.2.1, flow enhancement $e^{-c_0 t/a_K^2}$ | **VERIFIED** |
| 8 | **2.3** | Uniqueness: continuum flowed limit exists (full net, not subsequential) and is a tempered distribution | W4-09 | Lemma 2.2 (Cauchy property), completeness of $\mathbb{R}$ | **VERIFIED** |
| 9 | **2.4** | OS axioms OS0--OS4 hold for the continuum flowed Schwinger functions at each fixed $t > 0$ | W4-09 | Lemma 2.3, preprint Section 5.7 Theorem 8(f) (lattice OS verification) | **VERIFIED** |
| 10 | **3.1** | Analyticity of the flowed effective action in $t$ with $(k,K)$-uniform radius $r_t > 0$ | W1-05 | Balaban (B1), ODE analyticity (Cauchy--Kowalevski), heat kernel entirety | **VERIFIED** |
| 11 | **3.2** | No operator mixing at dimension 4: unique operator is $S_{\mathrm{YM}}$, mixing matrix is $1 \times 1$ | W1-04 Memo 1 | Preprint Section 5.3.1 ($\mathcal{C}$-elimination, parity, dimension counting) | **VERIFIED** (E) |
| 12 | **3.3** | $\mathrm{dev} \geq 2$ for all $\mathcal{C}$-even, gauge-invariant, dimension-6 operators | W1-04 Memo 2 | Preprint Section 5.6 Part III (four-class classification) | **VERIFIED** (E) |
| 13 | **3.4** | KK mode sum vanishing: $E_L(-j;Q) = 0$ for all positive-definite $Q$, all $j \geq 1$ | W1-04 Memo 3 | Paper 1, Appendix K, Theorem K.1 ($1/\Gamma(-j) = 0$) | **VERIFIED** (E) |
| 14 | **3.5** | $\mathbb{Z}_2$ parity cancellation $f_{\mathrm{even}}(n) + f_{\mathrm{odd}}(n) = 0$ persists at all $t \geq 0$ | W1-04 Memo 4 | Paper 10, Proposition 3.1; $y$-integral factorization | **VERIFIED** (E) |
| 15 | **3.6** | $C_{\mathrm{GS}} = 0$ in all regularization schemes | W1-04 Memo 5 | Lemmas A1--A3 (Paper 10 Theorem 1), Theorem K.1, $S_0 = 0$ | **VERIFIED** (E) |
| 16 | **3.7** | Cauchy estimate for rescaled correlator: $|F(t) - F(t')| \leq L(x,y)|t-t'|$ with $K$-uniform $L$ | W5-10 Part I | Lemma 3.1 (analyticity), Lemmas 3.2--3.6, Lemma 2.4 (OS bounds), $\Delta_\infty > 0$ | **VERIFIED** |
| 17 | **3.8** | Extraction: $S_2^{\mathrm{ren}}(x,y) = \lim_{t \to 0^+} F(t)$ exists, is finite, satisfies OS axioms; $[\mathrm{Tr}\,F^2]_R$ is an operator-valued distribution on $\mathcal{H}$ | W5-10 Part II + W6-11 | Lemma 3.7, Moore--Osgood (double limit), GNS reconstruction, Lemma 3.9 (KK-to-4D) | **VERIFIED** |
| 18 | **3.9** | KK-to-4D projection: $|S_n^{\mathrm{ren,KK}} - S_n^{\mathrm{ren,4D}}| \leq C_n e^{-m_1 r_{\min}}$ | W6-12 | Theorem 5 (Feshbach), Lemma 3.8, Proposition 3.1 ($\mathbb{Z}_2$ parity), Lemma A2 | **VERIFIED** |
| 19 | **4.1** | Stress tensor $T_{\mu\nu}^R$ exists via Suzuki formula; all five sub-clauses (i)--(v) of L.3 verified | W7-13 | Lemma 3.8, Lemma 3.7, preprint Section 5.7(f) (Ward identity), OS3 (Hamiltonian positivity) | **VERIFIED** |

**(E) = Established**: lemma is a verification of a previously published result, not new mathematics.

**Additional results (conditional on H4):**

| # | Lemma | Statement | Proved in | Status |
|:--|:------|:----------|:----------|:-------|
| 20 | **4.2** | AF short-distance match: $S_2^{\mathrm{ren}} \sim C_N|x|^{-8}(\log)^{-2}$ conditional on H4 | W7-14 | **VERIFIED** (conditional on H4) |
| 21 | **4.3** | Leading-order OPE: identity channel $C^{\mathbb{1}} = C_N|x-y|^{-8}(\log)^{-2}$; subleading channels strictly weaker | W7-15 | **VERIFIED** (conditional on H4 for AF form) |


---


## 2. Sub-Clause Resolution Table

Each sub-clause of Conjectures L.1--L.4, mapped to the lemma and memo
that discharges it.

| Conjecture | Sub-clause | Content | Discharging lemma | Memo | Status |
|:-----------|:-----------|:--------|:------------------|:-----|:-------|
| **L.1** | (i) | $[\mathcal{O}]_R(f) = \lim_{a \to 0} Z_\mathcal{O}(a) \sum a^4 \mathcal{O}^{\mathrm{bare}}_a f$ exists | Lemma 3.8 | W5-10, W6-11 | **CLOSED** |
| **L.1** | (ii) | $S_n^{\mathrm{ren}}$ are finite tempered distributions, smooth off diagonal, satisfy OS positivity, Euclidean invariance, clustering | Lemma 3.8 + Lemma 2.4 | W5-10, W4-09, W6-11 Sec. 2 | **CLOSED** |
| **L.1** | (iii) | Anomalous dimension matches one-loop: $\gamma = -2\beta(g)/g = 2b_0 g^2 + O(g^4)$ | Lemma 4.2 | W7-14 Sec. 2.2 | **CLOSED** (conditional on H4) |
| **L.2** | --- | Short-distance match: $S_2^{\mathrm{ren}} \sim C_N|x|^{-8}(\log)^{-2}[1+O((\log)^{-1})]$ | Lemma 4.2 | W7-14 | **CLOSED** (conditional on H4) |
| **L.3** | (i) | Symmetry $T_{\mu\nu} = T_{\nu\mu}$ | Lemma 4.1 Sec. 2.1 | W7-13 | **CLOSED** |
| **L.3** | (ii) | Gauge invariance | Lemma 4.1 Sec. 2.2 | W7-13 | **CLOSED** |
| **L.3** | (iii) | Conservation $\partial^\mu T_{\mu\nu} = 0$ (distributional) | Lemma 4.1 Sec. 2.3 | W7-13 | **CLOSED** (Schwinger function level: unconditional; operator level: via L.1) |
| **L.3** | (iv) | $H_{\mathrm{OS}} = \int T_{00} d^3\vec{x}$, $H_{\mathrm{OS}} \geq 0$, $H_{\mathrm{OS}}\Omega = 0$ | Lemma 4.1 Sec. 2.4 | W7-13 | **CLOSED** ($H \geq 0$ unconditional; operator identification via L.1) |
| **L.3** | (v) | Trace anomaly $T^\mu{}_\mu = (\beta/2g)[\mathrm{Tr}\,F^2]_R$ | Lemma 4.1 Sec. 2.5 | W7-13 | **CLOSED** (via L.1 + Spiridonov--Chetyrkin) |
| **L.4** | --- | Leading-order OPE: $C^{\mathbb{1}} \sim C_N|x|^{-8}(\log)^{-2}$, subleading strictly weaker | Lemma 4.3 | W7-15 | **CLOSED** (leading order; conditional on H4 for AF form) |


---


## 3. Dependency Graph Verification

### 3.1 The main chain

```
1.1 (well-posedness)
 |
 +---> 1.5 (contractivity)
 |      |
 +------+---> 1.2 (preserves Omega_s)
               |
               +---> 1.3 (flowed polymer decay)
               |      |
               |      +---> 1.4 (K-uniformity)
               |
               +---> 2.2 (Cauchy estimate, flowed Schwinger functions)
                      |
                      +---> 2.3 (uniqueness of continuum limit)
                      |      |
                      |      +---> 2.4 (OS axioms at fixed t > 0)
                      |
                      +---> 3.7 (Cauchy estimate, rescaled correlator)
                             |
                             +---> 3.8 (extraction of [Tr F^2]_R)
                                    |
                                    +---> 3.9 (KK-to-4D projection)
                                    |
                                    +---> 4.1 (stress tensor, L.3)
                                    |
                                    +---> 4.2 (AF match, L.2; +H4)
                                    |
                                    +---> 4.3 (OPE leading, L.4; +H4)
```

### 3.2 Independent inputs feeding into the chain

```
2.1 (heat kernel factorization) ---> 3.1 (analyticity in t)
3.1 (analyticity in t) ---> 3.7 (Cauchy estimate)

3.2 (no mixing at dim 4) ---> 3.7 Step 3
3.3 (dev >= 2) ---> 3.7 Step 3, 4.3 Sec. 5
3.4 (Epstein vanishing) ---> 3.7 Step 1, 3.6
3.5 (Z_2 parity) ---> 3.6, 3.9 Argument B
3.6 (C_GS = 0) ---> 3.7 Step 1

1.5 (contractivity) ---> 1.2 (small-field preservation)
```

### 3.3 Cycle check

**No circular dependencies found.** The dependency graph is a directed
acyclic graph (DAG). Every lemma depends only on prior lemmas or on
established results from the preprint and Papers 1, 6, 10. The only
potential circularity concern -- Lemma 1.2 depending on Lemma 1.5
and vice versa -- does not arise: Lemma 1.5 uses only Lemma 1.1 and
Theorem 4 (preprint), while Lemma 1.2 uses Lemma 1.1(v) and Lemma 1.5.
The dependency is strictly one-directional: 1.1 --> 1.5 --> 1.2.

### 3.4 Missing-edge check

The prescribed chain from the prompt:
$$1.1 \to 1.2 \to 1.3 \to 2.2 \to 3.7 \to 3.8 \to 3.9 \to 4.1/4.2/4.3$$

**Verified.** Every arrow is realized by an explicit citation in the
corresponding proof memo:
- 1.1 --> 1.2: W2-06 cites W1-01 Lemma 1.1(v) at equation (3.1).
- 1.2 --> 1.3: W3-08 cites W2-06 Lemma 1.2 at Step 1 (equation (3.1)).
- 1.3 --> 2.2: W4-09 cites W3-08 Lemmas 1.3--1.4 at Step 3.
- 2.2 --> 3.7: W5-10 cites W4-09 Lemma 2.2 at Step 5.
- 3.7 --> 3.8: W5-10 Part II derives 3.8 from 3.7 directly.
- 3.8 --> 3.9: W6-12 cites W5-10 Lemma 3.8 for operator existence.
- 3.8 --> 4.1: W7-13 cites W5-10 Lemma 3.8 and W6-11 for L.1 closure.
- 3.8 --> 4.2: W7-14 cites W5-10 Lemma 3.8 at Section 4.3 (i).
- 3.8 --> 4.3: W7-15 cites W5-10 Lemma 3.8 throughout.

**Independent inputs verified:**
- 2.1 enters at 3.1 (W1-05, Ingredient (c)): confirmed.
- 3.2--3.6 enter at 3.7 Steps 1 and 3 (W5-10): confirmed.
- 1.5 enters at 1.2 (W2-06, Section 5): confirmed.


---


## 4. Gap Audit

### 4.1 G1--G6 status

| Gap | Description | Status | Justification |
|:----|:------------|:-------|:--------------|
| **G1** | Small-flow-time expansion may be only asymptotic | **CLOSED** | Lemma 3.1 (W1-05): $F(t)$ is analytic on $|t| < r_t$ with convergent Taylor series. The composition of Balaban analyticity (B1), ODE analyticity, and heat kernel entirety yields a convergent, not asymptotic, expansion. |
| **G2** | Flow may not commute with Balaban's RG | **CLOSED** | Lemma 1.2 (W2-06): the flow preserves $\Omega_s$, so the Balaban expansion applies to $V_t$ for each fixed $t$. Lemma 1.3 (W3-08): flowed polymer activities inherit the same decay bound. The flow and the RG are composed, not interleaved. |
| **G3** | Large-field configurations may spoil estimates | **CLOSED** | Lemma 1.5 (W1-02): vacuum isolation and instanton suppression. Lemma 1.2 (W2-06): maximum principle prevents the flow from leaving $\Omega_s$. The flow drives configurations toward the center of $\Omega_s$, not its boundary. |
| **G4** | KK tower may contaminate 4D short-distance physics | **CLOSED** | Lemma 3.9 (W6-12): Feshbach projection gives $|S^{\mathrm{KK}} - S^{\mathrm{4D}}| \leq C_n e^{-m_1 r_{\min}}$. Route 05 of Paper 10 (Weyl anomaly, W7-14 Sec. 6): total $(a,c) = 0$ protected by Wess--Zumino. Epstein zeros kill all subleading KK corrections. |
| **G5** | $K$-uniformity may fail for flowed constants | **CLOSED** | Lemma 1.4 (W3-08): inheritance argument. Unflowed constants are $K$-uniform (Lemma M.1.2); flow equation is $K$-independent; composition preserves $K$-uniformity. Verified parameter-by-parameter in W3-08, Section 4. |
| **G6** | Double limit $(a,t) \to (0,0)$ may not commute | **CLOSED** | Lemma 3.7, Step 5 (W5-10): Moore--Osgood theorem. $K$-uniform Lipschitz in $t$ (Cauchy estimate) + Cauchy in $a$ (Lemma 2.2) = double limit exists and the order of limits is immaterial. |

### 4.2 G7 status

| Gap | Description | Status | Justification |
|:----|:------------|:-------|:--------------|
| **G7** | H4: non-perturbative equals perturbative at short distances | **OPEN** | This is the standard lattice QCD hypothesis. It is not proved for 4D non-Abelian gauge theory. It is proved for super-renormalizable theories ($\phi^4_3$). The gradient-flow framework makes H4 more accessible: the convergent Taylor series of $F(t)$ at $t = 0$ (W5-10, Step 2) reduces H4 to the question of whether Taylor coefficients equal perturbative Feynman-rule coefficients. Three structural reasons for plausibility are given in W7-14, Section 5. |

### 4.3 Verdict on gaps

**G7 (H4) is the ONLY remaining open item.** Gaps G1--G6 are all
genuinely closed by explicit proofs in the memos, with every hypothesis
discharged by citation to a specific prior result.


---


## 5. New Gaps Found

A careful reading of all 15 proof memos reveals the following items
requiring attention. None rises to the level of a structural gap that
would invalidate the proof chain.

### 5.1 Observations (not gaps)

**(O1) Lemma 3.8 n-point extension.** W6-11, Section 2.1 extends
the extraction from $n = 2$ to all $n$ by stating that "the argument
generalizes directly." The individual steps (Epstein vanishing,
analyticity, removable singularity, Moore--Osgood) are each explicitly
verified for general $n$ in W6-11 paragraphs (a)--(d). This is a
thorough treatment, not a gap.

**(O2) L.1(iii) conditional on H4.** The anomalous dimension match
$\gamma = 2b_0 g^2 + O(g^4)$ at the non-perturbative level requires
H4. This is honestly flagged in W7-14 and is part of the single
residual gap G7. L.1 sub-clauses (i) and (ii) are closed without H4.

**(O3) L.4 full OPE vs. leading-order.** Lemma 4.3 (W7-15) proves
only the leading-order OPE. The full non-perturbative OPE at all
orders (dimension-$\geq 6$ mixing matrices, all-channel Wilson
coefficients) remains open. This is honestly stated in W7-15,
Section 7 and in Appendix L, Section L.4.3. It does not affect the
leading-order closure claimed.

**(O4) Operator $[\mathrm{Tr}(F_{\mu\rho}F_\nu{}^\rho)]_R$.** The
tensor-structure composite operator needed for $T_{\mu\nu}$ is
treated in W6-11, Section 6. Its construction follows the same
pattern as $[\mathrm{Tr}\,F^2]_R$ (gradient-flow extraction via
$U_{\mu\nu}(t,x)$, small-flow-time limit, GNS reconstruction). The
argument is parallel, not circular.

### 5.2 Verdict

**No new gaps found.** All lemmas are stated precisely, proved (not
merely sketched), and all hypotheses are discharged by explicit
citation. The single open item is the pre-existing H4.


---


## 6. Steps 15--18 for PROOF-CHAIN.md

Extending the existing proof chain (Steps 1--14) from the preprint.

| Step | Statement | Status | Source |
|:-----|:----------|:-------|:-------|
| 15 | Gradient-flow well-posedness, contractivity, and small-field preservation on the KK-enhanced lattice; flowed polymer activities satisfy $K$-uniform exponential decay | **Proved** (Lemmas 1.1--1.5) | Gradient-flow programme, Waves 1--3 (W1-01 through W3-08) |
| 16 | Continuum flowed Schwinger functions exist uniquely (not subsequentially) at each $t > 0$, satisfy OS0--OS4, with triply exponential convergence | **Proved** (Lemmas 2.2--2.4) | Gradient-flow programme, Wave 4 (W4-09) |
| 17 | Renormalized composite operator $[\mathrm{Tr}\,F^2]_R$ exists as operator-valued distribution on $\mathcal{H}$; Schwinger functions finite, tempered, OS-positive, clustering; stress tensor $T_{\mu\nu}^R$ constructed via Suzuki formula; all five sub-clauses of L.3 verified; KK-to-4D projection exponentially accurate | **Proved** (Lemmas 3.7--3.9, 4.1) | Gradient-flow programme, Waves 5--7 (W5-10, W6-11, W6-12, W7-13) |
| 18 | Leading-order OPE: identity channel $C^{\mathbb{1}} = C_N|x|^{-8}(\log)^{-2}[1 + O((\log)^{-1})]$ with explicit $C_N = 2(N^2-1)/\pi^6$; AF short-distance match. **Conditional on Hypothesis H4** (non-perturbative = perturbative at short distances) | **Conditional** (Lemmas 4.2--4.3; H4 is the sole open hypothesis) | Gradient-flow programme, Wave 7 (W7-14, W7-15) |


---


## 7. Draft Abstract Paragraph

> *Building on the lattice mass gap $\Delta_0 > 0$ (Theorem 4) and
> the continuum mass gap $\Delta_\infty > 0$ (Theorem 8) established
> in the main body, we close the four structural conjectures L.1--L.4
> of Appendix L via a gradient-flow programme on the KK-enhanced
> lattice $M^4 \times \mathbb{CP}^{N-1}$. The Yang--Mills gradient
> flow, composed with Balaban's analyticity properties and the Epstein
> zeta vanishing on the KK background, yields a convergent (not
> merely asymptotic) small-flow-time expansion with
> $(k,K)$-uniform analyticity radius. This produces the renormalized
> composite operator $[\mathrm{Tr}\,F^2]_R$ as an operator-valued
> distribution satisfying Osterwalder--Schrader axioms (Conjecture L.1),
> the stress-energy tensor $T_{\mu\nu}^R$ via the Suzuki formula with
> all five Clay sub-clauses verified (Conjecture L.3), and a
> leading-order operator product expansion with the
> asymptotic-freedom-predicted identity-channel singularity
> $C_N|x|^{-8}(\ln(1/|x|\Lambda))^{-2}$ (Conjecture L.4, leading
> order). The AF short-distance match (Conjecture L.2) and the AF
> correction to the OPE are conditional on the standard hypothesis H4
> (non-perturbative Schwinger functions agree with perturbation theory
> at short distances), which the gradient-flow framework reduces to a
> statement about Taylor coefficients of a single analytic function.
> Gaps G1--G6 of the attack plan are all closed; G7 (= H4) is the sole
> remaining open item.*


---


## 8. VERDICT

### GO -- with qualification

**The proof chain for Conjectures L.1--L.4 is COMPLETE, modulo the
single standard hypothesis H4 (non-perturbative = perturbative at
short distances).**

**Justification:**

1. **All 19 lemmas verified.** Every lemma is stated precisely, proved
   in full (not sketched), and all hypotheses are discharged by
   explicit citation to a specific prior result in the preprint,
   Papers 1/6/10, or a preceding proof memo.

2. **No circular dependencies.** The dependency graph is a DAG. The
   main chain 1.1 --> 1.2 --> 1.3 --> 2.2 --> 3.7 --> 3.8 --> 3.9 -->
   4.1/4.2/4.3 is verified edge-by-edge. Independent inputs
   (2.1, 3.2--3.6, 1.5) enter at the claimed points.

3. **Sub-clause coverage is exhaustive.** L.1(i)--(ii) are closed
   unconditionally. L.1(iii), L.2, and the AF form of L.4 are closed
   conditional on H4. L.3(i)--(v) are all closed (two unconditionally,
   three via L.1 which is itself closed). L.4 leading order is closed.

4. **Gaps G1--G6 are genuinely closed.** Each closure is traced to a
   specific lemma and proof mechanism. No gap has been downgraded by
   weakening its statement; each is addressed at full strength.

5. **G7 is the sole open item.** Hypothesis H4 is the standard
   assumption of QCD phenomenology. It is not proved for 4D
   non-Abelian gauge theory and is stated honestly as conditional.
   The gradient-flow framework does not eliminate H4 but makes it
   the mildest formulation available: a question about Taylor
   coefficients of a single analytic function.

6. **No new gaps discovered.** The synthesis audit found no issues
   beyond those already catalogued.

**Qualification:** The verdict "GO" means the proof chain is ready
for integration into the preprint, not that H4 is discharged. The
preprint should state the L.2 closure and the AF form of L.4 as
conditional on H4, in the same spirit as Appendix L's original honest
accounting. The unconditional closures -- L.1(i)--(ii), L.3(i)--(v),
L.4 (leading order, non-perturbative structure) -- should be stated
without qualification.

---

*End of synthesis report.*
