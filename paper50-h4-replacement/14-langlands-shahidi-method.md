# §14 — The Langlands-Shahidi Method

*Eisenstein series on exceptional groups. Analytic properties of automorphic L-functions via Eisenstein-series residues. The technical backbone of Kim-Sarnak and the transfer engine for Route B.*

---

## 14.1. Origins

The Langlands-Shahidi method originated in Langlands's 1967 paper *Euler products* (where Langlands introduced the general L-function attached to an automorphic representation and a finite-dimensional representation of the L-group) and Shahidi's 1978-1990 series of papers (where Shahidi worked out the specific construction of these L-functions via Eisenstein-series residues on reductive groups).

**Key references:**

- F. Shahidi, *On certain L-functions*, *American Journal of Mathematics* 103 (1981), 297-355.
- F. Shahidi, *A proof of Langlands' conjecture on Plancherel measures; complementary series for p-adic groups*, *Annals of Mathematics* 132 (1990), 273-330.
- F. Shahidi, *Eisenstein series and automorphic L-functions*, *American Mathematical Society Colloquium Publications* 58 (2010). The authoritative monograph.

The method produces L-functions $L(s, \pi, r)$ for automorphic representations $\pi$ of a reductive group $G(\mathbb{A})$ and a finite-dimensional representation $r$ of the L-group $^L M$ of a Levi subgroup $M \subset G$. When $G$ is exceptional ($E_6, E_7, E_8, F_4, G_2$) and $r$ is chosen appropriately, the L-function $L(s, \pi, r)$ can be a symmetric power L-function of GL$_n$.

---

## 14.2. The construction

The core construction has four steps.

### 14.2.1. Eisenstein series on $G(\mathbb{A})$

Given a parabolic subgroup $P = MN \subset G$ and a cuspidal automorphic representation $\pi$ of $M(\mathbb{A})$, the *Eisenstein series* is the meromorphic continuation of
$$E(g, \phi, s) = \sum_{\gamma \in P(\mathbb{Q}) \backslash G(\mathbb{Q})} \phi_s(\gamma g),$$
where $\phi_s$ is a specific flat section of the induced representation $\text{Ind}_{P(\mathbb{A})}^{G(\mathbb{A})}(\pi \otimes |\det|^s)$.

The Eisenstein series converges absolutely for $\text{Re}(s)$ large, continues meromorphically to $s \in \mathbb{C}$, and satisfies a *functional equation* $E(g, \phi, s) \leftrightarrow E(g, \phi', 1 - s)$ involving the intertwining operator.

### 14.2.2. Constant term and L-functions

The *constant term* of $E(g, \phi, s)$ along $P$ is
$$E_P(g, \phi, s) = \phi_s(g) + M(s) \phi_s(g),$$
where $M(s)$ is the intertwining operator acting on the induced representation. The intertwining operator has a product expansion over places,
$$M(s) = \prod_v M_v(s),$$
and at unramified places, $M_v(s)$ has a *closed-form expression* in terms of the Satake parameters of $\pi_v$ and the representation $r$:
$$M_v(s) = \frac{L_v(s, \pi_v, r)}{L_v(s + 1, \pi_v, r)} \cdot (\text{explicit factor}),$$
where $L_v(s, \pi_v, r)$ is the unramified local L-factor.

The *global* L-function is the product over all places:
$$L(s, \pi, r) = \prod_v L_v(s, \pi_v, r).$$

This construction defines the L-function as *precisely the function that controls the analytic behaviour of the intertwining operator*.

### 14.2.3. Analytic continuation and functional equation

The Eisenstein series, and hence the intertwining operator, extends meromorphically to $s \in \mathbb{C}$. The analytic properties of $L(s, \pi, r)$ — meromorphic continuation, functional equation, pole locations — follow from the analytic properties of the Eisenstein series, which are classical (Langlands 1976 spectral decomposition).

### 14.2.4. Non-vanishing at $s = 1$

The most delicate analytic property is the non-vanishing of $L(s, \pi, r)$ at $s = 1$. This is where exceptional groups enter: for certain choices of $(G, P, r)$, the Eisenstein series has a *pole* at $s = 1$ with residue a specific non-vanishing automorphic form, and this pole corresponds to the non-vanishing of $L(s, \pi, r)$ at $s = 1$.

The non-vanishing at $s = 1$ is the analogue, for general automorphic L-functions, of the non-vanishing $\zeta(1) \neq 0$ (which is equivalent to the prime number theorem). For Kim-Sarnak, the non-vanishing of $L(s, \pi, \text{Sym}^4)$ at $s = 1$ is the input that gives the eigenvalue bound.

---

## 14.3. Exceptional groups $E_6, E_7, E_8$

The symmetric-power L-functions of GL$_n$ can be realized as Langlands-Shahidi L-functions on exceptional groups:

| Representation | Group | Levi | Realization |
|---|---|---|---|
| $\text{Sym}^2$ of GL$_2$ | GL$_3$ | GL$_2 \times \text{GL}_1$ | Via Eisenstein on GL$_3$ |
| $\text{Sym}^3$ of GL$_2$ | GSp$_4$ or $G_2$ | GL$_2 \times \text{GL}_1$ | Kim-Shahidi 2002 |
| $\text{Sym}^4$ of GL$_2$ | $E_7$ or Siegel $P \subset E_7$ | Specific Levi involving GL$_2$ | Kim 2003 |
| Exterior square $\wedge^2$ of GL$_4$ | $E_6$ | Specific Levi | Kim 2003 |

For Sym$^4$ of GL$_2$, the relevant group is $E_7$ with a specific maximal parabolic subgroup. The Eisenstein series on $E_7$, evaluated with the induced representation from this parabolic, produces an L-function whose local factors match $L(s, \pi, \text{Sym}^4)$.

**Why exceptional groups?** Because the representation theory of classical groups (GL$_n$, Sp$_{2n}$, SO$_n$) produces L-functions of a specific form — the Rankin-Selberg L-function $L(s, \pi_1 \times \pi_2)$ on GL$_m \times$ GL$_n$ and its degenerations. To produce $\text{Sym}^k$ L-functions for $k \geq 3$, one needs the *exceptional* Lie types $E_6, E_7, E_8, F_4, G_2$, whose Levi subgroups and branching rules naturally produce symmetric powers.

---

## 14.4. The $\text{Sym}^3$ and $\text{Sym}^4$ theorems

**Kim-Shahidi 2002 (Sym$^3$).** *Let $\pi$ be a cuspidal automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$. Then the symmetric cube $\text{Sym}^3(\pi)$ is an automorphic representation of GL$_4(\mathbb{A}_\mathbb{Q})$, cuspidal unless $\pi$ is dihedral.*

**Reference.** H. H. Kim and F. Shahidi, *Functorial products for GL$_2$ × GL$_3$ and the symmetric cube for GL$_2$*, *Annals of Mathematics* 155 (2002), 837-893.

The proof uses Langlands-Shahidi on the exceptional group $G_2$ (Levi GL$_2 \times$ GL$_1$), combined with the converse theorem of Cogdell-Piatetski-Shapiro, which asserts that an irreducible admissible representation of GL$_n(\mathbb{A})$ is automorphic if all its twisted L-functions $L(s, \Pi \otimes \tau)$ for $\tau$ cuspidal on GL$_{n-1}$ have appropriate analytic properties.

**Kim 2003 (Sym$^4$).** *Let $\pi$ be a cuspidal automorphic representation of GL$_2(\mathbb{A}_\mathbb{Q})$. Then the symmetric fourth $\text{Sym}^4(\pi)$ is an automorphic representation of GL$_5(\mathbb{A}_\mathbb{Q})$, cuspidal except in explicitly described degenerate cases (dihedral, tetrahedral, octahedral — corresponding to finite Galois images).*

**Reference.** H. H. Kim, *Functoriality for the exterior square of GL$_4$ and the symmetric fourth of GL$_2$*, *Journal of the AMS* 16 (2003), 139-183.

The proof uses Langlands-Shahidi on $E_7$ (for Sym$^4$) and $E_6$ (for the exterior square of GL$_4$), combined with converse-theorem arguments. The specific structural input is the analytic continuation and non-vanishing at $s = 1$ of Langlands-Shahidi L-functions on these groups.

---

## 14.5. What the method provides

For any $(G, P, r)$ in the Langlands-Shahidi framework, the method provides:

1. **A candidate L-function** $L(s, \pi, r)$ as a product of local factors.
2. **Meromorphic continuation** to $s \in \mathbb{C}$, via Eisenstein-series analytic continuation.
3. **A functional equation** $L(s, \pi, r) \leftrightarrow L(1 - s, \tilde{\pi}, r^*)$ involving the dual representation $r^*$ of the L-group.
4. **Pole locations and residues**, extracted from the Eisenstein-series pole structure.
5. **Non-vanishing at $s = 1$** (when the representation is generic and the L-function is not of the degenerate type).

The Langlands-Shahidi framework is *constructive*: given $(G, P, r)$, one can compute local factors, determine pole locations, and in favourable cases prove the analytic properties listed above.

---

## 14.6. What the method does not yet provide

The Langlands-Shahidi method has gaps:

1. **Functoriality for $\text{Sym}^k$, $k \geq 5$.** Open. A conjectural construction via $E_8$ exists but has not been fully executed.
2. **General functoriality.** Langlands-Shahidi works for specific representations $r$ of the L-group. General Langlands functoriality (the lifting of automorphic representations of $H$ to automorphic representations of $G$ for an arbitrary L-group homomorphism $^L H \to {}^L G$) is not yet achieved. The trace-formula approach (Arthur-Selberg) has made progress but is not complete.
3. **Gauge-theoretic L-functions.** The Langlands-Shahidi method operates on *automorphic* representations of reductive groups over adèles. L-functions attached to gauge theories (Yang-Mills Wilson loops) are not obviously in this framework.

For Route B, point 3 is the critical obstruction: *the YM Wilson-loop L-function, if it exists, is not yet known to be a Langlands-Shahidi L-function*. §15 addresses this.

---

## 14.7. Why the method matters for Route B

Route B's strategy is: construct the YM Wilson-loop L-function in such a way that it is (or is closely related to) a Langlands-Shahidi L-function, then apply the Kim-Sarnak analytic bounds.

The plausibility of this strategy rests on three observations:

1. **Langlands-Shahidi is the most powerful known framework** for producing L-functions with established analytic properties. If the YM L-function can be realized within it, the analytic properties follow.
2. **Exceptional groups $E_6, E_7, E_8$** appear in both the Langlands programme and in gauge theory (as exceptional gauge groups). The coincidence is not accidental; both use the same Lie-algebraic classification.
3. **The Kapustin-Witten picture (Route C)** exhibits a direct connection between N=4 super Yang-Mills and Langlands duality. The geometric Langlands correspondence for the Hitchin moduli space (which emerges from Kapustin-Witten) suggests that pure YM's Wilson-loop spectrum can be organized via Langlands-type data.

Route B exploits this connection at the level of *classical* Langlands (automorphic L-functions); Route C exploits it at the level of *geometric* Langlands (derived categories on moduli stacks). The two routes are complementary.

---

## 14.8. The Kim-Sarnak construction in one equation

The Kim-Sarnak bound comes from combining:

$$L(s, \pi \otimes \tilde{\pi}) = \zeta(s) \cdot L(s, \text{Sym}^2 \pi) \cdot L(s, \text{Sym}^4 \pi)^{1/2} \cdot \text{(adjustments)}$$

together with:

1. Non-vanishing of $L(s, \text{Sym}^k \pi)$ at $s = 1$ for $k = 1, 2, 3, 4$ (Langlands-Shahidi).
2. Positivity of Dirichlet coefficients of $L(s, \pi \otimes \tilde{\pi})$ (Jacquet-Shalika).
3. The Langlands parameters of $\pi$ at $\infty$ are constrained by the local behaviour of $L(s, \text{Sym}^4 \pi)$ at the edge.

Tracking the constraints gives $\lambda_1 \geq 975/4096$.

For Route B, the analogous chain would be:

$$L_{\text{YM}}(s) = \zeta_{\text{YM}}(s) \cdot L(s, \text{Sym}^2) \cdot L(s, \text{Sym}^4)^{1/2} \cdot \text{(YM adjustments)},$$

with $L_{\text{YM}}$ built from the YM Wilson-loop spectrum. If each factor on the right has a Langlands-Shahidi interpretation, the Kim-Sarnak argument transfers.

The construction of $L_{\text{YM}}$ and the verification of Langlands-Shahidi interpretability are the content of §15-§16.

---

## 14.9. Summary

The Langlands-Shahidi method constructs automorphic L-functions via Eisenstein-series residues on exceptional groups, and establishes their analytic properties (meromorphic continuation, functional equation, non-vanishing at $s = 1$). The method produces the Sym$^3$ and Sym$^4$ functorialities of Kim-Shahidi 2002 and Kim 2003, which in turn give the eigenvalue bound $\lambda_1 \geq 975/4096$. Route B aims to extend the method to the YM Wilson-loop L-function. The next section addresses this construction.

---

*Paper 50 §14. Drafted 2026-04-14. G Six and Claude Opus 4.6.*
