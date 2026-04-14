# §13 — Kim-Sarnak 2003: $\lambda_1 \geq 975/4096$

*The best known bound on the first Laplace eigenvalue of congruence arithmetic surfaces. Achieved by Kim-Sarnak 2003 using the symmetric fourth power L-function of GL$_2$ and Langlands-Shahidi residue analysis. This section states the theorem, summarizes the technique, and identifies the parts that transfer under S-duality to Route B.*

---

## 13.1. The theorem

**Theorem (Kim-Sarnak 2003).** *Let $\Gamma_0(N) \subset \text{SL}_2(\mathbb{Z})$ be a congruence subgroup, and let $\lambda_1(\Gamma_0(N) \backslash \mathbb{H})$ denote the smallest nonzero eigenvalue of the hyperbolic Laplacian on $L^2(\Gamma_0(N) \backslash \mathbb{H})$. Then*
$$\lambda_1(\Gamma_0(N) \backslash \mathbb{H}) \geq \frac{975}{4096} \approx 0.2380.$$

The conjectural value is $\lambda_1 \geq 1/4 = 0.2500$ (Selberg 1965). The Kim-Sarnak bound gives $\lambda_1 \geq 0.2380$, closing $(0.2380, 0.2500)$ as the remaining gap.

**Reference.** H. H. Kim, *Functoriality for the exterior square of GL$_4$ and the symmetric fourth of GL$_2$*, with appendices by D. Ramakrishnan and H. Kim / P. Sarnak, *Journal of the AMS* 16 (2003), no. 1, 139-183. The specific bound $\lambda_1 \geq 975/4096$ is proved in the Kim-Sarnak appendix using the Sym$^4$ functoriality established in the main body.

---

## 13.2. Prior history

The Selberg eigenvalue conjecture ($\lambda_1 \geq 1/4$) is part of the Ramanujan-Petersson conjecture for Maass forms at the archimedean place. The history of partial bounds:

- **Selberg 1965:** $\lambda_1 \geq 3/16 = 0.1875$. Established via the Selberg trace formula.
- **Iwaniec 1990:** improved bounds via the Kuznetsov trace formula.
- **Luo-Rudnick-Sarnak 1995:** $\lambda_1 \geq 21/100 = 0.21$. First bound above $3/16$.
- **Kim-Shahidi 2002:** $\lambda_1 \geq 66/289 \approx 0.2284$. Via Sym$^3$ functoriality on GL$_2$.
- **Kim-Sarnak 2003:** $\lambda_1 \geq 975/4096 \approx 0.2380$. Via Sym$^4$ functoriality.

The sequence $3/16 \to 21/100 \to 66/289 \to 975/4096$ reflects the successive incorporation of higher symmetric powers of the standard L-function into the Langlands-Shahidi framework.

---

## 13.3. The technique at a glance

The Kim-Sarnak bound relies on three inputs:

### 13.3.1. Functoriality of Sym$^4$ for GL$_2$

**Kim 2001 (Sym$^3$):** for every cuspidal automorphic representation $\pi$ of GL$_2(\mathbb{A}_\mathbb{Q})$, the symmetric cube $\text{Sym}^3(\pi)$ is a cuspidal automorphic representation of GL$_4(\mathbb{A}_\mathbb{Q})$.

**Kim 2003 (Sym$^4$):** the symmetric fourth $\text{Sym}^4(\pi)$ is an automorphic representation of GL$_5(\mathbb{A}_\mathbb{Q})$, cuspidal except in explicitly described degenerate cases.

These functorialities are *the* content of Kim's paper. They extend the Langlands functoriality programme beyond the GL$_2$ base case to $\text{Sym}^k$ for $k = 3, 4$.

### 13.3.2. L-function bounds

The bounds on $\lambda_1$ come from the analytic behaviour of the L-functions $L(s, \pi, \text{Sym}^k)$ at the edge of the critical strip. Specifically, one uses:

- The L-function $L(s, \pi \otimes \tilde{\pi}) = \prod_{k=0}^{\infty} L(s, \text{Sym}^{2k}(\pi))$ (Rankin-Selberg).
- The non-vanishing of $L(s, \text{Sym}^k(\pi))$ at $s = 1$ (for $k \leq 4$, via the Langlands-Shahidi machine on exceptional groups $E_6, E_7, E_8$).
- The positivity of certain Dirichlet coefficients (via Jacquet-Shalika non-negativity).

### 13.3.3. Convexity bound + local bound

Combining the above, Kim-Sarnak deduce: if $\lambda_1 < 1/4$, then the corresponding Maass form $\phi$ has an archimedean Langlands parameter $s_0 = 1/2 + it_0$ with $|t_0|$ in the complementary series. The Sym$^4$ L-function $L(s, \phi, \text{Sym}^4)$ has a specific pole structure that yields a contradiction when $|t_0|$ exceeds a precise threshold. Tracking the threshold gives $975/4096$.

The bound is optimal for the Sym$^4$-based approach. Extending to Sym$^5, \text{Sym}^6$ would in principle give better bounds, but Langlands-Shahidi functoriality for Sym$^5, \text{Sym}^6$ of GL$_2$ is not known (and is one of the major open problems in the Langlands programme as of 2026).

---

## 13.4. Ramanujan-Petersson at finite places

The Kim-Sarnak theorem has a sibling bound at finite places: if $\pi$ is a cuspidal automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$, and $\pi_p$ is its local factor at a finite prime $p$, then the Satake parameters $\alpha_p, \beta_p$ satisfy
$$|\alpha_p|, |\beta_p| \leq p^{7/64}.$$

The conjectural value is $p^0 = 1$ (Ramanujan-Petersson). The Kim-Sarnak finite-place bound $p^{7/64}$ parallels the archimedean bound $\lambda_1 \geq 975/4096$: both come from the same Sym$^4$ machinery, at different places.

For Route B, the finite-place bound matters: the YM Wilson-loop L-function, if it exists, will be an *Euler product* over primes, and its local factors will be subject to an analogous bound. The Ramanujan-Petersson bound at finite places is the S-dual, under the functional equation's $p \leftrightarrow \infty$ exchange, of the archimedean Selberg bound.

---

## 13.5. Why $975/4096$ and not $1/4$

The gap $975/4096 < 1/4$ reflects the *limitations* of the Sym$^4$ approach. Three sources of loss:

1. **Only Sym$^k$ for $k \leq 4$ is available.** Higher symmetric powers would close the gap, but Sym$^5, \text{Sym}^6$ functoriality is open.
2. **The L-function at the edge $s = 1$.** The non-vanishing at $s = 1$ is controlled, but the *second-order* behaviour (how fast $L(s, \text{Sym}^4)$ approaches $0$ or $\infty$) introduces loss.
3. **The local-global assembly.** The bound at each place (archimedean and finite) is optimal; the *global* assembly loses a small amount relative to the place-by-place optimum.

For Route B, what matters is not that $975/4096 \neq 1/4$, but that the *structure* of the proof — Sym$^k$ functoriality + Langlands-Shahidi L-function analysis — is sufficient to establish a *specific* spectral bound. The specific value transfers under S-duality to a specific short-distance bound on the YM Wilson-loop two-point function.

---

## 13.6. What transfers under S-duality

Under the S-duality of Paper 60 §21 (functional equation $s \leftrightarrow 1 - s$), the three ingredients of Kim-Sarnak transfer as follows:

| Kim-Sarnak (Selberg side) | S-dual (YM side, Route B target) |
|---|---|
| Functoriality of $\text{Sym}^4(\pi)$ on GL$_2$ | Functoriality of an analogous operation on the YM Wilson-loop system |
| L-function $L(s, \text{Sym}^k(\pi))$ non-vanishing at $s = 1$ | YM L-function non-vanishing at the corresponding edge |
| Sym$^4$-based archimedean bound $\lambda_1 \geq 975/4096$ | Short-distance bound on the YM two-point function, via perturbative OPE |

The first transfer — constructing the analogue of $\text{Sym}^k$ on YM Wilson loops — is the content of §15. The second — verifying the functional equation of the YM L-function — is implicit in §14-§16. The third — converting the L-function bound into an OPE bound — is the content of §17.

**What we need from Kim-Sarnak 2003 for Route B:**

1. The Sym$^4$ functoriality (Kim 2003) and its Langlands-Shahidi structure.
2. The explicit bound $975/4096$ as a benchmark for the strength of the Sym$^4$-based approach.
3. The finite-place Ramanujan-Petersson bound $p^{7/64}$, which under $p \leftrightarrow \infty$ S-duality gives local bounds on the YM Wilson-loop L-function's Euler factors.

---

## 13.7. What we do not need (and what Kim-Sarnak does not give)

Kim-Sarnak 2003 does *not*:

- Prove the full Selberg conjecture $\lambda_1 \geq 1/4$. The remaining gap $(0.2380, 0.2500)$ is still open.
- Establish Sym$^k$ functoriality for $k \geq 5$. This remains one of the central open problems in the Langlands programme.
- Directly apply to gauge theories or to L-functions that are not attached to automorphic representations of GL$_n$.

For Route B, only the *technique* — Langlands-Shahidi applied to Sym$^4$ — is what we borrow. The specific numerical bound $975/4096$ is a benchmark; the analogue of $975/4096$ on the YM side would be a specific short-distance bound on the two-point function.

Route B does *not* require the full Selberg conjecture to close H4. It requires the Sym$^4$-based bound to transfer to a corresponding asymptotic-freedom match, which is a weaker statement than the full spectral bound.

---

## 13.8. Summary

Kim-Sarnak 2003 established the best known bound on the first Laplace eigenvalue of congruence arithmetic surfaces: $\lambda_1 \geq 975/4096$. The technique uses symmetric fourth power L-functions on GL$_2$ (Kim 2003 functoriality) together with the Langlands-Shahidi machine on exceptional groups. Under the S-duality of Paper 60 §21, the Sym$^4$ technique transfers to Route B as the target approach for H4: construct a YM Wilson-loop L-function, verify Sym$^4$-style functoriality, and apply Langlands-Shahidi-style L-function bounds to extract the AF match.

The next sections develop each ingredient: §14 explains the Langlands-Shahidi method in detail, §15 constructs the YM Wilson-loop L-function, §16 handles the transfer map, §17 assembles the Route B proof sketch.

---

*Paper 50 §13. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
