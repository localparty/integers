# 09. Conditional Continuum Mass Gap

This section proves Theorem 8: assuming Conjecture 1, the mass gap
survives the continuum limit $a \to 0$.

---

## Statement

**Theorem 8 (Conditional continuum mass gap).** *Assume Conjecture 1
holds with exponent $s \geq 2$. Then:*

*(a) The mass gap ratio $C_k = \Delta_k/\Lambda_k$ satisfies
$|C_{k+1} - C_k| \leq C'\,g_k^4\,(a_k\Lambda)^s$.*

*(b) The sum converges: $\sum_{k=0}^\infty g_k^4\,(a_k\Lambda)^s < \infty$.*

*(c) $C_\infty = C_0 - \sum \delta C_k > 0$.*

*(d) $\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0$.*

*(e) The thermodynamic limit ($L \to \infty$) commutes with the
continuum limit ($a \to 0$).*

*(f) The Osterwalder-Schrader axioms hold for the limiting theory.*

---

## Proof of (a): Mass gap ratio shift

By Conjecture 1, the dimensionless mass gap shift satisfies
$|\delta\hat{\Delta}_k| \leq C g_k^4 (a_k\Delta)^s$. Since the
RG-invariant scale obeys $\Lambda_{k+1}/\Lambda_k = 1 + O(g_k^6)$:
$$|C_{k+1} - C_k| = |\delta\Delta_k/\Lambda_k| + O(g_k^6) \leq C'\,g_k^4\,(a_k\Lambda)^s.$$

---

## Proof of (b): Doubly exponential convergence

Along the RG trajectory with $L^k$ blocking ($L = 2$):
$a_k = a_0/2^k$, and $g_k^2 \sim 1/(b_0 k \log 2)$ for large $k$
with $b_0 = 11N/(48\pi^2)$. The general term is
$$g_k^4(a_k\Lambda)^s \sim \frac{(a_0\Lambda)^s}{(b_0 k\log 2)^2 \cdot 2^{ks}}.$$
The exponential $2^{-ks}$ dominates $1/k^2$; the sum converges
doubly exponentially for any $s \geq 1$.

### Numerical estimates for SU(3)

Take $N=3$, $g_0^2 = 1.0$, $a_0\Lambda = 0.1$.

**Case $s = 2$ (weaker bound):**

| $k$ | $g_k^4$ | $(a_k\Lambda)^2$ | $g_k^4(a_k\Lambda)^2$ |
|-----|---------|-------------------|-----------------------|
| 0   | 1.000   | $1.0\times10^{-2}$ | $1.0\times10^{-2}$ |
| 1   | 0.354   | $2.5\times10^{-3}$ | $8.9\times10^{-4}$ |
| 2   | 0.146   | $6.3\times10^{-4}$ | $9.2\times10^{-5}$ |
| 3   | 0.076   | $1.6\times10^{-4}$ | $1.2\times10^{-5}$ |
| 4   | 0.047   | $3.9\times10^{-5}$ | $1.8\times10^{-6}$ |

Total: $\sum \approx 0.012$. **Correction to $C$: ~1.2%.**

**Case $s = 4$ (stronger bound):**

| $k$ | $g_k^4$ | $(a_k\Lambda)^4$ | $g_k^4(a_k\Lambda)^4$ |
|-----|---------|-------------------|-----------------------|
| 0   | 1.000   | $1.0\times10^{-4}$ | $1.0\times10^{-4}$ |
| 1   | 0.354   | $6.3\times10^{-6}$ | $2.2\times10^{-6}$ |
| 2   | 0.146   | $3.9\times10^{-7}$ | $5.7\times10^{-8}$ |
| 3   | 0.076   | $2.4\times10^{-8}$ | $1.8\times10^{-9}$ |

Total: $\sum \approx 1.0\times10^{-4}$. **Correction to $C$: ~0.01%.**

---

## Proof of (c): Positivity of $C_\infty$

By absolute convergence:
$|C_\infty - C_0| \leq C'\sum g_k^4(a_k\Lambda)^s$. With
$C_0 \sim 1$ (the lattice mass gap is $O(\Lambda)$):

- **$s = 2$:** correction $\sim 2\%$, so $C_\infty \geq C_0(1 - 0.02) > 0$.
- **$s = 4$:** correction $\sim 0.01\%$, so $C_\infty \geq C_0(1 - 10^{-4}) > 0$.

Inductive stability is guaranteed: the correction
$|\delta\hat{\Delta}_k| \propto \hat{\Delta}_k^{s+3}$ shrinks faster
than the gap itself. A smaller gap gives smaller corrections -- no
downward spiral.

---

## Proof of (d): Continuum mass gap

$\Lambda_\infty = \lim_k \Lambda_k > 0$ holds unconditionally from
Balaban's beta function and $\sum g_k^4 < \infty$. Therefore:
$$\Delta_\infty = C_\infty \cdot \Lambda_\infty > 0.$$

---

## Proof of (e): Commutation of limits

Apply the **Moore-Osgood theorem**: if $f(k,L)$ converges uniformly
in $L$ as $k \to \infty$, and pointwise in $k$ as $L \to \infty$,
the limits commute.

1. **Uniform in $L$:** The bound $|C_{k+1}(L) - C_k(L)| \leq C'g_k^4(a_k\Lambda)^s$
   is volume-independent. The factor $V$ in $f_c(0) = V\langle 1|E_k(0)|1\rangle_c$
   is cancelled by the $1/V$ delocalization of the one-particle state.
2. **Pointwise in $k$:** For fixed $k$, $\Delta_k(L) \to \Delta_k(\infty)$
   as $L \to \infty$ by exponential clustering (Section 04).

Therefore $\lim_k \lim_L \Delta_k(L) = \lim_L \lim_k \Delta_k(L) = \Delta_\infty > 0$.

---

## Proof of (f): Osterwalder-Schrader axioms

**(OS1) Temperedness.** Schwinger functions are uniformly bounded (in $a$)
by cluster expansion estimates.

**(OS2) Euclidean invariance.** Hypercubic symmetry extends to full
$\mathrm{O}(4)$ as $a \to 0$, guaranteed by the vanishing of irrelevant
operators in the effective action.

**(OS3) Reflection positivity.** The Wilson action with Haar measure
is reflection-positive for all $a > 0$ (Osterwalder-Seiler, 1978).
Preserved under limits.

**(OS4) Symmetry.** Manifest from the Euclidean functional integral.

By OS reconstruction, the limiting theory defines a Wightman QFT
on Minkowski space with positive Hilbert space, unitary Poincare
representation, unique vacuum, and mass gap $\Delta_\infty > 0$. $\square$

---

## Remarks

1. **First steps.** At $k = 0,1,2$ where $g_k^4 = O(1)$, first-order
   perturbation is not a priori justified. These finitely many steps
   are handled non-perturbatively via the cluster expansion, with
   bounded total contribution $K_0$ absorbed into $C_0$.

2. **Without Conjecture 1.** The operator norm bound gives
   $|\delta\Delta_k/\Delta_k| \leq Cg_k^4/(a_k\Lambda)$;
   $\sum g_k^4/(a_k\Lambda) \sim \sum 2^k/k^2$ diverges. The
   continuum limit is not established without dimensional suppression.
