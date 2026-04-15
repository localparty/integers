# Summary: Hostile Referee Report on the Yang–Mills Mass Gap Preprint

**Cycle:** notation-math-referee, single run
**Posture:** Skeptical. Burden of proof on the authors. "Plausible" is not "proved."

This run was tasked specifically with auditing the K-vs-k notation convention (per the script's CRITICAL section) in addition to the standard hostile review of Points A1–G4.

---

## Verdicts at a Glance

| Point | Title | Verdict |
|:------|:------|:--------|
| A1 | Weitzenböck spectral gap | CLOSABLE GAP |
| A2 | KK propagator bound | SOUND |
| A3 | Bogomolny bound on lattice | CLOSABLE GAP |
| B1 | Cluster expansion convergence | SOUND |
| B2 | Fredenhagen–Marcu | CLOSABLE GAP |
| B3 | IR equivalence / Feshbach | SOUND |
| C1 | Balaban UV stability scope | **GENUINE GAP** (K-vs-k) |
| C2 | Large/small field decomposition | CLOSABLE GAP |
| C3 | Coupling regime overlap | GENUINE GAP (consequence of C1) |
| D1 | Dimension-6 classification | SOUND |
| D2 | Stability of deviation order | SOUND |
| D3 | Spectral lemma | SOUND (with one closable technical gap) |
| D4 | Single-step bound | SOUND |
| E1 | Inductive stability | **GENUINE GAP** (consequence of C1) |
| E2 | Convergence of sum | **GENUINE GAP** (consequence of C1) |
| F1 | OS axioms simultaneity | SOUND/CLOSABLE |
| F2 | Reflection positivity chain | SOUND |
| F3 | Thermodynamic limit | CLOSABLE GAP (conditional on C1) |
| F4 | Uniqueness of continuum limit | SOUND (correctly hedged) |
| F5 | OS reconstruction → Wightman | PARTIAL (non-triviality argument has logic hole; field operators issue) |
| G1 | Jaffe–Witten requirements | **GENUINE GAP** (scope: only SU(N) actually proved) |
| G2 | Gauge invariance through RG | SOUND |
| G3 | $N$-dependence | SOUND for fixed $N$ (conditional on C1) |
| G4 | Local field operators, stress tensor, OPE, AF matching | **GENUINE GAP** (4 missing/partial Clay requirements) |

**Notation convention audit:** FAIL (cross-checks 1, 2, 4, 6); PARTIAL (3, 5). See `notation-convention.md`.

**Clay C1–C11 checklist:** 1 PASS, 5 PARTIAL, 5 FAIL. See `clay-checklist.md`.

---

## Overall Assessment

### Is the claimed result proved?

**No, and here are the specific gaps.**

The preprint makes two distinct claims:
1. **Mass gap of SU(N) Wilson lattice gauge theory in the continuum limit** ($\Delta_\infty > 0$).
2. **Clay Millennium Prize-eligible Yang–Mills existence and mass gap proof.**

**For claim (1):** the proof is *structurally* in place but has a *literally fatal* notation issue in §5.4 (Point C1, E1, E2). The "$1/4$ contraction" in the recursion §5.4.5 and the "$\hat\Delta_k^2 \sim 4^{-k}$" in §5.4.6 require *opposite* conventions for the index $k$ in §5.1.2 / §5.4.1. As written, the convergence sum diverges under the convention of §5.4.1; it converges only under a different (refining) convention that the proof never declares. The intended structural reading — the script's $K$ for bare-refinement vs. $k$ for Balaban inner — is mathematically sound, but the preprint conflates the two indices throughout. Computational verification: the §5.4.1 convention gives $\sum k^{\gamma-2} \cdot 4^{+k}$ (divergent, ratio test = 4); the bare-refinement convention gives $\sum K^{\gamma-2} \cdot 4^{-K}$ (convergent, ratio test = 1/4).

**Closing the K-vs-k issue is a notation cleanup of about 1 page**, but it requires *also* establishing that the inner Balaban RG within each bare theory delivers a $K$-uniform form factor — a step that Balaban himself did not perform and that the preprint papers over by conflating the two indices. **This is potentially a 1-paper-worth of additional rigorous work.**

**For claim (2):** the proof addresses *roughly half* of the Clay requirements. Even granted the mass gap, the J–W statement explicitly requires:
- Local quantum field operators in correspondence with curvature polynomials (FAIL — only Schwinger functions of bare lattice observables, no renormalized operators).
- Short-distance match to perturbative AF (FAIL — only the free $|x|^{-2}$ singularity, no AF logarithmic running).
- Stress tensor (FAIL — not even mentioned).
- Operator product expansion with prescribed AF singularities (FAIL — asserted, not derived).
- All compact simple gauge groups (FAIL — only SU(N) treated; $G_2, F_4, E_6, E_7, E_8$ sketched in Appendix K but not executed).

**These are not minor cosmetic gaps.** Each is a structural Clay requirement that has not been addressed. Total estimated additional work to meet the full Clay requirement: **3–5 papers**, in addition to the K-vs-k cleanup.

### Clay Prize Eligibility

**Would this proof, as written, survive review by the Clay Scientific Advisory Board?**

**No.** The Clay SAB would identify the K-vs-k notation issue immediately (a referee with experience in Balaban's CMP series will catch the §5.4.1 vs §5.4.6 contradiction on a first reading), and the absence of local field operators / stress tensor / OPE / AF matching would be flagged as not addressing the Jaffe–Witten statement. The proof would be returned for "major revisions" with the recommendation to:

1. Resolve the K-vs-k notation collision and re-derive the convergence sum cleanly.
2. Construct renormalized local field operators and verify their short-distance AF behavior.
3. Construct the stress tensor.
4. Establish (at least the leading) OPE for gauge-invariant composite operators.
5. Either complete the proof for all compact simple gauge groups or restrict the claim to SU(N).

After items 1–5, the result would be a substantive contribution but might still face challenges (e.g., the SU(2) case uses a different construction in Appendix H that does not obviously match the SU(N) framework; the proof's "starting condition" via cluster expansion lives at a coarse scale that is conceptually orthogonal to the continuum-limit direction).

### The three most critical issues (ranked)

1. **K-vs-k notation collision in §5.4 (Point C1, E1, E2).** The proof's central convergence claim "$\hat\Delta_k^2 \sim 4^{-k}$ so $\sum$ converges doubly exponentially" is *contradicted* by the §5.4.1 setup "$a_{k+1} = 2 a_k$, $\hat\Delta_{k+1} = 2\hat\Delta_k$" which gives $\hat\Delta_k^2 \sim 4^{+k}$ and a *divergent* sum. The two conventions are conflated under a single letter $k$, and the resolution requires the script's $K$/$k$ separation that the preprint never makes.

2. **Missing Jaffe–Witten structural ingredients (Point G4).** The Clay statement requires local field operators, stress tensor, OPE, and short-distance AF matching. The proof provides Schwinger functions but does not construct renormalized composite operators, does not construct a stress tensor, does not establish an OPE, and does not match short-distance correlators to AF predictions. These are direct structural failures of the Clay requirement.

3. **Scope: "any compact simple G" is overstated (Point G1, C1).** The full proof is for SU(N) only. Appendix I.4 + K sketch the extension to SO(N), Sp(N), and the exceptionals but do not execute it. The abstract and §1 claim "for any compact simple gauge group $G$" — this is incorrect as written. For Clay, this is binding: the J–W problem statement asks for *all* compact simple groups.

### What would make this a complete, prize-eligible proof

**Step 1 (K-vs-k cleanup, ~1 page):** Adopt the script's $K$/$k$ separation explicitly. Restate §5.4 as a recursion comparing form factors of bare theories at consecutive bare scales, with each bare theory's UV stability handled by Balaban's inner RG.

**Step 2 (inner RG K-uniformity, ~1 paper):** Prove that within each bare theory $K$, Balaban's inner RG delivers a form factor whose constant is bounded uniformly in $K$. This is the genuinely non-trivial step that is currently obscured by the notation conflation.

**Step 3 (renormalized composite operators, ~1 paper):** Construct renormalized $\mathrm{Tr}\,F^2$, $\mathrm{Tr}\,F\tilde F$, etc. as operator-valued distributions on the GNS space, with multiplicative renormalization $Z_O(a)$ chosen to absorb the lattice UV divergence. Verify the short-distance AF behavior matches perturbative QCD.

**Step 4 (stress tensor, ~1 paper):** Construct the gauge-invariant Belinfante–Rosenfeld stress tensor on the GNS space and verify its conservation as a distributional identity. Verify the energy positivity $T_{00} \geq 0$.

**Step 5 (OPE, ~1 paper or more):** Establish at least the leading OPE for two curvature operators, with coefficients computed perturbatively (one-loop) and matched to AF predictions.

**Step 6 (gauge group extension, ~1 paper):** Execute the proof for SO(N), Sp(N), $G_2, F_4, E_6, E_7, E_8$ (or restrict the Clay claim to SU(N)). Appendix K sketches the structure; the actual computations of cluster-expansion constants, dimension-6 operator classifications, and Balaban analyticity radii for the exceptional groups need to be done.

**Total additional rigorous work: 5–6 papers worth, plus the notation cleanup.** This is not "minor revisions"; it is a substantive multi-year program.

---

## Reluctant Concessions

Having scrutinized the proof with maximal skepticism, I do make the following concessions to the preprint:

1. **The dimension-6 classification (Point D1) and stability of deviation order (Point D2) are sound.** The proof's central technical innovation — using the universal Lüscher–Weisz operator basis to bypass the failure of perturbative splitting — is mathematically valid. The previous referees (r05, r06) correctly identified this as the proof's main contribution.

2. **Theorem 5 (IR equivalence, Point B3) is a complete rigorous proof, not a sketch.** The Feshbach + Weyl–Kato + reduced transfer matrix argument works.

3. **The cluster expansion (Point B1) gives $\Delta_0 > 0$ at any fixed coarse lattice spacing.** The Kotecký–Preiss criterion is verified correctly and the polymer combinatorics on $\mathbb{Z}^4$ are sound (modulo the N-dependence corrections from A1).

4. **Reflection positivity (Point F2) is preserved through the construction.** OS / Bochner / Portmanteau give RP at the lattice level, the KK enhancement preserves it, and the continuum limit inherits it via weak limits.

5. **The handling of the §6.6 footnote 2 caution (Point F4) is correct in principle.** The proof uses Banach–Alaoglu but combines it with the RG telescoping to establish properties of *the specific limit constructed*, not just of "some weak limit." This is the right strategy for the Clay footnote.

6. **The previous referee gaps from r05 (Point 1d, Point 2c) have been addressed.** The current preprint's spectral lemma includes the explicit two-particle threshold argument, and the dimension-6 classification's second two-derivative operator is now verified explicitly.

These concessions notwithstanding, the **structural** problems (K-vs-k notation, missing Clay ingredients) outweigh the technical successes.

---

## What I Could Not Break

Despite sustained effort, I could not find a *direct* mathematical error in the dimension-6 classification (Point D1, D2) or in the spectral lemma's deviation extraction (Point D3 modulo the locality radius issue). These are the proof's main technical innovations and they appear to be correct as stated.

The §6.6 footnote 2 handling (Point F4) is also correct: the proof's claim is appropriately hedged ("we do not claim uniqueness, only that every subsequential limit has the gap"), and the strategy of establishing subsequence-independence of $\Delta_\infty = C_\infty \cdot \Lambda_\infty$ through the RG flow is valid in principle.

**I could not find a way to rescue the K-vs-k notation collision** without rewriting §5.4 from scratch. Any attempt to interpret the §5.4.1 setup ($a_k = 2^k a_0$, $\hat\Delta_{k+1} = 2 \hat\Delta_k$) as compatible with §5.4.6's $\hat\Delta_k^2 \sim 4^{-k}$ leads to a literal contradiction, verified computationally.

**I could not find a way to declare G4 (local fields, stress tensor, OPE, AF matching) "closable"** without invoking 3–5 papers worth of additional constructive QFT — and that program (renormalized composite operators in non-Abelian gauge theory in 4D) is a known open problem in mathematical physics.

---

## Tools added during this run

None. The default `code/requirements.txt` packages (sympy, mpmath, numpy, scipy, networkx, pypdf) sufficed for all computational verifications.

## Computational verifications performed

| Check | Tool | Result |
|:------|:-----|:-------|
| Ricci coefficient $2N/r_3^2$ on $\mathbb{CP}^{N-1}$ | sympy | Confirmed for $N=2,\ldots,8$; preprint's $6/r_3^2$ correct only for $N=3$ |
| KK mass $m_1 = 2\sqrt{N}/r_3$ vs claimed $2\sqrt{3}/r_3$ | sympy | $2\sqrt{3}$ is N=3-specific; off by 18% for $N=2$, 15% for $N=4$, 29% for $N=5$ |
| Spectral lemma exponent $g^4 \leq 1/(4 C_B) \Leftrightarrow g^2 \leq 1/(2\sqrt{C_B})$ | sympy | Equivalent (algebraic identity) |
| Haar integral $\int (\mathrm{Re}\,\mathrm{Tr}\,U)^2 dU$ | analytical | $1/2$ for $N \geq 3$, $1$ for $N=2$ — agrees with preprint line 2661 |
| Lie algebra constants for SU(N), SO(N), Sp(N), $G_2, F_4, E_{6,7,8}$ | standard tables | All finite; preprint Appendix I.4/K identifies them correctly |
| RG sum $\sum k^{\gamma-2} \cdot 4^{-k}$ vs $\sum k^{\gamma-2} \cdot 4^{+k}$ | sympy + numerical | First convergent (ratio test 1/4), second divergent (ratio test 4); the §5.4.1 convention gives the *divergent* sum, contradicting §5.4.6's claimed convergence |

All computations verified in `code/.venv` (sympy 1.14.0, mpmath 1.3.0, numpy 2.4.4).
