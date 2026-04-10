# Hostile Referee Report: Release Candidate

Date: 2026-04-05

---

## Point 1: The Stability of Excitation Number Lemma

**Verdict:** CLOSABLE GAP

**Finding:**

**(a) Exhaustiveness of the classification.**
The four-class classification (Section 5.6, Part III.3) is sound. The question whether lattice-specific operators contaminate the dimension-6 sector has a clean negative answer. On the hypercubic lattice, products of plaquettes at a single site -- such as $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^3$ -- expand as:

$$(\mathrm{Re}\,\mathrm{Tr}\,U_P)^3 = N^3 - \tfrac{3N}{2}\,a^4\,\mathrm{Tr}(F^2) + O(a^8)$$

The leading non-constant term is dimension 4 (absorbed into coupling renormalization). The next correction is dimension 8. There is **no dimension-6 contribution from zero-derivative plaquette products**. The reason is structural: each factor of $(U_P - \mathbf{1})$ contributes dimension 4, so a product of $n$ factors gives dimension $4n$; dimension 6 requires exactly one factor of $(U_P - \mathbf{1})$ (dimension 4) composed with a derivative operation (dimension 2). The lattice artifact at $O(a^2)$ in the expansion of a single plaquette is precisely $a^6 \mathrm{Tr}(DF)^2 + \ldots$, which has two covariant derivatives and falls into Class III.

The Luscher--Weisz operator basis confirms that the complete list of dimension-6 lattice operators in the C-even sector consists of the two-derivative operators $\mathrm{Tr}(D_\rho F_{\mu\nu})^2$ and $\mathrm{Tr}(D_\mu F^{\mu\rho} D_\nu F^\nu{}_\rho)$ (related by equations of motion), plus the C-odd cubics (eliminated). **The classification is exhaustive.**

**(b) Ghost fields and gauge fixing.**
No gap. Balaban's construction uses axial gauge fixing for the fluctuation integral, but the resulting effective action $S_k[V]$ is gauge-invariant by the gauge-equivariance of the block-spin kernel (CMP 98, Sec. 2). The Faddeev--Popov determinant is integrated out at each step; its contribution is absorbed into the polymer activities $K_k(X,V)$, which are gauge-invariant by construction. Ghost-dependent operators do not appear as separate terms in the gauge-invariant effective action. The dimension-6 classification applies to this gauge-invariant object.

**(c) Lattice artifacts from the Wilson action.**
No gap. The Wilson action's $O(a^2)$ lattice artifacts are dimension-6 operators of the $\mathrm{Tr}(DF)^2$ type, falling into Class III. Under the block-spin RG, these propagate as dimension-6 contributions to the remainder $E_k$. They cannot mix with $S_{\mathrm{YM}}$ (dimension 4) because $S_{\mathrm{YM}}$ is the unique dimension-4 operator -- confirmed in [VERIFY] item #3. The coupling renormalization absorbs the dimension-4 content exactly, and the remainder is genuinely dimension $> 4$.

**(d) Perturbative to non-perturbative transition.**
This is the substantive issue. The paper's argument (Section 5.6, Part III.4) is:

> "Balaban's effective action is C-invariant... The dimension-6 part $\delta E_k^{d=6}$ of the remainder is by construction a C-even, dimension-6, gauge-invariant local operator. By the Lemma: $\mathrm{exc}(\delta E_k^{d=6}) \geq 2$."

The claim that $\mathrm{exc} \geq 2$ follows from the classification is logically correct: every C-even dimension-6 operator is a sum of Class III and Class IV operators, all of which produce connected matrix elements of order $O(\hat{\Delta}^2)$ or higher. The diagonal vanishing $(e^0-1)^2 = 0$ is not relied upon as a symmetry -- it is a structural consequence of the "squared temporal difference" form of Class III operators. The non-perturbative operator inherits this form because the operator classification is exhaustive: there are no C-even dimension-6 operators with a different structure.

**However, there is a formal mismatch** between Definition 2.1 of $\mathrm{exc}$ (Section 5.5.2) and its application. Definition 2.1 requires that all intermediate-state tuples $\mathbf{n}$ with nonzero weight $W_\alpha^{(m)}(\mathbf{n}) \neq 0$ have $\#(\mathbf{n}) \geq p$. For $\mathrm{Tr}(D_0 F)^2$ with $R=1$ (one internal $\hat{T}$-insertion), the intermediate-state sum involves a single index $n_1$. The channel $n_1 = 0$ (vacuum intermediate) has nonzero weight $(e^{\hat{\Delta}}-1)^2 |\langle 1|F|0\rangle|^2 \neq 0$ for the $m=1$ matrix element, but $\#(n_1=0) = 0 < 2$. **Definition 2.1 gives $\mathrm{exc}(\mathrm{Tr}(D_0 F)^2) = 0$, not $\geq 2$.**

The $O(\hat{\Delta}^2)$ bound still holds for the connected matrix element -- this is verified by the direct spectral computation in Section 5.5.4. But it does not follow from the spectral lemma (Section 5.5.3) applied through Definition 2.1, because the hypothesis $\mathrm{exc} \geq 2$ is not satisfied in the formal sense.

What the paper actually uses is a different property: that the connected matrix element $\langle 1|\mathcal{O}|1\rangle_c$ is $O(\hat{\Delta}^2)$ because the diagonal channel ($n = m$) vanishes (the structural zero $(e^0-1)^2 = 0$) and the vacuum channel ($n = 0$) contributes $(e^{\hat{\Delta}}-1)^2 \sim \hat{\Delta}^2$. This is correct but is not what Definition 2.1 captures.

**What is needed to close this gap:** Either (i) revise Definition 2.1 to capture the "order of vanishing of the Boltzmann weight at $n = m$" rather than "number of excited intermediate slots," or (ii) reformulate the spectral lemma to take as hypothesis that the connected matrix element's low-excitation channels have total weight bounded by $C M \hat{\Delta}^p$ (a weaker condition that IS satisfied). Either revision is straightforward and does not require new mathematics.

**Impact on the claimed result:**
This is a formal presentation gap, not a mathematical error. The actual bound $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| \leq C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$ is correctly established by the classification + direct spectral mechanism. The gap is in the formal machinery connecting the classification to the bound -- the spectral lemma's hypothesis (Definition 2.1) does not formally apply as stated, though the conclusion is correct by independent reasoning. This does not invalidate the main claim $\Delta_\infty > 0$.


---


## Point 2: The Spectral Lemma -- Step 5 (Exponential to Polynomial)

**Verdict:** SOUND

**Finding:**

**(a) The general case.**
The text states (lines 1027--1030): "each of the $p$ excitations contributes a factor $(1 - e^{-\hat{\Delta}})$ relative to the baseline where that slot is in the vacuum."

For the specific application ($p = 2$, the only case used in the proof), the mechanism is explicit and verified in Section 5.5.4: the factor $(e^{E_m - E_n} - 1)^2$ provides two powers of $\hat{\Delta}$ from the vacuum intermediate state. The "cross terms" mentioned at line 541 come from distinct Lorentz index configurations and are controlled by the same spectral mechanism -- each temporal derivative brings one factor of $(e^{-\hat{\Delta}} - 1)$, and the squared structure ensures cross terms contribute $O(\hat{\Delta}^2)$ or higher.

For the hypothetical general case ($p > 2$), the argument that $p$ excitations independently contribute $p$ factors of $(1 - e^{-\hat{\Delta}})$ is stated as a conclusion without detailed proof. But for the actual proof chain, only $p = 2$ is used (dimension-6 operators have exactly two extra derivatives). The general case is not load-bearing.

**(b) The baseline.**
There is no double-counting. The connected matrix element $\langle 1|\mathcal{O}|1\rangle_c = \langle 1|\mathcal{O}|1\rangle - \langle 0|\mathcal{O}|0\rangle$ subtracts the vacuum diagonal. The "deviation structure" in Step 5 refers to the deviation of Boltzmann weights $e^{-E_{n_j}}$ from the diagonal channel ($n_j = m$), which is a separate structural feature. For $m = 1$: the diagonal gives $(e^0-1)^2 = 0$ (structural zero), and the vacuum intermediate gives $(e^{\hat{\Delta}}-1)^2 \sim \hat{\Delta}^2$ (the deviation). The vacuum subtraction ($m=0$ contribution) is the second term in the connected matrix element and is independently $O(\hat{\Delta}^2)$. No double-counting occurs; the two subtractions (connected structure and deviation structure) act on different aspects of the spectral sum.

**(c) The bound $C_p$.**
The quantity $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$ involves the spectral gap above the one-particle state. The paper bounds $\zeta$ using locality (hypothesis (ii), lines 999--1004): "by locality... $\zeta$ is bounded by a constant $\zeta(R_0, N)$ independent of the volume (using the cluster property in the gapped phase)."

This bound is valid. In a gapped lattice theory with gap $\hat{\Delta} > 0$, a local operator supported within $R_0$ sites couples to multi-particle states with spatial extent $\lesssim R_0$. The density of such states at energy $E$ grows polynomially in $E$ (bounded by the number of lattice configurations in the support region), while the Boltzmann weights $e^{-(E_n - E_1)}$ decay exponentially. The sum $\zeta$ converges and is bounded by $C(R_0, N, d)$ independent of $k$.

The concern about the gap $E_2 - E_1$ closing at some RG step is unfounded in this context. The gap $E_2 - E_1$ is the gap between the one-particle state and the next state (typically the two-particle threshold at $\sim 2E_1$, or a higher glueball). This gap is $\geq E_1 = \hat{\Delta} > 0$ throughout the RG flow (by the inductive hypothesis $\hat{\Delta}_k > 0$ at each step). Since $\zeta \leq \sum_{n \geq 1} e^{-n\hat{\Delta}} \cdot p(n)$ where $p(n)$ is a polynomial degeneracy factor, $\zeta$ is uniformly bounded as long as $\hat{\Delta} > 0$.

The bound is $k$-independent because the Boltzmann factors and the locality radius $R_0$ are both $k$-independent.

**Impact on the claimed result:**
None. The spectral lemma proof is correct as applied ($p = 2$). The general case for $p > 2$ is stated without full proof but is not used.


---


## Point 3: The Multi-Time-Slice Correction and Its Completeness

**Verdict:** CLOSABLE GAP

**Finding:**

**(a) Applicability to the full Balaban operator.**
The stability argument (Section 5.6, Part III) does NOT verify Definition 2.1 channel by channel for the non-perturbative operator $\delta E_k^{d=6}$. Instead, it proceeds by operator classification:

1. $\delta E_k^{d=6}$ is C-even, gauge-invariant, dimension-6, and analytic (by (B1)).
2. All such operators are sums of Class III (two-derivative) and Class IV ($\geq 3$-derivative) operators.
3. Class III operators produce connected matrix elements $O(\hat{\Delta}^2)$ by the spectral mechanism.
4. Class IV operators produce $O(\hat{\Delta}^{\geq 3})$.
5. Therefore $|\langle 1|\delta E_k^{d=6}(0)|1\rangle_c| = O(\hat{\Delta}^2)$.

This argument is logically valid. It does not require verifying Definition 2.1 for the non-perturbative operator; it bypasses the formal definition entirely by establishing the bound through the operator classification. The key input is that (B1) makes the dimension-6 projection exact (convergent, not asymptotic), so the classification applies to the actual non-perturbative object.

However, the paper presents this as an application of the spectral lemma (Section 5.5.3) via the stability-of-excitation-number lemma (Section 5.6, Part III.3). As noted in Point 1, the formal Definition 2.1 does not match the actual mechanism. **The spectral lemma is not the correct formal tool here.** The correct tool is the direct spectral computation (Section 5.5.4) applied to each class of operators in the classification.

This is the same gap as Point 1(d). The conclusion is correct; the formal machinery needs revision.

**(b) Vacuum intermediate vs. all channels.**
For the connected matrix element, the guarantee that all $\#(\mathbf{n}) = 1$ channels are absent (or contribute $O(\hat{\Delta}^2)$) comes from the specific spectral structure of the DF${}^2$ operator:

- For $m = 1$: the diagonal channel ($n = m = 1$, with $\# = 1$ in the standard counting) has weight $(e^0 - 1)^2 = 0$. The vacuum channel ($n = 0$, $\# = 0$) has weight $(e^{\hat{\Delta}} - 1)^2 = O(\hat{\Delta}^2)$. Higher states contribute $O(e^{-(E_n - E_1)})$.
- For $m = 0$: the diagonal channel ($n = 0$, $\# = 0$) has weight 0. The $n = 1$ channel ($\# = 1$) has weight $(e^{-\hat{\Delta}} - 1)^2 = O(\hat{\Delta}^2)$.

The connected matrix element is the difference of these two, which is $O(\hat{\Delta}^2)$. The $\# = 1$ channel for $m = 0$ is NOT absent -- it contributes $O(\hat{\Delta}^2)$. This is consistent with the bound but inconsistent with the formal Definition 2.1 requiring $\mathrm{exc} \geq 2$ (which would require all $\# < 2$ channels to be absent). **The bound holds not because $\# = 1$ channels are absent, but because all channels contribute at most $O(\hat{\Delta}^2)$.**

**(c) Corrected mechanism vs. Newton decomposition.**
The paper correctly identifies (Appendix G) that the Newton decomposition gives zero (not $\hat{\Delta}^2$) in energy eigenstates, and that the correct mechanism uses the internal $D_0$ in $\mathrm{Tr}(D_0 F)^2$. The identification of the non-perturbative operator $\delta E_k^{d=6}$ with $c_6 \mathrm{Tr}(DF)^2$ at leading order is made rigorous by (B1): the analyticity of the effective action ensures the perturbative expansion converges, so the leading operator is exactly $\mathrm{Tr}(DF)^2$ (not just approximately). The non-perturbative corrections are $O(g_k^6)$ and produce dimension-$\geq 8$ operators with form factors $O(\hat{\Delta}^{\geq 4})$, which are subleading.

The preprint makes this identification in Section 5.6, Part III.4 (lines 1335--1357), citing (B1) as the key property. This is the correct location and the argument is sound.

**Impact on the claimed result:**
Same as Point 1. The bound on the connected matrix element is correctly established by the classification + spectral mechanism. The formal mismatch with Definition 2.1 does not invalidate the result. Closing this gap requires revising the definition and lemma to match the actual argument.


---


## Point 4: Theorem 5 -- IR Equivalence Is a Proof Sketch

**Verdict:** GENUINE GAP

**Finding:**

**(a) Does Section 5 actually provide the non-perturbative decoupling?**
No. The paper claims (lines 855--859):

> "A rigorous proof of the IR equivalence requires non-perturbative control of the decoupling of heavy KK modes, which is provided by Section 5 (Balaban's renormalization group)."

This claim is not justified by the content of Section 5. Section 5 applies Balaban's block-spin RG to a single lattice gauge theory (the standard 4D $\mathrm{SU}(N)$ Wilson theory, as stated in Section 5.1.1). It proves that IF the starting lattice has $\Delta_0 > 0$, THEN $\Delta_\infty > 0$. Section 5 does not:

- Compare the KK-enhanced theory with the standard theory
- Prove that the two theories have the same mass gap
- Provide non-perturbative control of the decoupling of KK modes
- Establish any equivalence between the theories at any scale

The decoupling argument in Theorem 5 (lines 813--853) is self-contained and purely Wilsonian/perturbative. Section 5's RG analysis is for a different purpose (continuum limit of a single theory, not comparison of two theories).

The logical chain of the paper is:

$$\Delta_0^{\mathrm{KK}} > 0 \;(\text{Thm 4})
  \;\xrightarrow[\text{Thm 5, proof sketch}]{\text{decoupling}}\;
  \Delta_0^{\mathrm{std}} > 0
  \;\xrightarrow[\text{Section 5}]{\text{Balaban RG}}\;
  \Delta_\infty^{\mathrm{std}} > 0$$

Theorem 5 is the bridge between the KK-enhanced theory (where the mass gap is proved) and the standard theory (where the continuum limit is taken). This bridge is a proof sketch, not a proof.

**(b) The Appelquist--Carazzone limitation.**
The proof sketch invokes Wilsonian decoupling of heavy modes, citing Appelquist--Carazzone (1975). This theorem is proved perturbatively. Its hypotheses (the heavy modes are weakly coupled to the light modes at the scale $m_1$) are satisfied in the regime $m_1 \gg \Lambda_{\mathrm{QCD}}$. But the conclusion that the string tension is unchanged -- $\sigma_{\mathrm{std}} = \sigma_{\mathrm{KK}} + O(\Lambda_{\mathrm{QCD}}^4/m_1^2)$ -- is a statement about a non-perturbative observable. No non-perturbative version of Appelquist--Carazzone exists in the constructive QFT literature.

The verification report (Issue 14) correctly identifies this: "Appelquist-Carazzone decoupling (1975) is a perturbative result. Its validity non-perturbatively... is not established."

**(c) Logical consequence for the main claim.**
The preprint's abstract claims:

> "We prove that $\mathrm{SU}(N)$ lattice gauge theory confines and has a mass gap $\Delta > 0$ at all couplings in the physical regime, and that this mass gap survives the continuum limit $a \to 0$."

And explicitly: "The theory is the standard four-dimensional $\mathrm{SU}(N)$ Wilson lattice gauge theory."

This claim requires Theorem 5. Without it, the paper proves:

| Result | Actually proved? |
|:-------|:-----------------|
| $\Delta_0^{\mathrm{KK}} > 0$ (KK-enhanced, lattice) | **Yes** (Theorem 4) |
| $\Delta_0^{\mathrm{std}} > 0$ (standard, lattice) | **No** (requires Theorem 5) |
| $\Delta_\infty^{\mathrm{KK}} > 0$ (KK-enhanced, continuum) | **Requires extending Balaban to KK theory** |
| $\Delta_\infty^{\mathrm{std}} > 0$ (standard, continuum) | **No** (requires $\Delta_0^{\mathrm{std}} > 0$) |

The paper proves the mass gap for the KK-enhanced lattice theory. The transfer to the standard theory, and the continuum limit of either theory, both depend on unproved steps.

To be precise: if one accepts Theorem 5 as a physics argument (not a mathematical proof), then the remaining proof chain (Section 5) is rigorous (modulo the closable gaps in Points 1 and 3). The gap is specifically at the bridge between the two theories.

**Impact on the claimed result:**
This is the most significant issue. The paper does not prove $\Delta > 0$ for the standard $\mathrm{SU}(N)$ Yang--Mills theory. It proves $\Delta > 0$ for the KK-enhanced theory on the lattice, and provides a physically compelling but mathematically incomplete argument for the equivalence. The Millennium Problem asks for a proof about the standard theory. The KK-enhanced theory is a different theory (with additional fields), and the equivalence between the two is not established.


---


## Point 5: The Confirmed Balaban Items -- Are They Actually Confirmed?

**Verdict:** SOUND

**Finding:**

**(a) Uniqueness of $S_{\mathrm{YM}}$.**
The uniqueness argument is correct. The concern about $\sum_P (\mathrm{Re}\,\mathrm{Tr}\,U_P)^2$ is resolved by the standard continuum expansion:

$$(\mathrm{Re}\,\mathrm{Tr}\,U_P)^2
  = \left(N - \frac{a^4}{2N}\mathrm{Tr}\,F^2 + O(a^6)\right)^2
  = N^2 - \frac{a^4}{N}\,\mathrm{Tr}\,F^2 + O(a^8)$$

The constant $N^2$ is dimension 0 (absorbed into vacuum energy). The $a^4$ term is dimension 4 (proportional to $\mathrm{Tr}\,F^2 = S_{\mathrm{YM}}$, absorbed into coupling renormalization). The next term is $O(a^8)$ (dimension 8). **There is no dimension-6 contribution from $(\mathrm{Re}\,\mathrm{Tr}\,U_P)^2$.**

Balaban defines the "dimension-6 part" of the effective action through his coupling renormalization: $g_{k+1}$ is defined as the coefficient of $S_{\mathrm{YM}}$, and the remainder $E_{k+1}$ is everything else. Since $S_{\mathrm{YM}}$ is the unique dimension-4 operator, the subtraction cleanly separates dimension 4 from dimension $> 4$. The "dimension-6 part" is then the leading-order contribution to $E_{k+1}$, which scales as $a^6$ in the continuum expansion. This is a lattice definition that agrees with the continuum assignment.

**(b) The caveat about page numbers.**
The paper's proof chain cites specific Balaban references (CMP 95 Prop. 3.2, CMP 109 Thm 2.1, etc.) from the extraction in Appendix H, not from the published journal text. The verification report explicitly acknowledges: "I have not independently verified the page numbers... against the published journal text."

Is this "unconditional"? In the strict sense: no, the proof chain has an unverified bibliographic dependency. In the mathematical sense: the arguments in the verification report are self-contained. A referee can verify them without the page numbers -- the page numbers serve as pointers for checking that the claimed results actually appear in Balaban's papers.

The epistemic status: the proof chain is **logically complete** (every step has a self-contained argument), but **bibliographically unverified** (the specific Balaban citations have not been checked against the primary sources). This is a normal state for a paper that builds on prior work -- the arguments are traceable and checkable, but the final bibliographic verification requires a referee to read Balaban CMP 95--119.

**(c) CMP 95 Proposition 3.2.**
I cannot verify that a Proposition 3.2 with the claimed content (analyticity of the propagator $G_k(V) = (-D^2[V] + m_W^2)^{-1}$) exists in Balaban CMP 95 (1984). The verification report acknowledges the same limitation: "Specific page/equation numbers are from the extraction in Appendix H and have not been checked against the published journal pages."

However, the mathematical content -- that the inverse of a polynomial operator with positive mass term is analytic in the field variables -- is standard functional analysis. Whether Balaban states this as "Proposition 3.2" is a bibliographic question, not a mathematical one. The argument does not depend on the proposition number.

**Impact on the claimed result:**
None of these issues affects the mathematical validity of the proof chain. The arguments are self-contained. The bibliographic caveat is appropriate and honestly stated.


---


## Point 6: The OS Axioms

**Verdict:** CLOSABLE GAP

**Finding:**

**(a) OS1 (Temperedness).**
The text states (lines 1583--1587):

> "The Schwinger functions $S_n(x_1,\ldots,x_n)$ are bounded as $|S_n| \leq C^n e^{-c\sum_{i<j}|x_i-x_j|\Delta}$ uniformly in $a$, following from the cluster expansion estimates of Section 4.3. Distributional temperedness follows from this exponential bound and Sobolev embedding."

This is too compressed. The stated bound is on the **connected** Schwinger functions (which decay exponentially by clustering). OS1 requires temperedness of the **full** (disconnected) Schwinger functions.

The implication connected $\Rightarrow$ full is valid but requires the linked cluster theorem: the full $n$-point function is a sum over partitions of products of connected functions. Each connected function decays exponentially, and the sum over partitions introduces at most a combinatorial factor $n!$ (or equivalently, the number of partitions of $\{1,\ldots,n\}$). The product of connected functions at well-separated points is bounded by a product of exponentials, giving overall exponential decay for the full function. This is stronger than polynomial growth, hence the full Schwinger functions are tempered distributions.

The argument is standard (cf. Glimm--Jaffe, Chapter 18) but the paper should state it explicitly rather than citing "Sobolev embedding" (which is relevant for regularity, not for the growth bound that temperedness requires).

**No mathematical error.** The bound is correct; the derivation is too terse.

**(b) OS2 (Euclidean covariance).**
The claim that O(4) invariance is "recovered in the $a \to 0$ limit" with corrections "suppressed by powers of $a\Lambda$" is correct in principle. The precise rate is: the leading O(4)-breaking operators in the effective action are dimension-6 ($\mathrm{Tr}(DF)^2$ with lattice-specific index contractions), with coefficients $O(g_k^4)$. The O(4)-breaking corrections to Schwinger functions scale as $O(g_k^4 \cdot (a_k\Lambda)^2)$, which vanishes as $a \to 0$ along the RG trajectory. The rate is controlled by the same RG analysis that establishes the mass gap.

The paper should state the rate explicitly: $O(a^2 \Lambda^2)$ corrections from dimension-6 lattice artifacts. This is standard in lattice QFT (Symanzik improvement program) and follows from the RG analysis of Section 5.

**(c) OS reconstruction.**
The concern about different subsequences for different axioms is addressed by the uniformity of the bounds. Each OS axiom is verified **uniformly in $a$** (not just for specific subsequences):

- OS1: the temperedness bound $|S_n| \leq C^n$ is $a$-independent (from the uniform cluster expansion).
- OS2: the O(4)-breaking corrections are $O(a^2\Lambda^2) \to 0$ for every convergent subsequence.
- OS3: reflection positivity holds for every $a > 0$; weak limits of reflection-positive measures are reflection-positive.
- OS4: automatic.
- OS5: follows from $\Delta_\infty > 0$.

Since all five axioms hold uniformly, they hold simultaneously for every convergent subsequence. By the Osterwalder--Schrader compactness theorem (applied via the Banach--Alaoglu theorem to the space of tempered distributions), at least one convergent subsequence exists. For this subsequence, all five axioms hold simultaneously, and the OS reconstruction theorem gives a Wightman QFT.

**No mathematical error.** The argument is correct but should be expanded from four lines to at least a page.

**Impact on the claimed result:**
These are presentation deficiencies in a section that deserves careful treatment, not logical gaps. The OS axioms hold for the limiting theory by standard arguments. None of these issues affects the validity of $\Delta_\infty > 0$.


---


## Point 7: The Inductive Stability -- Precise Version

**Verdict:** SOUND

**Finding:**

**(a) The $O(g_k^2 C_k)$ correction.**
The recursion $C_{k+1} = (C_k/4 + C_{\mathrm{new}})(1 + \alpha g_k^2)$ produces accumulated growth:

$$C_k \leq C_* \cdot \prod_{j=0}^{k-1}(1 + \alpha g_j^2)
  \leq C_* \cdot \exp\!\left(\alpha \sum_{j=0}^{k-1} g_j^2\right)$$

Since $g_j^2 \sim 1/(b_0 j \ln 2)$ and $\sum_{j=1}^k 1/j \sim \ln k$, the exponential is $\exp(\alpha \ln k / (b_0 \ln 2)) = k^{\alpha/(b_0 \ln 2)} = k^\gamma$.

Could the growth be faster than polynomial? Only if the $O(g_k^2)$ corrections accumulated multiplicatively faster than $1/(b_0 k \ln 2)$ per step. Balaban's estimates bound the coupling renormalization corrections at $O(g_k^2)$ with a $k$-independent constant $\alpha$, so the growth is strictly $k^\gamma$ (polynomial). Exponential growth would require $g_k^2 = O(1)$ at every step, which contradicts asymptotic freedom ($g_k^2 \to 0$).

The convergence $\sum_k k^{\gamma-2} 4^{-k} < \infty$ for all $\gamma$ is immediate: $4^{-k}$ decays faster than any polynomial grows. Explicitly, $k^{\gamma-2} 4^{-k} \leq C \cdot 3^{-k}$ for all $k \geq k_0(\gamma)$. **The bound is correct.**

**(b) Starting constant $C_0$.**
At $k = 0$, the cluster expansion (Section 4) gives $\|E_0\| \leq C g_0^4$ per site, with $C$ depending on $N$, the lattice geometry, and the cluster expansion constants (controlled by $m_1 a$). Since $\hat{\Delta}_0 \sim O(1)$ at the starting scale, the inductive hypothesis $|\langle 1|E_0(0)|1\rangle_c| \leq C_0 g_0^4 \hat{\Delta}_0^2$ is trivially satisfied with $C_0 = C/\hat{\Delta}_0^2 = O(1)$ (because $\hat{\Delta}_0 = O(1)$).

The constant $C_0$ is finite and computable from the cluster expansion. It depends on $N$ (through the gauge group constants) and on $m_1 a$ (through the cluster expansion convergence), but both are bounded at the starting scale. The convergence from $C_0$ to the fixed point $C_* = 4C_{\mathrm{new}}/3$ is geometric with rate $4^{-k}$, so the transient contribution is finite.

**(c) Perturbative vs. non-perturbative at the starting scale.**
The cluster expansion (Section 4) applies for all $\beta$ in the range $\beta < m_1 a / 6 - \mathrm{const}$, which includes $\beta \sim 10^{14}$ (very large $\beta$, very small $g_0$). Balaban's construction requires $g_0$ small, i.e., $\beta$ large. **The two regimes overlap**: for $\beta \sim 10^{6}$ (say), the coupling $g_0^2 = 2N/\beta \sim 10^{-5}$ is small enough for Balaban, and the cluster expansion convergence condition is satisfied with a margin of $\sim 10^{14}$.

The overlap is not just in a narrow window -- it spans many orders of magnitude of $\beta$. At any $\beta$ in this overlap, both the cluster expansion (giving $\Delta_0 > 0$) and Balaban's construction (giving UV stability) apply simultaneously. The RG recursion starts here and proceeds to $k \to \infty$ via Section 5.

**Impact on the claimed result:**
None. All aspects of the inductive stability are correctly established.


---


## Point 8: The Dimension-6 Coefficient -- Which Bound Is Used?

**Verdict:** SOUND

**Finding:**

**(a) The $O(g_k^2)$ matrix element.**
The paper uses two different bounds on $|\langle 1|s_P(0)|1\rangle_c|$ in different contexts:

- **Perturbative estimate** (Section 5.3.2): $O(g_k^2)$, from the one-glueball coupling to $\mathrm{Tr}\,F^2$ involving one gauge-field exchange.
- **Non-perturbative bound** (Section 5.3.3): $O(1)$, from the operator norm $\|s_P\| \leq 2$.

The theorem statement (Section 5.3.3, line 600) uses the non-perturbative bound:

$$|\langle 1|\delta E_k(0)|1\rangle_c|
  \leq C_{\mathrm{new}}\,g_k^4\,\hat{\Delta}_{k+1}^2$$

The $g_k^4$ comes from Balaban's generic estimate $|c_6^{(k)}| \leq C g_k^{d_O - 2} = C g_k^4$ for $d_O = 6$, combined with the $O(1)$ matrix element bound. This accounting is:

$$|c_6^{(k)}| \times |\langle 1|\mathcal{O}_6(0)|1\rangle_c|
  \leq C g_k^4 \times C' \hat{\Delta}^2 = C_{\mathrm{new}} g_k^4 \hat{\Delta}^2$$

The alternative accounting (one-loop coefficient $O(g_k^2)$ times perturbative matrix element $O(g_k^2)$) gives the same result:

$$|c_6^{(1\text{-loop})}| \times |\langle 1|s_P|1\rangle_c^{\mathrm{pert}}|
  \leq C g_k^2 \times C' g_k^2 \hat{\Delta}^2 = C'' g_k^4 \hat{\Delta}^2$$

Both methods yield $O(g_k^4 \hat{\Delta}^2)$. The distinction is cosmetic for the final bound. The theorem statement correctly uses the non-perturbative accounting (Balaban's generic bound), which does not require the perturbative estimate of the matrix element.

**(b) The coefficient bound.**
The tracking is as follows:

| Source | $|c_6|$ | $|\langle 1|\mathcal{O}_6|1\rangle_c|$ | Product |
|:-------|:--------|:--------------------------------------|:--------|
| One-loop coefficient + pert. matrix element | $O(g_k^2)$ | $O(g_k^2 \hat{\Delta}^2)$ | $O(g_k^4 \hat{\Delta}^2)$ |
| Balaban generic bound + operator norm | $O(g_k^4)$ | $O(\hat{\Delta}^2)$ | $O(g_k^4 \hat{\Delta}^2)$ |

Both give $O(g_k^4 \hat{\Delta}^2)$. The theorem uses the second line (Balaban's generic bound), which is the non-perturbative version. The first line (one-loop + perturbative) is presented in Section 5.3.2 as the perturbative motivation.

The factor $g_k^4$ in the final bound comes from **Balaban's generic estimate alone** (the dimension formula $|c_{d_O}| \leq C g_k^{d_O-2}$ for $d_O = 6$). The one-loop coefficient and the perturbative matrix element are not used in the formal theorem; they serve as a cross-check.

The convergence $\sum g_k^4 \hat{\Delta}_k^2 < \infty$ holds regardless of whether the $g_k^4$ comes from the coefficient or the matrix element:
- $g_k^4 \sim 1/(b_0 k \ln 2)^2$
- $\hat{\Delta}_k^2 \sim 4^{-k}$
- Sum $\sim \sum k^{-2} 4^{-k} < \infty$

If the matrix element were $O(1)$ (not $O(g_k^2)$), the bound becomes $g_k^4 \hat{\Delta}^2$ (same). If the coefficient were $O(g_k^2)$ (one-loop), the bound becomes $g_k^2 \hat{\Delta}^2$, and $\sum g_k^2 \hat{\Delta}_k^2 \sim \sum k^{-1} 4^{-k} < \infty$ (also converges). **The convergence is robust to the precise $g_k$ power.**

**Impact on the claimed result:**
None. The accounting is internally consistent and the convergence is robust.


---


## Overall Assessment

**Is the claimed result proved?**
No. The paper proves the mass gap for the KK-enhanced Yang--Mills theory on the lattice ($\Delta_0^{\mathrm{KK}} > 0$, Theorem 4) by a rigorous cluster expansion. The continuum limit argument (Section 5) is logically valid, contingent on the starting mass gap for the standard theory. But the transfer of the mass gap from the KK-enhanced theory to the standard $\mathrm{SU}(N)$ Yang--Mills theory (Theorem 5) is a proof sketch relying on perturbative decoupling (Appelquist--Carazzone 1975), which has no non-perturbative proof.

The paper claims to prove $\Delta_\infty > 0$ for "the standard four-dimensional $\mathrm{SU}(N)$ Wilson lattice gauge theory" (abstract). This claim is not established. What IS established:

1. $\Delta_0^{\mathrm{KK}} > 0$ for the KK-enhanced theory at all physical couplings. **(Rigorous.)**
2. The continuum limit argument $\Delta_0 > 0 \Rightarrow \Delta_\infty > 0$ via the RG recursion and stability of excitation number. **(Rigorous, with closable formal gaps in the spectral lemma machinery.)**
3. The equivalence between KK-enhanced and standard theories. **(Proof sketch, physically compelling, mathematically incomplete.)**

If one accepts (3) as established, the proof of $\Delta_\infty > 0$ for the standard theory is complete up to the closable formal gaps in Points 1 and 3.

**The single most important issue:**
Theorem 5 (IR equivalence / decoupling) is a proof sketch, not a proof. The paper's claim that "Section 5 provides non-perturbative control of the decoupling" is not substantiated: Section 5 addresses the continuum limit of a single theory, not the comparison between two theories.

**What would make this a complete proof:**

1. **(Critical)** Prove the non-perturbative decoupling of KK modes: either (a) establish a rigorous non-perturbative Appelquist--Carazzone theorem in the constructive QFT framework, or (b) extend Balaban's block-spin RG to the KK-enhanced theory and show that the effective action at scales $a_k \ll 1/m_1$ converges to the standard YM effective action, or (c) prove $\Delta_0 > 0$ for the standard lattice theory directly (without KK enhancement), bypassing Theorem 5 entirely.

2. **(Closable)** Revise Definition 2.1 of excitation number and the spectral lemma (Section 5.5) to match the actual argument. The current formal definition ($\#(\mathbf{n}) \geq p$ for all nonzero channels) does not apply to the operators at hand (for which the relevant property is the "squared deviation" structure, not the absence of low-excitation channels). A revised definition should capture the order of vanishing of the Boltzmann weight factor at $n = m$, which is the actual mechanism producing the $\hat{\Delta}^p$ bound.

3. **(Minor)** Expand the OS axioms verification (Section 5.7(f)) from four lines to a page, with explicit arguments for each axiom. The arguments exist and are standard; they need only to be stated.
