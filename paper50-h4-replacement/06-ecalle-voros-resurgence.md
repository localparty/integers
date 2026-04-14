# §06 — Écalle-Voros Resurgence Basics

*Classical resurgence theory. Transseries, alien calculus, Stokes phenomena. The "asymptotic series → non-perturbative completion" mechanism. Framework for Route A.*

---

## 6.1. The resurgence viewpoint

Resurgence is a mathematical framework, developed by Écalle (1981) and independently by Voros (1983), for recovering non-perturbative information from a divergent asymptotic series. The central claim: for a wide class of analytic problems (ODEs with irregular singular points, difference equations, functional equations arising in dynamical systems and QFT), the asymptotic expansion *encodes* the full non-perturbative answer, and a systematic procedure — the *transseries completion* + *alien calculus* + *Stokes automorphism* — reconstructs the answer.

The heuristic statement: "the divergence *is* the non-perturbative content." The factorial growth of the perturbative coefficients reflects the presence of additional saddle points in the path integral; these saddles contribute exponentially small terms that are invisible to the perturbative expansion but *recoverable* from it.

---

## 6.2. Asymptotic series and Borel summation: the baseline

An asymptotic series $\sum_{n \geq 0} a_n z^n$ represents a function $f(z)$ as $z \to 0^+$ in the Poincaré sense: for every $N$,

$$
\left| f(z) - \sum_{n=0}^{N} a_n z^n \right| \;\leq\; C_N\, |z|^{N+1}.
$$

The series generally diverges — it does not converge to $f$, it only approximates $f$ at small $z$. If $|a_n| \sim M^n n!$, the series has zero radius of convergence, and the constant $M$ is a non-perturbative action: the Borel transform

$$
B(t) \;:=\; \sum_{n \geq 0} \frac{a_n}{n!}\, t^n
$$

has radius of convergence $1/M$, and $B(t)$ has a singularity at $t = 1/M$ (or more generally, at $t = A$ for various singular actions $A$).

**Ordinary Borel summation** recovers $f(z)$ from the Borel transform:

$$
f(z) \;=\; \int_0^\infty e^{-t/z}\, B(t)\, \frac{dt}{z}.
$$

This works when $B(t)$ extends analytically along $\mathbb{R}_+$ without singularities on the positive real axis.

**When $B(t)$ has singularities on $\mathbb{R}_+$** — as it does for 4D YM (§§03, 07) — ordinary Borel summation fails. The resurgence program steps in.

---

## 6.3. Transseries: the general form

A **transseries** is a formal object

$$
\widetilde{f}(z) \;=\; \sum_{n=0}^{N} \sigma_n \, e^{-A_n/z}\, z^{\alpha_n}\, \phi_n(z),
$$

where:
- $A_0 = 0$ (perturbative sector), $A_n > 0$ ordered increasing for $n \geq 1$ (non-perturbative sectors).
- $\sigma_n \in \mathbb{C}$ are **transseries parameters** (free a priori; fixed by consistency).
- $\alpha_n \in \mathbb{C}$ are power-law exponents.
- $\phi_n(z)$ are themselves asymptotic power series in $z$.

The transseries encodes *perturbative + non-perturbative* contributions. The exponential factors $e^{-A_n/z}$ are invisible to Taylor expansion at $z = 0$ (they are flat at 0 to all orders), but they contribute finite amounts at finite $z$.

**Key fact:** the inner series $\phi_n(z)$ are themselves generally divergent, with Borel transforms having their own singularities, and their own transseries completions. This recursive structure — divergent series within divergent series — is called the **resurgent structure**.

---

## 6.4. Alien calculus: computing Stokes transitions

Écalle's **alien derivative** $\Delta_A$ is an operator acting on transseries. For an action $A > 0$, $\Delta_A$ extracts the coefficient of the singularity at $t = A$ in the Borel transform $B(t)$:

$$
\Delta_A \widetilde{f} \;=\; \lim_{t \to A^+} \bigl(B(t) - B^{\mathrm{reg}}(t)\bigr),
$$

where $B^{\mathrm{reg}}$ is the regular part and the limit extracts the discontinuity. $\Delta_A$ is a derivation on the algebra of transseries, and the key identity — the **bridge equation** — relates $\Delta_A$ to the Stokes constant $S_A$:

$$
\Delta_A \widetilde{f} \;=\; S_A \cdot \partial_\sigma \widetilde{f}|_{\mathrm{sector}},
$$

where the right-hand side is a specific differential operator with respect to the transseries parameters $\sigma$. The Stokes constants $S_A$ are the *physical content* of the resurgent structure.

**Écalle-Voros theorem.** For a wide class of transseries (quasi-resurgent functions), the Stokes constants $S_A$ are *computable* from the perturbative series alone via the alien derivative. This means: the non-perturbative sectors of $\widetilde{f}$ are *determined* (up to the transseries parameters $\sigma_n$) by the perturbative sector.

---

## 6.5. Stokes phenomena and lateral Borel summation

When $B(t)$ has a singularity at $t = A$ on the positive real axis, the Laplace integral

$$
f_\theta(z) \;:=\; \int_0^{\infty e^{i\theta}} e^{-t/z}\, B(t)\, \frac{dt}{z}
$$

depends on the direction $\theta$ of the contour. For $\theta > 0$ (passing *above* the singularity) and $\theta < 0$ (passing *below*), one gets *different* functions $f_+(z)$ and $f_-(z)$, differing by a discontinuity:

$$
f_+(z) - f_-(z) \;=\; 2\pi i \cdot S_A \cdot e^{-A/z} \cdot (\text{non-perturbative sector}).
$$

This is the **Stokes phenomenon**: the lateral Borel sums $f_\pm$ differ by an exponentially small non-perturbative term proportional to the Stokes constant $S_A$.

The **Stokes automorphism** $\mathfrak{S}$ relates $f_+$ to $f_-$:

$$
f_+ \;=\; \mathfrak{S}\, f_- \;=\; f_- \cdot \exp\bigl(\sum_A 2\pi i\, S_A\, e^{-A/z}\, \partial_\sigma\bigr).
$$

The Stokes automorphism is a group element that acts on the transseries by shifting the transseries parameters. When one crosses a Stokes line (a ray in the complex $z$-plane where a new singularity aligns with the Borel contour), the transseries parameters *jump* by a fixed amount determined by $S_A$.

**Lateral Borel summation:** choose $\theta = \pm \epsilon$ for small $\epsilon > 0$, defining $f_\pm$ unambiguously. The resulting $f_\pm$ are each genuine analytic functions — they *resum* the asymptotic series to actual numbers — but they differ from each other by the Stokes contributions. The "physical" answer is obtained by picking the correct $\pm$ (or the *median* average, in certain schemes).

---

## 6.6. The non-perturbative completion mechanism

The central mechanism of resurgence: **the transseries completion of a divergent asymptotic series is an actual analytic function, provided the transseries parameters are correctly fixed**.

Concretely:

**Step 1.** Compute the perturbative asymptotic series $\sum a_n z^n$. Verify it is divergent: $|a_n| \sim M^n n!$.

**Step 2.** Compute the Borel transform $B(t)$ and identify its singularities $\{A_1, A_2, \ldots\}$ on the positive real axis.

**Step 3.** For each singularity $A_k$, postulate a non-perturbative sector with action $A_k$. Compute the Stokes constants $S_{A_k}$ via alien derivatives applied to the perturbative series.

**Step 4.** Assemble the transseries $\widetilde{f}(z) = \sum_k \sigma_k e^{-A_k/z} z^{\alpha_k} \phi_k(z)$ with free parameters $\{\sigma_k\}$.

**Step 5.** *Fix the transseries parameters.* This is the hard step. Constraints include:
- Reality of the physical answer (usually, $\mathrm{Im}\, f = 0$, which constrains $\mathrm{Im}\,\sigma_k$).
- Boundary conditions (e.g., behaviour at $z \to \infty$, or matching to a known special value).
- Consistency with the Stokes automorphism (the jumps of $\sigma_k$ across Stokes lines must close up).

**Step 6.** Compute the lateral Borel sums $f_\pm(z)$ with the transseries parameters fixed. Check that they agree as analytic functions, or that their discontinuities are absorbed into the transseries jumps.

**Step 7.** Verify: $\widetilde{f}_{\pm}(z) \cdot$ (lateral Borel sum of perturbative sector $+$ transseries sectors with $\sigma_k$ fixed) $=$ the analytic function we were looking for.

For ODEs with irregular singular points, Steps 1-7 are a theorem (Écalle-Voros). For QFT, Steps 1-4 are available as computational framework; Step 5 is the hardest, and it is where Route A for 4D YM currently sits.

---

## 6.7. Classical examples where resurgence closes

**Stokes' asymptotic expansion of Airy function.** The Airy function $\mathrm{Ai}(z)$ has asymptotic expansion at $z \to +\infty$ that is divergent; the Borel transform has a singularity at $A = \frac{2}{3} z^{3/2}$. Transseries completion with the Stokes constant $S = -1/(2\sqrt{\pi})$ reproduces the exact Airy function.

**Gamma function's Stirling expansion.** $\log \Gamma(z)$ has Stirling's divergent series; Bernoulli-number transseries with explicit Stokes structure reproduces $\Gamma$.

**Painlevé equations.** Painlevé I-VI admit transseries solutions whose parameters are fixed by compatibility with the monodromy data of the linearized system. Resurgence determines the monodromy, which determines the transseries parameters.

**1D anharmonic oscillator.** The $x^4$ potential's ground-state energy has a divergent perturbative expansion; instanton + anti-instanton transseries with specific Stokes constants (Zinn-Justin) reproduces the exact answer to high precision.

**2D sine-Gordon / 2D YM.** 2D soluble models admit complete transseries analyses (§9).

---

## 6.8. The step from 1D to QFT

In 1D quantum mechanics and 0D matrix models, the transseries program closes because the underlying problem is an ODE or a finite-dimensional integral, and the Écalle-Voros framework applies directly.

In QFT, the transseries program *partially* extends. The Feynman path integral is formally an infinite-dimensional analogue, and the Lipatov saddle-point argument gives the expected action $A = S_0$ (instanton action). The Dyson-Schwinger equations can be written as a fixed-point equation in function space, and Klaczynski (2016) showed that transseries solutions exist in truncations of the DSE (§8).

What does NOT automatically extend:

- **The alien derivative as a computable operation on QFT amplitudes.** Formally $\Delta_A$ makes sense, but computing it requires the full Borel transform, which requires summing Feynman diagrams at all orders.
- **Fixing the transseries parameters.** In QFT, the boundary conditions are physical (reality of S-matrix, cluster decomposition, OS positivity), and translating these to transseries-parameter constraints is non-trivial.
- **Rigour.** Écalle-Voros is a theorem for ODEs; for QFT, it is a computational framework, not a proof.

Route A's task is to push the resurgence framework into 4D SU(N) YM with sufficient rigour to match the non-perturbative Schwinger functions at short distances.

---

## 6.9. Summary

Resurgence theory provides:

- A systematic framework for non-perturbative completion of divergent asymptotic series.
- The transseries structure (perturbative + exponentially small sectors).
- The alien calculus (computing Stokes constants from the perturbative series).
- Lateral Borel summation + Stokes automorphism (resuming in the presence of singularities).

The framework is a *theorem* for ODEs (Écalle 1981, Voros 1983), a *computational technology* for matrix models and 1D QM, and a *partial extension* to QFT (Dyson-Schwinger, truncated).

Route A's task is to apply this framework to 4D SU(N) YM, handle the IR-renormalon obstruction via lateral Borel summation, and match the resulting transseries completion to the non-perturbative Schwinger functions at short distances.

§07 analyses the specific structure of IR renormalons in 4D YM. §08 reviews Klaczynski's DSE+transseries framework. §09 reviews the 2D YM complete analysis. §10 introduces the programme-internal ITPFI contribution. §11 gives Route A's proof sketch.

---

*Paper 50 §06. Drafted 2026-04-14. G Six and Claude Opus 4.6.*

*Key references: Écalle 1981, Les fonctions résurgentes; Voros 1983, The return of the quartic oscillator; Costin 2009, Asymptotics and Borel summability; Aniceto-Basar-Schiappa 2019, A primer on resurgent transseries.*
