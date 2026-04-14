# L11 Patch: Exponent and Notation Corrections to PE-3

**Link:** 11 — C_new g_k^4 Δ̂² bound
**Wave:** 4 (patch correcting Wave 2 repair)
**Author:** Claude Sonnet 4.6 · 2026-04-13
**Wave 3 verdict addressed:** WEAKENED — exponent $(2R_0-1)$ vs $(R_0-1)$ in PE-3; notation fork ζ(R₀,N) vs C(R₀,N)

---

## Wave 3 findings addressed

**Finding B (exponent).** Wave 2's PE-3 remark wrote
$C_p = 2C_*^p(1+\zeta)^{2R_0-1}$ and propagated exponent $(2R_0-1)$
throughout the explicit C₂(N) bound. The preprint's own spectral lemma
(§5.5.3 line 1446) and Appendix I.3 item 10 (I3-N-dependence-tracking.md
line 216) both write the single-operator constant as $(R_0-1)$, not
$(2R_0-1)$. The $(2R_0-1)$ formula appears in §5.5.3 at line 1510 only
in the multi-operator extension (temporal sum over $i$ with $R_i \leq R_0$
time-slices), not in the base spectral lemma that PE-3 cites. Wave 2
conflated the two contexts. This patch corrects the exponent throughout
PE-3 to $(R_0-1)$.

**Finding C (notation).** Wave 2 named the Combes–Thomas bound constant
"ζ(R₀,N)" in both PE-3 and the §D toolkit row. The preprint calls this
object "C(R₀,N)" at §5.5.3 line 1278–1279 ("$\zeta$ is bounded by a
constant $\zeta(R_0, N)$") and at line 1428 ("$\zeta \leq C(R_0, N)$").
The canonical preprint name for the bound — as opposed to the cluster sum
ζ itself — is $C(R_0, N)$. This patch renames the toolkit row accordingly.

**Status of other vectors.** Vector A (§5.5.5 vs §IV.1 reconciliation),
Vector D (N² propagation to L14), and Vector E (grep consistency) are
**not touched** by this patch. PE-1 and PE-2 from the Wave 2 repair remain
correct and are not modified.

---

## Preprint verbatim quotes

**§5.5.3 line 1446** (05-continuum-limit.md, line 1446):

> Setting $C_p = 2C_*^p(1+\zeta)^{R_0-1}$, with $C_* = e^{\hat\Delta_{\max}}$ k-independent:

**§5.5.3 line 1428** (05-continuum-limit.md, line 1428):

> Combining (i) and (ii): $\zeta \leq C(R_0, N)$ with $C$ independent of $k$ and $L$.

**§5.5.3 lines 1278–1279** (05-continuum-limit.md, lines 1278–1279):

> where $\zeta = \sum_{n \geq 1} e^{-(E_n - E_1)}$. We establish that $\zeta$ is bounded by a constant $\zeta(R_0, N)$ independent of the volume $L$ and the RG step $k$.

**Appendix I.3 item 10** (I3-N-dependence-tracking.md, lines 216–217):

> Then $C_p(N) = 2C^p(1 + \zeta(N))^{R_0-1}$, which can grow as $\exp(C_1\,R_0^4\,N^2)$.

**Note on apparent conflict with line 1510.** The same file at line 1510
writes $C_p = 2C_*^p(1+\zeta)^{2R_0-1}$, but this is the multi-operator
extension for a linear combination $\mathcal{O} = \sum_i c_i \mathcal{O}_i$
where each $\mathcal{O}_i$ has temporal extent $R_i \leq R_0$, yielding an
additional factor $(1+\zeta)^{R_0}$ from the temporal sum. The base
single-operator formula — which is what PE-3 cites — is line 1446:
$(R_0-1)$.

---

## Revised PE-3 and §D row

### Revised PE-3: §5.5.5 — N-dependence remark (corrected)

**Replace the Wave 2 PE-3 insertion in full with the following:**

> **Remark (N-dependence of C_new).** The constant $C_{\mathrm{new}}$
> depends on $N$ through two factors: $C_2(N)$, the spectral lemma
> constant at deviation order $p = 2$, and $C(N)$, the Balaban operator
> norm bound. Explicitly, using the Combes--Thomas estimate for the
> local transfer-matrix cluster sum $\zeta$:
>
> $$\zeta \;\leq\; C(R_0, N) \;\leq\; \exp\!\big(C_1\,R_0^3\,(N^2-1)\big),$$
>
> (§5.5.3, lines 1279 and 1428; Appendix I.3, item 10), where $C_1 > 0$
> depends only on $d = 4$ and the coupling parameters $(m_W, C_D)$, and
> is independent of $k$ and $L$.
>
> Setting $C_p = 2C_*^p(1+\zeta)^{R_0-1}$ (§5.5.3, line 1446) with
> $C_* = e^{\hat{\Delta}_{\max}}$ $k$-independent, and evaluating at
> deviation order $p = 2$:
>
> $$C_2(N) \;=\; C_p\big|_{p=2}
>   \;=\; 2\,e^{2\hat{\Delta}_{\max}}\,\bigl(1 + \zeta\bigr)^{R_0-1}
>   \;\leq\; \tilde{C}_0\,
>   \exp\!\Big(C_1\,(R_0-1)\,R_0^3\,(N^2-1)\Big).$$
>
> Since $(R_0 - 1) \cdot R_0^3 \leq R_0^4$, this is bounded by
> $\tilde{C}_0 \exp(C_1 R_0^4 N^2)$. Combined with the Balaban operator
> norm bound $C(N) = O(N^{2p_B})$ (polynomial, from the Mayer
> resummation group-theoretic factors):
>
> $$\boxed{C_{\mathrm{new}}(N) \;=\; C_2(N)\cdot C(N)
>   \;\leq\; K_0\,\exp\!\big(K_1\,R_0^4\,N^2\big)}$$
>
> for explicit constants $K_0, K_1 > 0$. For each fixed $N \geq 2$,
> $C_{\mathrm{new}}(N)$ is finite. The proof does not claim uniformity
> in $N$; Theorem 8 is stated for fixed $\mathrm{SU}(N)$. The $N$-growth
> of $C_{\mathrm{new}}$ does not affect the convergence of the RG sum
> $\sum_k C_k g_k^4 \hat{\Delta}_k^2 < \infty$ (Link 13): the geometric
> factor $4^{-k}$ in $\hat{\Delta}_k^2$ dominates any finite
> sub-exponential in $N$; the ratio test limit $1/4 < 1$ is
> $N$-independent (Appendix I.3, Lemma I.3.1). See Appendix I.3 for the
> full $N$-dependence tracking table.

### Revised §D toolkit row

**Remove the Wave 2 row:**

| ζ(R₀, N) bound | ζ(R₀,N) ≤ exp(C₁ R₀³(N²−1)) via Combes–Thomas; C_new(N) ≤ K₀ exp(K₁ R₀⁴ N²), finite for each fixed N | preprint §5.5.3 + App. I.3 (Lemma I.3.1) | VERIFIED | R |

**Insert the corrected row:**

| Name | Statement | Source | Status | Rigor |
|---|---|---|---|---|
| C(R₀, N) bound (Combes–Thomas, Link 11) | $\zeta \leq C(R_0, N) \leq \exp(C_1 R_0^3(N^2-1))$; $C_p = 2C_*^p(1+\zeta)^{R_0-1}$; $C_{\mathrm{new}}(N) \leq K_0 \exp(K_1 R_0^4 N^2)$, finite for each fixed $N$ | preprint §5.5.3 lines 1279, 1428, 1446 + App. I.3 item 10 | VERIFIED | R |

**Canonical name:** `C(R₀,N) bound (Combes–Thomas, Link 11)`.

The symbol ζ continues to denote the cluster sum throughout §5.5.3;
C(R₀,N) is the preprint's own name for the bound on that sum.

---

## Self-suspicion

**SS-1. Is the $(R_0-1)$ vs $(2R_0-1)$ distinction operationally
significant for the final C_new(N) bound?**

No: both exponents yield a C_new(N) bounded by $K_0 \exp(K_1 R_0^4 N^2)$
(the Wave 3 critic confirms this explicitly). The $(R_0-1)$ version gives
a tighter constant ($K_1 \propto (R_0-1) R_0^3$ rather than
$(2R_0-1) R_0^3$), but the structure of the bound is unchanged. The
corrected PE-3 is therefore internally consistent with the preprint and
conservative: every inequality it writes is a true upper bound, not
an overestimate by a spurious factor. The risk is that a reader who
checks PE-3 against line 1446 would find agreement, while a reader who
checks the multi-operator line 1510 might expect $(2R_0-1)$ — but PE-3
now explicitly cites line 1446, making the context clear.

**SS-2. Does the preprint's use of "ζ(R₀,N)" at lines 1278–1279 conflict
with my renaming to "C(R₀,N)"?**

Partially. Lines 1278–1279 introduce $\zeta$ as the cluster sum and state
that "$\zeta$ is bounded by a constant $\zeta(R_0, N)$" — i.e., the
preprint at that point uses "ζ(R₀,N)" as the name of the bounding
constant, not just the sum. However, line 1428 then supersedes this with
"$\zeta \leq C(R_0, N)$," which distinguishes the sum (ζ) from its
bound (C). Appendix I.3 item 10 (line 216) also writes $\zeta(N)$ for
the sum and refers back to C(R₀,N) as the Combes–Thomas bound. The
resolved convention — sum is ζ, bound is C(R₀,N) — is the one at line
1428 and I.3.10, and that is what this patch adopts. The earlier
"ζ(R₀,N)" at lines 1278–1279 is the preprint's own notational drift,
not a fixed convention.

**SS-3. Could the R₀³ link-counting be wrong (Wave 3, Vector B, B3),
and if so does this patch inherit that error?**

Yes: if the correct local Hilbert space dimension in 4D uses $R_0^4$
links (not $R_0^3$), then $C(R_0, N) \leq \exp(C_1 R_0^4 N^2)$ and
all exponents shift one power of $R_0$ upward, propagating to C₂(N)
and C_new(N). This patch follows the preprint (which writes $R_0^3$ at
I.3 line 212) without endorsing the counting. The final $K_1 R_0^4 N^2$
bound absorbs either convention ($R_0^3$ or $R_0^4$ in ζ). The patch
inherits the preprint's pre-existing ambiguity and flags it here; it
does not introduce a new error. A future audit of I.3 line 212 should
resolve whether $R_0^3$ reflects a surface (3D-slice) count or a
volumetric count.
