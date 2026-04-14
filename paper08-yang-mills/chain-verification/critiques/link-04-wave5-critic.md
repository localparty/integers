# Link 4 Wave 5 Critic Verdict

**Target:** (B1) analyticity of polymer activities, k-independent radius
**Wave:** 5 (independent final verification of Wave 4 patch)
**Instance:** Different Claude instance from Wave 2/Wave 4 Authors
**Incoming status:** WEAKENED (Wave 3) → claimed VERIFIED (Wave 4 patch)
**Wave 5 verdict:** SURVIVED
**Confidence:** 9/10

---

## Primary source protocol

PDF `journals/balaban-CMP109-1987.pdf` read directly at journal pages 260,
262, 265, 269, 280–281. All four checks made against the scan. No secondary
paraphrase substituted. Preprint files read at the cited lines.

---

## C1 — §1 (1.2) and §2 eqs. 2.2–2.3 verbatim quotes correct?

**CONFIRMED.**

Journal p. 260, condition (1.2):

> $|U(\partial p)-1| = |(\partial U)(p)-1| < \varepsilon_0\eta^2$,
> $\eta = L^{-k}$, $p \in T$,
> $|J| < \varepsilon_0$ on $T$,
> $J = D^{2\alpha}_{U_k}\xi^{-2}\pi\operatorname{Im}\partial U$

The patch quote matches the core bound verbatim. The J-definition tail is
omitted from the patch quote but is not misquoted; the cited substance is
accurate.

Journal p. 265, eqs. (2.2)–(2.3):

> $V \to \mathbf{G}(V) + A(U_k(V))$, $V: \bar{V} = W$. (2.2)

> $V^{(k)} = \bar{U}^k_{+1} = M^k(U_{k+1})$. (2.3)

Both match the patch exactly. The surrounding prose — "there exists the
exactly one critical point … which is a minimum of the function (2.2),
denoted by $V^{(k)} = V^{(k)}(W)$" — is correctly characterised in the
patch as establishing uniqueness and regularity of the saddle-point.

**C1 result: PASS.**

---

## C2 — §3 Lemma 4 scope correctly identified (fluctuation-composition only)?

**CONFIRMED.**

Journal p. 280, Lemma 4 statement:

> For $\mathbf{U} \in U^c_{k+1}(\square_0,(1+2\beta)\alpha_0,
> (1+2\beta)\alpha_1)$, $\mathbf{A}$ defined on $\square_0$ and satisfying
> (3.31), $B'$ defined on the set of bonds connected with the definition
> of $U_j(\square_0,\cdot)$ and satisfying $|B'| < \alpha_3$, we have
>
> $(U_j(\square_0,\exp i(\tau B + B')),J_j(\square_0,\exp i(\tau B +
> B')))|_X \in U^c_j(X,\alpha_0,\alpha_1)$ (3.53)

The objects $B$, $B'$ are unambiguously fluctuation fields (lattice
$T_1^{(k)}$ bonds). The Lemma's hypothesis is that the background
**U** belongs to the inflated domain with parameters $(1+2\beta)\alpha_0$,
$(1+2\beta)\alpha_1$; its conclusion is domain-membership of the
fluctuation-composed output pair. This is the fluctuation-integration step,
not the saddle-point step. The patch's two-sentence split — Sentence A for
the saddle-point center via §1 (1.2) + §2 eqs. 2.2–2.3, Sentence B for the
fluctuation-composition via Lemma 4 — correctly attributes each result to
the right authority. The Wave 3 substantive attack (A3) is fully resolved.

**C2 result: PASS.**

---

## C3 — "(i)–(iv)" correct per CMP 109 §1 p. 262?

**CONFIRMED.**

Journal p. 262 reads: "The space $U^c_j(X,\alpha_0,\alpha_1)$ is a union of
orbits $[(\mathbf{U},\mathbf{J})]$ determined by the **four conditions**
written below." Conditions (i)–(iv) all appear on p. 262:

- (i): $\mathbf{U} = U'U$, $|\partial U - 1| < \alpha_0\xi^2$ on $X$,
  gauge transformation $u$ with $U^u = \exp i\xi A$.
- (ii): $U' = \exp i\xi A'$, $A' \in \mathfrak{g}^c$, bounds on $A'$.
- (iii): $|\partial U - 1| < \alpha_0\xi^2$, $|\mathbf{J}| < \gamma_0$ on $X$.
- (iv): Sequence $\{\Omega_n\}$, $n=1,\ldots,j$, of maximal domains; functions
  $U_n(V)$ in axial gauges; pair $(U_n(M'(\mathbf{U})), J_n(M'(\mathbf{U})))$
  satisfies the stated bounds on $\tilde{X}^{-2}$.

The patch uses "(i)–(iv)" throughout, correcting the Wave 2 "(i)–(iii)." The
Wave 3 trivial attack (A2) is resolved. The count is correct.

**C3 result: PASS.**

---

## C4 — Line 1628 bonus fix verifiable (Sec 3 vs Sec 4)?

**CONFIRMED with note of residual instance.**

Current preprint text at line 1628:

```
convergent series of analytic cluster activities (CMP 109, Sec. 4);
```

PDF confirms:

- §3 (pp. 269–280): "An Expansion of Terms in Fluctuation Field Integral,
  and Preliminary Analytic Extensions." Lemma 4 and the analytic extension
  of cluster activity terms (eq. 3.53, bound 3.54) are here.
- §4 (p. 281): "Ward-Takahashi Identities and Their Consequences." Content
  is WT identities used to extract β-function coefficients, not cluster
  activity analyticity.

The patch's fix ("Sec. 4" → "Sec. 3") at line 1628 is correct and
consistent with `05-continuum-limit.md` line 1635 ("CMP 109, Sec. 3;
CMP 119, Sec. 2") and `H-balaban-analyticity.md` §3 Step (c) source line.

**Note (not blocking):** A second unremediated instance appears at
`05-continuum-limit.md` line 1948: "CMP 109 Sec. 4 (Mayer convergence)."
This is outside the scope of the Wave 4 patch (which targets line 1628
only) but is the same pre-existing error. A future pass should align it
with the §3 correction.

**C4 result: PASS (patch correct; one further instance flagged for future
cleanup, not a defect in the patch itself).**

---

## Cross-node check

The two-sentence split in `H-balaban-analyticity.md` §3 Step (b) does not
affect Links 5 or 10. Link 5 (SL(N,ℂ) extension) relies on polar
decomposition and Cauchy estimates, independent of the Lemma 4 attribution.
Link 10 (non-pert dev ≥ 2) treats (B1) as a black box; the box is intact.
No cascade.

---

## Summary (≤150 words)

All four checks pass against the primary source. The §1 (1.2) and §2
eqs. 2.2–2.3 quotes are verbatim accurate. Lemma 4's scope is correctly
identified as the fluctuation-composition step, not the saddle-point center
— the two-sentence split fully resolves Wave 3 attack A3. The condition
count "(i)–(iv)" is confirmed at p. 262, resolving Wave 3 attack A2. The
Sec. 3 fix at line 1628 is correct; §4 is Ward-Takahashi identities, not
cluster activity analyticity. One additional uncorrected instance of the
same error appears at line 1948 of `05-continuum-limit.md` — not a defect
in the Wave 4 patch but flagged for a future cleanup pass. No logical gap
remains; no cascade to downstream nodes.

**Verdict: SURVIVED.**
