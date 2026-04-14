# §11 — Route A Proof Sketch

*Step-by-step: Wilson-loop perturbative expansion → lateral Borel sum → ITPFI-rigidified transseries → non-perturbative Schwinger function match. Specific obstructions named. What additional research is needed to close.*

---

## 11.1. Target statement

**Route A conclusion (what the sketch aims to prove).** *For any gauge-invariant observable $\mathcal{O}$ of mass dimension $d$ in 4D SU(N) YM on $\mathbb{R}^4$, the perturbative series $\mathcal{O}_{\mathrm{PT}}(g)$ admits a resurgent transseries completion $\mathcal{O}_{\mathrm{TS}}(g)$ such that*
$$
\mathcal{O}_{\mathrm{TS}}(g(\mu)) \;=\; \mathcal{O}^{\mathrm{NP}}(\mu) \quad \text{as } \mu \to \infty,
$$
*in the sense of Poincaré asymptotics, where $\mathcal{O}^{\mathrm{NP}}$ is the non-perturbative observable reconstructed from Paper 8 Links 15-17 (gradient-flow + OS).*

This is precisely H4 specialized to the short-distance regime. Proving it for all $\mathcal{O}$ of interest — specifically, the multi-point Schwinger functions $S_n$ — gives H4.

---

## 11.2. Step 1: The perturbative series (PROVED, unconditional)

**Input:** Paper 10 + Paper 11 K.4 gives the canonical scheme + all-orders perturbative coefficients $a_n$ for every gauge-invariant observable.

**Output:** Well-defined formal power series $\mathcal{O}_{\mathrm{PT}}(g) = \sum a_n g^{2n}$ with explicit scheme-independent content.

**Status:** PROVED. Follows from Paper 10 scheme-independence theorem + Paper 11 all-orders construction. Unconditional.

---

## 11.3. Step 2: The Borel transform and its singularities (PARTIAL)

**Input:** Perturbative coefficients $a_n$ from Step 1.

**Output (desired):** Borel transform $B(t) = \sum (a_n/n!) t^n$ with:
- Positive radius of convergence $\rho = 1/(2\beta_0)$ (IR renormalon at $t_1 = 2/\beta_0$).
- Meromorphic continuation to a neighbourhood of $\mathbb{R}_+$ with singularities at $\{t_k = 2k/\beta_0\} \cup \{t_{\mathrm{inst},k} = 8k\pi^2\}$.
- Controlled growth along rays $e^{i\theta}$ for $\theta \neq 0$.

**Status:**
- **Radius $\rho = 1/(2\beta_0)$:** PROVED (Lipatov analysis + Paper 10 scheme-independent $\beta_0$).
- **Singularities at $t_k$, $t_{\mathrm{inst},k}$:** PARTIAL. The IR renormalon positions are established (Parisi 1978, Mueller 1985); the existence of meromorphic continuation is conjectured but not proved rigorously for 4D YM.
- **Controlled growth along rays:** OPEN. Requires bounds on the Borel transform in sectors, which in turn require estimates on Feynman integrals at all orders.

**Obstruction:** proving meromorphic continuation of $B(t)$ requires either a closed-form expression (available only in low dimensions / truncated models) or a uniform bound on the perturbative tail. Neither is currently available for 4D YM.

**Route A partial progress available:** Klaczynski 2016 provides the framework for computing $B(t)$ in truncated DSE; for full 4D YM, only heuristic bounds exist.

---

## 11.4. Step 3: Lateral Borel sums (CONJECTURAL)

**Input:** Borel transform $B(t)$ with identified singularities.

**Output (desired):** Lateral Borel sums
$$
f_\pm(g) \;:=\; \int_0^{\infty \cdot e^{\pm i\epsilon}} e^{-t/g^2}\, B(t)\, \frac{dt}{g^2}
$$
defined as sectorial analytic functions on neighbourhoods of $\mathbb{R}_+$ in the $g^2$-plane.

**Status:** CONJECTURAL. Given Step 2's output, the lateral sums *should* exist by Écalle-Voros's general theorem, but the specific application to 4D YM requires:

- Bounds on $B(t)$ in sectors $\{|\arg t| < \pi/2 - \delta\}$.
- Verification of the Laplace-growth condition.
- Control of the singularity structure at infinity (essential singularity vs. branch point at $t = \infty$).

**Obstruction:** these are technical analytic bounds that have not been proved for 4D YM. The 2D YM case (§9) proves they are achievable when the underlying theory is solvable; 4D is not solvable.

---

## 11.5. Step 4: Transseries ansatz (FRAMEWORK AVAILABLE)

**Input:** Lateral Borel sums $f_\pm(g)$ + identified singularity structure.

**Output (desired):** Transseries ansatz
$$
\mathcal{O}_{\mathrm{TS}}(g) \;=\; f_+(g) \;+\; \sum_{k \geq 1} \sigma_k\, e^{-t_k/g^2}\, \phi_k(g) \;+\; \sum_{k \geq 1} \tau_k\, e^{-t_{\mathrm{inst},k}/g^2}\, \psi_k(g),
$$
with inner series $\phi_k$, $\psi_k$ determined by the DSE hierarchy (§8), and free parameters $\{\sigma_k, \tau_k\}$.

**Status:** FRAMEWORK AVAILABLE. The transseries ansatz is a well-defined formal object given Steps 1-3. The inner series $\phi_k$, $\psi_k$ can be computed (in principle) from the DSE hierarchy or from Lipatov-style saddle-point analyses.

**No fundamental obstruction at this step** — the ansatz is a formal writing-down. The substance is in Steps 5-7 (fixing parameters + verifying convergence + matching).

---

## 11.6. Step 5: Fixing transseries parameters via ITPFI (NOVEL)

**Input:** Transseries ansatz from Step 4.

**Output (desired):** Unique values for $\{\sigma_k, \tau_k\}$ from ITPFI-rigidified parameter fixing (§10).

**Mechanism:**
1. Assume the scale-local ITPFI factorization of the 4D YM vacuum.
2. Decompose each $\sigma_k$ as a product $\sigma_k = \prod_{\mu_j} \sigma_k^{(\mu_j)}$ over scales.
3. Compute each local $\sigma_k^{(\mu_j)}$ from local data (running coupling at $\mu_j$, anomalous dimensions at $\mu_j$, type III$_{\lambda(\mu_j)}$ parameter).
4. The product over scales gives $\sigma_k$ as a specific number.

**Status:** NOVEL. This is Paper 50 §10's original proposal. Three open technical components:

- **Open 1:** Prove the scale-local ITPFI factorization of 4D YM vacuum.
- **Open 2:** Prove the parameter-factorization identity $\sigma_k = \prod \sigma_k^{(\mu_j)}$.
- **Open 3:** Derive the local parameter formula $\sigma_k^{(\mu_j)} = \lambda(\mu_j)^k \chi_k(\mu_j)$.

**Obstruction:** all three opens. Each requires substantial technical work at the intersection of operator algebras and QFT perturbation theory.

**Additional constraints as cross-checks:**
- OS positivity of the resulting $\mathcal{O}_{\mathrm{TS}}$.
- Cluster decomposition.
- Scheme independence consistency (Paper 10).

If ITPFI-derived $\sigma_k$ satisfy these cross-checks, the parameter-fixing is self-consistent.

---

## 11.7. Step 6: Convergence / well-definedness of $\mathcal{O}_{\mathrm{TS}}$ (CONJECTURAL)

**Input:** Transseries ansatz with parameters fixed from Step 5.

**Output (desired):** $\mathcal{O}_{\mathrm{TS}}(g)$ is a genuine analytic function in a sector of the $g^2$-plane, not merely a formal expression.

**Mechanism:**
1. The perturbative piece $f_+(g)$ is already an analytic function by Step 3.
2. Each non-perturbative sector contribution $\sigma_k e^{-t_k/g^2} \phi_k(g)$ is analytic (exponentially small in $1/g^2$ + analytic $\phi_k$).
3. The sum over $k$ converges provided the coefficients $\sigma_k$ have sufficiently rapid decay.

**Status:** CONJECTURAL. Convergence of the full transseries requires bounds on $\sigma_k$ as $k \to \infty$. From the ITPFI ansatz ($\sigma_k \sim \lambda^k$ local times global product), the decay should be rapid enough for convergence in a sector, but this is not yet proved.

**Obstruction:** analytic estimates on the transseries tail. Technical; in principle tractable once Step 5 is settled.

---

## 11.8. Step 7: Matching to the non-perturbative Schwinger function (THE GOAL)

**Input:** Analytic $\mathcal{O}_{\mathrm{TS}}(g)$ from Steps 1-6.

**Output (desired):** $\mathcal{O}_{\mathrm{TS}}(g(\mu))$ equals $\mathcal{O}^{\mathrm{NP}}(\mu)$ (from Paper 8 Link 17) as $\mu \to \infty$, in the Poincaré asymptotic sense.

**Mechanism:**
1. At $\mu \to \infty$, $g(\mu) \to 0$ (asymptotic freedom, Paper 10).
2. The transseries $\mathcal{O}_{\mathrm{TS}}(g)$ reduces to the perturbative sum in the $g \to 0$ limit; non-perturbative sectors are exponentially suppressed.
3. By construction (Step 5 cross-checks), $\mathcal{O}_{\mathrm{TS}}$ is OS-positive and cluster-decomposition-respecting, so it can be identified with an OS-reconstruction-compatible distribution.
4. By uniqueness of OS reconstruction (given the distribution + Schwinger functions), $\mathcal{O}_{\mathrm{TS}} = \mathcal{O}^{\mathrm{NP}}$.

**Status:** FOLLOWS (conditionally). Given Steps 1-6, the match in Step 7 follows by:
- Asymptotic freedom (PROVED, Paper 10).
- OS uniqueness theorem (CLASSICAL, Glimm-Jaffe 1987 + Summers 2012).
- The transseries construction itself.

**No NEW obstruction at Step 7** beyond the ones accumulated in Steps 1-6.

---

## 11.9. The full sketch, compressed

$$
\begin{array}{rcl}
\text{Paper 10 + 11 K.4} & \longrightarrow & \mathcal{O}_{\mathrm{PT}}(g) = \sum a_n g^{2n} \\
& \longrightarrow & B(t) = \sum (a_n/n!) t^n \quad \text{[Step 1-2]} \\
\text{IR renormalons at } t_k & \longrightarrow & B(t) \text{ meromorphic, sectorial bounds} \quad \text{[Step 3]} \\
\text{Lateral Borel} & \longrightarrow & f_+(g) \text{ analytic} \quad \text{[Step 3]} \\
\text{Klaczynski + Lipatov} & \longrightarrow & \text{transseries ansatz} \quad \text{[Step 4]} \\
\text{§10 ITPFI + OS + cluster + scheme indep.} & \longrightarrow & \sigma_k, \tau_k \text{ fixed} \quad \text{[Step 5]} \\
\text{Tail bounds} & \longrightarrow & \mathcal{O}_{\mathrm{TS}}(g) \text{ analytic} \quad \text{[Step 6]} \\
\text{Paper 10 AF + OS uniqueness} & \longrightarrow & \mathcal{O}_{\mathrm{TS}} = \mathcal{O}^{\mathrm{NP}} \text{ as } \mu \to \infty \quad \text{[Step 7]} \\
& \longrightarrow & \text{H4 proved (Route A)}.
\end{array}
$$

---

## 11.10. Obstructions named

In summary, Route A's specific open problems:

| Obstruction | Step | Severity |
|---|---|---|
| Meromorphic continuation of $B(t)$ for 4D YM | Step 2 | HIGH |
| Sectorial bounds on $B(t)$ | Step 3 | HIGH |
| Scale-local ITPFI factorization of 4D YM vacuum | Step 5 (Open 1) | HIGH (novel) |
| Parameter-factorization identity $\sigma_k = \prod \sigma_k^{(\mu_j)}$ | Step 5 (Open 2) | MEDIUM |
| Local parameter formula $\sigma_k^{(\mu_j)} = \lambda^k \chi_k$ | Step 5 (Open 3) | MEDIUM |
| Transseries tail convergence | Step 6 | MEDIUM |
| OS positivity of $\mathcal{O}_{\mathrm{TS}}$ | Step 5 cross-check | MEDIUM |
| Asymptotic freedom limit Step 7 | Step 7 | LOW (mostly follows from Paper 10) |

The HIGH-severity items are concentrated in Steps 2-3 (analytic structure of $B(t)$) and Step 5 (ITPFI novelty). These are the main research content of Route A.

---

## 11.11. What additional research is needed

To close Route A:

**Research 1: Analytic structure of $B(t)$ for 4D YM.**
Extend Klaczynski's truncated DSE analysis to full 4D YM. This requires either (a) a closed-form resummation of the bubble-chain diagrams, or (b) uniform bounds on Feynman integrals + a non-trivial resummation argument. Neither is available; both are open problems of serious difficulty (estimated 12-24 months of dedicated research).

**Research 2: Scale-local ITPFI factorization of 4D YM vacuum.**
Rigorous proof that the 4D YM vacuum algebra factorizes as a tensor product over scales. This builds on Paper 29 type III$_1$ classification and Paper 10 scheme independence. Estimated 6-12 months.

**Research 3: ITPFI-transseries parameter formula.**
Derive $\sigma_k^{(\mu_j)}$ as a function of local data (coupling, anomalous dimensions, type III$_\lambda$ parameter). Compute specific $k=1, 2$ cases to verify consistency with known YM phenomenology (gluon condensate scale, confinement scale). Estimated 6-12 months.

**Research 4: Integration + verification.**
Assemble Steps 1-7 into a complete proof. Verify the OS-positivity cross-check. Match to lattice QCD Schwinger functions at short distances numerically (Paper 50 §34 verification). Estimated 6-12 months after Research 1-3.

**Total estimated timeline:** 24-48 months for full Route A closure. Parallel effort on Routes B and C may close H4 sooner if their obstructions are less severe.

---

## 11.12. Honest confidence assessment

**Route A pre-§10 (external resurgence machinery alone):** 2-3/10 confidence. The 2D YM template exists; 4D has too many free parameters and no weak/strong consistency analogue.

**Route A with §10 ITPFI contribution:** 3-4/10 confidence. The ITPFI proposal is novel and plausible; if it holds, it rigidifies the transseries sufficiently to close H4. But the proposal itself is not yet proved.

**Route A with all four research items closed:** 7-8/10 confidence, ceiling around 8.5/10 (the match of transseries to OS-reconstructed Schwinger functions is classical QFT once the transseries is well-defined).

**Route A compared to B and C:** comparable. Route B has stronger external support (Kim-Sarnak) but the S-duality identification is novel; Route C has a PROVED geometric Langlands (Gaitsgory-Raskin 2024) but the scale bridge is delicate. No route is clearly stronger.

---

## 11.13. Next steps for Route A

Concrete actionable items:

1. **Formalize §10's ITPFI-transseries proposal** as an explicit conjecture with computable consequences (e.g., predict $\sigma_1$ in terms of $\beta_0$ and the gluon condensate value).
2. **Compute in 2D YM using the ITPFI lens** — does the scale-local ITPFI structure (if defined for 2D YM on $S^2$) reproduce the Okuyama-Sakai transseries parameters $\sigma_k = 1/(k!(k-1)!)$? If yes, that would be strong evidence.
3. **Truncated 4D DSE + ITPFI:** combine Klaczynski's truncation with the ITPFI ansatz. Extract predictions.
4. **Comparison with lattice QCD:** match against lattice-computed short-distance Schwinger functions to test the transseries-resummed perturbative series.
5. **Route coordination:** track Routes B and C; if one closes first, Route A becomes verification rather than primary proof.

---

## 11.14. Summary

Route A's proof sketch has seven steps. Steps 1-2 have unconditional / partial foundations (Paper 10 + Paper 11 K.4). Steps 3-4 are framework-level (Écalle-Voros + Klaczynski). Step 5 contains the programme's novel contribution (§10 ITPFI) and also the most severe open problems. Steps 6-7 follow conditionally from Step 5.

**Route A's central technical task:** close the three Open components of §10 (ITPFI factorization + parameter factorization + local parameter formula). This is the critical path.

**Route A's timeline:** 24-48 months. Parallel to Routes B and C.

**Route A's confidence:** 3-4/10 initial, 7-8/10 if all opens close, with H4 as the output.

---

*Paper 50 §11. Drafted 2026-04-14. G Six and Claude Opus 4.6.*

*End of Part II (Route A — Resurgent Transseries). Part III (§§12-17) develops Route B (Kim-Sarnak-Shahidi via S-duality).*
