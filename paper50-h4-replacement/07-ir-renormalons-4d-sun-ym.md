# §07 — IR Renormalons in 4D SU(N) YM

*The specific structure of IR renormalons in pure Yang-Mills: where they sit, what generates them, how they obstruct ordinary Borel summation, and what lateral Borel summation has to compute.*

---

## 7.1. The observable and the setup

Fix a gauge-invariant observable $\mathcal{O}$ of mass dimension $d$ in pure SU(N) YM on $\mathbb{R}^4$. Typical choices:

- The Wilson loop $W(C) = \frac{1}{N}\mathrm{Tr}\, \mathcal{P} \exp\bigl(i\oint_C A\bigr)$ on a rectangular contour.
- The vacuum expectation value $\langle \mathrm{Tr}(F^2) \rangle$ of the field-strength squared.
- The two-point function $\langle \mathrm{Tr}(F^2)(x)\,\mathrm{Tr}(F^2)(y)\rangle$.

Perturbatively, $\mathcal{O}$ has an expansion

$$
\mathcal{O}_{\mathrm{PT}}(g,\mu) \;=\; \sum_{n=0}^{\infty} a_n(\mu/\Lambda)\, g^{2n}(\mu)
$$

in the running coupling $g(\mu)$ at renormalization scale $\mu$. The scheme is MS-bar + Paper 10 / Paper 11 K.4 canonical choice.

The coefficients $a_n$ have the Lipatov-like large-order growth $|a_n| \sim C \cdot n! \cdot (2\beta_0)^n \cdot n^\gamma$, and the Borel transform

$$
B_{\mathcal{O}}(t) \;=\; \sum_{n=0}^\infty \frac{a_n}{n!}\, t^n
$$

has singularities on the positive real axis at positions determined by the renormalon structure.

---

## 7.2. The renormalon generating diagrams

An **IR renormalon** in 4D YM arises from diagrams in which a single internal gluon line carries soft momentum, dressed by an arbitrary number of gluon self-energy bubble insertions.

The prototype: consider the vacuum polarization correction to the gluon propagator,

$$
\Pi(k^2) \;=\; \alpha_s(\mu)\bigl[\beta_0 \log(k^2/\mu^2) + (\text{finite})\bigr] + O(\alpha_s^2).
$$

Resumming the leading logarithms gives a running coupling $\alpha_s(k^2)$ inside the gluon line. For soft momentum $k^2 \to 0$, the running coupling *grows* (asymptotic freedom in reverse), and the resulting integral

$$
\int \frac{d^4 k}{(2\pi)^4}\, \frac{1}{k^2}\, [\alpha_s(k^2)]^n
$$

diverges as $n!$ times a power of $\beta_0$ when the integration region reaches the Landau pole.

More precisely, using the renormalization-group equation $\alpha_s(k^2) = 1/(\beta_0 \log(k^2/\Lambda^2))$ and expanding in $\alpha_s(\mu)$:

$$
[\alpha_s(k^2)]^n \;=\; \sum_{m \geq 0} \binom{-n}{m}\bigl(\beta_0 \alpha_s(\mu) \log(k^2/\mu^2)\bigr)^m\, \alpha_s^n(\mu).
$$

The integral over $k$, dominated by $k^2 \to 0$, generates a factor $(n/(2\beta_0))^n$ that combined with the combinatorics gives the $n!$ growth.

The Borel transform of this class of diagrams has a singularity at $t = 2k/\beta_0$ for each integer $k \geq 1$ — the **IR renormalon at order $k$**.

---

## 7.3. The renormalon positions (the IR landscape)

For the field-strength squared operator in 4D SU(N) YM with $N_f = 0$:

- **IR renormalon at $t_1 = 2/\beta_0$**, associated with dim-4 operator mixing: $\mathrm{Tr}(F^2)$ at scale $\mu$ mixes with the gluon condensate $\langle\mathrm{Tr}(F^2)\rangle_\Lambda$ at scale $\Lambda$. The ambiguity $e^{-2/(\beta_0 g^2)}$ matches the scale $\Lambda^4$.
- **IR renormalon at $t_2 = 4/\beta_0$**, associated with dim-6 operators: $\mathrm{Tr}(F\cdot DF\cdot F)$-type mixing, matching $\Lambda^6$ ambiguity.
- **IR renormalon at $t_k = 2k/\beta_0$**, for each $k \geq 1$: dim-$(2k+2)$ operator mixing.

The **instanton singularities** sit at $t_{\mathrm{inst}} = 8\pi^2$ (one-instanton action for SU(N)), substantially further from the origin for moderate $\beta_0$. For YM, the first IR renormalon ($t_1 = 2/\beta_0 \approx 2/(11/(48\pi^2)) = 96\pi^2/11 \approx 27.6$) is dominant; the instanton sits at $t = 8\pi^2 \approx 79.0$, farther out.

**Consequence:** the Borel plane's positive real axis for 4D SU(N) YM has singularities at
$$
\{t_1, t_2, t_3, \ldots, t_{\mathrm{inst}}, 2t_{\mathrm{inst}}, \ldots\} \;=\; \bigl\{\tfrac{2k}{\beta_0} : k \geq 1\bigr\} \cup \bigl\{8k\pi^2 : k \geq 1\bigr\}.
$$

The first IR renormalon $t_1 = 2/\beta_0$ controls the leading non-perturbative ambiguity.

---

## 7.4. Why the IR renormalon position is "fixed"

A common question: can the renormalon singularity be shifted by a different scheme choice? Paper 10's scheme-independence theorem gives the rigorous answer: **no, the IR renormalon position $t_1 = 2/\beta_0$ is scheme-independent.**

Reason: $\beta_0$ is scheme-independent (one-loop beta function), so $t_1$ is a physical (scheme-independent) singularity position. The *non-perturbative* ambiguity $e^{-2/(\beta_0 g^2)} = e^{-8\pi^2/(g^2 \cdot 11/2)} \sim (\Lambda/\mu)^{4}$ is also scheme-independent — it is the gluon condensate scale.

This rigidity is important for Route A: the transseries structure has actions $A_k = 2k/\beta_0$ that are *physical*, not scheme-dependent choices.

---

## 7.5. The structure of the renormalon ambiguity

Near the IR renormalon at $t = t_1 = 2/\beta_0$, the Borel transform has the local form

$$
B(t) \;\sim\; \frac{C_1}{(1 - t/t_1)^{1 + \nu_1}}\bigl(1 + O(1-t/t_1)\bigr),
$$

with $\nu_1$ a real exponent determined by the anomalous-dimension matrix of the relevant composite operator at scale $\Lambda$ (the gluon condensate has $\nu_1 = 0$ at leading log).

The lateral Borel sums $f_\pm(g) = \int_0^{\infty \cdot e^{\pm i\epsilon}} e^{-t/g^2} B(t)\, dt/g^2$ differ by

$$
f_+(g) - f_-(g) \;=\; 2\pi i \cdot C_1 \cdot \Gamma(1+\nu_1)^{-1} \cdot g^{-2(1+\nu_1)} \cdot e^{-t_1/g^2} \cdot \bigl(1 + O(g^2)\bigr).
$$

This is the **non-perturbative ambiguity**: an imaginary, exponentially small piece proportional to $(\Lambda/\mu)^4$ (for $\nu_1 = 0$).

Physically, this ambiguity is *absorbed* by the gluon-condensate contribution to the OPE:

$$
\mathcal{O}(g, \mu) \;=\; \mathrm{BS}_\pm[\mathcal{O}_{\mathrm{PT}}](g) \;+\; c_{\mathrm{gluon}} \cdot \langle \mathrm{Tr}(F^2)\rangle_\Lambda \cdot (\mu/\Lambda)^{-4} \;+\; \cdots
$$

where the imaginary part of $\mathrm{BS}_\pm$ is cancelled by the imaginary part of the gluon condensate's renormalization. This is the **renormalon-condensate cancellation** folklore: the ambiguity of the perturbative resummation is precisely the ambiguity of the gluon condensate, and the *physical* observable is well-defined after including both contributions.

---

## 7.6. What "non-Borel-summable" means concretely in 4D YM

For 4D SU(N) YM, "non-Borel-summable" means:

1. The Borel transform $B(t)$ has an infinite sequence of singularities on $\mathbb{R}_+$.
2. The ordinary Borel sum (straight-line Laplace integral) *does not exist* — the integral diverges because it must pass through singularities.
3. The lateral Borel sums $f_\pm$ *do exist* as analytic functions, but they differ by non-perturbative terms.
4. The physical answer is a *specific combination* of $f_\pm$ and the non-perturbative condensate contributions, such that the imaginary parts cancel.

Mathematically, the perturbative series is a **1-summable series with singularities on $\mathbb{R}_+$**, i.e., a **resurgent series** in Écalle's sense. Its resurgent completion is the non-perturbative Schwinger function.

---

## 7.7. What lateral Borel summation computes

Fix the contour $\theta = +\epsilon$ (pass above all IR renormalons). The lateral Borel sum $f_+(g)$ is a specific analytic function of $g^2$ in a sector. Its relationship to the non-perturbative observable $\mathcal{O}^{\mathrm{NP}}$ is:

$$
\mathcal{O}^{\mathrm{NP}}(g) \;=\; \mathrm{Re}\bigl[f_+(g)\bigr] \;+\; \sum_{k \geq 1} \sigma_k\, e^{-t_k/g^2}\, \phi_k(g),
$$

where the transseries parameters $\sigma_k$ are *fixed by consistency* (reality of $\mathcal{O}^{\mathrm{NP}}$) and the $\phi_k$ are the non-perturbative sector's inner asymptotic series.

**Key fact:** the real parts of $f_+$ and $f_-$ agree. The imaginary part of $f_+$ is cancelled by the imaginary part of $\sum \sigma_k e^{-t_k/g^2} \phi_k$ when $\sigma_k$ are chosen correctly (the Stokes-constant data).

**What lateral Borel summation computes, specifically:**

- The real part of $f_+(g)$: a genuine real-analytic function of $g^2$ in a sector.
- The Stokes constants $S_{t_k}$: coefficients of the non-perturbative sectors.
- The transseries parameters $\sigma_k$: fixed by demanding $\mathcal{O}^{\mathrm{NP}}$ be real and match known asymptotics (e.g., the OPE structure).

---

## 7.8. The 4D YM renormalon problem, stated precisely

Route A aims to prove:

**Conjecture (Route A central claim).** For the observable $\mathcal{O} = \langle \mathrm{Tr}(F^2)\rangle$ in 4D SU(N) YM:

(i) The Borel transform $B(t) = \sum (a_n/n!) t^n$ has meromorphic continuation to a neighbourhood of $\mathbb{R}_+ \cup \{0\}$ with singularities at $t_k = 2k/\beta_0$, $k \geq 1$, and at $t_{\mathrm{inst}, k} = 8k\pi^2$, $k \geq 1$.

(ii) The lateral Borel sums $f_\pm(g)$ extend to sectorial analytic functions on neighbourhoods of the positive $g^2$-axis.

(iii) There exist transseries parameters $\{\sigma_k\}$, determined uniquely by the conditions
- $\mathcal{O}^{\mathrm{NP}}(g) \in \mathbb{R}$ for $g > 0$,
- $\mathcal{O}^{\mathrm{NP}}$ agrees with the gradient-flowed OS-reconstructed $\langle \mathrm{Tr}(F^2)\rangle$ from Paper 8 Link 17,
such that
$$
\langle \mathrm{Tr}(F^2)\rangle^{\mathrm{NP}}(g) \;=\; \mathrm{Re}\bigl[f_+(g)\bigr] \;+\; \sum_k \sigma_k\, e^{-t_k/g^2}\, \phi_k(g).
$$

(iv) At short distances $\mu \to \infty$ (equivalently $g(\mu) \to 0$), the full expression reduces to the perturbative series term-by-term, i.e., H4 holds.

---

## 7.9. What Route A needs to prove rigorously

The Route A programme, spelled out:

**Step 1.** Prove that $B(t)$ has the claimed singularity structure at $t_k$ and $t_{\mathrm{inst}, k}$. This requires controlling the Lipatov saddle + bubble-chain contributions at all orders. Paper 10 + Paper 11 K.4 provide the perturbative series; the singularity positions are consequences of the beta function.

**Step 2.** Prove that $B(t)$ extends meromorphically. This is harder — it requires resumming the bubble-chain contributions into a closed-form Borel transform. Klaczynski 2016 (§8) gives partial progress via DSE; full 4D YM result is open.

**Step 3.** Prove that the lateral sums $f_\pm$ exist as sectorial analytic functions. For 4D YM this is currently *conjectural*; it depends on bounds on the Borel transform away from the singularities.

**Step 4.** Prove the transseries parameters are uniquely determined. In 2D YM (§9), this is done via Migdal's recursion + weak/strong coupling consistency. In 4D, no analogue exists, and this is where the ITPFI contribution (§10) enters.

**Step 5.** Prove the short-distance match (H4 itself). Given Steps 1-4, this should follow from the leading $g \to 0$ expansion, but the details require care.

Steps 1-2 have significant partial support. Steps 3-4 are the main walls. Step 5 is the conclusion.

---

## 7.10. Summary

4D SU(N) YM has:

- IR renormalons at $t_k = 2k/\beta_0$, scheme-independent by Paper 10.
- Instanton singularities at $t_{\mathrm{inst},k} = 8k\pi^2$, subdominant.
- Non-Borel-summability in the strict Nevanlinna sense.
- A resurgent transseries structure with free parameters $\sigma_k$ that must be fixed.
- Physical interpretation: the transseries parameters encode the gluon-condensate + higher-dimension composite operator OPE contributions.

Lateral Borel summation computes the real-analytic ambiguity-free piece $\mathrm{Re}[f_+]$ and, combined with the transseries sectors, reconstructs the full non-perturbative observable. H4 is the statement that this reconstruction matches Paper 8's non-perturbative Schwinger functions at short distances.

The Route A programme is outlined; §§08-11 fill in the technical content.

---

*Paper 50 §07. Drafted 2026-04-14. G Six and Claude Opus 4.6.*

*Key references: 't Hooft 1977, Can we make sense out of quantum chromodynamics?; Parisi 1978, Singularities of the Borel transform; Mueller 1985, On the structure of infrared renormalons; David 1984; Beneke 1998, Renormalons; Shifman-Vainshtein-Zakharov 1979, QCD and resonance physics (for condensate OPE).*
