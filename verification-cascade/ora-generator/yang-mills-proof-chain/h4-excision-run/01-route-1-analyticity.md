# Route 1: Analyticity + Identity Theorem

*ORA v8 Tier B excision run. Route 1 of 4.*
*Target: Prove H4 via analytic continuation uniqueness.*

---

## 1. Prior state (from H4 closure run)

Route A was BLOCKED-DECOMPOSED at two sub-problems:
- **R.A.1a**: Analyticity of F^pert(t) on a complex disk — OPEN, comparable to Borel summability of 4D YM.
- **R.A.1b**: Independent-point agreement F(t_0) = F^pert(t_0) — OPEN, no candidate mechanism.

The prior run correctly identified that the identity theorem requires TWO analytic functions, and F^pert(t) is only a formal power series.

## 2. New angle: the Suzuki formula as term-by-term bridge

The brief suggests: can the Suzuki formula's small-t expansion be matched term-by-term to perturbative Feynman diagrams?

**The Suzuki formula** (Lemma L.4.1, eq. L.4.1) constructs T_{mu nu}^R from flowed composite operators:

$$T_{\mu\nu}^R(x) = \lim_{t \to 0^+}\bigl[c_1(t) U_{\mu\nu}(t,x) + c_2(t) \delta_{\mu\nu} E(t,x) + c_3(t) \delta_{\mu\nu} \langle E(t)\rangle \mathbb{1}\bigr]$$

The Wilson coefficients c_i(t) are computed perturbatively (Suzuki PTEP 2013, Harlander-Neumann JHEP 2016, Artz et al. JHEP 2019). They have explicit perturbative expansions:
- c_1(t) = 1 + O(g-bar^2)
- c_2(t) = b_0 g-bar^2/2 + O(g-bar^4)

**Key structural observation**: The small-flow-time expansion of the flowed energy density E(t,x) is:

$$E(t,x) = c_0(t) \mathbb{1} + c_1(t) [\text{Tr } F^2]_R(x) + \sum_{d_k \geq 6} c_k(t) \mathcal{O}_k(x)$$

This expansion is CONVERGENT for |t| < r_t by Lemma L.3.7 Step 2. The Wilson coefficients c_k(t) satisfy c_k(t)/c_1(t) ~ t^{(d_k-4)/2} for dimension-d_k operators, so higher-dimension operators are suppressed by powers of t.

**Can the Suzuki coefficients be identified with Feynman diagrams term-by-term?**

The Luscher gradient-flow perturbative expansion (arXiv:1006.4518, Section 3) provides an EXPLICIT perturbative framework: the flowed field B_mu(t,x) at flow time t satisfies the flow equation and has a perturbative solution as a power series in g:

$$B_\mu(t,x) = B_\mu^{(0)}(t,x) + g B_\mu^{(1)}(t,x) + g^2 B_\mu^{(2)}(t,x) + \cdots$$

where each B_mu^{(n)} is computed by Feynman rules with modified propagators containing the flow-time heat kernel factor e^{-tp^2}.

**The critical question**: Does the non-perturbative B_mu(t,x) constructed by the Balaban programme agree, order by order in g, with the perturbative B_mu^{(n)}(t,x)?

## 3. Attempt at closure

**Claim (attempted)**: The non-perturbative F(t) has Taylor coefficients at t=0 that are computable by perturbative Feynman rules.

**Argument sketch**:
1. F(t) is analytic on |t| < r_t (Lemma L.3.7 Step 2). Its Taylor series converges: F(t) = sum_{n >= 0} a_n t^n.
2. Each a_n = F^{(n)}(0)/n! is the n-th derivative of the rescaled non-perturbative correlator at t=0.
3. At each FIXED t > 0, the flowed correlator S_{2,t}^c is UV-finite (Luscher-Weisz theorem). The perturbative expansion of S_{2,t}^c at fixed t is an expansion in g-bar^2(q) at q = (8t)^{-1/2}.
4. The Reisz power-counting theorem guarantees lattice PT = continuum PT at each order.

**WHERE THIS BREAKS**:

The Taylor coefficients a_n are derivatives WITH RESPECT TO t at t=0. The perturbative expansion is in powers of g-bar^2. These are DIFFERENT expansions. To identify a_n with perturbative Feynman diagrams, we would need:

(a) Expand each Feynman diagram contribution to F(t) in powers of t.
(b) Sum over all Feynman diagrams at each power of t.
(c) Show the sum converges to a_n.

Step (b) is exactly the Borel summability problem — at each order in t, we sum over arbitrarily many loops, and the loop sum may be factorially divergent.

**The gradient-flow regularization does NOT solve this**: While the flow time provides UV finiteness at t > 0, the perturbative series in g^2 at FIXED t is still a formal power series with potentially factorial growth from renormalons.

However, there is a subtlety. The small-flow-time expansion is an expansion in OPERATORS (not in the coupling). The Wilson coefficients c_k(t) are functions of t that capture the matching between flowed operators and renormalized operators. The expansion:

$$E(t,x) = c_1(t) [\text{Tr } F^2]_R(x) + \text{higher-dim ops}$$

is convergent in t by Lemma L.3.7. The c_1(t) coefficient is computed perturbatively, but this is a different statement from "the full correlator's perturbative expansion converges."

**The OPE structure provides a crucial constraint**: In the two-point function F(t) = S_{2,t}^c/c_1(t)^2, the rescaling by c_1(t)^2 absorbs the leading UV divergence. The RESCALED object F(t) approaches F(0) = S_2^ren(x,y) as t -> 0. The question of whether S_2^ren has the perturbative short-distance form is then a question about F(0), which is the t=0 VALUE of an analytic function — not about matching two expansions.

**New sub-question**: Can we compute F(0) independently by two methods (non-perturbative and perturbative) that provably give the same answer?

Non-perturbative: F(0) = lim_{t->0} S_{2,t}^c/c_1(t)^2 = S_2^ren(x,y). This exists and is finite by Lemma L.3.7.

Perturbative: F^pert(0) = C_N/|x-y|^8 * (log(1/|x-y|Lambda))^{-2} * [1 + O((log)^{-1})]. This is the RG-improved two-point function.

The identity F(0) = F^pert(0) IS H4. We have not escaped.

## 4. Verdict: BLOCKED

Route 1 is BLOCKED at the same obstruction as the prior run's Route A. The new angle (Suzuki formula term-by-term matching) does not resolve the fundamental problem: the perturbative and non-perturbative expansions are organized differently (powers of g^2 vs powers of t), and converting between them requires summing the perturbative series, which is the Borel summability problem.

**What is new**: The recognition that the small-flow-time expansion is an OPERATOR expansion (convergent) rather than a COUPLING expansion (divergent) is structurally important. The Wilson coefficients c_k(t) are perturbatively computable AND the operator expansion converges. But the CORRELATOR at t=0 requires evaluating the non-perturbative matrix elements of the operators, which is where H4 enters.

**Specific blocker**: F(0) = S_2^ren(x,y) is a non-perturbative number. Its identification with the perturbative prediction IS H4. No amount of analyticity in t can compute a specific VALUE without additional input.

**Re-entry gate**: A proof that the Balaban construction's polymer expansion, when evaluated on correlators of renormalized operators, reproduces the perturbative coefficients order by order. This would require a rigorous perturbative expansion of the Balaban effective action — a constructive QFT result not currently available for 4D YM.

---

## What the next runner needs to know

- **State at handoff**: BLOCKED. Same obstruction as prior Route A but with refined understanding.
- **Open dependencies**: Borel summability of 4D YM (R.A.1a from prior run) remains the key external unlock.
- **Watch out for**: The convergent small-flow-time expansion is an OPERATOR expansion, not a CORRELATOR expansion. This distinction is load-bearing.
- **Preferred next move**: Investigate whether the Balaban construction provides a rigorous perturbative expansion (polymer activities have perturbative expansions at each RG scale — can these be assembled into a full perturbative expansion of correlators?).
- **Voice canon citation**: P6 — the difficulty IS the projection.
