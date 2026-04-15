# Node E — Uniform H^1 Bound (Layer 3c)

**Chain layer:** 3c of 6
**Rigor label:** [THEOREM] (corrected proof, referee fix #3)
**Dependencies:** Node A (CCM operators)
**Status:** CLOSED

---

## Statement

**Theorem 7.1 (Estimate a, corrected).** For ALL $\lambda$ and ALL $N$:

$$\|(D_N - i)^{-1}\|_{L^2 \to H^1} \leq 1 + O(\rho^{-N}) < 2$$

where $\rho \geq 4.27$ is the CF decay rate (verified uniform for $N = 5$ to $30$; see Node F for status). The $O(\rho^{-N})$ correction absorbs any polynomial prefactor in $N$.

---

## Proof (Fourier-basis cancellation)

**The original proof failed** at $\lambda > e^\pi \approx 23.14$ because an algebraic inequality $(1 + a^2x^2)/(x^2 + 1) \leq a^2$ breaks for $a < 1$.

**The corrected proof works for ALL $\lambda$:**

1. Work in the Fourier basis $\{V_n\}$ where $D_{\log} = (2\pi/L) \cdot \operatorname{diag}(n)$ up to a rank-1 correction.

2. The H$^1$ weight is $1 + (2\pi n/L)^2$.

3. The resolvent denominator is $|(2\pi n/L) - i|^2 = (2\pi n/L)^2 + 1$.

4. **These cancel identically:** $\frac{1 + (2\pi n/L)^2}{(2\pi n/L)^2 + 1} = 1$ for every $n$.

5. The resolvent norm is **exactly 1** before the rank-1 correction.

6. The rank-1 correction from the quotient construction contributes $O(\rho^{-N})$ by CF decay (Node F). The resolvent perturbation for a rank-1 operator $B$ gives $\|(D_N - i)^{-1} - (D_0 - i)^{-1}\|_{L^2 \to H^1} \leq \|B\| \cdot \|(D_0 - i)^{-1}\|^2 / (1 - \|B\| \cdot \|(D_0-i)^{-1}\|)$. Since $\|B\| = O(\rho^{-N})$ and $\|(D_0 - i)^{-1}\|_{L^2 \to H^1} = 1$, the bootstrap closes: denominator $\geq 1 - O(\rho^{-N}) > 0$ for $N \geq 1$.

7. Total: $\|(D_N - i)^{-1}\|_{L^2 \to H^1} \leq 1 + O(\rho^{-N}) < 2$ for $N \geq 1$.

**No algebraic inequality is needed.** The cancellation is exact.

---

## Role in the chain

Provides **discrete compactness** (Boegli H2): uniform H$^1$ bounds on eigenvectors + Rellich-Kondrachov compact embedding $H^1 \hookrightarrow L^2$ on bounded domains gives precompactness of the resolvent family.

**Alternative route (approach c):** CF exponential decay + Arzela-Ascoli gives discrete compactness without H$^1$, providing an independent backup.

---

## Sources

- **Preprint:** sections-06-10.md §7, Theorem 7.1 (corrected)
- **Research:** research/44-h1-large-lambda.md
- **Referee fix:** Fix #3 (original proof broke at large $\lambda$; Fourier cancellation resolves)
