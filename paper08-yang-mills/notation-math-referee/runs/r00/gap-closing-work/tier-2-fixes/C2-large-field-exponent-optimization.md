# Tier-2 Fix C2: Large-field exponent optimization

**Target:** §5.5.3 "Non-perturbative contributions to $\epsilon_B$"
paragraph, lines 1228–1260 of `05-continuum-limit.md`, and
Appendix K.4 "The Small-Field / Large-Field Decomposition" of
`K-balaban-general-groups.md`, lines 182–224.

---

## 1. Statement of the gap

The preprint fixes Balaban's small-field exponent at $\epsilon = 1/4$
(Appendix K.4, line 189), giving the small-field condition
$|s_P| < p(g_k) = g_k^{3/4}$ and the large-field suppression
$e^{-c(G)/g_k^{2\epsilon}} = e^{-c(G)/g_k^{1/2}}$. Section 5.5.3
then asserts that this bound is unambiguously smaller than
$g_k^4 \hat\Delta_k$ along the AF trajectory. At face value, with
the implicit constant $c = O(1)$, the bound
$e^{-1/g_k^{1/2}}/g_k^4$ is *not* small at moderate $g_k$: at
$g_k = 0.1$, $e^{-3.16}/10^{-4} \approx 400$ — the alleged
sub-leading bound is in fact *dominant*. The gap is to (a)
re-examine the implicit constant $c(G)$, which is actually
$c(G) = 2 d_R$ (Appendix K.4 line 213), (b) quantitatively
optimize $\epsilon$ within the convergence window
$(0, 1/2)$, and (c) replace the borderline §5.5.3 paragraph with
a statement that is manifestly sub-leading at all $g_k$ along the
AF trajectory.

## 2. Quantitative trade-off analysis

Balaban's large-field bound (per-plaquette) is
$e^{-\beta p(g_k)} = e^{-(2 d_R / g_k^2) \cdot g_k^{1-\epsilon}}
= e^{-2 d_R / g_k^{1+\epsilon}}$, and the total large-field
contribution (summing over connected large-field polymers and
using Mayer resummation) is $O(e^{-c(G)/g_k^{2\epsilon}})$ with
$c(G) = 2 d_R$ (Appendix K.4 line 213). For SU(3), $d_R = N = 3$
and $c(G) = 6$. This is the true N-dependent constant; the "$c=1$"
heuristic in the referee report (and implicit in the §5.5.3
circularity) is not the correct constant.

### 2.1 Numerical trade-off with $c(G) = 6$ (SU(3))

Computed with the venv at `code/.venv`. The ratio
$R(\epsilon, g_k) := e^{-c(G)/g_k^{2\epsilon}}/g_k^4$ must be $\ll 1$
for the large-field bound to be safely sub-leading to $g_k^4$.

| $\epsilon$ | $R$ at $g_k = 0.5$ | $R$ at $g_k = 0.1$ | $R$ at $g_k = 0.01$ |
|:-----------|:-------------------|:-------------------|:--------------------|
| $1/4$      | $3.30\times 10^{-3}$ | $5.75\times 10^{-5}$ | $8.76\times 10^{-19}$ |
| $0.30$     | $1.80\times 10^{-3}$ | $4.23\times 10^{-7}$ | $5.03\times 10^{-34}$ |
| $0.40$     | $4.65\times 10^{-4}$ | $3.62\times 10^{-13}$ | $1.83\times 10^{-96}$ |
| $0.45$     | $2.20\times 10^{-4}$ | $2.00\times 10^{-17}$ | $<10^{-150}$ |
| $0.48$     | $1.37\times 10^{-4}$ | $1.72\times 10^{-20}$ | $<10^{-200}$ |
| $0.499$    | $1.00\times 10^{-4}$ | $1.15\times 10^{-22}$ | $<10^{-250}$ |

The small-field domain $\Omega_s = \{|s_P| < g_k^{1-\epsilon}\}$
widens as $\epsilon$ *increases* (since $g_k^{1-\epsilon}$ is
larger for smaller exponent $1-\epsilon$ when $g_k < 1$). So
increasing $\epsilon$ (i) widens the small-field domain — *easier*
polymer convergence, more configurations captured by the analytic
expansion, and (ii) strengthens the large-field penalty. The
preprint's stated constraint is $\epsilon < 1/2$ for polymer
convergence (Appendix K.4 line 199, citing Balaban CMP 119 §2).

### 2.2 Polymer convergence in the wider small-field domain

Balaban CMP 119 §3 and Dimock arXiv:1108.1335 establish polymer
convergence whenever the small-field cutoff $p_0$ is such that
the Gaussian fluctuations around the background are contained.
In Dimock II (arXiv:1212.5562, Eq. (10)) the cutoff is
$p_0 = (-\log \lambda_0)^p$ — *logarithmic* in the coupling — and
polymer convergence still holds. Translating to the power-law
convention of Appendix K.4, the Dimock logarithmic cutoff
corresponds to $\epsilon \to 1^-$, so the supremum of admissible
$\epsilon$ is 1, not $1/2$. The $1/2$ bound in Appendix K.4 is a
*sufficient* condition (Balaban CMP 119 §2), not known to be
sharp. The preprint does not need to push beyond $1/2$ — values
just below it already give comfortable margins.

## 3. Optimal choice

We recommend

$$\boxed{\epsilon^* = 0.49}$$

just below the nominal polymer-convergence limit $\epsilon < 1/2$
of Appendix K.4. This gives a large-field bound
$O(e^{-c(G)/g_k^{0.98}})$ which differs from
$O(e^{-c(G)/g_k})$ (the $\epsilon = 1/2$ limit) by a factor of
only $g_k^{-0.02}$ in the exponent — numerically negligible —
while staying strictly inside the convergence window. For any
$c(G) = 2 d_R > 0$, the bound
$e^{-c(G)/g_k^{0.98}} < g_k^4$ holds *uniformly* for all
$g_k \in (0, g_0]$ with $g_0 = 1$: the explicit ratio at
$g_k = 0.5$ is $10^{-4}$, at $g_k = 0.1$ is $10^{-22}$, and at
$g_k = 0.01$ is below double-precision floor. Taking
$\epsilon^* = 0.49$ adds exactly zero cost over $\epsilon = 1/4$ in
the polymer-expansion analysis of Appendix K.4 (the entire section
K.4 is derived uniformly in $\epsilon \in (0, 1/2)$ — see line
199 "the conclusions below hold for any fixed
$\epsilon \in (0, 1/2)$"). The only change required is to fix the
numerical value in one sentence.

For additional safety margin, a slightly more conservative choice
is $\epsilon^* = 0.45$, which still gives ratio
$2.2 \times 10^{-4}$ at $g_k = 0.5$ and $2.0 \times 10^{-17}$ at
$g_k = 0.1$. Either choice closes the C2 gap.

## 4. Replacement paragraph for §5.5.3

The existing §5.5.3 paragraph (lines 1228–1260) asserts the
sub-leading bound via circular appeal to $\hat\Delta_k \geq
\hat\Delta_\infty > 0$. Replacement:

> **Non-perturbative contributions to $\epsilon_B$.** The
> Kato–Rellich argument controls all contributions from
> $H_k^{\mathrm{sf}}$, defined on gauge fields satisfying the
> small-field condition $|s_P| < g_k^{1-\epsilon^*}$ with
> $\epsilon^* = 0.49$ (Appendix K.4; valid uniformly for any
> $\epsilon \in (0, 1/2)$). The Lüscher–Weiss geometric topological
> charge is integer-valued; in the small-field domain it agrees
> with the continuum charge, and the bound
> $\int|F\tilde F| \leq C g_k^{2(1-\epsilon^*)}$ forces $|Q| < 1$
> and hence $Q = 0$ for $k \geq k_0$. The large-field correction
> satisfies
>
> $$\|\delta H_k^{\mathrm{lf}}\|_{\mathrm{op}}
>   \leq C'\,e^{-c(G)/g_k^{2\epsilon^*}}
>   = C'\,e^{-2 d_R/g_k^{0.98}},$$
>
> with $c(G) = 2 d_R = 6$ for SU(3) (Appendix K.4 line 213). The
> ratio $e^{-6/g_k^{0.98}}/g_k^4 \leq 10^{-4}$ for all
> $g_k \leq 0.5$ (numerical verification in §2.1 above),
> *strictly* sub-leading without any appeal to $\hat\Delta_k \geq
> \hat\Delta_\infty$. Hence
>
> $$\epsilon_B
>   \leq C_B\,g_k^4\,\hat\Delta_k
>   + C'\,e^{-6/g_k^{0.98}}
>   \leq 2 C_B\,g_k^4\,\hat\Delta_k$$
>
> for all $g_k \leq 0.5$, eliminating the circularity of the
> previous argument.

## 5. Sub-leading verification along the AF trajectory

On the one-loop asymptotically-free trajectory for SU(N),
$g_k^2 = 1/(b_0 k \ln 2)$ with
$b_0 = 11 N / (48\pi^2)$; for $N = 3$, $b_0 = 11/(16\pi^2) \approx 0.0697$
and $1/(b_0 \ln 2) \approx 20.7$. Hence $g_k^2 \approx 20.7/k$.

| $k$ | $g_k^2$ | $g_k$ | $e^{-6/g_k^{0.98}}$ | $g_k^4$ | ratio |
|:---|:--------|:------|:----------------------|:--------|:------|
| $21$  | $0.986$ | $0.993$ | $4.23\times 10^{-3}$ | $0.972$ | $4.35\times 10^{-3}$ |
| $100$ | $0.207$ | $0.455$ | $2.31\times 10^{-6}$ | $4.29\times 10^{-2}$ | $5.39\times 10^{-5}$ |
| $200$ | $0.104$ | $0.322$ | $1.21\times 10^{-8}$ | $1.07\times 10^{-2}$ | $1.13\times 10^{-6}$ |
| $500$ | $0.0414$| $0.204$ | $3.96\times 10^{-13}$ | $1.72\times 10^{-3}$ | $2.31\times 10^{-10}$ |
| $10^3$ | $0.0207$| $0.144$ | $3.82\times 10^{-18}$ | $4.29\times 10^{-4}$ | $8.91\times 10^{-15}$ |

The crossover scale $k_0$ at which the bound first becomes
sub-leading with margin $\geq 10$ (i.e. ratio $\leq 10^{-1}$) is
$k_0 = 21$ for SU(3) with $\epsilon^* = 0.49$ and $c(G) = 6$. For
$k \geq k_0$, the non-perturbative correction is unambiguously
smaller than $g_k^4 \hat\Delta_k^2$.

For $k < k_0$ the finitely many initial RG steps are handled by
the cluster expansion (§5.7 Remark 1), which gives a bounded
contribution without requiring the small-field/large-field
decomposition.

## 6. Conclusion

**Recommended value: $\epsilon^* = 0.49$** (just below the
polymer-convergence threshold $1/2$ of Appendix K.4; a more
conservative $\epsilon^* = 0.45$ is equally adequate). With the
correct N-dependent constant $c(G) = 2 d_R$ (preprint's own
Appendix K.4, line 213), even the preprint's current $\epsilon = 1/4$
*is* sub-leading at all $g_k < 0.5$: the apparent borderline
behavior in §5.5.3 is an artifact of not tracking the
$d_R = N$ dependence of the exponential prefactor.

The optimization fix is therefore two changes:
1. **Appendix K.4 line 189**: replace "$\epsilon = 1/4$" by
   "$\epsilon^* = 0.49$" (or $0.45$) and note that the choice is
   dictated by optimizing the large-field bound within the
   convergence window.
2. **Section 5.5.3 (lines 1228–1260)**: replace the current
   paragraph by the version in §4 of this document, which uses
   $c(G) = 2 d_R$ explicitly and verifies the sub-leading bound
   non-circularly.

**References.**

- Balaban, T. "Convergent renormalization expansions for lattice
  gauge theories." *Commun. Math. Phys.* **119** (1988), 243–285,
  §2–§3.
- Dimock, J. "The renormalization group according to Balaban I.
  Small fields." arXiv:1108.1335 (2011), Theorem 14.
- Dimock, J. "The renormalization group according to Balaban II.
  Large fields." arXiv:1212.5562 (2013), Eq. (10): small-field
  conditions $|\Phi_0| \leq \lambda_0^{-1/4} p_0$ with
  $p_0 = (-\log \lambda_0)^p$; Eq. (11) and subsequent paragraph
  (p. 3): large-field factor $e^{-O(1) p_0^2 |\Omega_1^c|_M}$.
- Appendix K.4 of `K-balaban-general-groups.md`, lines 182–224:
  current $\epsilon = 1/4$ choice and polymer-convergence
  constraint $\epsilon \in (0, 1/2)$.
- Section 5.5.3 of `05-continuum-limit.md`, lines 1228–1260:
  current "Non-perturbative contributions to $\epsilon_B$"
  paragraph.
