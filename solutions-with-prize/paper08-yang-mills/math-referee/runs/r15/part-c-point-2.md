## Part C, Point 2: The Large-Field / Small-Field Decomposition

**Weight:** MEDIUM
**Verdict:** SOUND

**Finding:**

This point interrogates the small-field/large-field decomposition
$\Omega_s = \{|F_{\mu\nu}| < p(g_k)\}$,
$\Omega_l = \{|F_{\mu\nu}| \geq p(g_k)\}$
with cutoff $p(g_k) = g_k^{1-\epsilon}$, and asks whether the
large-field contribution is sufficiently suppressed for the RG
recursion to work. I address each sub-question.

---

**(a) What is $\epsilon$? Is the dimension-6 classification valid only
in $\Omega_s$?**

The value of $\epsilon$ is made explicit in Appendix K.4:
**$\epsilon = 1/4$ is fixed throughout**, following Balaban (CMP 119,
Section 2). The preprint states three constraints on $\epsilon$:

(i) $\epsilon > 0$: the threshold $p(g_k) = g_k^{3/4} \to 0$ as
$g_k \to 0$, ensuring the small-field region expands in the UV.

(ii) $\epsilon < 1/2$: the large-field suppression
$e^{-c/g_k^{2\epsilon}} = e^{-c/g_k^{1/2}}$ is stronger than any
power of $g_k$. This is crucial and correct: for any fixed $n$,
$e^{-c/\sqrt{g_k}} \ll g_k^n$ as $g_k \to 0$.

(iii) $\epsilon < 1$: the threshold $p(g_k) \ll 1$ ensures the
field is genuinely small.

The paper states that conclusions hold for any fixed
$\epsilon \in (0, 1/2)$, and $\epsilon = 1/4$ is a specific
admissible choice.

Regarding the dimension-6 classification: yes, the operator
classification (Section 5.6, Part III) and the analyticity
properties (B1)--(B2) are established only in $\Omega_s$. The
preprint is explicit about this. The dimension-6 projection is
exact within $\Omega_s$ because the Taylor expansion of the
polymer activities converges there (by (B1)). In $\Omega_l$, the
effective action is not decomposed into local operators at all --
the entire large-field contribution is bounded as a single
exponentially suppressed remainder.

This is the standard strategy in constructive QFT: control the
small-field region analytically (perturbation theory + polymer
expansion), and bound the large-field region non-perturbatively
(exponential suppression from the Boltzmann weight). The two
contributions are combined at the level of the partition function
(or transfer matrix), not at the level of operator decomposition.

**Sub-verdict on (a):** Sound. $\epsilon = 1/4$ is fixed. The
dimension-6 classification applies in $\Omega_s$ only, and the
$\Omega_l$ contribution is handled separately as a suppressed
remainder. This is standard and correct.

---

**(b) Is the large-field suppression $O(e^{-c/g_k^{2\epsilon}})$
sufficient for the RG recursion?**

This is the critical technical question. With $\epsilon = 1/4$,
the large-field suppression is $O(e^{-c/g_k^{1/2}})$. The
question is whether this is negligible compared to the small-field
contribution $g_k^4 \hat{\Delta}_k^2$.

On the asymptotically free trajectory, $g_k^2 \sim 1/(b_0 k \ln 2)$,
so:

- Small-field contribution: $g_k^4 \hat{\Delta}_k^2 \sim k^{-2} \cdot 4^{-k}$.
- Large-field contribution: $e^{-c/g_k^{1/2}} \sim e^{-c(b_0 k \ln 2)^{1/4}}$.

The large-field term $e^{-c \cdot k^{1/4}}$ decays as a stretched
exponential in $k$. The small-field term $k^{-2} \cdot 4^{-k}$ decays
as a pure exponential (geometric) in $k$. For large $k$, the
geometric decay $4^{-k}$ eventually dominates the stretched
exponential $e^{-c k^{1/4}}$, meaning the small-field term decays
FASTER than the large-field term.

The comparison between the two contributions requires care with the
notation. The preprint uses two conventions for $a_k$ in different
sections: in Sections 5.4--5.6 (the block-spin RG), $a_k = 2^k a_0$
is the COARSENED lattice spacing (growing with $k$); in Section 5.7
(the continuum limit), $a_k = a_0/2^k$ is the lattice spacing at
the $k$-th REFINEMENT step (shrinking with $k$). The continuum limit
sends $a_0 \to 0$, and the RG steps index the same physics in
opposite directions. This notational inconsistency between sections
should be flagged but is not a mathematical error.

In the continuum limit convention (Section 5.7), the comparison is:

- Small-field contribution per step: $g_k^4 (a_k \Lambda)^s \sim
  k^{-2} \cdot 2^{-ks}$, which decays geometrically.
- Large-field contribution per step:
  $e^{-c/g_k^{2\epsilon}} = e^{-c/g_k^{1/2}} \sim
  e^{-c(b_0 k \ln 2)^{1/4}}$, which decays as a stretched
  exponential.

Both are summable over $k$. The geometric decay $2^{-ks}$ is
faster than the stretched exponential $e^{-c k^{1/4}}$ for large $k$,
so the large-field term eventually dominates the small-field term.

**This means the preprint's claim (Section 5.5.3, line 1244) that
$e^{-c/g_k^{1/2}} \ll g_k^4 \hat{\Delta}_k$ is imprecise.** In the
coarsening convention (where $\hat{\Delta}_k = a_k \Delta_k$ grows
as $2^k$), the comparison $e^{-c/g_k^{1/2}} \ll g_k^4 \hat{\Delta}_k$
becomes $e^{-c k^{1/4}} \ll k^{-2} \cdot 2^k$, which IS true
(the right side grows exponentially while the left decays). So in
the coarsening convention used in Section 5.5.3, the claim is
correct. In the continuum-limit convention, the analogous comparison
would be $e^{-c/g_k^{1/2}} \ll g_k^4 (a_k \Lambda)^s$, which
fails for large $k$.

**However**, the proof does not actually require this pointwise
comparison in the continuum-limit convention. What Section 5.5.3
establishes is that the large-field contribution to the TWO-GLUEBALL
BINDING ENERGY $\epsilon_B^{\mathrm{lf}}$ is negligible compared to
the gap $\hat{\Delta}_k$ itself (in the coarsening convention).
This is used to show $E_2 - E_1 \geq \hat{\Delta}_k/2$, which is
the input to the spectral lemma constant $\zeta$ being bounded.
This comparison IS correct in the coarsening convention.

The summability of the total mass gap correction (Section 5.7) uses
both terms separately:

$$|\delta C_k| \leq C_{\mathrm{sf}} g_k^4 (a_k\Lambda)^s
  + C_{\mathrm{lf}} e^{-c/g_k^{1/2}}$$

Both are summable (the first geometrically, the second as a
stretched exponential). The proof of $\Delta_\infty > 0$ goes through.

**Sub-verdict on (b):** The large-field suppression is sufficient.
The claim in Section 5.5.3 that $e^{-c/g_k^{1/2}} \ll g_k^4 \hat{\Delta}_k$
is correct in the coarsening convention used there (where $\hat{\Delta}_k$
grows as $2^k$). The claim in Section 5.6, Part III.5 that large-field
corrections are "negligible" is correct in the sense that the total
large-field contribution to $\Delta_\infty$ is bounded by the convergent
sum $\sum e^{-c/g_k^{1/2}} < \infty$. The word "negligible" in Part III.5
could be sharpened to "separately summable and smaller than the small-field
contribution at each step in the coarsening convention," but this is a
presentational refinement, not a gap. The notational inconsistency between
Sections 5.4--5.6 (coarsening: $a_k = 2^k a_0$) and Section 5.7
(refinement: $a_k = a_0/2^k$) should be flagged for the reader.

---

**(c) Is $|F_{\mu\nu}| < p(g_k)$ gauge-invariant?**

The lattice field strength $F_{\mu\nu}$ is defined through the
plaquette variable $U_P$, and the condition is actually on the
plaquette action variable $s_P = 1 - (1/N) \mathrm{Re}\,\mathrm{Tr}(U_P)$.
This is stated explicitly in Appendix K.4:

> The small-field condition $\Omega_s = \{|s_P| < p(g_k)\}$ with
> $p(g_k) = g_k^{1-\epsilon}$ is defined in terms of the plaquette
> variable $s_P = 1 - (1/d_R)\,\mathrm{Re}\,\mathrm{Tr}_R(U_P)$,
> which is gauge-invariant and well-defined for any compact $G$.

The plaquette variable $s_P$ is manifestly gauge-invariant:
$U_P \to g_x U_P g_x^{-1}$ under gauge transformations, so
$\mathrm{Tr}(U_P)$ is invariant. The small-field condition is
therefore gauge-invariant.

Balaban's construction uses axial gauge as a computational device
for the fluctuation integral, but the small-field/large-field
decomposition is defined in terms of gauge-invariant quantities.
The gauge fixing interacts with the fluctuation propagator
$G_k(V)$ (which depends on the gauge-fixing choice) but not with
the partition into $\Omega_s$ and $\Omega_l$.

**Sub-verdict on (c):** Sound. The condition is on the gauge-invariant
plaquette variable $s_P$, not on $F_{\mu\nu}$ in a fixed gauge.
The notation $|F_{\mu\nu}| < p(g_k)$ in the main text is informal;
the precise condition is $|s_P| < p(g_k)$, which is gauge-invariant.

---

**Overall assessment of C2:**

The small-field/large-field decomposition is handled correctly.
The value $\epsilon = 1/4$ is fixed and explicit. The dimension-6
classification applies only in $\Omega_s$, and this is correctly
stated. The gauge-invariance of the decomposition is ensured by
using plaquette variables.

Two minor issues:

(1) The claim that large-field contributions are "negligible" in
Section 5.6 Part III.5 is correct but could be stated more
precisely: the large-field terms are summable over $k$ and smaller
than the small-field terms at each step in the coarsening convention,
though in the continuum-limit convention the comparison reverses for
large $k$ (both contributions remain separately summable regardless).

(2) There is a notational inconsistency between Sections 5.4--5.6
(where $a_k = 2^k a_0$, coarsening) and Section 5.7 (where
$a_k = a_0/2^k$, refinement). This should be standardized or at
least flagged with a remark. It does not affect the mathematics.

Neither issue constitutes a gap. The proof is sound.

**Impact on the claimed result:**

(i) The main claim $\Delta_\infty > 0$ is not affected. The summability
of both the small-field and large-field contributions is established.

(ii) No subsidiary claim is affected.

(iii) Clay prize eligibility is not affected. The notational
inconsistency should be cleaned up in the final version.
