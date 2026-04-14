# PROOF-CHAIN -- Collatz Conjecture (Paper 41)

*Every positive integer eventually reaches 1 under the map $n \to n/2$ (even) or $n \to 3n+1$ (odd).*
*Framework route: the Collatz map IS a Hecke-semigroup endomorphism on $\mathbb{N}^*$ interleaving $\mu_2$ (even step) and $\mu_3$ (odd step). C\*-algebra formulation exists (arXiv:2411.08084, Nov 2024). KMS$_1$ orbit constraints via BC spectral measure.*

*Status: 2/7 links closed | Confidence: 3/10*

## Chain table

| Link | Statement | Status | Depends on | Key reference |
|---|---|---|---|---|
| 1 | The Collatz map $T: \mathbb{N} \to \mathbb{N}$ defined by $T(n) = n/2$ (even), $T(n) = (3n+1)/2$ (odd) is an endomorphism of the multiplicative monoid $\mathbb{N}^*$ interleaving the Hecke generators $\mu_2$ (division by 2) and $\mu_3$ (multiplication by 3 + correction) | ESTABLISHED | -- | Elementary; BC Hecke semigroup structure |
| 2 | C\*-algebra formulation: the Collatz map generates a C\*-algebra $\mathcal{A}_T$ via three equivalent constructions — (a) single operator, (b) two-operator, (c) Cuntz algebra $\mathcal{O}_2$. Convergence to 1 $\iff$ no non-trivial reducing subspaces (single-op) or equivalently $\iff$ simplicity conditions on $\mathcal{A}_T$ | LITERATURE | -- | arXiv:2411.08084 (Nov 2024) |
| 3 | The backward transfer operator $\mathcal{L}_T$ on weighted Banach spaces satisfies Lasota-Yorke inequalities with explicit contraction constant; quasi-compactness and spectral gap with unique invariant positive density | LITERATURE | -- | arXiv preprint 2025 (spectral calculus for arithmetic dynamics) |
| 4 | **BC embedding**: the Collatz C\*-algebra $\mathcal{A}_T$ embeds into the BC algebra $A_{BC}$ via the identification $T_{\text{even}} = \mu_2^* \mu_2$ (projection to even sublattice) and $T_{\text{odd}} = \mu_3 \circ \text{shift}$ (odd step as Hecke-3 action + additive correction). The Cuntz algebra $\mathcal{O}_2$ generators $s_0, s_1$ (encoding even/odd branches) map to BC Hecke operators | CONJECTURED | 1, 2 | Framework construction |
| 5 | **KMS orbit constraint**: at KMS$_1$, the unique BC state $\omega_1$ evaluates on Collatz orbits as $\omega_1(T^k(n)) = (T^k(n))^{-1}$. Convergence to 1 means $\omega_1(T^k(n)) \to 1$. The BC spectral measure constrains which orbits are achievable: divergent orbits would require $\omega_1$-mass on sequences with $T^k(n) \to \infty$, violating the KMS$_1$ normalization $\omega_1(e_1) = 1$ | CONJECTURED | 4, Paper 1 (BC algebra) | Framework; KMS$_1$ uniqueness |
| 6 | **Spectral gap transfer**: the backward transfer operator's spectral gap (Link 3) + the BC algebra's KMS$_1$ spectral gap combine to show that divergent orbits have measure zero under ANY KMS$_\beta$ state for $\beta \geq 1$. Non-trivial cycles (periodic orbits other than $\{1, 2\}$) are ruled out by the Araki-Woods type III$_1$ ergodicity of the BC modular flow (the flow has no periodic orbits except the fixed point) | OPEN | 3, 5 | Wall |
| 7 | Collatz conjecture: every positive integer reaches 1 | FOLLOWS | 6 | -- |

## Current wall

**Link 6 (spectral gap transfer + cycle elimination).** Two sub-problems:

**6a. Divergent orbits.** The backward transfer operator's spectral gap gives exponential mixing, which should force orbits into the basin of attraction of the fixed point. But "measure-zero divergent orbits" is not the same as "no divergent orbits" — need to upgrade from measure-theoretic to pointwise.

**6b. Non-trivial cycles.** If a cycle $n_1 \to n_2 \to \cdots \to n_k \to n_1$ existed with $k > 1$ and all $n_i > 2$, it would be a periodic orbit of the BC modular flow restricted to the Collatz sub-algebra. The type III$_1$ structure (no minimal projections, Connes spectrum = $\mathbb{R}$) constrains periodic orbits: the only periodic orbit of the modular flow on a type III$_1$ factor is the trivial one. But transferring this from the full BC factor to the Collatz sub-algebra requires the embedding (Link 4) to preserve the type classification.

**Known classical results:**
- Verified for all $n < 2^{68}$ (Barina 2020)
- Almost all orbits converge (Terras 1976, density-1 result)
- No non-trivial cycles of length $< 186$ billion (Eliahou 1993)
- Tao 2019: almost all Collatz orbits attain almost bounded values (strongest partial result)

## The Hecke-semigroup insight

The Collatz map is fundamentally about the interplay of $\times 2$ and $\times 3$ — the first two primes. In the BC algebra:

- $\mu_2$ (Hecke at $p=2$): the "even step" $n \to n/2$ is $\mu_2^* \mu_2$ (project to 2-divisible, then halve)
- $\mu_3$ (Hecke at $p=3$): the "odd step" $n \to 3n+1$ involves $\mu_3$ (multiply by 3) plus an additive shift (+1)

The additive shift is where the BC algebra's multiplicative structure meets the additive structure of $\mathbb{N}$ — exactly the same tension that Goldbach (Paper 33) faces. The Collatz conjecture asks: does alternating between the $p=2$ and $p=3$ Hecke actions always return to the fixed point?

The BC algebra's KMS$_1$ partition function $Z(1) = \zeta(1) = \infty$ (divergent at the critical point) means the system is at a phase transition. Collatz orbits are trajectories in this critical landscape. The conjecture is that the critical landscape has a single basin of attraction.

## Programme graph edges

- **QG5D (Paper 1):** BC Hecke semigroup $\mathbb{N}^* = \langle 2, 3, 5, \ldots \rangle$ is the multiplicative backbone; Collatz uses $\langle 2, 3 \rangle$ specifically
- **Goldbach (Paper 33):** same additive-multiplicative tension; both ask about the interplay of additive shifts and multiplicative Hecke actions on $\mathbb{N}$
- **PvNP (Paper 28):** Collatz orbit structure relates to computational complexity — Collatz verification is in NP, but proving convergence for all $n$ requires structural insight beyond individual verification
- **BGS (Paper 32):** backward transfer operator spectral gap connects to type III$_1$ ergodicity
- **Twin Primes (Paper 34):** Collatz at $p=2,3$ and twin primes at gap $=2$ are both about the smallest prime structure

## Physical observable

None direct (pure arithmetic dynamics). But: the Collatz map's orbit statistics are a dynamical-systems question about the Hecke semigroup's action space. If the BC algebra's KMS$_1$ state constrains all orbits to converge, the Collatz conjecture becomes a SPECTRAL consequence of the same operator algebra whose eigenvalues are the Riemann zeros.

## Honest assessment

**What's genuinely novel:** the C\*-algebra formulation (arXiv:2411.08084) is published and the Cuntz algebra $\mathcal{O}_2$ connection is established. The BC embedding (Link 4) is the framework's contribution — identifying the Collatz map as a Hecke-semigroup endomorphism using $\mu_2$ and $\mu_3$. Nobody has made this specific connection.

**What's hard:** Link 4 (BC embedding) requires handling the additive shift $+1$ in the odd step, which breaks the pure multiplicative structure. The BC algebra is multiplicative; the $+1$ is additive. This is the same wall that Goldbach faces. Link 6 requires transferring spectral-gap and type-III$_1$-ergodicity results from the full BC algebra to a Collatz sub-algebra — non-trivial.

**Confidence: 3/10.** The C\*-algebra infrastructure exists (Links 2-3 are LITERATURE). The BC embedding (Link 4) is natural but conjectural. The wall (Link 6) is where everything rests.

---

*v1: 2026-04-14. The Collatz map is the universe's simplest dynamical system on the Hecke semigroup. Does the BC algebra's spectral structure force it to have a unique attractor? The first two primes, the simplest map, the deepest question.*
