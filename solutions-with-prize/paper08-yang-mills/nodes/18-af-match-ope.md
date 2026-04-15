# Node 18 -- AF Match and Leading-Order OPE

**Chain step:** 18 of 18
**Rigor label:** [CONDITIONAL on H4]
**Dependencies:** Steps 15--17 (gradient flow, Schwinger functions, composite operators)
**Status:** CONDITIONAL on Hypothesis H4 (Lemmas L.4.2--L.4.3)

---

## Statement

**Lemmas L.4.2--L.4.3 (AF match and OPE).** *Assuming Hypothesis H4, the following hold for $\mathrm{SU}(N)$, $N \geq 2$:*

*(i) Short-distance match (Conjecture L.2):*
$$S_2^{\mathrm{ren}}(x,y) = \frac{C_N}{|x-y|^8}\,\Bigl(\ln\frac{1}{|x-y|\Lambda}\Bigr)^{-2}\bigl[1 + O\bigl((\log)^{-1}\bigr)\bigr], \quad C_N = \frac{2(N^2-1)}{\pi^6}.$$

*(ii) Anomalous dimension (Conjecture L.1(iii)): $\gamma_{\mathrm{Tr}\,F^2} = -2\beta(g)/g = 2b_0 g^2 + O(g^4)$ at the non-perturbative level.*

*(iii) Leading-order OPE (Conjecture L.4): identity-channel coefficient $C^{\mathbb{1}} = C_N |x-y|^{-8}(\ln(1/|x-y|\Lambda))^{-2}[1 + O((\log)^{-1})]$; subleading channels strictly weaker.*

---

## The single conditional: Hypothesis H4

**Hypothesis H4** (Non-perturbative equals perturbative at short distances). *The renormalised non-perturbative Schwinger function $S_2^{\mathrm{ren}}(x,y)$ admits a short-distance asymptotic expansion whose leading term coincides with the perturbative prediction (eq. L.7.1).*

**Standing of H4:**
- **Proved** in super-renormalisable cases ($\phi^4_3$: Glimm--Jaffe; Magnen--Rivasseau--Seneor, CMP 155, 1993)
- **Open** for 4D non-Abelian gauge theory
- **Extensively tested** numerically (lattice QCD scaling tests, step-scaling, gradient-flow coupling measurements)
- **Universally invoked** implicitly in SVZ sum rules, lattice $\alpha_s$ determinations, perturbative matching

**H4 is the sole unverified input in the entire 18-step chain.** Steps 1--17 are unconditional. This is analogous to the CBB conditionality in the RH/BSD proofs (Papers 13, 26).

---

## What is unconditional without H4

Even without H4, Steps 1--17 establish:
- $\Delta_\infty > 0$ (mass gap, unconditional)
- $[\mathrm{Tr}\,F^2]_R$ exists (composite operators, unconditional)
- $T_{\mu\nu}^R$ with all five Clay sub-clauses (unconditional)
- OPE identity-channel singularity $O(|x|^{-8})$ (power law, unconditional)

H4 is needed only for the AF logarithmic correction $(\log)^{-2}$ and the non-perturbative anomalous dimension.

---

## Why the gradient-flow framework makes H4 more tractable

The flow provides a smooth interpolation between non-perturbative ($t \gg \Lambda^{-2}$) and perturbative ($t \ll \Lambda^{-2}$) regimes. The rescaled correlator $F(t) = S_{2,t}^c / c_1(t)^2$ is analytic in $t$ with convergent Taylor series (Lemma L.3.1), reducing H4 to: *are the Taylor coefficients $F^{(k)}(0)$ computable by Feynman rules?*

---

## Sources

- **Preprint:** Appendix L, Section L.4; Section L.7 (Hypothesis H4)
- **Proof chain:** PROOF-CHAIN.md, Step 18
- **Literature:** Luscher--Weisz JHEP 02 (2011) 051; Harlander et al. arXiv:2111.14376
