## §35 — Verification of Route B

*L-function construction + Langlands-Shahidi analytic continuation checks. Sym$^k$ values at specific arguments. The verification programme for Route B's functorial-transfer closure of H4.*

---

## 35.1. The verification target

Route B's analytic construction produces a Wilson-loop L-function $L(s, W)$ for pure Yang-Mills, verifies that it admits a Langlands-Shahidi functorial lift of the form $L(s, \pi, \mathrm{Sym}^k)$ for some automorphic $\pi$, and applies Kim-Sarnak's non-vanishing machinery to derive short-distance bounds that imply H4.

Verification has three components:

**V-B1 (L-function construction check).** Verify that $L(s, W)$ is well-defined: absolute convergence in a right half-plane, meromorphic continuation to $\mathbb{C}$, functional equation $\Lambda(s, W) = \epsilon \Lambda(1-s, W)$ with appropriate gamma factors.

**V-B2 (Functorial-lift check).** Verify that $L(s, W)$ factors through a Langlands-Shahidi lift. Identify the lift's automorphic representation $\pi$ (a representation of $\mathrm{GL}_n$ for some $n$) and the symmetric power $k$. Check that the standard Eisenstein-series construction for $L(s, \pi, \mathrm{Sym}^k)$ produces the same L-function.

**V-B3 (Kim-Sarnak non-vanishing).** Verify that $L(s, \pi, \mathrm{Sym}^k)$ is non-zero on $\mathrm{Re}(s) = 1$ (and, more refined, meets the Kim-Sarnak bound on the local Satake parameters). This is the Ramanujan-type statement that transfers to H4's short-distance bound.

All three components together verify Route B's analytic claim.

---

## 35.2. L-function construction check (V-B1)

The Wilson-loop L-function $L(s, W)$ is constructed from the Wilson-loop expectation values $\langle W(C) \rangle$ as a Dirichlet series:

$$L(s, W) = \sum_{C \in \mathcal{C}} \frac{\langle W(C) \rangle}{N(C)^s}$$

where $\mathcal{C}$ is a set of distinguished loops (e.g., primitive geodesic loops on a fixed lattice or continuum background), and $N(C)$ is a norm associated to $C$ (e.g., its length, or a Minkowski-signature-appropriate quantity).

**Verification check 1: absolute convergence.** For $\mathrm{Re}(s) > s_0$ (for some $s_0$ to be determined), the series converges absolutely. The proof uses polynomial boundedness of $\langle W(C) \rangle$ (a consequence of the lattice continuum limit) together with the polynomial growth of $N(C)$.

**Verification check 2: meromorphic continuation.** $L(s, W)$ continues meromorphically to $\mathbb{C}$ with poles at specific locations (possibly at $s = 1$, corresponding to the mass gap). The proof uses integral representations and the Hecke-operator machinery applied to the Wilson-loop observables.

**Verification check 3: functional equation.** $\Lambda(s, W) = L(s, W)$ multiplied by appropriate gamma factors satisfies $\Lambda(s, W) = \epsilon \Lambda(1-s, W)$. The gamma factors are fixed by the local structure of the Wilson loop at each prime and at infinity.

The verification checks are performed symbolically (using computer algebra to manipulate the Dirichlet series and its integral representations) and checked against closed-form expressions at low rank (e.g., for $N = 2$).

---

## 35.3. Functorial-lift check (V-B2)

The Langlands-Shahidi method constructs L-functions from Eisenstein series on specific groups. For Sym$^k$ lifts of $\mathrm{GL}_2$ automorphic representations:

- $k = 2$: $\mathrm{Sym}^2$ lift lives on $\mathrm{GL}_3$. Constructed via Gelbart-Jacquet 1978.
- $k = 3$: $\mathrm{Sym}^3$ lift lives on $\mathrm{GL}_4$. Constructed by Kim-Shahidi 2002.
- $k = 4$: $\mathrm{Sym}^4$ lift lives on $\mathrm{GL}_5$. Constructed by Kim 2003.

For Route B, the required identification is: the Wilson-loop L-function $L(s, W)$ equals $L(s, \pi, \mathrm{Sym}^k)$ for a specific $\pi$ on $\mathrm{GL}_n$ (for some $n, k$ to be determined by the YM theory's structure).

**Verification protocol.**

1. **Identify the base automorphic $\pi$.** From the Wilson-loop L-function's local Euler factors, identify the local Satake parameters. Match these to the Satake parameters of a known automorphic representation of $\mathrm{GL}_n$.

2. **Identify the symmetric-power index $k$.** From the Euler-factor structure, identify how the Satake parameters combine. The combination $\mathrm{Sym}^k$ is visible in how many "copies" of the base parameter appear in the Euler factor.

3. **Verify Eisenstein-series construction.** Use the Langlands-Shahidi method: write the L-function as a residue or non-residue term of an Eisenstein series on a suitable group (E$_7$ for Sym$^3$-on-GL$_2$, E$_8$ for Sym$^4$-on-GL$_2$, etc.). The verification is that the residue or non-residue term equals the Wilson-loop L-function.

4. **Cross-check.** The functorial lift, once identified, must be consistent with the known lifts in the Langlands-Shahidi literature. If the lift is novel (new $(n, k)$ pair), Route B requires an extension of the existing literature.

---

## 35.4. Kim-Sarnak non-vanishing (V-B3)

The third verification step is the Kim-Sarnak non-vanishing result itself, applied to the Wilson-loop L-function.

Kim-Sarnak 2003 proved: for automorphic $\pi$ of $\mathrm{GL}_2$ over $\mathbb{Q}$, the L-function $L(s, \pi, \mathrm{Sym}^4)$ does not vanish on $\mathrm{Re}(s) = 1$. This implies that the local Satake parameters $\alpha_p$ satisfy $|\alpha_p| \leq p^{7/64}$ — the $7/64$ exponent is the Kim-Sarnak bound.

For Route B, the analogous result is: the Wilson-loop L-function $L(s, W) = L(s, \pi_W, \mathrm{Sym}^{k_W})$ (for the identified $\pi_W, k_W$) does not vanish on $\mathrm{Re}(s) = 1$. This non-vanishing implies bounds on the Wilson-loop local data that transfer to short-distance behavior of $\langle W(C) \rangle$ as $|C| \to 0$.

**Verification check.** Apply Kim-Sarnak's proof directly to $L(s, \pi_W, \mathrm{Sym}^{k_W})$. The proof requires:

- Existence of the Eisenstein-series construction (V-B2).
- A specific identity for the residue of the L-function at $s = 1$, relating it to inner products of automorphic forms.
- Positivity of these inner products (which is where Kim-Sarnak's argument turns the crank).

If the Eisenstein-series construction is in a case where Kim-Sarnak's argument applies verbatim (e.g., $(n, k) = (2, 4)$ over $\mathbb{Q}$), V-B3 is immediate. If the case is more exotic (e.g., $(n, k) = (3, 4)$ or base field other than $\mathbb{Q}$), V-B3 requires an extension of Kim-Sarnak's argument — potentially the hardest step in Route B.

---

## 35.5. Numerical values at specific arguments

In addition to the analytic verifications V-B1, V-B2, V-B3, Route B includes numerical computation of L-function values at specific arguments.

**Critical values.** Compute $L(s_0, \pi_W, \mathrm{Sym}^{k_W})$ at $s_0 = 1, 1/2, 2$ numerically. These values are related to Wilson-loop expectation values at specific scales via the Mellin-transform relation.

**Method.** Use the Langlands-Shahidi Eisenstein-series expression to compute the L-function at these values. For $s_0 = 1$, the computation involves the inner product of automorphic forms. For $s_0 = 1/2$ (critical line), the computation uses the approximate-functional-equation method.

**Cross-check against lattice QCD.** Compute the Wilson-loop expectation values $\langle W(C) \rangle$ at a representative loop $C$ on the lattice (same lattice QCD runs as used for V-A3). Apply the Mellin transform to get a numerical value of $L(s_0, W)$. This lattice-derived value should match the Eisenstein-series-computed value.

**Expected match quality.** ~5-10% combined error, dominated by lattice statistical error at finite lattice spacing and truncation error in the Eisenstein-series numerical evaluation.

---

## 35.6. Cross-check against Route A

Route B's L-function values can be cross-checked against Route A's Borel-sum estimates. The relation is via the standard identity

$$L(s_0, W) = \int_0^\infty \langle W(C(\mu)) \rangle \mu^{s_0 - 1} d\mu$$

(with $C(\mu)$ a one-parameter family of loops at scale $\mu$). Route A's Borel-sum estimate of $\langle W(C(\mu)) \rangle$ integrated against $\mu^{s_0 - 1}$ should reproduce Route B's L-function value.

Consistency between Routes A and B is an internal check: if the two routes disagree on $L(s_0, W)$, one of them has a gap. This is the triangulation principle (§25) applied at the numerical level.

---

## 35.7. Verification infrastructure and cost

Route B's verification is mostly symbolic + numerical analytic-number-theory work, less compute-heavy than Route A's lattice QCD.

- **L-function construction check (V-B1):** symbolic manipulation, ~20 author-days.
- **Functorial-lift check (V-B2):** requires specialists in Langlands-Shahidi + reference-checking, ~60 author-days.
- **Kim-Sarnak non-vanishing (V-B3):** either verbatim application (~10 author-days) or extension (~200 author-days for novel $(n, k)$ cases).
- **Numerical L-function values:** ~10 CPU-days on a cluster using PARI/GP or SageMath.

Total: ~100-300 author-days (depending on V-B3's difficulty) plus ~10 CPU-days compute.

Route B's verification is more author-hour-intensive than Route A's but less compute-intensive. The bottleneck is V-B2 (functorial-lift identification, requiring deep Langlands-Shahidi expertise) and V-B3 in the extension case.

---

## 35.8. Failure modes and repair

**Failure mode B1: Wilson-loop L-function is not well-defined.** V-B1 fails (e.g., the Dirichlet series diverges everywhere, or meromorphic continuation has natural boundary). Repair: redefine the L-function with different weights or Hecke-operator structure. Possible, but may push Route B out of the standard Langlands-Shahidi framework.

**Failure mode B2: No functorial lift exists.** V-B2 fails (the Wilson-loop L-function does not match any standard Langlands-Shahidi lift). Repair: Route B is not closable as formulated. Alternative: formulate a generalized-Langlands-Shahidi framework (potentially Beyond Endoscopy, Langlands 2004) that accommodates the YM Wilson loop. This is a major extension of Route B, not a repair.

**Failure mode B3: Kim-Sarnak argument does not transfer.** V-B3 fails (the non-vanishing proof requires inputs not available for the Wilson-loop lift). Repair: extend Kim-Sarnak to the relevant case, or use a weaker bound (e.g., $\lambda_1 \geq 3/16$, Burger-Sarnak 1991, which would produce a weaker H4 statement).

Each failure mode has a repair strategy. The repairs vary in cost. V-B1 is the easiest repair (reformulate the L-function); V-B2 is the hardest (would require new Langlands-Shahidi extensions).

---

## 35.9. Summary

Route B's verification has three components: L-function construction check (V-B1), functorial-lift identification (V-B2), and Kim-Sarnak non-vanishing application (V-B3), plus numerical computation of L-function values at specific arguments and cross-check against Route A's Borel-sum estimates. The verification is ~100-300 author-days plus modest compute. The primary risk is V-B2 (functorial-lift identification) and V-B3 extension for novel cases. The expected match quality against lattice QCD is ~5-10%. Route B is verified when all three components close with adversarial threshold consistency.

---

*Paper 50 §35. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
