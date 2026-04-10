# Clay Millennium Prize Mandatory Checks

## C1: Compact simple gauge group $G$ — all, not just SU($N$)
**Status: PARTIAL**

The body of the paper proves the mass gap for SU($N$), $N \geq 2$. Appendix I.4 (Theorem I.4.1) extends the result to all compact simple Lie groups — SO($N$), Sp($N$), $G_2$, $F_4$, $E_6$, $E_7$, $E_8$ — via compact irreducible symmetric spaces as internal manifolds and the Weitzenböck–Bochner theorem. The extension is structurally sound but relies on the (unpublished) generalization of Balaban's UV stability from SU(2) to arbitrary groups. For SU($N$), the extension from SU(2) is argued in Section 5.1.2 and tracked in Appendix I.3. Limitation: the extension to exceptional groups depends on the universality of Balaban's construction, which is not separately published.

## C2: Non-trivial (not free/Gaussian)
**Status: PARTIAL**

The proof establishes a mass gap and string tension $\sigma > 0$ for an interacting lattice gauge theory. The theory is manifestly non-Gaussian at the lattice level (the Wilson action is non-quadratic). However, the paper does not explicitly verify that a connected 4-point function of the continuum theory is nonzero. This is closable in 1 paragraph (the connected 4-point function is $O(g^2) \neq 0$ by lattice perturbation theory, and $g$ does not vanish in the continuum limit by asymptotic freedom).

## C3: Axioms at least as strong as Wightman OR OS
**Status: PASS**

OS1 (temperedness), OS2 (Euclidean covariance — restored in the continuum limit), OS3 (reflection positivity — Osterwalder–Seiler at each $a$, preserved under weak limits), OS4 (symmetry — gauge invariance manifest), OS5 (clustering — from $\Delta_\infty > 0$) are all verified in Section 5.7(f). The 1975 corrected version of OS0' is used. The OS reconstruction theorem then gives a Wightman QFT.

Location: Section 5.7(f), with RP in Appendix D (Lemma D.2).

## C4: $\mathrm{spec}(H) \subseteq \{0\} \cup [\Delta, \infty)$, $\Delta > 0$ AND $m < \infty$
**Status: PASS (for $\Delta > 0$) / PARTIAL (for $m < \infty$)**

$\Delta_\infty > 0$ is the main result: established via the 14-step proof chain (PROOF-CHAIN IV.1). The finiteness condition $m < \infty$ (the spectrum above 0 is non-empty) requires showing the existence of a one-particle state of finite mass. This is related to C2 (non-triviality): a non-trivial interacting theory must have particles. The glueball $0^{++}$ state is identified at $\sim 1.5$ GeV by comparison with lattice QCD, but this is a numerical prediction, not a rigorous proof of $m < \infty$. A rigorous proof would follow from the non-triviality of the connected 4-point function (C2 gap).

## C5: No weak-existence-only solution
**Status: PASS**

The proof does not merely assert the existence of a weak limit. It propagates the mass gap and OS axioms through the limit via explicit bounds (the RG recursion gives $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$ by convergent sums, not by compactness alone). The Schwinger functions of the limit satisfy OS1–OS5 by the bounds established at each lattice spacing, not by extraction from a hypothetical limit.

Location: Section 5.7, assembly of Theorem 8.

## C6: Local gauge-invariant field operators in correspondence with $\mathrm{Tr}\,F_{ij}F_{kl}$
**Status: FAIL**

Not addressed. The paper constructs Schwinger functions of gauge-invariant observables (Wilson loops, plaquette traces) but does not construct local field operators $\mathrm{Tr}\,F_{ij}F_{kl}(x)$ as operator-valued distributions on the reconstructed Hilbert space. Acknowledged as Conjecture L.1 in Appendix L.

## C7: Short-distance match to perturbative AF
**Status: FAIL**

Not addressed. The two-point function is not checked against the perturbative AF prediction at short distances. Acknowledged as Conjecture L.2 in Appendix L.

## C8: Stress tensor exists
**Status: FAIL**

Not constructed. The gauge-invariant improved stress tensor $T_{\mu\nu}$ requires renormalized composite operators. Acknowledged as Conjecture L.3 in Appendix L.

## C9: Operator product expansion with prescribed singularities
**Status: FAIL**

Not established. Acknowledged as Conjecture L.4 in Appendix L.

## C10: RP preserved or recovered through every regularization step
**Status: PASS**

Lattice RP: Osterwalder–Seiler theorem (Lemma D.2) for the Wilson + KK action. The KK enhancement preserves the checkerboard decomposition. Through Balaban's RG: RP is not required at intermediate steps. Continuum limit: RP preserved by lower semicontinuity (Portmanteau theorem). The chain is complete.

Location: Appendix D (Lemma D.2), Section 5.7(f) OS3.

## C11: $\mathbb{T}^4 \to \mathbb{R}^4$ with volume-uniform mass gap
**Status: PASS (with minor gap)**

The mass gap is shown uniform in $L$ at each lattice spacing (cluster expansion, Theorem 4(c)). The double limit $a \to 0, L \to \infty$ is handled via Moore–Osgood (Section 5.7(e)), with volume independence of connected matrix elements established via Hastings–Koma clustering. Minor gap: the uniformity in $a$ of the $L$-convergence rate should be stated more explicitly as a consequence of the $a$-independent physical mass gap.

Location: Section 5.7(e), Section 5.5.3 Step 3(i).
