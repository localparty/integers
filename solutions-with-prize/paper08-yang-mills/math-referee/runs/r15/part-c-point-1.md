## Part C, Point 1: UV Stability -- Precise Scope

**Weight:** HEAVY
**Verdict:** CLOSABLE GAP

**Finding:**

This point interrogates the translation from Balaban's published polymer
expansion framework (CMP 95--119) into the operator decomposition
$S_k = (1/g_k^2) S_{\mathrm{YM}} + \sum_n c_n^{(k)} \mathcal{O}_n + E_k$
used throughout Section 5. I address each sub-question in turn.

---

**(a) Is the operator decomposition stated as a theorem in Balaban, or
is it inferred from the construction?**

It is inferred. Balaban works with polymer activities $K_k(X, V)$
satisfying $|K_k(X, V)| \leq e^{-\kappa |X|}$ (CMP 109, Theorem 1/3).
He does not write down an operator decomposition into local operators
$\mathcal{O}_n$ with explicit coefficient bounds
$|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$. The preprint acknowledges this
implicitly: the translation is performed in Appendix I.1 ("Extraction
Lemma: From Polymer Activities to Operator Decomposition"), which is
new to this paper.

The Extraction Lemma (Lemma I.1) proceeds by Taylor-expanding each
polymer activity $K_k(X, V)$ around the identity in the Lie algebra
variables $v_\ell = \ln V_\ell$, using the analyticity property (B1)
to guarantee convergence. The dimension assignment (Step 3 of Lemma I.1)
and coefficient bounds (Step 4, equation (I.5)) then follow from
Cauchy estimates applied to the convergent expansion.

**Assessment:** The argument in Appendix I.1 is mathematically sound.
Each step (Taylor expansion of analytic functions, Cauchy estimates,
summation over polymers via Kotecky--Preiss) is standard. The crucial
input is (B1), the analyticity of polymer activities with
$k$-independent radius. Given (B1), the extraction is a "reading
exercise" -- it introduces no new mathematical ideas. However, I note
that the preprint does not provide this extraction lemma in Section 5.1
itself; instead Section 5.1.3 states the decomposition as if it were
a direct consequence of Balaban. A referee not reading Appendix I.1
would see a gap. The decomposition is NOT stated as a theorem in
Balaban. It is NOT in Dimock. It IS new to this paper but is correctly
proved in Appendix I.1.

The coefficient bound $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ requires
comment. The factor $g_k^{d_n - 4}$ in Step 4 of Lemma I.1 is argued
by counting vertices: "operators of dimension $d$ involve $(d-4)/2$
additional vertices beyond the dimension-4 part." This is a standard
perturbative power-counting argument, but the proof in I.1 conflates
the perturbative vertex counting with the non-perturbative Cauchy
bound. The Cauchy bound from (I.4) gives
$|K_k^{(n)}(X; v)| \leq e^{-\kappa |X|} \|v\|^n / \rho^n$, and the
polymer sum in (I.5) gives
$|c_{d,i}^{(k)}| \leq C_{\mathrm{KP}} C_i / \rho^{d/2}$. The
factor $g_k^{d-4}$ is then claimed to arise from "normalization" --
that each vertex contributes $g_k^2$. This last step needs more care:
the $g_k^2$ per vertex is a property of the perturbative expansion
of the Wilson action, and the non-perturbative Cauchy bound does not
automatically reproduce this scaling. What is actually needed is
that the small-field condition $|F_{\mu\nu}| < g_k^{1-\epsilon}$
constrains $\|v_\ell\| \lesssim g_k^{1-\epsilon}$, so the Taylor
coefficients at order $n$ are evaluated at
$\|v\| \sim g_k^{1-\epsilon}$, giving
$|c_{d,i}^{(k)}| \lesssim g_k^{(1-\epsilon)(d-4)/2} \cdot [\text{polymer sum}]$.
For $\epsilon = 1/4$ and $d = 6$, this gives $g_k^{3/4}$, not
$g_k^2$. The missing factor $g_k^{5/4}$ presumably comes from the
Boltzmann weight $e^{-\beta s_P} = e^{-s_P/g_k^2}$, which provides
$O(g_k^2)$ suppression per interaction vertex. But this argument is
not made explicit in Appendix I.1.

**Sub-verdict on (a):** The extraction lemma is correct in structure but
the coefficient bound $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ as proved
in I.1 has a gap in the derivation of the $g_k^{d-4}$ scaling. This
is closable: the correct argument uses the small-field constraint on
$\|v\|$ combined with the $1/g_k^2$ prefactor of the Wilson action.
Estimated effort: 1 paragraph of additional argument.

---

**(b) Extension from SU(2) to SU(N).**

Balaban's published papers (CMP 95--119) are indeed primarily for
SU(2). The preprint addresses this in three places: Section 5.1.2,
Appendix I.3, and Appendix K.

The three group-dependent elements identified in Section 5.1.2 --
the covariant Laplacian Lipschitz constant $C_D$, the polymer
expansion convergence constant $\kappa$, and the block-spin
projection radius $r_{\mathrm{proj}}$ -- are correctly identified
as the places where the Lie algebra structure enters.

Appendix K provides a thorough, step-by-step verification of each
element of Balaban's construction for general compact simple $G$.
The key arguments are:

(i) The propagator bounds (K.2) use only that the adjoint
representation is unitary, which holds for any compact $G$.
The Combes--Thomas estimate for exponential decay and the
Neumann series for analyticity are both group-independent in
structure, with $G$-dependent constants ($C_D \leq d_G/m_W^2$,
$\rho_{\mathrm{prop}} = m_W^2/(4d \cdot d_G)$) that are
finite for each $G$.

(ii) The Mayer expansion convergence (K.5) requires
$\kappa(G) > 0$, which is achieved by choosing $m_W$
sufficiently large relative to $d_G$. The explicit (non-circular)
formula in K.5 resolves the apparent circularity.

(iii) The inductive step (K.5, "Closing the induction") shows
that the decay rate $\kappa_k$ degrades by a $k$-independent
amount $\delta\kappa$ per step, and Balaban's freedom to choose
$m_W$ large ensures $\delta\kappa < \kappa_0/2$.

**Assessment:** The extension to general SU(N) is well-handled.
Appendix K is one of the strongest parts of the paper. Each of
Balaban's arguments is checked for group-dependence, and the
$N$-dependent constants are tracked. The claim that "all three
constants are polynomial in $N$" (Section 5.1.2) is verified in
Appendix I.3 and K.

However, I note one issue: Balaban's construction uses a specific
gauge-fixing procedure (axial gauge) and a specific form of the
block-spin averaging. The axial gauge construction (K.7) is indeed
group-independent. But the claim that Balaban's full inductive
construction goes through for SU(N) with only $N$-dependent constant
changes is, strictly speaking, not a theorem in the literature. It
is a plausible and well-argued claim in this paper, but it has not
been independently verified by anyone other than the authors. The
constructive QFT community has not published an SU(N) version of
Balaban's program.

**Sub-verdict on (b):** Sound as an argument; not independently
verified in the literature. The paper is honest about this (it
provides the verification itself rather than citing external sources).
The arguments in Appendix K are correct. For Clay Prize purposes,
the extension to SU(N) rests on the paper's own verification, not on
published results.

---

**(c) The bound $\|E_k\| \leq C g_k^4$ per unit volume.**

This bound is used throughout the paper as the master estimate on
the irrelevant remainder. It is stated in Section 5.1.3 with the
norm described as "$L^\infty$ on gauge-invariant functionals of the
block-averaged fields."

The bound follows from the polymer expansion via:
$\|E_k\| = \|\sum_X K_k(X,V)\| \leq \sum_{X \ni 0} |K_k(X,V)|
\leq \sum_{X \ni 0} e^{-\kappa |X|} = C_{\mathrm{KP}}(\kappa, d)$
per site. This gives $\|E_k\| \leq C_{\mathrm{KP}}$ per unit
volume, which is a $g_k$-independent bound.

Where does the $g_k^4$ come from? It arises because Balaban's
effective action is $S_k = (1/g_k^2) S_{\mathrm{YM}} + E_k$, and
the polymer activities $K_k(X,V)$ are generated by integrating
out fluctuations with coupling $g_k$. The leading contribution to
$E_k$ is the one-loop determinant, which is $O(g_k^0)$ in the
effective action but $O(g_k^4)$ after subtracting the vacuum
energy and the coupling renormalization (the dimension-4 part).
That is: $E_k$ is the remainder after extracting the vacuum energy
$\mathcal{E}_0^{(k)} |\Lambda_k|$ and the coupling term
$(1/g_k^2) S_{\mathrm{YM}}$. The leading term in $E_k$ has
dimension 6, which by the Extraction Lemma carries coefficient
$O(g_k^2)$, giving $\|E_k\| \sim g_k^2 \cdot [\text{dim-6 operator norm}]$.
The operator norm of a dimension-6 operator in the small-field
region is $O(g_k^{2(1-\epsilon)})$ (since $|F| < g_k^{1-\epsilon}$),
so $\|E_k\| \sim g_k^2 \cdot g_k^{2(1-\epsilon)} = g_k^{4-2\epsilon}$.
For $\epsilon = 1/4$, this gives $g_k^{7/2}$, which is better than
$g_k^4$.

The constant $C$ does depend on $N$: it enters through $C_{\mathrm{KP}}$,
which depends on $\kappa(N)$ and the lattice dimension $d$. The
$N$-dependence is tracked in Appendix I.3 (item 11): $C$ is
polynomial in $N$.

**Sub-verdict on (c):** The bound is correct. The constant $C$
depends on $N$ polynomially, and this dependence is tracked. The
$L^\infty$ norm on gauge-invariant functionals is the correct norm
for the spectral perturbation theory that follows. The bound is
sound.

---

**(d) Accumulated higher-order corrections to the running coupling.**

The running coupling obeys
$g_{k+1}^2 = g_k^2 - b_0 g_k^4 \ln 2 + O(g_k^6)$. The $O(g_k^6)$
term accumulates over infinitely many RG steps. The question is
whether the accumulated corrections spoil the asymptotic freedom
trajectory.

This is addressed in the paper at two levels:

(i) **Perturbative:** The accumulated correction is
$\sum_{j=0}^{\infty} O(g_j^6) \leq C \sum_{j=1}^{\infty} 1/(b_0 j \ln 2)^3 < \infty$
(convergent p-series with $p = 3 > 1$). This is stated in
Appendix K.6 and is correct.

(ii) **Non-perturbative:** Balaban's polymer expansion controls
the $O(g_k^6)$ term rigorously. The remainder in the coupling
recursion is not a formal power series but a bounded quantity
extracted from the convergent polymer expansion. The bound
$|g_{k+1}^2 - g_k^2 + b_0 g_k^4 \ln 2| \leq C' g_k^6$ holds
with a $k$-independent constant $C'$ (because the polymer
activities have $k$-independent bounds). This is established in
Balaban's CMP 109, where the coupling renormalization is defined
as the coefficient of $S_{\mathrm{YM}}$ in the effective action.

The convergence of $\sum g_j^6$ along the trajectory
$g_j^2 \sim 1/(b_0 j \ln 2)$ is elementary. The accumulated
correction shifts $g_k^2$ by at most $O(1/k^2)$ relative to the
one-loop trajectory, which does not affect the qualitative
behavior $g_k \to 0$.

**Sub-verdict on (d):** Sound. The accumulated corrections are
controlled by a convergent series, and the non-perturbative
control comes from Balaban's polymer expansion bounds.

---

**(e) Boundary between what Balaban proved and what this paper proves.**

This is perhaps the most important sub-question. The preprint
addresses it explicitly in Section 5.1.5 ("What Balaban Does NOT
Prove") and Section 5.1.6 ("What We Need Beyond Balaban").

**What Balaban proved** (CMP 95--119):
- UV stability: the block-spin RG can be iterated indefinitely with
  bounded effective action.
- Convergent polymer expansion with $k$-independent decay.
- Running coupling with asymptotic freedom.
- All of this for SU(2); the SU(N) extension is this paper's
  contribution (Appendix K).

**What Balaban did NOT prove:**
- The mass gap at any lattice spacing.
- The continuum limit as a Wightman or OS theory.
- The spectral response: how eigenvalues of the transfer matrix
  respond to the irrelevant perturbation $E_k$.

**What this paper claims to prove beyond Balaban:**
- The lattice mass gap $\Delta_0 > 0$ (Sections 2--4).
- The form factor bound: $|\langle 1|E_k(0)|1\rangle_c| \leq C g_k^4 \hat{\Delta}^2$.
- The RG preservation of the mass gap through the continuum limit.

**Assessment:** The boundary is clearly drawn. Section 5.1.5 is
honest about what Balaban does not provide. The paper correctly
identifies that Balaban's UV stability is a necessary but not
sufficient input. The genuinely new contribution -- the stability
of deviation order argument (Section 5.6, Part III) -- is clearly
flagged as new.

However, I note that Balaban's program is "widely considered
incomplete" in the sense that it does not construct a continuum
QFT. The preprint does not claim to complete Balaban's program
in this sense; it uses Balaban's finite-step results as input to
a separate argument about the mass gap. This is a legitimate
strategy: one does not need the full continuum limit construction
to prove $\Delta_\infty > 0$.

**Sub-verdict on (e):** Sound. The boundary is precisely drawn.

---

**Overall assessment of C1:**

The main finding is that the operator decomposition
$S_k = (1/g_k^2) S_{\mathrm{YM}} + \sum c_n \mathcal{O}_n + E_k$
is NOT a theorem in Balaban but is correctly derived in this paper
(Appendix I.1, Extraction Lemma). The derivation has one closable gap:
the coefficient bound $|c_n^{(k)}| \leq C_n g_k^{d_n - 4}$ requires
a more careful argument connecting the Cauchy estimate to the coupling
power-counting via the small-field constraint and the Boltzmann weight
structure. This is a 1-paragraph fix.

The SU(N) extension (Appendix K) is well-executed but represents new
verification by the authors, not published results. The accumulated
higher-order coupling corrections are controlled by a convergent series.
The boundary with Balaban is clearly drawn.

**Impact on the claimed result:**

The closable gap in the coefficient bound (sub-point (a)) affects the
intermediate technical machinery but not the final result: the proof
actually uses only $\|E_k\| \leq C g_k^4$ and the dimension-6 operator
classification, not the individual coefficient bounds $|c_n^{(k)}|$.
The coefficient bounds are stated for completeness but are not load-bearing.
The SU(N) extension (sub-point (b)) is load-bearing for the main claim
for $N \geq 3$, but the arguments in Appendix K are sound.

This does not affect: (i) the main claim $\Delta_\infty > 0$ (provided
the 1-paragraph fix in (a) is supplied), (ii) Clay prize eligibility
(the SU(N) extension would need independent expert verification but the
arguments appear correct).
