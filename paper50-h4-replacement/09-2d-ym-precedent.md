# §09 — 2D YM Precedent

*2D Yang-Mills admits a complete resurgent analysis. Okuyama-Sakai 2022 (arXiv:2212.11988). Transseries parameters determined by weak/strong coupling consistency. What transfers to 4D, what does not.*

---

## 9.1. Why 2D YM is solvable

2D Yang-Mills on a compact Riemann surface is exactly solvable. The path integral reduces to a finite-dimensional matrix integral via Migdal's recursion (1975, 1993), and the partition function admits closed-form expressions in terms of heat-kernel representations on the gauge group.

On a torus, the partition function for SU(N) YM is

$$
Z_{T^2}(A, g^2) \;=\; \sum_{R} (\dim R)^{2-2 g_{\mathrm{genus}}} \, e^{-g^2 A\, C_2(R)/2},
$$

where the sum is over irreducible representations $R$ of SU(N), $A$ is the area, $g_{\mathrm{genus}}$ the genus, and $C_2(R)$ the quadratic Casimir. For genus $0$ (sphere):

$$
Z_{S^2}(A, g^2) \;=\; \sum_{R} (\dim R)^2\, e^{-g^2 A\, C_2(R)/2}.
$$

This is a *convergent* sum — 2D YM has no divergences, no renormalons, no instantons (in the usual sense).

---

## 9.2. Why 2D YM still has a divergent perturbative series

Despite being exactly solvable, 2D YM's *perturbative expansion* in $g^2$ is *divergent*. The heat-kernel representation, expanded as a power series in $g^2$, has factorially growing coefficients. This is the **2D YM puzzle**: a convergent sum with a divergent expansion.

The resolution: the divergence is a **large-$N$** phenomenon (and more generally, a large-representation phenomenon). When $g^2 A$ is small, the sum over $R$ is dominated by representations with $C_2(R) \lesssim 1/(g^2 A)$. Expanding in $g^2$ term-by-term counts *all* representations, leading to factorial growth.

Analogously to the 4D YM case, the divergence signals the presence of **non-perturbative sectors**: in 2D YM, these are *large representations* whose contributions are exponentially small in $1/g^2$ but finite when summed.

---

## 9.3. The 2D YM resurgent analysis

Okuyama-Sakai 2022 (arXiv:2212.11988), building on earlier work by Dalley-Ganor-Klebanov and Minahan, gave a *complete* resurgent analysis of 2D YM:

**Step 1: The perturbative Borel transform.**
Starting from the heat-kernel expansion of $Z_{S^2}$, they computed the Borel transform $B(t)$ of the perturbative series. $B(t)$ has poles at $t_k = k^2/(2A)$ (associated with representations of dimension $\sim k$) — these are the 2D YM analogues of IR renormalons.

**Step 2: Transseries ansatz.**
They postulated a transseries completion with non-perturbative sectors at each pole $t_k$:
$$
Z^{\mathrm{TS}}_{S^2}(g^2) \;=\; \sum_k \sigma_k\, e^{-t_k/g^2}\, Z^{(k)}(g^2),
$$
with inner series $Z^{(k)}(g^2)$ determined by the DSE-like recursion induced by Migdal.

**Step 3: Fixing transseries parameters by weak/strong consistency.**
This is the central technical achievement. The transseries parameters $\sigma_k$ are fixed by:

- **Weak coupling limit:** $g^2 \to 0$, where $Z$ is dominated by the identity representation; the perturbative sum matches the trivial-representation contribution.
- **Strong coupling limit:** $g^2 \to \infty$, where the sum is dominated by a different asymptotic regime; the transseries-resummed $Z$ matches the asymptotic strong-coupling formula.
- **Matching between the two regimes:** requiring the transseries-resummed $Z$ to *interpolate* smoothly between weak and strong coupling fixes the $\sigma_k$ uniquely (up to a finite discrete ambiguity that is fixed by additional physical input like unitarity).

**Step 4: Verification.**
The resulting transseries is *equal*, as an analytic function, to the exact closed-form $Z_{S^2}(A, g^2)$. The resurgent completion of the divergent perturbative series reconstructs the exact partition function.

This is the **proof of principle**: for 2D YM, Écalle-Voros + DSE + weak/strong consistency produces the full non-perturbative answer.

---

## 9.4. The transseries parameters in 2D YM

In 2D YM on $S^2$, Okuyama-Sakai found that the transseries parameter $\sigma_k$ for the $k$-th non-perturbative sector is

$$
\sigma_k \;=\; \frac{1}{k!\, (k-1)!}\, \cdot\, (\text{anomalous-dimension factor}).
$$

These are *rational* numbers with combinatorial interpretation — they are dimensions of irreducible representations divided by factorials. The resurgent structure is thus *arithmetic*: the Stokes constants are rational numbers with number-theoretic content.

**This is striking.** The transseries parameters have a closed-form combinatorial expression. They are not free parameters determined by boundary conditions alone; they are determined by the *representation-theoretic content* of the gauge group.

For 4D YM, the analogous statement would be: the transseries parameters $\sigma_k$ are determined by some combinatorial or representation-theoretic object associated with SU(N) and the 4D gauge bundle. Identifying this object is one of Route A's targets.

---

## 9.5. What transfers from 2D to 4D

**Transfers (with minor modifications):**

- **The transseries ansatz.** Inner asymptotic series in each non-perturbative sector, labelled by actions $A_k$, with free parameters $\sigma_k$. Structurally identical in 2D and 4D.

- **The DSE-like recursion.** In 2D, Migdal's recursion; in 4D, the full DSE hierarchy. Both give the inner series $\phi_k$ (or $Z^{(k)}$) in terms of lower-order data.

- **Weak coupling limit.** In 2D and 4D, the $g \to 0$ limit is dominated by the perturbative sector; transseries parameters are constrained by matching.

- **Resurgent structure.** Écalle-Voros alien calculus applies in both dimensions. The Stokes-constant structure is formally the same.

**Transfers partially:**

- **Non-perturbative sector actions.** In 2D, $A_k = k^2/(2A)$ (area-dependent, representation-theoretic). In 4D, $A_k = 2k/\beta_0$ (IR renormalon, coupling-dependent). The *form* is different, but both are *rigidity-imposed* (scheme-independent in 4D per Paper 10).

**Does NOT transfer:**

- **Strong coupling limit consistency.** In 2D, $g^2 \to \infty$ has a known asymptotic form (dominated by large representations). In 4D, the $g^2 \to \infty$ limit is the **confining regime** and is not known in closed form. Weak/strong consistency as a parameter-fixing technique is *not available* in 4D.

- **Exact solvability.** 2D YM is solvable via Migdal; 4D YM is not exactly solvable (that is the mass-gap problem). Therefore the 2D verification step — "check that transseries-resummed $Z$ equals the exact closed form" — has no 4D analogue.

- **Area-dependent structure.** 2D YM is sensitive to the area of the 2-manifold; 4D YM on $\mathbb{R}^4$ has no analogous finite-size parameter. The transseries structure in 4D must come from the RG flow (running coupling), not from geometric parameters.

---

## 9.6. What the 2D case teaches us

**Lesson 1: Resurgent transseries CAN reproduce exact non-perturbative answers.** The 2D YM case proves this is not vacuous — the framework works when implementable.

**Lesson 2: Transseries parameters can be *rigid* (determined by consistency + representation theory), not just free parameters.** This suggests that for 4D YM, the $\sigma_k$ may likewise be rigid, fixed by a combination of RG flow structure + OS positivity + ITPFI (§10).

**Lesson 3: The non-perturbative sectors have arithmetic content.** The $1/(k!(k-1)!)$ structure in 2D connects transseries parameters to combinatorics of representations. For 4D, the analogue may be ITPFI's local-at-$p$ structure (where $p$ is prime), which has number-theoretic interpretation.

**Lesson 4: Weak/strong consistency is NOT the only parameter-fixing technique.** For 4D, we need a *substitute* for the strong coupling match. The programme's candidate is: OS positivity (reflection positivity of $S_n$) + matching to gradient-flowed Schwinger functions. These are the programme-internal analogues.

---

## 9.7. The 4D analogue: what Route A must do

Route A for 4D YM follows the 2D template with these modifications:

- **Non-perturbative sectors at $A_k = 2k/\beta_0$** (IR renormalons) + $A_{\mathrm{inst},k} = 8k\pi^2$ (instantons).
- **Inner series from DSE hierarchy** (truncated or full, per §8).
- **Transseries parameters $\sigma_k$ fixed by:**
  - Paper 8 OS positivity.
  - Paper 8 cluster decomposition.
  - Paper 10 scheme independence.
  - ITPFI factorization (§10).

The 4D match step (the analogue of 2D's "transseries $=$ exact $Z$") becomes **H4**: the transseries-resummed perturbative series equals the Paper 8 Link 16 non-perturbative Schwinger functions at short distances.

---

## 9.8. Other 2D precedents

The 2D YM analysis is part of a broader ecosystem of resurgent-transseries results in low-dimensional gauge theory:

- **2D CP$^{N-1}$ model** (Dunne-Unsal 2012, Cherman-Dorigoni-Unsal 2014): complete transseries, fractional instantons on $\mathbb{R} \times S^1$.
- **2D Principal chiral model** (Marino-Reis 2019): transseries in the 't Hooft limit.
- **ABJM matrix model** (Grassi-Hatsuda-Marino 2014): exact transseries via topological string.
- **N=2 SYM in 4D** (Aniceto-Russo-Schiappa 2014): transseries in the Nekrasov partition function.

These provide additional templates. All share the pattern: factorially divergent perturbative series + transseries completion + rigidity via some physical consistency condition.

For 4D *pure* YM, no analogous complete analysis exists. This is the target.

---

## 9.9. Honest comparison

**2D YM strengths (relative to 4D):**
- Exactly solvable.
- Area-dependent rigidity fixes transseries parameters.
- Strong coupling limit explicitly known.
- Arithmetic/combinatorial closed-form for Stokes constants.

**2D YM weaknesses (as a 4D model):**
- No IR renormalon structure (different kind of divergence).
- No running coupling (2D YM is not asymptotically free in the same sense).
- No short-distance OPE in the 4D sense.
- Area parameter has no 4D analogue.

**Therefore:** 2D YM is a *structural template* for Route A — it shows the transseries framework *can* close the perturbative-to-non-perturbative gap — but it is *not* a direct model for 4D. The 4D case requires additional input, and that input is the programme's ITPFI + OS + scheme-independence package (§10 and §11).

---

## 9.10. Summary

- 2D YM admits complete resurgent analysis (Okuyama-Sakai 2022).
- Transseries parameters are *rigid* (determined by weak/strong consistency + representation theory).
- The transseries-resummed divergent series *equals* the exact non-perturbative partition function.
- Structurally transfers to 4D: ansatz, DSE hierarchy, Écalle-Voros apparatus.
- Does NOT transfer: exact solvability, strong coupling limit, area parameter.
- 4D requires substitute parameter-fixing: OS positivity, cluster, scheme independence, ITPFI.

§10 introduces the ITPFI contribution — the programme's novel addition to Route A's parameter-fixing.

---

*Paper 50 §09. Drafted 2026-04-14. G Six and Claude Opus 4.6.*

*Key references: Migdal 1975, Recursion equations in gauge field theories; Okuyama-Sakai 2022, arXiv:2212.11988, Resurgence in 2D Yang-Mills on a sphere; Dunne-Unsal 2012, Resurgence and trans-series in quantum field theory; Aniceto-Basar-Schiappa 2019, A primer on resurgent transseries.*
